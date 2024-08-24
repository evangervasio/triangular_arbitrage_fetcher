import os
import csv
from tqdm import tqdm
from collections import defaultdict

"""
The `FetchTrianglesNew` function identifies all possible triangles of tokens from a list of trading pairs 
in a decentralized exchange (DEX). Specifically, it calculates all valid combinations of three pairs that share tokens 
in such a way that they form a "triangle", where the tokens are interconnected, enabling a cyclic trade route.

### Detailed Function Workflow:

1. **Initialize File Paths:**
   - The function begins by setting up the file paths needed to locate the list of trading pairs (`pairs.csv`) associated 
     with the given swap (`swapName`). The path is constructed relative to the current directory.

2. **Load Pairs and Build Data Structures:**
   - A `defaultdict` of sets (`pairs`) is created to store each token and the set of tokens it can be traded with. 
     Additionally, a `pair_info` dictionary is initialized to store detailed information about each pair.
   - The function reads the `pairs.csv` file and processes each row to extract token pair information:
     - For each pair of tokens (`token0` and `token1`), the function updates the `pairs` dictionary to record their 
       relationship.
     - The `pair_info` dictionary is populated with detailed pair data, allowing quick access later in the process.

3. **Identify Triangular Arbitrage Opportunities:**
   - The function iterates through the `pairs` dictionary to identify all sets of three tokens that can form a triangle:
     - For each token (`token0`), it retrieves the set of tokens (`set1`) it can be traded with.
     - It then checks each token in `set1` (`token1`) to find its own set of tradeable tokens (`set2`).
     - The function identifies the intersection of `set1` and `set2` to find a common third token (`token2`) that, 
       along with `token0` and `token1`, forms a valid triangular arbitrage opportunity.
     - Triangles are recorded only if `token0` and `token2` are distinct.

4. **Compile Full Triangle Information:**
   - For each identified triangle, the function gathers detailed information for all three pairs involved using the 
     `pair_info` dictionary. It retrieves data such as token addresses, reserve values, and other relevant information.
   - This information is compiled into a list (`trianglesFull`) that contains all the necessary details for each 
     triangular arbitrage opportunity.

5. **Save Triangles to CSV:**
   - The function constructs a path for saving the triangle data to a new CSV file (`triangles.csv`), which is stored in 
     a directory specific to the swap (`swapName`). If the directory does not exist, it is created.
   - The compiled triangle data is written to the CSV file, with each row representing a fully described triangular 
     arbitrage opportunity.

### Parameters:
- `swapName`: A string representing the name of the DEX swap in use. This is used to locate the appropriate 
  input and output files.

### Returns:
- None. The function saves the calculated triangular arbitrage opportunities to a CSV file for further analysis.

### Key Features:
- **Comprehensive Triangle Detection:** The function efficiently identifies all valid triangular arbitrage opportunities 
  by leveraging the relationships between tokens in the trading pairs.
- **Detailed Data Compilation:** Each identified triangle is supplemented with comprehensive data from the original 
  trading pairs, ensuring that all necessary information is available for subsequent use.
- **Automated File Handling:** The function handles file path construction and ensures that the output directory exists 
  before saving the results.
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


