# Documentation Index

### Table of Contents:

1. [Calculator Functions](#calculator-functions)
   - [CalculatorAmountIter](#calculatoramountiter)
   - [CalculatorDecimalIn](#calculatordecimalin)
   - [CalculatorPriceImpact](#calculatorpriceimpact)
   - [CalculatorSetOrderTokensABC](#calculatorsetordertokensabc)
   - [CalculatorSetSwap](#calculatorsetswap)
   - [CalculatorSwap](#calculatorswap)
   - [CalculatorTokens](#calculatortokens)
   - [CalculatorTruncate](#calculatortruncate)

2. [Fetch Functions](#fetch-functions)
   - [Fetch_all_reserves](#fetch_all_reserves)
   - [Fetch_pair_data](#fetch_pair_data)
   - [FetchArbitrage](#fetcharbitrage)
   - [FetchExchangeInfo](#fetchexchangeinfo)
   - [FetchGasPrice](#fetchgasprice)
   - [FetchGetAmountsOut](#fetchgetamountsout)
   - [FetchReserves](#fetchreserves)
   - [FetchTokenPriceInWmatic](#fetchtokenpriceinwmatic)
   - [FetchTrianglesNew](#fetchtrianglesnew)

3. [Executer Functions](#executer-functions)
   - [ExecuterSwap](#executerswap)

---



## Calculator Functions


## CalculatorAmountIter

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

---

## CalculatorDecimalIn

This function determines the decimal position number (p.e. 18) of the token we are putting an amount input in and getting
an amount output from in a triangular arbitrage transaction.
### Parameters:
- `maxAmount`: The maximum amount of the token that can be used as input for the arbitrage transaction.
- `decimals`: The number of decimal places used by the token, relevant for precise calculations.
- `a12`, `a21`, `a23`, `a32`, `a13`, `a31`: The reserve balances of the tokens involved in the triangular arbitrage, 
  used for calculating potential outputs.
- `r1`, `r2`: Ratio or fee parameters, representing Uniswap forks fees.

### Returns:
- `Decimal`: The optimal input amount of the token that should be used for the arbitrage transaction to achieve 
  the maximum possible profit.This function determines the decimal position number (p.e. 18) of the token we are putting an amount input in and getting
an amount output from in a triangular arbitrage transaction.

### Parameters:
- `triangle`: An array representing the triangular arbitrage transaction, where tokens are ordered in a specific
  sequence.
- `decimals`: A list or array containing the decimal precision for two tokens involved in the transaction.

### Returns:
- `int`: The number of decimal places used by the token that is being used as input for the arbitrage transaction.Calculates the price impact for trades on an Automated Market Maker (AMM) like Uniswap.

---

## CalculatorPriceImpact

This function computes the price impact of a swap, which is the effect of a swap on the price of a token within 
an AMM liquidity pool. The price impact is derived from the Uniswap pricing formulas, reflecting how the price changes 
in response to a swap, based on the input and output amounts of the tokens involved.

### Parameters:
- `a12`: Reserve of the first token in the pool.
- `a21`: Reserve of the second token in the pool.
- `amountIn1`: Amount of the first token being input into the pool.
- `amountIn2`: Amount of the second token being input into the pool.
- `amountOut1`: Amount of the first token being output from the pool.
- `amountOut2`: Amount of the second token being output from the pool.

### Returns:
- `Decimal`: The price impact of the trade, indicating the change in price resulting from the specified swap parameters.The `CalculatorSetOrderTokensABC` function arranges tokens in a specified order to represent the sequence of trades 
in a triangular arbitrage transaction. In this context, triangular arbitrage involves trading between three different 
tokens in such a way that the trader starts and ends with the same token, ideally generating a profit in the process.

---

## CalculatorSetOrderTokensABC
Calculates the price impact for trades on an Automated Market Maker (AMM) like Uniswap.

This function computes the price impact of a swap, which is the effect of a swap on the price of a token within 
an AMM liquidity pool. The price impact is derived from the Uniswap pricing formulas, reflecting how the price changes 
in response to a swap, based on the input and output amounts of the tokens involved.

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
  critical requirement for triangular arbitrage strategies.The `CalculatorSetSwap` function returns the ordered reserves of tokens involved in a triangular arbitrage, based on their 
positions in the triangle and respective liquidity pools. This ordering is crucial for calculating potential arbitrage 
profits as it determines the correct sequence of reserve amounts.

---

## CalculatorSetSwap
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
  it adaptable to different arbitrage opportunities.The `CalculatorSwap` function simulates a triangular arbitrage transaction, calculating the output amount after a 
series of swaps across three different trading pairs. The function leverages price impact calculations at each stage 
of the swap to determine the final output amount.

---

## CalculatorSwap
The `CalculatorSwap` function simulates a triangular arbitrage transaction, calculating the output amount after a 
series of swaps across three different trading pairs. The function leverages price impact calculations at each stage 
of the swap to determine the final output amount.
### Detailed Function Workflow:

1. **Initial Swap (First Pair):**
   - The function starts by calculating the output amount after swapping an initial input (`optAmountInA`) of the 
     first token reserve (`a12`) with the second token reserve (`a21`). This is done using the `CalculatorPriceImpact.CalculatorPriceImpact` 
     function, which accounts for price impact based on liquidity reserves. 
   - The result of this swap, `amountOut1`, is scaled by the ratio `r2` which represents the fee used in Uniswap forks smart contract calculations.

2. **Second Swap (Second Pair):**
   - Next, the function uses `amountOut1` as the input for the second swap, where the second token is swapped 
     with the third token. Again, the `CalculatorPriceImpact.CalculatorPriceImpact` function is used to 
     account for price impact. 
   - The output of this swap `amountOut2` is also scaled by `r2`.

3. **Final Swap (Third Pair):**
   - In the final step, `amountOut2` is swapped for the first token, completing the triangular arbitrage. 
     The output, `amountOut3`, represents the final amount obtained after the entire sequence of swaps.
   - The function returns `amountOut3` as the calculated output amount after the arbitrage.

### Parameters:
- `optAmountInA`: The optimal input amount of the first token to be used in the triangular arbitrage.
- `a12`: Reserve of the first token in the first pool.
- `a21`: Reserve of the second token paired with the first token in the first pool.
- `a23`: Reserve of the second token in the second pool.
- `a32`: Reserve of the third token paired with the second token in the second pool.
- `a13`: Reserve of the third token in the third pool.
- `a31`: Reserve of the first token paired with the third token in the third pool.
- `r1`: Uniswap forks fee.
- `r2`: Uniswap forks fee.

### Returns:
- `amountOut3`: The final output amount of the first token after completing the triangular arbitrage, taking into 
  account the price impacts at each stage of the swap.

### Key Features:
- **Triangular Arbitrage Simulation:** The function effectively simulates the entire arbitrage process across three 
  trading pairs, providing a realistic estimate of the final output.
- **Price Impact Consideration:** By integrating the `CalculatorPriceImpact.CalculatorPriceImpact` function, the 
  function accurately accounts for the price impact of each swap, which is crucial for determining potential profitability.
- **Flexible Input Handling:** The use of `r1` and `r2` allows for flexible adjustment of the input and output amounts 
  based on varying DEX fees.The `CalculatorTokens` function filters a CSV file containing triangular arbitrage opportunities (referred to as 
"triangles") based on inclusion and exclusion criteria specified in separate CSV files. The resulting filtered 
triangles are then saved into a new CSV file.

---
## CalculatorTokens
The `CalculatorTokens` function filters a CSV file containing triangular arbitrage opportunities (referred to as 
"triangles") based on inclusion and exclusion criteria specified in separate CSV files. The resulting filtered 
triangles are then saved into a new CSV file.
### Detailed Function Workflow:

1. **Paths Setup:**
   - The function constructs relative paths for the required CSV files:
     - `tokensToInclude.csv`: Contains tokens to include in the filtering process.
     - `tokensToExclude.csv`: Contains tokens to exclude from the filtering process.
     - `trianglesFilter.csv`: The input file containing triangles to be filtered, which will also serve as the output 
       file after filtering.

2. **Read Inclusion Tokens:**
   - The function reads `tokensToInclude.csv` to create a list of tokens (`tokensToInclude`). Only triangles containing 
     these tokens will be retained during the initial filtering phase.

3. **Read Exclusion Tokens:**
   - Similarly, `tokensToExclude.csv` is read to create a list of tokens (`tokensToExclude`). Any triangle containing 
     these tokens will be removed during the subsequent filtering phase.

4. **Filter Triangles by Inclusion:**
   - The function reads the triangles from `trianglesFilter.csv` and filters them based on the inclusion tokens. 
     A triangle is retained if it contains at least one of the tokens in `tokensToInclude`.

5. **Filter Triangles by Exclusion:**
   - The filtered list of triangles is further processed to remove any triangles containing tokens from 
     `tokensToExclude`.

6. **Remove Duplicates:**
   - The function removes any duplicate triangles from the filtered list by converting the list of lists into a 
     list of tuples (for hashing), then back into a list of lists.

7. **Write the Filtered Triangles:**
   - The final list of filtered triangles is written back to the `trianglesFilter.csv` file, overwriting its previous content.

### Parameters:
- `selectedSwap`: An object that contains relevant information about the swap, including its name, 
  which is used to determine file paths.

### CSV Files Used:
- `tokensToInclude.csv`: Contains the tokens to include in the filtering process.
- `tokensToExclude.csv`: Contains the tokens to exclude from the filtering process.
- `trianglesFilter.csv`: Both the input and output file for triangles before and after filtering.

### Returns:
- The function does not return any value but writes the filtered triangles to a CSV file.

### Key Features:
- **Flexible Token Filtering:** The function allows for both inclusion and exclusion of specific tokens in the 
  arbitrage triangles, making it highly customizable.
- **Duplicate Removal:** The function ensures that the output contains only unique triangles, avoiding redundant data.Truncates a decimal number to a specified number of decimal places without rounding.

---
## CalculatorTruncate
Truncates a decimal number to a specified number of decimal places without rounding.

### Parameters:
- `number`: The decimal number to be truncated.
- `decimals`: The number of decimal places to truncate the number to.

### Returns:
- `Decimal`: The truncated decimal number with the specified number of decimal places, without rounding.The `FetchArbitrage` function scans through every triangular arbitrage opportunity listed in a CSV file associated 
with a specific decentralized exchange (DEX) swap configuration. It calculates the potential profitability of each 
triangular arbitrage scenario by taking into account various factors including blockchain transaction fees, DEX fees, price impact, 
and the user's maximum input amount. When a profitable arbitrage opportunity is identified, the function is designed to 
simulate its execution without actually initiating the transaction, for security purposes.

---
## Fetch Functions
## FetchArbitrage
The `FetchArbitrage` function scans through every triangular arbitrage opportunity listed in a CSV file associated 
with a specific decentralized exchange (DEX) swap configuration. It calculates the potential profitability of each 
triangular arbitrage scenario by taking into account various factors including blockchain transaction fees, DEX fees, price impact, 
and the user's maximum input amount. When a profitable arbitrage opportunity is identified, the function is designed to 
simulate its execution without actually initiating the transaction, for security purposes.

### Detailed Function Workflow:

1. **Initialize Counters and Paths:**
   - The function begins by setting up the path to a CSV file containing 
     token limits specific to the selected swap (`path_token_limits`).

2. **Load Token Limits:**
   - It reads the `tokensLimits.csv` file, which contains limits on the amount of specific tokens that can be used in 
     arbitrage, and stores these limits in the `tokensLimits` list.

3. **Determine Triangles Source:**
   - Based on the `filter` parameter, it decides whether to use a filtered set of triangular arbitrage opportunities 
     (`trianglesFilter.csv`) or the complete set (`triangles.csv`).

4. **Fetch Reserves:**
   - The function retrieves the current reserve data for each potential arbitrage triangle from the blockchain, using 
     the `fetch_all_reserves` function.

5. **Iterate Through Triangles:**
   - The function enters a loop where it reads through each triangle configuration (set of three token pairs) from the 
     CSV file.

6. **Extract and Convert Reserve Data:**
   - For each triangle, it extracts reserve and decimal data, converting them into a `decimal.Decimal` format suitable 
     for precise calculations.

7. **Calculate Arbitrage Parameters:**
   - The function calculates the ordered reserves amounts (`a12`, `a21`, `a23`, `a32`, `a13`, `a31`) required to evaluate 
     the potential arbitrage profit.
   - It determines the maximum allowable input amount (`maxAmount`) for the arbitrage based on token limits or a 
     proportion of the calculated amount.

8. **Optimal Input Calculation:**
   - Using the `CalculatorAmountIter` function, it computes the optimal input amount that would yield the highest 
     profit given the reserves and trading parameters.

9. **Profitability Check:**
   - The function then evaluates whether the calculated profit is positive. If so, it logs the potential profit and 
     details of the triangle.

10. **Transaction Simulation:**
    - If the arbitrage is potentially profitable, the function continues to simulate the transaction:
        - It calculates the output amount after accounting for fees using the `FetchGetAmountsOut` function.
        - It fetches the current gas price and determines the overall transaction cost.
        - If the transaction remains profitable after considering blockchain fees, the function simulates sending the 
          transaction for execution.

11. **Logging and Repeat Cycle:**
    - The function logs the results of each iteration, including errors or unprofitable scenarios, and then repeats the 
      cycle for continuous monitoring of arbitrage opportunities.

### Security Note:
- The function is configured in this state to only simulate the execution of profitable arbitrage opportunities. 
  Actual transactions are not executed, providing a safeguard against unintended trades during development and testing.

### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, with attributes such as the factory and router smart contracts, the name and the network (polygon, ethereum..).
- `filter`: A boolean flag indicating whether to use a filtered set of arbitrage triangles (`True`) or the complete set (`False`).

### Returns:
- None. The function operates in a continuous loop, logging its findings and simulations to the console.

---
## FetchExchangeInfo
Automatically fetches all pairs of a given Uniswap fork router contract without an API, then calculates all the possible triangles for triangular arbitrage.

### Key Features:
- **No API Dependency:** The function directly interacts with the blockchain via Web3 to retrieve pair information, 
  avoiding reliance on external APIs.
- **Concurrency:** Utilizes concurrent processing to efficiently handle large numbers of pairs, improving performance.
- **Automated Triangle Calculation:** After fetching pair data, it automatically calculates all possible triangular 
  arbitrage opportunities, streamlining the arbitrage discovery process.This function determines the gas price for executing transactions on either the Polygon or Ethereum network, depending 
on the `Network` attribute of the `selectedSwap` object. It uses different APIs for each network to retrieve the most 
recent gas price data.
---
## FetchGasPrice
This function determines the gas price for executing transactions on either the Polygon or Ethereum network, depending 
on the `Network` attribute of the `selectedSwap` object. It uses different APIs for each network to retrieve the most 
recent gas price data.
### Detailed Function Workflow:

1. **Check Network Type:**
   - The function checks the `Network` attribute of the `selectedSwap` object to determine which blockchain network 
     is being used (Polygon or Ethereum).

2. **Fetch Gas Price for Polygon:**
   - If the network is Polygon, the function sends a GET request to the Blockscan API's Polygon endpoint to retrieve 
     the current gas price in Gwei. Specifically, it requests the "rapid" gas price, which is the price for fast transaction 
     processing.

3. **Fetch Gas Price for Ethereum:**
   - If the network is Ethereum, the function sends a GET request to the Etherscan API's gas tracker endpoint. It retrieves 
     the "SafeGasPrice," which represents a gas price that is likely to result in a timely transaction confirmation.

4. **Return the Gas Price:**
   - The function returns the gas price as an integer value. If the network is neither Polygon nor Ethereum, the function 
     returns `-1` to indicate that the gas price could not be fetched.

### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, containing attributes such as `Network`, 
  which determines the blockchain network (Polygon, Ethereum, etc.) where the swap will take place.

### Returns:
- `int`: The gas price in Gwei for the selected network. Returns `-1` if the network is unsupported.Calls the `getAmountOut` function from the Uniswap fork's router smart contract to calculate the output amount 
for a given input amount across a specified token path (triangle).
This function is used to fetch the expected output for a swap transaction in decentralized exchanges (DEXs) that are 
forks of Uniswap, such as those on the Polygon and Ethereum networks. The calculation is done by querying the router 
contract of the selected swap.

---
## FetchGetAmountsOut
Calls the `getAmountOut` function from the Uniswap fork's router smart contract to calculate the output amount 
for a given input amount across a specified token path (triangle).
This function is used to fetch the expected output for a swap transaction in decentralized exchanges (DEXs) that are 
forks of Uniswap, such as those on the Polygon and Ethereum networks. The calculation is done by querying the router 
contract of the selected swap.
### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, containing attributes such as `Router` 
  (the address of the router contract) and `Network` (the blockchain network).
- `amountIn`: The input amount for the swap, which will be converted into an integer format.
- `triangle`: A list of token addresses representing the path of the triangular arbitrage.

### Returns:
- `int` or `list`: The output amount(s) resulting from the swap along the specified path. Returns `0` if the contract call fails.This function interacts with the liquidity pool contract (referred to as `pair`) on a Uniswap fork to retrieve the 
current reserves of the two tokens involved. These reserves are crucial for determining the price impact and 
calculating potential arbitrage opportunities.

---
## FetchReserves
This function interacts with the liquidity pool contract (referred to as `pair`) on a Uniswap fork to retrieve the 
current reserves of the two tokens involved. These reserves are crucial for determining the price impact and 
calculating potential arbitrage opportunities.
### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, including attributes such as `Router`, 
  `Factory`, and `Network`.
- `pair`: The address of the liquidity pool contract from which the reserves will be fetched.

### Returns:
- `tuple`: A tuple containing the reserve balances of the two tokens in the liquidity pool. The reserves are returned 
  as two separate values corresponding to the two tokens in the pair.This function retrieves the price of a token (specified by its contract address) in USD and then converts 
this price into WMATIC using the current USD value of WMATIC. The function interacts with the CoinGecko API 
to obtain both the token price in USD and the WMATIC price in USD.

---
## FetchTokenPriceInWmatic
This function retrieves the price of a token (specified by its contract address) in USD and then converts 
this price into WMATIC using the current USD value of WMATIC. The function interacts with the CoinGecko API 
to obtain both the token price in USD and the WMATIC price in USD.

### Parameters:
- `token` (str): The contract address of the token on the Polygon network. This address should be provided as a string.

### Returns:
- `price_in_wmatic` (float): The price of the token in WMATIC.The `FetchTrianglesNew` function identifies all possible triangles of tokens from a list of trading pairs 
in a decentralized exchange (DEX). Specifically, it calculates all valid combinations of three pairs that share tokens 
in such a way that they form a "triangle", where the tokens are interconnected, enabling a cyclic trade route.
---
## FetchTrianglesNew
The `FetchTrianglesNew` function identifies all possible triangles of tokens from a list of trading pairs 
in a decentralized exchange (DEX). Specifically, it calculates all valid combinations of three pairs that share tokens 
in such a way that they form a "triangle", where the tokens are interconnected, enabling a cyclic trade route.

### Detailed Function Workflow:

1. **Initialize File Paths:**
   - The function begins by setting up the file paths needed to locate the list of trading pairs (`pairs.csv`) associated 
     with the given swap (`swapName`). The path is constructed relative to the current directory.

2. **Load Pairs and Build Data Structures:**
   - A `defaultdict` of sets (`pairs`) is created to store each token and the set of tokens it can be traded with. 
     Additionally, a `pair_info` dictionary is initialized to store detailed information about each pair.
   - The function reads the `pairs.csv` file and processes each row to extract token pair information:
     - For each pair of tokens (`token0` and `token1`), the function updates the `pairs` dictionary to record their 
       relationship.
     - The `pair_info` dictionary is populated with detailed pair data, allowing quick access later in the process.

3. **Identify Triangular Arbitrage Opportunities:**
   - The function iterates through the `pairs` dictionary to identify all sets of three tokens that can form a triangle:
     - For each token (`token0`), it retrieves the set of tokens (`set1`) it can be traded with.
     - It then checks each token in `set1` (`token1`) to find its own set of tradeable tokens (`set2`).
     - The function identifies the intersection of `set1` and `set2` to find a common third token (`token2`) that, 
       along with `token0` and `token1`, forms a valid triangular arbitrage opportunity.
     - Triangles are recorded only if `token0` and `token2` are distinct.

4. **Compile Full Triangle Information:**
   - For each identified triangle, the function gathers detailed information for all three pairs involved using the 
     `pair_info` dictionary. It retrieves data such as token addresses, reserve values, and other relevant information.
   - This information is compiled into a list (`trianglesFull`) that contains all the necessary details for each 
     triangular arbitrage opportunity.

5. **Save Triangles to CSV:**
   - The function constructs a path for saving the triangle data to a new CSV file (`triangles.csv`), which is stored in 
     a directory specific to the swap (`swapName`). If the directory does not exist, it is created.
   - The compiled triangle data is written to the CSV file, with each row representing a fully described triangular 
     arbitrage opportunity.

### Parameters:
- `swapName`: A string representing the name of the DEX swap in use. This is used to locate the appropriate 
  input and output files.

### Returns:
- None. The function saves the calculated triangular arbitrage opportunities to a CSV file for further analysis.

### Key Features:
- **Comprehensive Triangle Detection:** The function efficiently identifies all valid triangular arbitrage opportunities 
  by leveraging the relationships between tokens in the trading pairs.
- **Detailed Data Compilation:** Each identified triangle is supplemented with comprehensive data from the original 
  trading pairs, ensuring that all necessary information is available for subsequent use.
- **Automated File Handling:** The function handles file path construction and ensures that the output directory exists 
  before saving the results.Fetches all the reserves of the triangles listed in a CSV file for a specific swap configuration.

---
## fetch_all_reserves
This function retrieves reserve data for each token pair in triangular arbitrage opportunities. It reads from a CSV 
file containing triangular arbitrage data, and concurrently fetches reserve information for each token pair in the 
triangles using multiple threads. The results are then organized and returned in a structured format.

### Detailed Function Workflow:

1. **Determine CSV Path:**
   - Based on the `filter` parameter, the function sets the path to the appropriate CSV file (`trianglesFilter.csv` 
     for filtered results or `triangles.csv` for the complete set).

2. **Initialize Reserve Storage:**
   - An empty dictionary, `reserves`, is initialized to store the reserve data for each triangle.

3. **Read CSV File:**
   - The function opens and reads the CSV file containing the triangle data. It processes each row to fetch reserve 
     data for the tokens listed in the triangle.

4. **Fetch Reserves Concurrently:**
   - Using a thread pool, the function submits tasks to concurrently fetch reserve data for each token pair in the 
     triangles. Each task is associated with the specific row and token pair index.

5. **Collect and Organize Results:**
   - As tasks complete, the function collects the results and organizes them into the `reserves` dictionary. The dictionary 
     keys are row indices, and the values are dictionaries containing reserves for each token pair.

### Parameters:
- `selectedSwap`: An object representing the selected swap configuration, including network and other relevant details.
- `filter`: A boolean flag indicating whether to use a filtered CSV file (`True`) or the complete CSV file (`False`).

### Returns:
- `dict`: A dictionary where each key is a row index from the CSV file, and the value is another dictionary containing 
  the reserves for the token pairs in that row. If a token pair's reserve fetching fails, it is logged but does not disrupt 
  the entire process.Returns essential data about a token pair, including the tokens involved, their symbols, and decimal places.

---
## fetch_pair_data
This function retrieves information about a token pair contract on the blockchain. It uses the pair contract's ABI to 
fetch addresses of the two tokens involved and then queries each token's contract for additional details such as their 
decimals and symbols. The function includes retry logic to handle temporary errors and ensure successful data retrieval.

### Parameters:
- `pair`: The address of the pair contract for which data needs to be fetched.

### Returns:
- `tuple`: A tuple containing:
  - The pair address.
  - The address of the first token (`token0`).
  - The address of the second token (`token1`).
  - The decimal places for the first token (`token0_decimals`).
  - The decimal places for the second token (`token1_decimals`).
  - The symbol of the first token (`symbol0`).
  - The symbol of the second token (`symbol1`).
If any of the values could not be retrieved, they are returned as `None`.
---
## Executer Functions
## ExecuterSwap

The `ExecuterSwapPolygon` function executes a triangular arbitrage transaction on a Polygon network Uniswap fork. 
This function handles all aspects of the transaction, including gas price management, token approval, and the swap 
itself. The actual sending of the transaction is commented out for security reasons.

### Detailed Function Workflow:

1. **Gas Price Check:**
   - The function first checks if the provided gas price (`gwei`) exceeds 500 gwei. If it does, the function 
     halts execution to avoid excessively high transaction costs.

2. **Token Approval (Optional):**
   - If `needToApprove` is `True`, the function will approve the router contract to spend a large amount of the 
     specified token on behalf of the user, doing this will prevent the need of doing multiple approval transactions for smaller amounts each time.
     This process involves:
     - Creating and signing an approval transaction.
     - Sending the signed transaction to the blockchain.
     - Pausing for a minute to ensure the approval transaction is processed.
     - Re-fetching the current gas price to ensure the transaction uses an optimal gas fee.

3. **Gas Price Re-Check:**
   - After approval, the function checks the gas price again. If it exceeds 500 gwei, the function halts to avoid 
     executing the swap with a high gas fee.

4. **Swap Transaction Preparation:**
   - Depending on whether the token has internal fees (`tokenFees` flag), the function prepares the appropriate 
     swap transaction:
     - **With Fees:** Uses `swapExactTokensForTokensSupportingFeeOnTransferTokens`.
     - **Without Fees:** Uses `swapExactTokensForTokens`.

5. **Transaction Signing:**
   - The function signs the swap transaction with the user's private key.

6. **Transaction Submission:**
   - The code that sends the signed transaction to the blockchain is commented out for security reasons.

### Parameters:
- `selectedSwap`: An object containing relevant swap details, such as the router contract address.
- `amountIn`: The amount of the initial token to be swapped.
- `minAmountOut`: The minimum acceptable amount of the final token after the swap.
- `path`: A list of token addresses representing the swap path (e.g., [TokenA, TokenB, TokenC]).
- `gwei`: The gas price in gwei to be used for the transaction.
- `needToApprove`: A boolean flag indicating whether token approval is required before the swap.
- `tokenFees`: A boolean flag indicating whether the token involves internal transfer fees, requiring the use of 
  a different swap function.

### Returns:
- The function does not return any value but prints execution details.

### Security Notes:
- **Gas Price Management:** The function includes checks to prevent executing transactions with overly high gas fees, 
  protecting the user from excessive costs.
- **Commented Transaction Sending:** The line that actually sends the swap transaction is commented out to prevent 
  accidental execution, which could lead to unintended blockchain interactions.

### Key Features:
- **Flexible Execution:** The function can handle both fee-on-transfer tokens and standard tokens, adapting the swap 
  method accordingly.
- **Automatic Approval Handling:** If required, the function can automatically approve the router contract to spend 
  the user's tokens.
- **Gas Price Monitoring:** The function dynamically monitors and adjusts for gas prices, ensuring the transaction 
  is executed under optimal conditions.
- **Uniswap Fork Compatibility:** The function is highly dynamic and works with every Uniswap fork on the Polygon network,
 making it adaptable to a wide range of decentralized exchanges.

### Potential Risks:
- If the gas price spikes suddenly after the initial check, the transaction may still go through at a higher cost 
  than expected. This is mitigated by a second gas price check after the approval step.
- The function assumes the provided `gwei` and `private_key` are valid and that the user has sufficient funds for gas.