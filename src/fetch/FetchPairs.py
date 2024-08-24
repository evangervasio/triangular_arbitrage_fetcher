import json
import csv
import sys
import os
import pandas as pd
from time import sleep
from tqdm import tqdm
import requests

sys.path.append("../")

def FetchPairsUniswap():

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
    request = requests.post(uniswapApiURL, json={"query": query1,"variables": variables})
    result = request.json()
    result = json.dumps(result)
    pairsDict = json.loads(result)

    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath("../tempUniswap/pairs.csv", cur_path)
    
    with open(new_path, "a", encoding="utf-8", newline='') as csvfile:
        rowwriter = csv.writer(csvfile)
        for x in pairsDict["data"]["pairs"]:
            pair=x["id"]
            token0=x["token0"]["id"]
            token1=x["token1"]["id"]

            symbol0=x["token0"]["symbol"]
            symbol1=x["token1"]["symbol"]
            decimals0=x["token0"]["decimals"]
            decimals1=x["token1"]["decimals"]
            rowwriter.writerow(
                 [pair, token0, token1, symbol0, symbol1, decimals0, decimals1]
            )

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
                pair = x["id"]
                token0 = x["token0"]["id"]
                token1 = x["token1"]["id"]

                symbol0 = x["token0"]["symbol"]
                symbol1 = x["token1"]["symbol"]
                decimals0 = x["token0"]["decimals"]
                decimals1 = x["token1"]["decimals"]
                rowwriter.writerow(
                    [pair, token0, token1, symbol0, symbol1, decimals0, decimals1]
                )
    except:
        print("exception occurred")
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
            pair = x["id"]
            token0 = x["token0"]["id"]
            token1 = x["token1"]["id"]

            symbol0 = x["token0"]["symbol"]
            symbol1 = x["token1"]["symbol"]
            decimals0 = x["token0"]["decimals"]
            decimals1 = x["token1"]["decimals"]
            rowwriter.writerow(
                [pair, token0, token1, symbol0, symbol1, decimals0, decimals1]
            )


