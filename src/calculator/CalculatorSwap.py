from calculator import CalculatorPriceImpact
"""
The `CalculatorSwap` function simulates a triangular arbitrage transaction, calculating the output amount after a 
series of swaps across three different trading pairs. The function leverages price impact calculations at each stage 
of the swap to determine the final output amount.

### Detailed Function Workflow:

1. **Initial Swap (First Pair):**
   - The function starts by calculating the output amount after swapping an initial input (`optAmountInA`) of the 
     first token reserve (`a12`) with the second token reserve (`a21`). This is done using the `CalculatorPriceImpact.CalculatorPriceImpact` 
     function, which accounts for price impact based on liquidity reserves. 
   - The result of this swap, `amountOut1`, is scaled by the ratio `r2` which represents the fee used in Uniswap forks smart contract calculations.

2. **Second Swap (Second Pair):**
   - Next, the function uses `amountOut1` as the input for the second swap, where the second token is swapped 
     with the third token. Again, the `CalculatorPriceImpact.CalculatorPriceImpact` function is used to 
     account for price impact. 
   - The output of this swap `amountOut2` is also scaled by `r2`.

3. **Final Swap (Third Pair):**
   - In the final step, `amountOut2` is swapped for the first token, completing the triangular arbitrage. 
     The output, `amountOut3`, represents the final amount obtained after the entire sequence of swaps.
   - The function returns `amountOut3` as the calculated output amount after the arbitrage.

### Parameters:
- `optAmountInA`: The optimal input amount of the first token to be used in the triangular arbitrage.
- `a12`: Reserve of the first token in the first pool.
- `a21`: Reserve of the second token paired with the first token in the first pool.
- `a23`: Reserve of the second token in the second pool.
- `a32`: Reserve of the third token paired with the second token in the second pool.
- `a13`: Reserve of the third token in the third pool.
- `a31`: Reserve of the first token paired with the third token in the third pool.
- `r1`: Uniswap forks fee.
- `r2`: Uniswap forks fee.

### Returns:
- `amountOut3`: The final output amount of the first token after completing the triangular arbitrage, taking into 
  account the price impacts at each stage of the swap.

### Key Features:
- **Triangular Arbitrage Simulation:** The function effectively simulates the entire arbitrage process across three 
  trading pairs, providing a realistic estimate of the final output.
- **Price Impact Consideration:** By integrating the `CalculatorPriceImpact.CalculatorPriceImpact` function, the 
  function accurately accounts for the price impact of each swap, which is crucial for determining potential profitability.
- **Flexible Input Handling:** The use of `r1` and `r2` allows for flexible adjustment of the input and output amounts 
  based on varying DEX fees.
"""

def CalculatorSwap(optAmountInA,a12,a21,a23,a32,a13,a31,r1,r2):
    amountOut1=(CalculatorPriceImpact.CalculatorPriceImpact(a12,a21,optAmountInA*r1,0,0,0))*r2

    amountOut2=(CalculatorPriceImpact.CalculatorPriceImpact(a23,a32,(amountOut1*r1),0,0,0))*r2

    amountOut3=(CalculatorPriceImpact.CalculatorPriceImpact(a13,a31,0,(amountOut2*r1),0,0))*r2
    
    return amountOut3

