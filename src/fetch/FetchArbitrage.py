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
from executer import ExecuterSwap
from tqdm import tqdm

import requests
import select
from fetch import FetchGasPrice
import concurrent.futures
from ratelimiter import RateLimiter
cur_path = os.path.dirname(__file__)
#this array is an array of [token, limit of that token]
#so for example [MATIC, 600000000000...]
#which means i am willing to spend at max that value
tokensLimits=[]
cur_path = os.path.dirname(__file__)
path_quickswap = os.path.relpath("../files/filesQuickswap/tokensLimits.csv", cur_path)


path_uniswap = os.path.relpath("../files/filesUniswap/tokensLimits.csv", cur_path)

path_apeswap = os.path.relpath("../files/filesApeswap/tokensLimits.csv", cur_path)

WMATIC='0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270'
##This function will scan for triangular arbitrage
#on uniswap for now
#TODO: optimize; create a separate function for Uniswap and Quickswap
#todo: apply tokensToExclude filter both to original triangles.csv AND trianglesFilter.csvimport concurrent.futures
rate_limiter = RateLimiter(max_calls=8, period=1)  # max 10 calls per second
@rate_limiter
def fetch_all_reserves(selectedSwap,filter):
    if filter:
        new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFilter.csv", cur_path)
    else: new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/triangles.csv", cur_path)
