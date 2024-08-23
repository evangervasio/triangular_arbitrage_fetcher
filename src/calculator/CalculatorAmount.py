from decimal import Decimal
from calculator import CalculatorSwap
import math

def CalculatorAmount(maxAmount,decimals,a12,a21,a23,a32,a13,a31,r1,r2):
    A1=1
    A2 = A1 * a12 * (1 - 0.03)
    A3 = A2 * a23 * (1 - 0.03)
    A1= A3 * a31 * (1 - 0.03)



def CalculatorAmountIter(maxAmount,decimals,a12,a21,a23,a32,a13,a31,r1,r2):

  i=math.ceil(maxAmount/30000)
  maxProfit=Decimal(0)
  optInput=Decimal(0)
  amount=Decimal(1)

  while amount<maxAmount:

    output=Decimal(CalculatorSwap.CalculatorSwap(amount,a12,a21,a23,a32,a13,a31,r1,r2))
    profit=Decimal(output-amount)

    if(profit>maxProfit):
      maxProfit=profit
      optInput=amount
    amount=amount+i
  return optInput

def CalculatorAmountIterNew(maxAmount, decimals, a12, a21, a23, a32, a13, a31, r1, r2):
    i = maxAmount // 30000
    maxProfit = Decimal(0)
    optInput = Decimal(0)

    for amount in range(1, maxAmount, i):
        output = Decimal(CalculatorSwap.CalculatorSwap(amount, a12, a21, a23, a32, a13, a31, r1, r2))
        profit = output - amount
        if profit > maxProfit:
            maxProfit = profit
            optInput = amount

    return optInput
def isArbitrageProfitable(decimals,a12,a23,a31):
    A1=1
    A2 = A1 * a12 * (Decimal(1) - Decimal(0.03))
    A3 = A2 * a23 * (Decimal(1) - Decimal(0.03))
    A1_= A3 * a31 * (Decimal(1) - Decimal(0.03))

    print(A1)
    print ("%.0f" % (A1_))
    if(A1_>A1):
        return True
    else: return False