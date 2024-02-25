from dotenv import load_dotenv
import os

from web3 import Web3

API_KEY = os.getenv('INFURA_API_KEY')

url = f"https://mainnet.infura.io/v3/{API_KEY}"

w3 = Web3(Web3.HTTPProvider(url))
res = w3.is_connected()
print(res)
