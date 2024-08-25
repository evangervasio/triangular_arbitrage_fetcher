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