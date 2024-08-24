import os
import sys
import time
import datetime
sys.path.append("../")
import csv
from fetch import FetchReserves
from fetch import FetchGetAmountsOut
import numpy as np
import decimal
from decimal import Decimal
from calculator import CalculatorTruncate
from calculator import CalculatorSetSwap
from calculator import CalculatorSwap
from calculator import CalculatorAmount
from calculator import CalculatorDecimalIn
from calculator import CalculatorTokens
from tqdm import tqdm
from executer import ExecuterSwap

from fetch import FetchGasPrice
import concurrent.futures
from ratelimiter import RateLimiter
cur_path = os.path.dirname(__file__)

tokensLimits=[]
cur_path = os.path.dirname(__file__)
path_quickswap = os.path.relpath("../files/filesQuickswap/tokensLimits.csv", cur_path)


path_uniswap = os.path.relpath("../files/filesUniswap/tokensLimits.csv", cur_path)

path_apeswap = os.path.relpath("../files/filesApeswap/tokensLimits.csv", cur_path)

WMATIC='0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270'

rate_limiter = RateLimiter(max_calls=8, period=1)

"""
Fetches all the reserves of the triangles in a csv list of a swap.
"""
@rate_limiter
def fetch_all_reserves(selectedSwap,filter):
    if filter:
        new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFilter.csv", cur_path)
    else: new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/triangles.csv", cur_path)
    reserves = {}
    with open(new_path, "r") as read_obj:
        csv_reader = csv.reader(read_obj)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {}
            for row_id, row in enumerate(csv_reader):
                for i in range(3):
                    future = executor.submit(FetchReserves.FetchReserves, selectedSwap, str(row[12 + i]))
                    futures[future] = (row_id, i)

            for future in tqdm(concurrent.futures.as_completed(futures)):
                row_id, i = futures[future]
                try:
                    reserve = future.result()
                except Exception as exc:
                    print(f'Generated an exception: {exc}')
                else:
                    if row_id not in reserves:
                        reserves[row_id] = {}
                    reserves[row_id][i] = reserve
    return reserves

