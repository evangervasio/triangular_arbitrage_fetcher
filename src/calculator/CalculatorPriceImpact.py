from decimal import Decimal

"""
Calculates the price impact for trades on an Automated Market Maker (AMM) like Uniswap.

This function computes the price impact of a swap, which is the effect of a swap on the price of a token within 
an AMM liquidity pool. The price impact is derived from the Uniswap pricing formulas, reflecting how the price changes 
in response to a swap, based on the input and output amounts of the tokens involved.

### Parameters:
- `a12`: Reserve of the first token in the pool.
- `a21`: Reserve of the second token in the pool.
- `amountIn1`: Amount of the first token being input into the pool.
- `amountIn2`: Amount of the second token being input into the pool.
- `amountOut1`: Amount of the first token being output from the pool.
- `amountOut2`: Amount of the second token being output from the pool.

### Returns:
- `Decimal`: The price impact of the trade, indicating the change in price resulting from the specified swap parameters.
"""
def CalculatorPriceImpact(a12, a21, amountIn1, amountIn2, amountOut1, amountOut2):
    constant = Decimal(a12 * a21)
    x = Decimal(0)
    if amountIn1 != 0:
        x = ((constant) / (-a12 - amountIn1)) + a21
    if amountIn2 != 0:
        x = ((constant) / (-a21 - amountIn2)) + a12

    if amountOut1 != 0:
        x = ((constant) / (a12 - amountOut1)) - a21
    if amountOut2 != 0:
        x = ((constant) / (a21 - amountOut2)) - a12

    return x

#Unused
def CalculatorPriceImpactS(a12, a21, amountIn1):
    constant = a12 * a21
    x = ((constant) / (-a12 - amountIn1)) + a21

    return x
