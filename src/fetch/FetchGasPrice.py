import requests
from fetch import creds

"""
Fetches gas price of the blockchain of the selected swap.
"""
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

