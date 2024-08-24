import os
import csv
from tqdm import tqdm
from collections import defaultdict

"""
Given a list of pairs, calculates all the possible combinations of three pairs that have tokens in common forming a 
"triangle"
"""
def FetchTrianglesNew(swapName):
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath(f"../temp/temp{swapName}/pairs.csv", cur_path)

    pairs = defaultdict(set)
    pair_info = dict()

    with open(new_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_file)
        for row in csv_reader:
            token0 = row[1]
            token1 = row[2]
            pairs[token0].add(token1)
            pairs[token1].add(token0)
            pair_info[(token0, token1)] = row
            pair_info[(token1, token0)] = row

    triangles = []

    for token0, set1 in tqdm(pairs.items()):
        for token1 in set1:
            set2 = pairs[token1]
            common = set1 & set2
            for token2 in common:
                if token0 != token2:
                    triangles.append([token0, token1, token2])

    trianglesFull = []

    for triangle in tqdm(triangles):
        infoPair0 = pair_info[(triangle[0], triangle[1])]
        infoPair1 = pair_info[(triangle[1], triangle[2])]
        infoPair2 = pair_info[(triangle[2], triangle[0])]

        fullInfo = [infoPair0[5], infoPair0[6], infoPair1[5], infoPair1[6], infoPair2[5], infoPair2[6],
                    infoPair0[1], infoPair0[2], infoPair1[1], infoPair1[2], infoPair2[1], infoPair2[2],
                    infoPair0[0], infoPair1[0], infoPair2[0], infoPair0[3], infoPair0[4], infoPair1[3], infoPair1[4],
                    infoPair2[3], infoPair2[4]]

        trianglesFull.append(fullInfo)

    new_path = os.path.relpath(f"../files/files{swapName}/triangles.csv", cur_path)
    directory, filename = os.path.split(new_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(new_path, "w", encoding="utf-8", newline="") as csvfile:
        rowwriter = csv.writer(csvfile)
        for triangle in trianglesFull:
            rowwriter.writerow(triangle)


