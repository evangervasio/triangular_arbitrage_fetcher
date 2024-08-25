The `CalculatorTokens` function filters a CSV file containing triangular arbitrage opportunities (referred to as 
"triangles") based on inclusion and exclusion criteria specified in separate CSV files. The resulting filtered 
triangles are then saved into a new CSV file.

### Detailed Function Workflow:

1. **Paths Setup:**
   - The function constructs relative paths for the required CSV files:
     - `tokensToInclude.csv`: Contains tokens to include in the filtering process.
     - `tokensToExclude.csv`: Contains tokens to exclude from the filtering process.
     - `trianglesFilter.csv`: The input file containing triangles to be filtered, which will also serve as the output 
       file after filtering.

2. **Read Inclusion Tokens:**
   - The function reads `tokensToInclude.csv` to create a list of tokens (`tokensToInclude`). Only triangles containing 
     these tokens will be retained during the initial filtering phase.

3. **Read Exclusion Tokens:**
   - Similarly, `tokensToExclude.csv` is read to create a list of tokens (`tokensToExclude`). Any triangle containing 
     these tokens will be removed during the subsequent filtering phase.

4. **Filter Triangles by Inclusion:**
   - The function reads the triangles from `trianglesFilter.csv` and filters them based on the inclusion tokens. 
     A triangle is retained if it contains at least one of the tokens in `tokensToInclude`.

5. **Filter Triangles by Exclusion:**
   - The filtered list of triangles is further processed to remove any triangles containing tokens from 
     `tokensToExclude`.

6. **Remove Duplicates:**
   - The function removes any duplicate triangles from the filtered list by converting the list of lists into a 
     list of tuples (for hashing), then back into a list of lists.

7. **Write the Filtered Triangles:**
   - The final list of filtered triangles is written back to the `trianglesFilter.csv` file, overwriting its previous content.

### Parameters:
- `selectedSwap`: An object that contains relevant information about the swap, including its name, 
  which is used to determine file paths.

### CSV Files Used:
- `tokensToInclude.csv`: Contains the tokens to include in the filtering process.
- `tokensToExclude.csv`: Contains the tokens to exclude from the filtering process.
- `trianglesFilter.csv`: Both the input and output file for triangles before and after filtering.

### Returns:
- The function does not return any value but writes the filtered triangles to a CSV file.

### Key Features:
- **Flexible Token Filtering:** The function allows for both inclusion and exclusion of specific tokens in the 
  arbitrage triangles, making it highly customizable.
- **Duplicate Removal:** The function ensures that the output contains only unique triangles, avoiding redundant data.