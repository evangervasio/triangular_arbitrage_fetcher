from calculator import CalculatorPriceImpact

def CalculatorSwap(optAmountInA,a12,a21,a23,a32,a13,a31,r1,r2):
    amountOut1=(CalculatorPriceImpact.CalculatorPriceImpact(a12,a21,optAmountInA*r1,0,0,0))*r2

    amountOut2=(CalculatorPriceImpact.CalculatorPriceImpact(a23,a32,(amountOut1*r1),0,0,0))*r2

    amountOut3=(CalculatorPriceImpact.CalculatorPriceImpact(a13,a31,0,(amountOut2*r1),0,0))*r2
    
    return amountOut3