#    new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFocused.csv", cur_path)
    reserves = {}
    with open(new_path, "r") as read_obj:
        csv_reader = csv.reader(read_obj)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {}
            for row_id, row in enumerate(csv_reader):
                #print(row)
                for i in range(3):
                    future = executor.submit(FetchReserves.FetchReserves, selectedSwap, str(row[12 + i]))
                    futures[future] = (row_id, i)
                    #print(row)

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
def FetchArbitrage(selectedSwap,filter):
    contatore=0
    #get all the reserves of all the triangles
    #and puts them in triangles.csv

    #Creates a new list of triangles which have as input token only
    #the tokens listed in files(dex)/tokensToInclude.csv

    path_token_limits=os.path.relpath(f"../files/files{selectedSwap.Name}/tokensLimits.csv", cur_path)

    with open(path_token_limits, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            tokensLimits.append(row[0].split(";"))


    #TODO: make option to apply filter of tokensToExclude or filter of tokensLimits separately
    if filter:
        CalculatorTokens.CalculatorTokens(selectedSwap)
        new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFilter.csv", cur_path)
    else: new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/triangles.csv", cur_path)
    #new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFocused.csv", cur_path)

    reserves = np.empty(6, dtype=object)
    decimals = np.empty(6, dtype=object)
    r1=Decimal(0.997)
    r2=Decimal(1)
    triangle=[]

    arbitrageResults=[]
    while True:
        rowid = 0
        reservesFull = fetch_all_reserves(selectedSwap, filter)
        print("reserved fetched")
        with open(new_path, "r") as read_obj:
            csv_reader = csv.reader(read_obj)
            for row in tqdm(csv_reader):
                #try:
                    row_=str(row[0])
                  #  print("R")
                  #  print(reservesFull)
                  #  print("R!")
                    row_=row
                   # print("T1")
                    #print(FetchReserves.FetchReserves(selectedSwap,row_[12]))
                   # print(FetchReserves.FetchReserves(selectedSwap, row_[13]))
                   # print(FetchReserves.FetchReserves(selectedSwap, row_[14]))
                  #  print("T2")

            #reserves[0],reserves[1]= FetchReserves.FetchReserves(selectedSwap,row_[12])
                    #reserves[2],reserves[3]= FetchReserves.FetchReserves(selectedSwap,row_[13])
                    #reserves[4],reserves[5]= FetchReserves.FetchReserves(selectedSwap,row_[14])
                    #print(reservesFull[rowid])
                    _reserves=reservesFull[rowid]
                  #  print(_reserves)
                    reserves[0],reserves[1]= _reserves[0]
                    reserves[2], reserves[3]=_reserves[1]
                    reserves[4], reserves[5]=_reserves[2]
                    rowid=rowid+1
                  #  print(reserves)
                    #decimals
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


                    #fetches max amount
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

                   # print(a12,a21,a23,a32,a13,a31)
                    arbitrageResults.append([optAmountIn, profit])

                    if profit>0:
                        if (triangle[0] == triangle[4] or triangle[0] == triangle[5]):
                            print("input token: "+triangle[0])
                        else:
                            print("input token: "+triangle[1])
                        print("profit !: "+str(profit)+ " input: "+str(optAmountIn)+" output: "+str(amountOut)+" triangle: "+triangle[0]+" ; "+triangle[1]+" ; "+triangle[2]+" ; "+triangle[3]+" ; "+triangle[4]+" ; "+triangle[5])
                        print("percentage: "+str((amountOut*100/optAmountIn)-100))

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
                        print("getAmountsOut: "+str(getAmountsOut))
                        #print("actual percentage: "+str(actualPercentage))
                #        '''
                        if actualPercentage>0:
                            gas_price_gwei=FetchGasPrice.FetchGasPrice(selectedSwap)

                            print("gas price: " + str(gas_price_gwei) + " gwei")

                            while gas_price_gwei>500:

                                time.sleep(1)
                                gas_price_gwei=FetchGasPrice.FetchGasPrice(selectedSwap)

                                print("gas price: "+ str(gas_price_gwei)+" gwei")


                            getAmountsOut = FetchGetAmountsOut.FetchGetAmountsOut(selectedSwap,optAmountIn, triangleAddresses)

                            if getAmountsOut[3]>getAmountsOut[0]:
                                #calculates profit with polygon fees
                                #this works only if the only token that we use is MATIC

                                fees=((gas_price_gwei*pow(10,-9))*270000)*pow(10,18)
                                #fees = ((gas_price_gwei * pow(10, -9)) * 270000)
                                print("-----------")
                                print(fees)

                                if selectedSwap.Network=="Polygon":

                                    if triangleAddresses[0].lower() != WMATIC.lower():
                                        try:
                                            #get price of token in matic
                                            token_price_in_wmatic=FetchGasPrice.FetchTokenPriceInWmatic(triangleAddresses[0])
                                            token_price_in_wmatic=token_price_in_wmatic*pow(10,18)

                                            #convert the amount In of the token and the amount Out in WMATIC
                                            amountIn=getAmountsOut[0]*token_price_in_wmatic
                                            amountOut=getAmountsOut[3]*token_price_in_wmatic
                                        except Exception as e:
                                            print(e)
                                            print("cant fetch price in wmatic of token")
                                            amountIn=-1
                                            amountOut=-1

                                    else:
                                        amountIn=getAmountsOut[0]
                                        amountOut=getAmountsOut[3]

                                if Decimal(amountOut)-Decimal(fees)>Decimal(amountIn):
                                    print(getAmountsOut)
                                    if selectedSwap.Name=="Quickswap":
                                        #TODO: remove this if if u have tokens in ur wallet other than wmatic
                                        if filter:
                                            #ExecuterSwap.ExecuterSwapQuickswap(getAmountsOut[0],getAmountsOut[0],triangleAddresses,gas_price_gwei,False,False)
                                            print("0-would have executed trade")

                                        else: print("1-would have executed trade")
                                    else:
                                        print("would have executed trade")

                                else:
                                    print("arbitrage not profitable because of fees: "+"%.0f" % (fees))
                                    print()
                            else:
                                print("arbitrage not anymore profitable")


    #'''
                    triangle=[]
                #except:
                    True

        print("Arbitrage Fetch Ended. WAITING 0 SECONDS."+ " --- "+str(datetime.datetime.now()))
        #time.sleep(30)
        print("REPEATING ARBITRAGE FETCH - counter: "+str(contatore) + " --- "+str(datetime.datetime.now()))
        contatore=contatore+1


