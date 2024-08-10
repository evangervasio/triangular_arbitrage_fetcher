import itertools
import os
import csv
from time import sleep
from tqdm import tqdm
from itertools import combinations
import pandas
## This function finds all the triangles
# of the uniswap pairs
# and puts them in a csv
# p.e. BTC/ETC, ETC/MATIC, MATIC,BTC
# for now only combinations of three are supported.
# NOTE: this is the most optimized version, with the only thing being 
# that it doesn't save the triangle with all the informations,
# but just the symbols.

#10/01/2023 : THIS IS THE RIGHT VERSION  THAT WORKS. Writing this only now but been so for long

def FetchTriangles(swapName):
    cur_path = os.path.dirname(__file__)
    #new_path = os.path.relpath("..//tempUniswap/pairsNoDup.csv", cur_path)
    new_path = os.path.relpath(f"../temp/temp{swapName}/pairs.csv", cur_path)


    pairs = []
    with open(new_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_file)
        for row in csv_reader:
            try:

                token0=row[1]
                token1=row[2]

                pairs.append([token0,token1])
            except:
                True

    triangles=[]

    for pair0 in tqdm(pairs):
        for pair1 in pairs:
            for pair2 in pairs:

                # 1. EXACTLY one of the tokens of the first pair appears also on the third
                if pair0[0] == pair2[0] or pair0[0] == pair2[1]:
                    if pair0[1] != pair2[0] and pair0[1] != pair2[1]:
                       # condition1 = True
                        token=pair0[0]
                        # 2. exactly one of the tok1ens of the second pair appears also on the third AND it isnt the same token as 1
                        if (pair1[0] == pair2[0] or pair1[0] == pair2[1]) and pair1[0]!=token:
                            if pair1[1] != pair2[0] and pair1[1] != pair2[1]:
                               # condition2 = True
                                token=pair1[0]
                                # 3. exactly one of the tokens of the first pair appears also on the second AND it isnt the same token as 2
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                      #  condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                     #   condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                        if (pair1[1] == pair2[0] or pair1[1] == pair2[1]) and pair1[1]!=token:
                            if pair1[0] != pair2[0] and pair1[0] != pair2[1]:
                               # condition2 = True
                                token=pair1[1]
                                # 3. exactly one of the tokens of the first pair appears also on the second AND it isnt the same token as 2
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                       # condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                        #condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                if pair0[1] == pair2[0] or pair0[1] == pair2[1]:
                    if pair0[0] != pair2[0] and pair0[0] != pair2[1]:
                       # condition1 = True
                        token=pair0[1]
                        # 2. exactly one of the tokens of the second pair appears also on the third AND it isnt the same token as 1
                        if (pair1[0] == pair2[0] or pair1[0] == pair2[1]) and pair1[0]!=token:
                            if pair1[1] != pair2[0] and pair1[1] != pair2[1]:
                               # condition2 = True
                                token=pair1[0]
                                # 3. exactly one of the tokens of the first pair appears also on the second AND it isnt the same token as 2
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                     #   condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                       # condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                        if (pair1[1] == pair2[0] or pair1[1] == pair2[1]) and pair1[1]!=token:
                            if pair1[0] != pair2[0] and pair1[0] != pair2[1]:
                             #   condition2 = True
                                token=pair1[1]
                                # 3. exactly one of the tokens of the first pair appears also on the second AND it isnt the same token as 2
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                        #condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                        #condition3 = True
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])

        # fetch other informations
        # we already have the other informations we need in pairsNoDup.csv, such as decimals, addresses, etc.

        pairs_file = os.path.relpath(f"../temp/temp{swapName}/pairs.csv", cur_path)


        trianglesFull = []
        with open(pairs_file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # the csv will be: pair0symbol0,pair0symbol1,pair1symbol0,pair1symbol1,pair2symbol0,pair2symbol1,pair0token0,pair0token1,pair1token0,pair1token1,pair2token0,pair2token1,
            # pairId0,PairId1,PairId2,tokenA0decimal,tokenA1decimal,tokenB0decimal,tokenB1decimal,tokenC0decimal,tokenC1decimal
            # pairNoDup is: pair,token0,token1,symbol0,symbol1,decimals0,decimals1
            # the triangles[] is: ['pair0token0/pair0token1/pair1token0/pair1token1/pair2token0/pair2token1]

            for triangle in tqdm(triangles):

                triangle=triangle.split("/")

                csv_file.seek(0)

                for row in csv_reader:
                    # search for the first pair, get information
                    if row[1] == triangle[0] and row[2] == triangle[1]:
                        infoPair0 = row

                    # search for the second pair, get information
                    if row[1] == triangle[2] and row[2] == triangle[3]:
                        infoPair1 = row

                    # search for the third pair, get information
                    if row[1] == triangle[4] and row[2] == triangle[5]:
                        infoPair2 = row


                fullInfo = []
                fullInfo.extend([infoPair0[3], infoPair0[4], infoPair1[3], infoPair1[4], infoPair2[3], infoPair2[4],
                                infoPair0[1], infoPair0[2], infoPair1[1], infoPair1[2], infoPair2[1], infoPair2[2],
                                infoPair0[0],
                                infoPair1[0], infoPair2[0], infoPair0[5], infoPair0[6], infoPair1[5], infoPair1[6],
                                infoPair2[5],
                                infoPair2[6]])

                trianglesFull.append(fullInfo)


    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath(f"../files/files{swapName}/triangles.csv", cur_path)

    # Split the path into the directory and filename
    directory, filename = os.path.split(new_path)

    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(new_path, "w", encoding="utf-8", newline="") as csvfile:
        rowwriter = csv.writer(csvfile)
        for triangle in trianglesFull:
            rowwriter.writerow(triangle)
    print("DONE---Triangles found saved in triangles.csv")


#FetchTriangles("Quickswap")