### Disclaimer:
This project was created and ended when i was 15 to 17, with
a very unexperienced and disorganized mind. I picked up this
project after 2 years to somehow make it "releasable", cleaning
up what i could and writing function documentation based
on what i remembered, with the help of AI. Therefore, the code
is buggy, unoptimized and badly structured. Even tho this bot
works, this project is unfinished.

This bot is not able to perfom actual profitable triangular
arbitrage at its current speed. 
Use this bot for economic gains at your own risk.

### Description:
Arbplus is a tool designed to completely automate the process
of triangular arbitrage:
1. fetch pair data
2. create triangles
3. find opportunities in real time
4. execute arb transaction on-chain

The other key feature of this tool is that this can be done
with every DEX that is a Uniswap fork, such as Quickswap
and Sushiswap. The only user input needed is the name of the
dex, its router smart contract address (easily obtainable on
dex documentation) and the network name. Everything is then
ready to fetch data and start scanning for triangular arbitrage
opportunities.
This is made possible by not relying on different APIs for
every DEX, but rather gathering data on chain.