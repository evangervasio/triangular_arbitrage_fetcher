import decimal
from decimal import Decimal

##this func returns the correct a12,a21,a23,a32,a13,a31 following the order
#of tokens and reserves of pairs
#of multiple swaps, to set the swap ready for other functions.
#p.e. triangle={"ETH/BTC/BTC/HEX/HEX/ETH"}
#reserves = {10,20,200,50,11,23}
#triangle="USDC/WETH/HEX/WETH/HEX/USDC"
#reserves=[100,200,300,70,15,950]
def CalculatorSetSwap(triangle, reserves):
    #triangle=triangle.split("/")
    a12=Decimal(0)
    a21=Decimal(0)
    a23=Decimal(0)
    a32=Decimal(0)
    a13=Decimal(0)
    a31=Decimal(0)
   # print(reserves)
 #   print(a12,a21,a23,a32,a13,a31)
    #find out who is the token A
    if triangle[0]==triangle[4] or triangle[0]==triangle[5]:
        a12=reserves[0]
        a21=reserves[1]
        #since A is token0 of the first pair, 
        #B must be token1 of the first pair
        
        #if B is token0 of the second pair
        if triangle[1]==triangle[2]:
            a23=reserves[2]
            a32=reserves[3]
            #since B is token0 of the second pair,
            #C must be token1 of the second pair
            if(triangle[3]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[3]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]
        if triangle[1]==triangle[3]:
            a23=reserves[3]
            a32=reserves[2]
            #since B is token1 of the second pair,
            #C must be token0 of the second pair
            if(triangle[2]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[2]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]

    if triangle[1]==triangle[4] or triangle[1]==triangle[5]:
        a12=reserves[1]
        a21=reserves[0]
        #since A is token1 of the first pair, 
        #B must be token0 of the first pair
        
        #if B is token0 of the second pair
        if triangle[0]==triangle[2]:
            a23=reserves[2]
            a32=reserves[3]
            #since B is token0 of the second pair,
            #C must be token1 of the second pair
            if(triangle[3]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[3]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]
        if triangle[1]==triangle[3]:
            a23=reserves[3]
            a32=reserves[2]
            #since B is token1 of the second pair,
            #C must be token0 of the second pair
            if(triangle[2]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[2]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]

#    print(str(a12)+" a12")
#    print(str(a21)+" a21")
#    print(str(a23)+" a23")
#    print(str(a32)+" a32")
#    print(str(a13)+" a13")
#    print(str(a31)+" a31")
    return a12,a21,a23,a32,a13,a31


def CalculatorSetOrderTokens(triangle):
    #TODO: use this logic even on the function above
    #A->B B->C C->A
    #if triangle[1] is A, swap order
    if triangle[1]==triangle[4] or triangle[1]==triangle[5]:
        temp=triangle[1]
        triangle[1]=triangle[0]
        triangle[0]=temp

    #if triangle[3] is B, swap order (because C should be there)
    if triangle[3]==triangle[0] or triangle[3]==triangle[1]:
        temp = triangle[3]
        triangle[3] = triangle[2]
        triangle[2] = temp

    # if triangle[5] is C, swap order (because A should be there)
    if triangle[5] == triangle[3] or triangle[5] == triangle[2]:
        temp = triangle[5]
        triangle[5] = triangle[4]
        triangle[4] = temp

    return triangle




##This function returns [A,B,C,A] to be used in the uniswap functions
def CalculatorSetOrderTokensABC(triangle):
    #A->B B->C C->A
    #if triangle[1] is A, swap order
    if triangle[1]==triangle[4] or triangle[1]==triangle[5]:
        a=triangle[1]
    else: a=triangle[0]

    #if triangle[3] is B, swap order (because C should be there)
    if triangle[3]==triangle[0] or triangle[3]==triangle[1]:
        b=triangle[3]
    else: b=triangle[2]

    # if triangle[5] is C, swap order (because A should be there)
    if triangle[5] == triangle[3] or triangle[5] == triangle[2]:
        c=triangle[5]
    else: c=triangle[4]

    tokens=[]
    tokens.append(a)
    tokens.append(b)
    tokens.append(c)
    tokens.append(a)

    return tokens


