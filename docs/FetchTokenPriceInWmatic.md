This function retrieves the price of a token (specified by its contract address) in USD and then converts 
this price into WMATIC using the current USD value of WMATIC. The function interacts with the CoinGecko API 
to obtain both the token price in USD and the WMATIC price in USD.

### Parameters:
- `token` (str): The contract address of the token on the Polygon network. This address should be provided as a string.

### Returns:
- `price_in_wmatic` (float): The price of the token in WMATIC.