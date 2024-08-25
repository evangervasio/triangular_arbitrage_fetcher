Calculates the price impact for trades on an Automated Market Maker (AMM) like Uniswap.

This function computes the price impact of a swap, which is the effect of a swap on the price of a token within 
an AMM liquidity pool. The price impact is derived from the Uniswap pricing formulas, reflecting how the price changes 
in response to a swap, based on the input and output amounts of the tokens involved.

### Parameters:
- `a12`: Reserve of the first token in the pool.
- `a21`: Reserve of the second token in the pool.
- `amountIn1`: Amount of the first token being input into the pool.
- `amountIn2`: Amount of the second token being input into the pool.
- `amountOut1`: Amount of the first token being output from the pool.
- `amountOut2`: Amount of the second token being output from the pool.

### Returns:
- `Decimal`: The price impact of the trade, indicating the change in price resulting from the specified swap parameters.