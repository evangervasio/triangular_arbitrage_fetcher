from decimal import Decimal


##This function returns you an input/output amount of the token
# you will get if you output/input an amount of the other token.
# The outcome is affected by the AMM price impact.

def CalculatorPriceImpact(a12, a21, amountIn1, amountIn2, amountOut1, amountOut2):
    constant = Decimal(a12 * a21)
    x = Decimal(0)
    # if u have certain A and u wanna buy B
    if amountIn1 != 0:
        x = ((constant) / (-a12 - amountIn1)) + a21
    # if u have certain B and u wanna buy A
    if amountIn2 != 0:
        x = ((constant) / (-a21 - amountIn2)) + a12

    # if u have A and u wanna buy certain B
    if amountOut1 != 0:
        x = ((constant) / (a12 - amountOut1)) - a21
    # if u have B and u wanna buy certain A
    if amountOut2 != 0:
        x = ((constant) / (a21 - amountOut2)) - a12

    return x


##This function returns you an input/output amount of the token
# with a single option.
# You are supposed to set accordingly token0 and token1
# so to swap them and their reserves if necessary.

def CalculatorPriceImpactS(a12, a21, amountIn1):
    constant = a12 * a21
    # if u have certain A and u wanna buy B
    x = ((constant) / (-a12 - amountIn1)) + a21

    return x
