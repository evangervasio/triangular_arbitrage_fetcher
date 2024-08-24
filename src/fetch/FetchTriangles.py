import os
import csv
from tqdm import tqdm


def FetchTriangles(swapName):
    cur_path = os.path.dirname(__file__)
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

                if pair0[0] == pair2[0] or pair0[0] == pair2[1]:
                    if pair0[1] != pair2[0] and pair0[1] != pair2[1]:
                        token=pair0[0]
                        if (pair1[0] == pair2[0] or pair1[0] == pair2[1]) and pair1[0]!=token:
                            if pair1[1] != pair2[0] and pair1[1] != pair2[1]:
                                token=pair1[0]
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                        if (pair1[1] == pair2[0] or pair1[1] == pair2[1]) and pair1[1]!=token:
                            if pair1[0] != pair2[0] and pair1[0] != pair2[1]:
                                token=pair1[1]
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                if pair0[1] == pair2[0] or pair0[1] == pair2[1]:
                    if pair0[0] != pair2[0] and pair0[0] != pair2[1]:
                        token=pair0[1]
                        if (pair1[0] == pair2[0] or pair1[0] == pair2[1]) and pair1[0]!=token:
                            if pair1[1] != pair2[0] and pair1[1] != pair2[1]:
                                token=pair1[0]
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                        if (pair1[1] == pair2[0] or pair1[1] == pair2[1]) and pair1[1]!=token:
                            if pair1[0] != pair2[0] and pair1[0] != pair2[1]:
                                token=pair1[1]
                                if (pair0[0] == pair1[0] or pair0[0] == pair1[1]) and pair0[0]!=token:
                                    if pair0[1] != pair1[0] and pair0[1] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])
                                if (pair0[1] == pair1[0] or pair0[1] == pair1[1]) and pair0[1]!=token:
                                    if pair0[0] != pair1[0] and pair0[0] != pair1[1]:
                                        triangles.append(pair0[0]+"/"+pair0[1]+"/"+pair1[0]+"/"+pair1[1]+"/"+pair2[0]+"/"+pair2[1])



        pairs_file = os.path.relpath(f"../temp/temp{swapName}/pairs.csv", cur_path)


        trianglesFull = []
        with open(pairs_file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for triangle in tqdm(triangles):

                triangle=triangle.split("/")

                csv_file.seek(0)

                for row in csv_reader:
                    if row[1] == triangle[0] and row[2] == triangle[1]:
                        infoPair0 = row

                    if row[1] == triangle[2] and row[2] == triangle[3]:
                        infoPair1 = row

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

    directory, filename = os.path.split(new_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(new_path, "w", encoding="utf-8", newline="") as csvfile:
        rowwriter = csv.writer(csvfile)
        for triangle in trianglesFull:
            rowwriter.writerow(triangle)


