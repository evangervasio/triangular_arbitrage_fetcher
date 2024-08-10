import requests
import json
import csv
import sys
import os
import re
import pandas as pd
from time import sleep
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from web3 import Web3
sys.path.append("../")


## Fetches the addresses of the tokens of the pairs of an exchange
# and puts them into a csv.
# The csv values are separated by a ';'
# In this case the exchange it's by default set to quickswap
# and we will be using thegraph as an API
# the csv will have values of "pair;token0;token1;reserve0;reserve1;symbol0;symbol1"

#volumeUSD_gt:"1000000000"
#3803 seems to be the maximum value of the skip variable that will give result
#of pairs with volumeUSD_gt:"1000000"
def FetchPairsUniswap():
  #i=1375
  #while i<3803:
  #for i in range(3803):
  for i in tqdm(range(3803)):
    query1= """query pairs($skip: Int!) {
   pairs(first: 1000, skip: $skip,where: {volumeUSD_gt:"1000000"}) {
     id
    token0 {
      id
      symbol
      decimals
    }
    token1 {
      id
      symbol
      decimals
    }
   }
 }"""
    #variables={"skip": i}
    variables={"skip": i}

    query = """
        {
  pairs(
    where: {volumeUSD_gt:"1000000"}
  ) {
    id
    token0 {
      id
      symbol
      decimals
    }
    token1 {
      id
      symbol
      decimals
    }
    reserve0
    reserve1
  }
}
    """
    uniswapApiURL = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    #request = requests.post(uniswapApiURL, json={"query": query})
    request = requests.post(uniswapApiURL, json={"query": query1,"variables": variables})
    result = request.json()
    result = json.dumps(result)
    pairsDict = json.loads(result)

    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath("../tempUniswap/pairs.csv", cur_path)
    
    with open(new_path, "a", encoding="utf-8", newline='') as csvfile:
        rowwriter = csv.writer(csvfile)
        for x in pairsDict["data"]["pairs"]:
            #GOOD parsing VERSION!
            pair=x["id"]
            token0=x["token0"]["id"]
            token1=x["token1"]["id"]
            #reserve0=x["reserve0"]
            #reserve1=x["reserve1"]
            symbol0=x["token0"]["symbol"]
            symbol1=x["token1"]["symbol"]
            decimals0=x["token0"]["decimals"]
            decimals1=x["token1"]["decimals"]
            rowwriter.writerow(
          #      [pair, token0, token1, reserve0, reserve1, symbol0, symbol1, decimals0, decimals1]
                 [pair, token0, token1, symbol0, symbol1, decimals0, decimals1]
            )
   # print(str(i)+" / "+str(3803))
    #i=i+1

def removeDuplicates(Uniswap,Quickswap):

  if Uniswap==True:
      cur_path = os.path.dirname(__file__)
      new_path = os.path.relpath("../temp/tempUniswap/pairs.csv", cur_path)
      new_pathOutput = os.path.relpath("../tempUniswap/pairsNoDup.csv", cur_path)
      df = pd.read_csv(new_path, sep=",")
      df.drop_duplicates(subset="pair", inplace=True)
      df.to_csv(new_pathOutput, index=False)

  if Quickswap==True:
      cur_path = os.path.dirname(__file__)
      new_path = os.path.relpath("../temp/tempQuickswap/pairs.csv", cur_path)
      new_pathOutput = os.path.relpath("../temp/tempQuickswap/pairsNoDup.csv", cur_path)
      df = pd.read_csv(new_path, sep=",")
      df.drop_duplicates(subset="pair", inplace=True)
      df.to_csv(new_pathOutput, index=False)


def FetchPairsQuickswap():

#  for i in tqdm(range(269)):

