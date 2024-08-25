import decimal
from decimal import Decimal


"""
Truncates a decimal number to a specified number of decimal places without rounding.

### Parameters:
- `number`: The decimal number to be truncated.
- `decimals`: The number of decimal places to truncate the number to.

### Returns:
- `Decimal`: The truncated decimal number with the specified number of decimal places, without rounding.
"""
def CalculatorTruncate(number, decimals):

    i = Decimal(1)/pow(Decimal(10), decimals)

    return decimal.Decimal(number).quantize(decimal.Decimal(str(i)), rounding=decimal.ROUND_DOWN)