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