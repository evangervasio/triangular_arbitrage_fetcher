from math import sqrt
from decimal import Decimal
from calculator import CalculatorSwap
from calculator import CalculatorTruncate
from time import sleep
from tqdm import tqdm
import math
from scipy.optimize import minimize
import numpy as np
import csv
import os
##This function calculates the output of formula that is for now a test
#the formula permits to calculate the optimal amount to input to a 
#triangular arbitrage for the max profit outcome
#where aij is the reserve of token "i" on his pair with token "j"
#and aji is the reserve of token "j" on his pair with "i"
#r1 is the fee of the exchange applied to the input, if it has any.
#r2 is the fee of the exchange applied to the output.
#p.e. r1=0.997, r2=1
#this function is the result of 
#the last pharagraph of https://arxiv.org/pdf/2105.02784.pdf
#problem; the function doesn't know which one is token0 and token1
#solution could be that before calling the func
#we, if needed, swap token0 and token1 and reserve0 and reserve1
def CalculatorAmount(maxAmount,decimals,a12,a21,a23,a32,a13,a31,r1,r2):
    A1=1
    A2 = A1 * a12 * (1 - 0.03)
    A3 = A2 * a23 * (1 - 0.03)
    A1= A3 * a31 * (1 - 0.03)

##This function does an iterative calculation of the optimal input amount
#and will save the optimal input amount based on the output of the swaps
#where 'max' is the maximum amount to calculate the output for,
#so the amount to increase the input amount to is proportional to the reserve
#so if the reserve is a lot big, i wont increase by 1, but maybe by 100000
#so a 'formula' to calculate how much to increase each time would be that
#the total iteration per triangle must be p.e. 30000
#so max amount / 30000 = amount to increase

def CalculatorAmountIter(maxAmount,decimals,a12,a21,a23,a32,a13,a31,r1,r2):

  i=math.ceil(maxAmount/30000)
  maxProfit=Decimal(0)
  optInput=Decimal(0)
  amount=Decimal(1)

 # print(12345)
  while amount<maxAmount:

   # amount=CalculatorTruncate.CalculatorTruncate(amount,decimalszzzz)
    output=Decimal(CalculatorSwap.CalculatorSwap(amount,a12,a21,a23,a32,a13,a31,r1,r2))
    profit=Decimal(output-amount)

    #print(maxAmount)
    if(profit>maxProfit):
      maxProfit=profit
      optInput=amount
    amount=amount+i
 # print(155555)
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