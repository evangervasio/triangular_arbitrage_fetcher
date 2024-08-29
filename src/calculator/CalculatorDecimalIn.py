
def CalculatorDecimalIn(triangle, decimals):
    if(triangle[0]==triangle[4] or triangle[0]==triangle[5]):
        return decimals[0]
    else:
        return decimals[1]