#from CalculatorAmount import CalculatorAmount
from calculator import CalculatorPriceImpact

##this function returns the outcome of the triangular swap
#!!!WITHOUT TAKING IN COUNT THE FEES OF THE BLOCKCHAIN!!!
#you should already have the optimal input amount that is tokenAIn.
#where aij is the reserve of token "i" on his pair with token "j"
#and aji is the reserve of token "j" on his pair with "i"
#r1 is the fee of the exchange applied to the input, if it has any.
#r2 is the fee of the exchange applied to the output.
#p.e. r1=0.997, r2=1
#problem; the function doesn't know which one is token0 and token1
#solution could be that before calling the func
#we, if needed, swap token0 and token1 and reserve0 and reserve1

def CalculatorSwap(optAmountInA,a12,a21,a23,a32,a13,a31,r1,r2):
    amountOut1=(CalculatorPriceImpact.CalculatorPriceImpact(a12,a21,optAmountInA*r1,0,0,0))*r2

    amountOut2=(CalculatorPriceImpact.CalculatorPriceImpact(a23,a32,(amountOut1*r1),0,0,0))*r2

    amountOut3=(CalculatorPriceImpact.CalculatorPriceImpact(a13,a31,0,(amountOut2*r1),0,0))*r2
    
    return amountOut3

