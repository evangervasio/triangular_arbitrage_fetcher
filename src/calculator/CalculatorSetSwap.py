from decimal import Decimal

def CalculatorSetSwap(triangle, reserves):
    a12=Decimal(0)
    a21=Decimal(0)
    a23=Decimal(0)
    a32=Decimal(0)
    a13=Decimal(0)
    a31=Decimal(0)

    if triangle[0]==triangle[4] or triangle[0]==triangle[5]:
        a12=reserves[0]
        a21=reserves[1]

        

        if triangle[1]==triangle[2]:
            a23=reserves[2]
            a32=reserves[3]

            if(triangle[3]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[3]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]
        if triangle[1]==triangle[3]:
            a23=reserves[3]
            a32=reserves[2]

            if(triangle[2]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[2]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]

    if triangle[1]==triangle[4] or triangle[1]==triangle[5]:
        a12=reserves[1]
        a21=reserves[0]

        if triangle[0]==triangle[2]:
            a23=reserves[2]
            a32=reserves[3]

            if(triangle[3]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[3]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]
        if triangle[1]==triangle[3]:
            a23=reserves[3]
            a32=reserves[2]

            if(triangle[2]==triangle[4]):
                a13=reserves[5]
                a31=reserves[4]
            if(triangle[2]==triangle[5]):
                a13=reserves[4]
                a31=reserves[5]

    return a12,a21,a23,a32,a13,a31

#Unused
def CalculatorSetOrderTokens(triangle):

    if triangle[1]==triangle[4] or triangle[1]==triangle[5]:
        temp=triangle[1]
        triangle[1]=triangle[0]
        triangle[0]=temp

    if triangle[3]==triangle[0] or triangle[3]==triangle[1]:
        temp = triangle[3]
        triangle[3] = triangle[2]
        triangle[2] = temp

    if triangle[5] == triangle[3] or triangle[5] == triangle[2]:
        temp = triangle[5]
        triangle[5] = triangle[4]
        triangle[4] = temp

    return triangle




def CalculatorSetOrderTokensABC(triangle):

    if triangle[1]==triangle[4] or triangle[1]==triangle[5]:
        a=triangle[1]
    else: a=triangle[0]

    if triangle[3]==triangle[0] or triangle[3]==triangle[1]:
        b=triangle[3]
    else: b=triangle[2]

    if triangle[5] == triangle[3] or triangle[5] == triangle[2]:
        c=triangle[5]
    else: c=triangle[4]

    tokens=[]
    tokens.append(a)
    tokens.append(b)
    tokens.append(c)
    tokens.append(a)

    return tokens


