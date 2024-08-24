from decimal import Decimal

"""
Calculates the price impact.
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
