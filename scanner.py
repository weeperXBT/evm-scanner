import os
import time

from web3 import Web3

API_KEY = os.getenv('INFURA_API_KEY')

infura_ws = f"wss://mainnet.infura.io/ws/v3/{API_KEY}"

w3 = Web3(Web3.WebsocketProvider(infura_ws))
print("Connection successful: ", w3.is_connected)

def handle_new_block(block_hash):
    print("----------- HANDLE EVENT ----------------")
    block = w3.eth.get_block(block_hash.hex(), full_transactions=True)
    
    print("-------------------- BLOCK DETAIL ---------------")
    print(f"New Block Number: {block.number}")
    print(f"Hash: {block.hash.hex()}")
    print(f"Parent Hash: {block.parentHash.hex()}")
    print(f"Miner: {block.miner}")
    print(f"Transactions: {len(block.transactions)}")

    print("---------------- TX Details ----------------")
    print(block.transactions) 

    # for tx in block.transactions:
    # if tx.to is None:


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_new_block(event)
        time.sleep(poll_interval)

new_block_filter = w3.eth.filter('latest')

log_loop(new_block_filter, 60)