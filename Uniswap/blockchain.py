from web3 import Web3, EthereumTesterProvider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/2d4d6a59129f49699bc30bab6d81321a'))
print(w3.isConnected())
print(w3.eth.get_block('latest'))