This function determines the decimal position number (p.e. 18) of the token we are putting an amount input in and getting
an amount output from in a triangular arbitrage transaction.

### Parameters:
- `triangle`: An array representing the triangular arbitrage transaction, where tokens are ordered in a specific
  sequence.
- `decimals`: A list or array containing the decimal precision for two tokens involved in the transaction.

### Returns:
- `int`: The number of decimal places used by the token that is being used as input for the arbitrage transaction.