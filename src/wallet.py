"""wallet using rinkeby testnet"""
from datetime import datetime
from web3.auto.infura.rinkeby import w3

import ultra_secret_signer


def send_ether(to_address: str, send_amt_in_eth):
    """Send ether to to_address"""

    # def prepare_transaction
    if w3.isConnected():
        print('Connected to block chain.')
        print(f'Preparing to send {send_amt_in_eth:.8f} eth, to {to_address}')

        transaction = dict(
            # nonce=new_nonce,  # transaction_count+1,
            maxFeePerGas=int(4e9),
            maxPriorityFeePerGas=int(3e9),
            gas=21000,
            to=to_address,
            value=int(send_amt_in_eth*1e18),
            data=b'',
            # (optional) the type is now implicitly set based on appropriate transaction params
            type=2,
            chainId=4,
        )

        signed_txn = ultra_secret_signer.sign_transaction(transaction)
        # print(f'Received signed transaction: {signed_txn}')

        # broadcast it!
        print('Broadcasting... ',end='')
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Done!\ntx_hash is\n{tx_hash.hex()}')
        print(
            f'You can track it at https://rinkeby.etherscan.io/tx/{tx_hash.hex()}')

    else:
        print('Not connected to block chain. Exiting')


# as a simple test,
# actual TO_ADDRESS should be from the camera QR code
if __name__ == "__main__":
    TO_ADDRESS = '0xd91ac3f8fbBb960d4e2698b4a55529159b567aFC'
    send_ether(TO_ADDRESS)
