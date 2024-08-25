Automatically fetches all pairs of a given Uniswap fork router contract without an API, with the possibility of excluding pools with 
a total liquidity under or over a certain threshold, then calculates all the possible triangles for triangular arbitrage.
### Key Features:
- **No API Dependency:** The function directly interacts with the blockchain via Web3 to retrieve pair information, 
  avoiding reliance on external APIs.
- **Liquidity Filtering:** It has the capability to exclude pairs based on liquidity thresholds, though this feature is 
  not explicitly implemented in the provided code snippet.
- **Concurrency:** Utilizes concurrent processing to efficiently handle large numbers of pairs, improving performance.
- **Automated Triangle Calculation:** After fetching pair data, it automatically calculates all possible triangular 
  arbitrage opportunities, streamlining the arbitrage discovery process.