"""
Returns the decimal position number (p.e. 18) of the token we are putting an amount input in and getting
an amount output from (supposedly greater) in a triangular arbitrage transaction.
"""
def CalculatorDecimalIn(triangle, decimals):
    if(triangle[0]==triangle[4] or triangle[0]==triangle[5]):
        return decimals[0]
    else:
        return decimals[1]