##!!! IMPORTANT NOTE: By looking how this subgraph and the majority of subgraph works i dont actually need to query all this times
#in this particular case just one time is needed, the first query already fetches all the pair
#because, in this case, the pairs are <1000 and the query can show 1000 items (pairs)
#and each iteration substracts a pair and is useless
#remember that in the query i said first:1000
#however in cases where there are more than 1000 items that can't get fetched in a single query
#looping is needed, but not always you need to increment i by just 1, because then the new query will add just one pair
#and is not used correctly, since a query can have a lot of pairs
#so instead of incrementing the skip value by 1 increment it by the number of pair that the query can have, 100, or 1000, or 2000, etc
#and if you get the skip value correctly you are not even gonna get duplicates

 for i in tqdm(range(1)):
    query0 = """query pairs($skip: Int!) {
    pairs(first: 1000, skip: $skip,where: {reserveUSD_gt:"1000000"}) {
      id
     token0 {
       id
       symbol
       decimals
     }
     token1 {
       id
       symbol
       decimals
     }
    }
  }"""
    query1 = """query pairs($skip: Int!) {
        pairs(first: 1000, skip: $skip,where: {reserveUSD_gt:"10000"}) {
          id
         token0 {
           id
           symbol
           decimals
         }
         token1 {
           id
           symbol
           decimals
         }
        }
      }"""
    variables = {"skip": i}
    quickswapApiURL = "https://api.thegraph.com/subgraphs/name/sameepsi/quickswap06"
    #sleep(3)
    request = requests.post(quickswapApiURL, json={"query": query1, "variables": variables})
    result = request.json()
    result = json.dumps(result)
    pairsDict = json.loads(result)

    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath("../temp/tempQuickswap/pairs.csv", cur_path)

    try:
        with open(new_path, "a", encoding="utf-8", newline='') as csvfile:
            rowwriter = csv.writer(csvfile)
            for x in pairsDict["data"]["pairs"]:
                # GOOD parsing VERSION!
                pair = x["id"]
                token0 = x["token0"]["id"]
                token1 = x["token1"]["id"]
                # reserve0=x["reserve0"]
                # reserve1=x["reserve1"]
                symbol0 = x["token0"]["symbol"]
                symbol1 = x["token1"]["symbol"]
                decimals0 = x["token0"]["decimals"]
                decimals1 = x["token1"]["decimals"]
                rowwriter.writerow(
                    #      [pair, token0, token1, reserve0, reserve1, symbol0, symbol1, decimals0, decimals1]
                    [pair, token0, token1, symbol0, symbol1, decimals0, decimals1]
                )
    except:
        print("EXCEPTION OCCURRED")
        i=i-1
        sleep(5)


def FetchPairsApeswap():
    query = """query pairs(first: 1000, where: {reserveUSD_gt:"1000"}) {
             id
          token0{
            id
            symbol
            decimals
          }
          token1 {
       id
       symbol
       decimals
     }
           }"""

    query1 = """query pairs($skip: Int!) {
            pairs(first: 1000, skip: $skip, where: {reserveUSD_gt:"10000"}) {
              id
             token0 {
               id
               symbol
               decimals
             }
             token1 {
               id
               symbol
               decimals
             }
            }
          }"""
    variables = {"skip": 0}
    apeswapApiURL="https://api.thegraph.com/subgraphs/name/prof-sd/as-matic-graft"
    request = requests.post(apeswapApiURL, json={"query": query1, "variables": variables})
    result = request.json()
    result = json.dumps(result)
    pairsDict = json.loads(result)

    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath("../temp/tempApeswap/pairs.csv", cur_path)

    with open(new_path, "a", encoding="utf-8", newline='') as csvfile:
        rowwriter = csv.writer(csvfile)
        for x in pairsDict["data"]["pairs"]:
            # GOOD parsing VERSION!
            pair = x["id"]
            token0 = x["token0"]["id"]
            token1 = x["token1"]["id"]
            # reserve0=x["reserve0"]
            # reserve1=x["reserve1"]
            symbol0 = x["token0"]["symbol"]
            symbol1 = x["token1"]["symbol"]
            decimals0 = x["token0"]["decimals"]
            decimals1 = x["token1"]["decimals"]
            rowwriter.writerow(
                #      [pair, token0, token1, reserve0, reserve1, symbol0, symbol1, decimals0, decimals1]
                [pair, token0, token1, symbol0, symbol1, decimals0, decimals1]
            )


