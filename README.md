### Introduction:
triangular_arbitrage_fetcher fetches pair data of any Uniswap forks without
third party APIs, calculates combinations of liquidity pools triangles, and scans
for profitable arbitrage on those combinations in real time.

https://github.com/user-attachments/assets/fd1e57fd-fe13-4774-a61f-6e7060011f27

### Key features:
- Fetches pair data universally from any Uniswap fork DEX

- Fetches pair data without any third party API (only rpc nodes needed)

- Combine pairs to create triangles of liquidity pools eligible for arbitrage

- Includes everything in profitability calculator (price impact, gas fees..)

- Calculate profitability with real time data

- Import a new Uniswap fork just by knowing its router contract address

- Possibility to save multiple Swaps

- Ability to exclude or include tokens from the arbitrage scan (avoiding scam tokens)

- Possibility to limit token amount usage in transaction
### Disclaimers:
- This bot at its current speed is not actually able to make real money from executing triangular arbitrage. If you choose to use this bot for economic purposes, you’re doing so at your own risks.

- This project was created when i was very unexperienced, so expect the code of this project to be unoptimized, and overall just pretty badly written. Function documentation is written with the help of AI.

- I am no longer willing to continue this project myself, but i will be happy to accept collaborators and review pull requests.
### Description:
triangular_arbitrage_fetcher is a tool designed to completely automate the process
of triangular arbitrage:
1. fetch pair data
2. create triangles
3. find opportunities in real time
4. execute arb transaction on-chain

The key feature of this tool is that this automation is possible
with every DEX that is a Uniswap fork, such as Quickswap
and Sushiswap (NOTE: even tho adding a network can be done easly, right now this tool supports only fully Polygon and partially Ethereum). The only user input needed is the name of the
dex, its router smart contract address and the network name. Everything is then
set to fetch data and start scanning for triangular arbitrage
opportunities.
This is made possible by not relying on different APIs for
every DEX, but rather gathering data on chain, making this method universally appliable.

### Installation:

1. clone the repo
2. install requirements.txt with python 3.9.10
2. get a free alchemy rpc key (for polygon network)
3. get a free infura rpc key (for ethereum network)
5. create a "creds.py" file and write on it these keys with the variables names "alchemy_key, infura_key"
6. copy and paste "creds.py" in the calculator, fetch and executer folder

### Usage:
**Add a new Uniswap fork:**
1. navigate on src/main and execute `__main__`.py with python
2. click on "Add Swap" and input the name, network and router
smart contract address of the wanted Uniswap fork, "factory" field is
optional as it will be obtained automatically.
3. click on "Save Swaps" once every needed information is added to save the newly added fork on file.
4. select the wanted fork and click on "Fetch Info" to fetch all required pair data. This
process might require some time based on how big the dex is. 
Note: this needs to be done only one time for a single swap.

**Fetch triangular arbitrage opportunities:**
1. select the wanted Uniswap fork and click on "Fetch Arbitrage" to start the arbitrage fetching loop. 
If there is the need to exclude some triangles from the arbitrage
   (tokens listed on the "tokensToExclude" csv of the selected
swap) or to only include triangles that have certain tokens
in them (tokensToInclude.csv), or if the amount of tokens to
spend needs to be limited (tokensLimits.csv), "Filter" checkbox needs to be checked.
Otherwise, every triangle fetched will be used.

### Documentation:

[Function Documentation](docs/docs.md)

### TODO list:

- Optimize FetchArbitrage cycle (too slow to be competitive)
- Optimize FetchExchangeInfo pair data fetch speed (too long for big swaps)
- Make GUI options for filtering instead of having to manually write to file
- Implement every network in a dynamic way, not just Polygon (alchemy now works on every network, no need for other rpcs)
- Display logs and useful info on GUI instead of terminal
- Divide FetchArbitrage into small functions
- Make rpc keys importable by GUI
