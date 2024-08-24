from decimal import Decimal

"""
The `CalculatorSetSwap` function returns the ordered reserves of tokens involved in a triangular arbitrage, based on their 
positions in the triangle and respective liquidity pools. This ordering is crucial for calculating potential arbitrage 
profits as it determines the correct sequence of reserve amounts.

### Detailed Function Workflow:

1. **Initialize Reserve Variables:**
   - The function begins by initializing six variables (`a12`, `a21`, `a23`, `a32`, `a13`, `a31`), these variables are initialized to `Decimal(0)` to handle large 
     or precise values.

2. **Determine the First Token Pair (a12 and a21):**
   - The function checks if the first token in the triangle (`triangle[0]`) matches either the fourth or fifth token 
     (`triangle[4]` or `triangle[5]`). This match identifies the first token pair in the arbitrage:
     - If a match is found, `a12` (the reserve of the first token) is assigned the value of `reserves[0]`, and `a21` 
       (the reserve of the second token in the pair) is assigned the value of `reserves[1]`.
     - The reverse assignment happens if `triangle[1]` matches `triangle[4]` or `triangle[5]`, where `a12` is assigned 
       `reserves[1]` and `a21` is assigned `reserves[0]`.

3. **Determine the Second Token Pair (a23 and a32):**
   - After establishing the first token pair, the function identifies the second token pair by checking the relationship 
     between the second and third tokens in the triangle (`triangle[1]`, `triangle[2]`, and `triangle[3]`):
     - If `triangle[1]` matches `triangle[2]`, `a23` is assigned `reserves[2]`, and `a32` is assigned `reserves[3]`.
     - If `triangle[1]` matches `triangle[3]`, `a23` is assigned `reserves[3]`, and `a32` is assigned `reserves[2]`.

4. **Determine the Third Token Pair (a13 and a31):**
   - The function then identifies the third token pair based on the remaining tokens in the triangle:
     - If `triangle[3]` matches `triangle[4]`, `a13` is assigned `reserves[5]`, and `a31` is assigned `reserves[4]`.
     - If `triangle[3]` matches `triangle[5]`, `a13` is assigned `reserves[4]`, and `a31` is assigned `reserves[5]`.
     - Similar checks and assignments occur for other token combinations involving `triangle[2]`, `triangle[4]`, and `triangle[5]`.

5. **Return Ordered Reserves:**
   - After determining all the necessary token pairs, the function returns the ordered reserves (`a12`, `a21`, `a23`, 
     `a32`, `a13`, and `a31`). These reserves represent the liquidity available for each pair of tokens involved in 
     the triangular arbitrage.

### Parameters:
- `triangle`: A list or array representing the tokens involved in the triangular arbitrage opportunity. The tokens are 
  not initially ordered and need to be arranged according to their respective reserves in the liquidity pools.
- `reserves`: A list or array containing the reserve amounts for the tokens involved in the arbitrage. The order of 
  reserves in this list corresponds to the token pairs in the `triangle`.

### Returns:
- A tuple containing six `Decimal` values representing the ordered reserves:
  - `a12`: Reserve of the first token in the first pool.
  - `a21`: Reserve of the second token paired with the first token in the first pool.
  - `a23`: Reserve of the second token in the second pool.
  - `a32`: Reserve of the third token paired with the second token in the second pool.
  - `a13`: Reserve of the third token in the third pool.
  - `a31`: Reserve of the first token paired with the third token in the third pool.

### Key Features:
- **Accurate Reserve Ordering:** The function correctly identifies and orders the reserves of tokens based on their 
  roles in the triangular arbitrage, ensuring the right sequence is used for profit calculation.
- **Precision Handling:** By using `Decimal` for reserve values, the function ensures high precision in calculations, 
  which is critical in arbitrage scenarios where small differences can determine profitability.
- **Versatile Token Matching:** The function can handle various configurations of token pairs in the triangle, making 
  it adaptable to different arbitrage opportunities.
"""
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



"""
The `CalculatorSetOrderTokensABC` function arranges tokens in a specified order to represent the sequence of trades 
in a triangular arbitrage transaction. In this context, triangular arbitrage involves trading between three different 
tokens in such a way that the trader starts and ends with the same token, ideally generating a profit in the process.

### Detailed Function Workflow:

1. **Identify Token 'A' (Starting and Ending Token):**
   - The function first identifies token 'A', which is the token that the transaction starts and ends with. This token 
     appears both at the first and last positions in the ordered array. The function checks if `triangle[1]` matches 
     either `triangle[4]` or `triangle[5]`:
     - If a match is found, `triangle[1]` is assigned as token 'A'.
     - Otherwise, `triangle[0]` is assigned as token 'A'.

2. **Identify Token 'B' (Intermediate Token 1):**
   - The function then identifies token 'B', which is the second token in the sequence. This token is traded with token 'A'.
     - It checks if `triangle[3]` matches either `triangle[0]` or `triangle[1]`:
     - If a match is found, `triangle[3]` is assigned as token 'B'.
     - Otherwise, `triangle[2]` is assigned as token 'B'.

3. **Identify Token 'C' (Intermediate Token 2):**
   - Finally, the function identifies token 'C', which is the third token in the sequence and is traded with token 'B'. 
     Token 'C' is then traded back to token 'A' to complete the triangle.
     - The function checks if `triangle[5]` matches either `triangle[3]` or `triangle[2]`:
     - If a match is found, `triangle[5]` is assigned as token 'C'.
     - Otherwise, `triangle[4]` is assigned as token 'C'.

4. **Create Ordered Token List:**
   - The function constructs a list (`tokens`) that represents the ordered sequence of tokens in the triangular arbitrage 
     transaction. The sequence is arranged as [A, B, C, A], ensuring that the trade begins and ends with token 'A'.

5. **Return Ordered Token List:**
   - The function returns the `tokens` list, which will then be used in further calculations and to execute the triangular 
     arbitrage transaction.

### Parameters:
- `triangle`: A list or array representing the tokens involved in the triangular arbitrage opportunity. The tokens in the 
  `triangle` array are not initially ordered and need to be arranged according to the sequence of trades.

### Returns:
- A list (`tokens`) containing the ordered sequence of tokens [A, B, C, A], where:
  - `A` is the token used as both the input and output in the arbitrage transaction.
  - `B` and `C` are the intermediate tokens involved in the triangular trade.

### Key Features:
- **Automatic Token Ordering:** The function intelligently identifies and orders the tokens involved in a triangular 
  arbitrage trade, ensuring the correct sequence is followed for profit calculation and transaction execution.
- **Versatile Token Handling:** The function can handle different triangular configurations by determining the correct 
  sequence based on token relationships within the `triangle` array.
- **Output Consistency:** The function guarantees that the output list starts and ends with the same token, which is a 
  critical requirement for triangular arbitrage strategies.
"""
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