"""
The `FetchArbitrage` function scans through every triangular arbitrage opportunity listed in a CSV file associated 
with a specific decentralized exchange (DEX) swap configuration. It calculates the potential profitability of each 
triangular arbitrage scenario by taking into account various factors including blockchain transaction fees, DEX fees, price impact, 
and the user's maximum input amount. When a profitable arbitrage opportunity is identified, the function is designed to 
simulate its execution without actually initiating the transaction, for security purposes.

### Detailed Function Workflow:

1. **Initialize Counters and Paths:**
   - The function begins by setting up the path to a CSV file containing 
     token limits specific to the selected swap (`path_token_limits`).

2. **Load Token Limits:**
   - It reads the `tokensLimits.csv` file, which contains limits on the amount of specific tokens that can be used in 
     arbitrage, and stores these limits in the `tokensLimits` list.

3. **Determine Triangles Source:**
   - Based on the `filter` parameter, it decides whether to use a filtered set of triangular arbitrage opportunities 
     (`trianglesFilter.csv`) or the complete set (`triangles.csv`).

4. **Fetch Reserves:**
   - The function retrieves the current reserve data for each potential arbitrage triangle from the blockchain, using 
     the `fetch_all_reserves` function.

5. **Iterate Through Triangles:**
   - The function enters a loop where it reads through each triangle configuration (set of three token pairs) from the 
     CSV file.

6. **Extract and Convert Reserve Data:**
   - For each triangle, it extracts reserve and decimal data, converting them into a `decimal.Decimal` format suitable 
     for precise calculations.

7. **Calculate Arbitrage Parameters:**
   - The function calculates the ordered reserves amounts (`a12`, `a21`, `a23`, `a32`, `a13`, `a31`) required to evaluate 
     the potential arbitrage profit.
   - It determines the maximum allowable input amount (`maxAmount`) for the arbitrage based on token limits or a 
     proportion of the calculated amount.

8. **Optimal Input Calculation:**
   - Using the `CalculatorAmountIter` function, it computes the optimal input amount that would yield the highest 
     profit given the reserves and trading parameters.

9. **Profitability Check:**
   - The function then evaluates whether the calculated profit is positive. If so, it logs the potential profit and 
     details of the triangle.

10. **Transaction Simulation:**
    - If the arbitrage is potentially profitable, the function continues to simulate the transaction:
        - It calculates the output amount after accounting for fees using the `FetchGetAmountsOut` function.
        - It fetches the current gas price and determines the overall transaction cost.
        - If the transaction remains profitable after considering blockchain fees, the function simulates sending the 
          transaction for execution.

11. **Logging and Repeat Cycle:**
    - The function logs the results of each iteration, including errors or unprofitable scenarios, and then repeats the 
      cycle for continuous monitoring of arbitrage opportunities.

### Security Note:
- The function is configured in this state to only simulate the execution of profitable arbitrage opportunities. 
  Actual transactions are not executed, providing a safeguard against unintended trades during development and testing.

### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, with attributes such as the factory and router smart contracts, the name and the network (polygon, ethereum..).
- `filter`: A boolean flag indicating whether to use a filtered set of arbitrage triangles (`True`) or the complete set (`False`).

### Returns:
- None. The function operates in a continuous loop, logging its findings and simulations to the console.

"""
def FetchArbitrage(selectedSwap,filter):
    contatore=0


    path_token_limits=os.path.relpath(f"../files/files{selectedSwap.Name}/tokensLimits.csv", cur_path)

    with open(path_token_limits, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            tokensLimits.append(row[0].split(";"))


    if filter:
        CalculatorTokens.CalculatorTokens(selectedSwap)
        new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFilter.csv", cur_path)
    else: new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/triangles.csv", cur_path)

    reserves = np.empty(6, dtype=object)
    decimals = np.empty(6, dtype=object)
    r1=Decimal(0.997)
    r2=Decimal(1)
    triangle=[]

    arbitrageResults=[]
    while True:
        rowid = 0
        reservesFull = fetch_all_reserves(selectedSwap, filter)
        print("Arbitrage Fetch: reserved fetched")
        with open(new_path, "r") as read_obj:
            csv_reader = csv.reader(read_obj)
            for row in tqdm(csv_reader):
                    row_=str(row[0])

                    row_=row



                    _reserves=reservesFull[rowid]
                    reserves[0],reserves[1]= _reserves[0]
                    reserves[2], reserves[3]=_reserves[1]
                    reserves[4], reserves[5]=_reserves[2]
                    rowid=rowid+1

                    try:
                        for x in range(6):
                            decimals[x]=row_[15+x]
                            tupleOfDigits=str(reserves[x])
                            arrOfDigits = np.empty(len(tupleOfDigits), dtype=object)
                            for y in range(len(tupleOfDigits)):
                                arrOfDigits[y]=int(tupleOfDigits[y])
                            arrOfDigits=tuple(arrOfDigits)

                            reserves[x]=decimal.Decimal((0,(arrOfDigits),(-(int(decimals[x])))))
                    except Exception as e:
                        continue


                    triangle.append(row_[0])
                    triangle.append(row_[1])
                    triangle.append(row_[2])
                    triangle.append(row_[3])
                    triangle.append(row_[4])
                    triangle.append(row_[5])


                    a12,a21,a23,a32,a13,a31=CalculatorSetSwap.CalculatorSetSwap(triangle,reserves)


                    if not tokensLimits==[]:
                        found=False
                        for t in tokensLimits:
                            if(t[0].lower()==row_[6].lower()):
                                maxAmount=int(t[1])
                                found = True
                        if not found:
                            maxAmount=a12/2
                        else:

                            tupleOfDigits = str(maxAmount)
                            arrOfDigits = np.empty(len(tupleOfDigits), dtype=object)
                            for y in range(len(tupleOfDigits)):
                                #logging.debug(tupleOfDigits)
                                arrOfDigits[y] = int(tupleOfDigits[y])
                            arrOfDigits = tuple(arrOfDigits)
                            maxAmount = decimal.Decimal((0, (arrOfDigits), (-(int(decimals[0])))))
                    else:
                        maxAmount=a12/2
                    if maxAmount>a12:
                        maxAmount=a12/2


                    optAmountIn = CalculatorAmount.CalculatorAmountIter(maxAmount, 1, a12, a21, a23, a32, a13, a31, r1, r2)

                    amountOut=CalculatorSwap.CalculatorSwap(optAmountIn,a12,a21,a23,a32,a13,a31,r1,r2)

                    profit=Decimal(amountOut-optAmountIn)

                    arbitrageResults.append([optAmountIn, profit])

                    if profit>0:

                        print("Arbitrage Fetch: possible profit calculated: "+str(profit)+ " input: "+str(optAmountIn)+" output: "+str(amountOut)+" triangle: "+triangle[0]+" ; "+triangle[1]+" ; "+triangle[2]+" ; "+triangle[3]+" ; "+triangle[4]+" ; "+triangle[5])
                        print("profit percentage: "+str((amountOut*100/optAmountIn)-100))
                        if (triangle[0] == triangle[4] or triangle[0] == triangle[5]):
                            print("input token: "+triangle[0])
                        else:
                            print("input token: "+triangle[1])
                        triangleAddresses=[]
                        triangleAddresses.append(row_[6])
                        triangleAddresses.append(row_[7])
                        triangleAddresses.append(row_[8])
                        triangleAddresses.append(row_[9])
                        triangleAddresses.append(row_[10])
                        triangleAddresses.append(row_[11])
                        triangleAddresses=CalculatorSetSwap.CalculatorSetOrderTokensABC(triangleAddresses)
                        decimal_=CalculatorDecimalIn.CalculatorDecimalIn(triangle,decimals)
                        optAmountIn=CalculatorTruncate.CalculatorTruncate(optAmountIn,Decimal(decimal_))
                        getAmountsOut=FetchGetAmountsOut.FetchGetAmountsOut(selectedSwap,optAmountIn,triangleAddresses)

                        actualPercentage=(getAmountsOut[3]*100/getAmountsOut[0])-100

                        if actualPercentage>0:
                            gas_price_gwei=FetchGasPrice.FetchGasPrice(selectedSwap)

                           # print("gas price: " + str(gas_price_gwei) + " gwei")

                            while gas_price_gwei>500:

                                time.sleep(1)
                                gas_price_gwei=FetchGasPrice.FetchGasPrice(selectedSwap)

                              #  print("gas price: "+ str(gas_price_gwei)+" gwei")


                            getAmountsOut = FetchGetAmountsOut.FetchGetAmountsOut(selectedSwap,optAmountIn, triangleAddresses)

                            if getAmountsOut[3]>getAmountsOut[0]:


                                fees=((gas_price_gwei*pow(10,-9))*270000)*pow(10,18)

                                if selectedSwap.Network=="Polygon":

                                    if triangleAddresses[0].lower() != WMATIC.lower():
                                        try:
                                            token_price_in_wmatic=FetchGasPrice.FetchTokenPriceInWmatic(triangleAddresses[0])
                                            token_price_in_wmatic=token_price_in_wmatic*pow(10,18)

                                            amountIn=getAmountsOut[0]*token_price_in_wmatic
                                            amountOut=getAmountsOut[3]*token_price_in_wmatic
                                        except Exception as e:
                                            print(e)
                                            print("Arbitrage Fetch: ERROR - cannot fetch price of token in wmatic")
                                            amountIn=-1
                                            amountOut=-1

                                    else:
                                        amountIn=getAmountsOut[0]
                                        amountOut=getAmountsOut[3]

                                if Decimal(amountOut)-Decimal(fees)>Decimal(amountIn):
                                    if selectedSwap.Name=="Quickswap":
                                        if filter:
                                            #ExecuterSwap.ExecuterSwapPolygon(selectedSwap,getAmountsOut[0],getAmountsOut[0],triangleAddresses,gas_price_gwei,False,False)
                                            print("Arbitrage Fetch: triangular arbitrage transaction sent in execution")

                                        else: print("Arbitrage Fetch: triangular arbitrage transaction sent in execution")
                                    else:
                                        # ExecuterSwap.ExecuterSwapPolygon(selectedSwap,getAmountsOut[0],getAmountsOut[0],triangleAddresses,gas_price_gwei,False,False)
                                        print("Arbitrage Fetch: triangular arbitrage transaction sent in execution")

                                else:
                                    print("Arbitrage Fetch: ERROR - arbitrage not profitable because of blockchain fees: "+"%.0f" % (fees))
                                    print()
                            else:
                                print("Arbitrage Fetch: ERROR - arbitrage not anymore profitable")


                    triangle=[]
                    True

        print("Arbitrage Info: arbitrage fetch ended."+ " --- "+str(datetime.datetime.now()))
        print("Arbitrage Info: repeating arbitrage cycle fetch - counter: "+str(contatore) + " --- "+str(datetime.datetime.now()))
        contatore=contatore+1


