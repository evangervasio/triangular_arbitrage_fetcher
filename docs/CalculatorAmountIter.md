Calculates the optimal input amount of a token for a triangular arbitrage transaction to maximize returns, 
using an iterative approach.

This function aims to determine the optimal amount of a token (e.g., token A) that should be used as the input 
in a triangular arbitrage transaction to yield the maximum possible profit. The calculation is performed 
iteratively by testing different input amounts within the specified range and selecting the one that results in the 
highest profit.

### Detailed Function Workflow:

1. **Initialize Variables:**
   - The function initializes key variables:
     - `i` is the step size, calculated as the ceiling of `maxAmount` divided by 30,000. This controls the increment 
       size for the input amount in each iteration.
     - `maxProfit` starts at zero and tracks the highest profit encountered during the iterations.
     - `optInput` is set to zero and will store the optimal input amount that yields the maximum profit.
     - `amount` is initialized to one and represents the current input amount being tested.

2. **Iterative Calculation:**
   - The function enters a loop that continues until `amount` exceeds `maxAmount`:
     - For each iteration, it calculates the expected output (`output`) using the `CalculatorSwap` function.
     - The potential profit (`profit`) is calculated as the difference between the `output` and the `amount`.
     - If the current `profit` exceeds `maxProfit`, the function updates `maxProfit` and stores the corresponding 
       `amount` as `optInput`.

3. **Step Size Adjustment:**
   - After each iteration, `amount` is incremented by `i`, allowing the function to explore the next potential input 
     amount.

4. **Return Optimal Input:**
   - Once the loop completes, the function returns `optInput`, which represents the input amount that results in the 
     highest calculated profit for the triangular arbitrage transaction.

### Parameters:
- `maxAmount`: The maximum amount of the token that can be used as input for the arbitrage transaction.
- `decimals`: The number of decimal places used by the token, relevant for precise calculations.
- `a12`, `a21`, `a23`, `a32`, `a13`, `a31`: The reserve balances of the tokens involved in the triangular arbitrage, 
  used for calculating potential outputs.
- `r1`, `r2`: Ratio or fee parameters, representing Uniswap forks fees.

### Returns:
- `Decimal`: The optimal input amount of the token that should be used for the arbitrage transaction to achieve 
  the maximum possible profit.