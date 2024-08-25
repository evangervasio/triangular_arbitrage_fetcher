This function interacts with the liquidity pool contract (referred to as `pair`) on a Uniswap fork to retrieve the 
current reserves of the two tokens involved. These reserves are crucial for determining the price impact and 
calculating potential arbitrage opportunities.
### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, including attributes such as `Router`, 
  `Factory`, and `Network`.
- `pair`: The address of the liquidity pool contract from which the reserves will be fetched.

### Returns:
- `tuple`: A tuple containing the reserve balances of the two tokens in the liquidity pool. The reserves are returned 
  as two separate values corresponding to the two tokens in the pair.