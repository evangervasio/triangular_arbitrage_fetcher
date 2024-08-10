import decimal
from decimal import Decimal

##This function truncates a Decimal
def CalculatorTruncate(number, decimals):

    i = Decimal(1)/pow(Decimal(10), decimals)

    return decimal.Decimal(number).quantize(decimal.Decimal(str(i)), rounding=decimal.ROUND_DOWN)