This function determines the gas price for executing transactions on either the Polygon or Ethereum network, depending 
on the `Network` attribute of the `selectedSwap` object. It uses different APIs for each network to retrieve the most 
recent gas price data.

### Detailed Function Workflow:

1. **Check Network Type:**
   - The function checks the `Network` attribute of the `selectedSwap` object to determine which blockchain network 
     is being used (Polygon or Ethereum).

2. **Fetch Gas Price for Polygon:**
   - If the network is Polygon, the function sends a GET request to the Blockscan API's Polygon endpoint to retrieve 
     the current gas price in Gwei. Specifically, it requests the "rapid" gas price, which is the price for fast transaction 
     processing.

3. **Fetch Gas Price for Ethereum:**
   - If the network is Ethereum, the function sends a GET request to the Etherscan API's gas tracker endpoint. It retrieves 
     the "SafeGasPrice," which represents a gas price that is likely to result in a timely transaction confirmation.

4. **Return the Gas Price:**
   - The function returns the gas price as an integer value. If the network is neither Polygon nor Ethereum, the function 
     returns `-1` to indicate that the gas price could not be fetched.

### Parameters:
- `selectedSwap`: An object representing the selected DEX swap configuration, containing attributes such as `Network`, 
  which determines the blockchain network (Polygon, Ethereum, etc.) where the swap will take place.

### Returns:
- `int`: The gas price in Gwei for the selected network. Returns `-1` if the network is unsupported.