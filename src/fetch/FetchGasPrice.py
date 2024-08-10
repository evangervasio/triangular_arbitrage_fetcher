import requests
# returns gas price in gwei
import creds
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

##Fetches the price of tokenA in tokenB
#p.e tokenA=USDC tokenB=ETH
#result=2k
def FetchTokenPriceInWmatic(token):

    token=token.lower()
    # Define the contract addresses of the tokens

    # Define the API endpoint and parameters
    api_endpoint = 'https://api.coingecko.com/api/v3/simple/token_price/polygon-pos'
    params = {
        'vs_currencies': 'usd',
        'contract_addresses': token,
    }

    # Send a GET request to the API and parse the response
    response = requests.get(api_endpoint, params=params)
    data = response.json()
    print(data)

    price_in_usd = data[0]['usd']

    #Fetch wmatic price in USD
    api_endpoint = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'wmatic',
        'vs_currencies': 'usd'
    }

    # Send a GET request to the API and parse the response
    response = requests.get(api_endpoint, params=params)
    data = response.json()
    print(data)
    print(data)
    wmatic_price_in_usd = data['wmatic']['usd']

    price_in_wmatic = price_in_usd / wmatic_price_in_usd

    return price_in_wmatic

