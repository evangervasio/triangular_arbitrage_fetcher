import requests
from fetch import creds

"""
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
- `int`: The gas price in Gwei for the selected network. Returns `-1` if the network is unsupported."""
def FetchGasPrice(selectedSwap):

    if selectedSwap.Network=="Polygon":
        response = requests.get("https://gpoly.blockscan.com/gasapi.ashx?apikey=key&method=pendingpooltxgweidata")
        data = response.json()
        return data["result"]["rapidgaspricegwei"]

    elif selectedSwap.Network=="Ethereum":
        url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={creds.etherscan}"
        response = requests.get(url)
        data = response.json()
        return int(data["result"]["SafeGasPrice"])


    return -1

"""
This function retrieves the price of a token (specified by its contract address) in USD and then converts 
this price into WMATIC using the current USD value of WMATIC. The function interacts with the CoinGecko API 
to obtain both the token price in USD and the WMATIC price in USD.

### Parameters:
- `token` (str): The contract address of the token on the Polygon network. This address should be provided as a string.

### Returns:
- `price_in_wmatic` (float): The price of the token in WMATIC.
"""
def FetchTokenPriceInWmatic(token):

    token=token.lower()

    api_endpoint = 'https://api.coingecko.com/api/v3/simple/token_price/polygon-pos'
    params = {
        'vs_currencies': 'usd',
        'contract_addresses': token,
    }

    response = requests.get(api_endpoint, params=params)
    data = response.json()

    price_in_usd = data[0]['usd']

    api_endpoint = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'wmatic',
        'vs_currencies': 'usd'
    }

    response = requests.get(api_endpoint, params=params)
    data = response.json()

    wmatic_price_in_usd = data['wmatic']['usd']

    price_in_wmatic = price_in_usd / wmatic_price_in_usd

    return price_in_wmatic

