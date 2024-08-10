##From user preference calculate which trinagles include the user selected tokens
#import logging
import os
import csv
import tqdm
cur_path = os.path.dirname(__file__)
#logging.basicConfig(level=logging.DEBUG)
##Fetches the triangles that have as input tokens only the tokens listed in
#files/filesDex/tokensToInclude.csv
#and exclude the ones that have in the triangle the tokens listed in
#files/filesDex/tokensToExclude
def CalculatorTokens(selectedSwap):
    try:
        path_include = os.path.relpath(f"../files/files{selectedSwap.Name}/tokensLimits.csv", cur_path)

        path_exclude=os.path.relpath(f"../files/files{selectedSwap.Name}/tokensToExclude.csv", cur_path)

        #new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/triangles.csv", cur_path)
        new_path = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFilter.csv", cur_path)
        path_to_write = os.path.relpath(f"../files/files{selectedSwap.Name}/trianglesFilter.csv", cur_path)

       # path_to_write = os.path.relpath(f"../files/files{selectedSwap}/trianglesFocused.csv", cur_path)

        tokensToInclude=[]

        with open(path_include, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                tokensToInclude.append((row[0].split(";"))[0].lower())

       # logging.debug(tokensToInclude)

        tokensToExclude=[]

        with open(path_exclude, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                tokensToExclude.append(row[0].lower())


        filtered_triangles=[]


        with open(new_path, "r", encoding="utf-8",) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                for t in tokensToInclude:
                    t=t.lower()
                    if (row[6].lower()==t or row[7].lower()==t) and (row[10].lower()==t or row[11].lower()==t):
                        filtered_triangles.append(row)

        filtered_triangles_=[]
        for t in tokensToExclude:
            t = t.lower()
            for filtered_triangle in filtered_triangles:
               if any(filtered_triangle[i].lower() == t for i in range(6, 12)):
                   filtered_triangles.remove(filtered_triangle)

        # REMOVE DUPLICATES
        cleaned_list = list(set(tuple(sublist) for sublist in filtered_triangles))
        cleaned_list = [list(sublist) for sublist in cleaned_list]

        with open(path_to_write, "w", encoding="utf-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file,delimiter=",")
            for t in cleaned_list:
                csv_writer.writerow(t)
    except Exception as e:
      #  logging.debug(e)
        print(e)

#CalculatorTokens("Quickswap")