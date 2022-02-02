"""this part should be kept air-gapped
by right the nonce should be supplied if really air-gapped
but here it is getting it from internet
"""
import os
from web3.auto.infura.rinkeby import w3


def sign_transaction(transaction_dict: dict):
    """Sign the transaction_dict with privatekey"""
    # ultra secret
    private_key = os.environ['FROM_PRIVATE_KEY']

    account = w3.eth.account.privateKeyToAccount(private_key)
    address = account.address
    balance = w3.fromWei(
        w3.eth.get_balance(address), 'ether')
    print(f'The originating account has a balance of ether: {balance}')

    nonce = w3.eth.get_transaction_count(address, 'pending')

    # completing the transaction dict
    transaction_dict['nonce'] = nonce
    transaction_dict['from'] = address

    # print(f'Signing transaction {transaction_dict}')
    print(f'Signing transaction... ',end='')
    signed_txn = w3.eth.account.sign_transaction(transaction_dict, private_key)
    print('Done')
    # print(f'Successfully signed as :{signed_txn}')
    return signed_txn
