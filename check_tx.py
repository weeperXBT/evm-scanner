import os
import time

from web3 import Web3

API_KEY = os.getenv('INFURA_API_KEY')
TX_HASH = os.getenv('TX_HASH')

infura_ws = f"wss://mainnet.infura.io/ws/v3/{API_KEY}"

w3 = Web3(Web3.WebsocketProvider(infura_ws))
print("Connection successful: ", w3.is_connected)



def print_tx(tx_hash):
    transaction = w3.eth.get_transaction(tx_hash)

    if transaction is None:
        print("Transaction not found.")

    else:
        # Print the full details of the transaction
        print("Transaction Details:")
        for key, value in transaction.items():
            # For better readability, convert value to hex for byte data
            if isinstance(value, bytes):
                value = value.hex()
            print(f"{key}: {value}")

        # If you want to include receipt details like gas used or logs, fetch the receipt as well
        receipt = w3.eth.get_transaction_receipt(tx_hash)
        print("\nTransaction Receipt:")
        for key, value in receipt.items():
            # Convert bytes to hex strings for readability
            if isinstance(value, bytes):
                value = value.hex()
            print(f"{key}: {value}")

print_tx(TX_HASH)