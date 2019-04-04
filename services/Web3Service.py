from web3 import Web3
from web3.eth import Eth
from eth_keys import keys
import os


class Web3Service:
    
    def __init__(self, http_endpoint):
        self.w3 = Web3(Web3.HTTPProvider(http_endpoint))
        self.eth = Eth(self.w3)
        self.accountPK = os.environ.get('BADGE_DROPER_PK') # get private key from environment
        if(self.accountPK == ''):
            raise NameError('The private key was not found in the enviroment variables')
        
        pk = keys.PrivateKey(self.w3.toBytes(hexstr=self.accountPK)) # used to derive public key
        self.accountPBK = pk.public_key.to_checksum_address()
        print("Started web3 service using this account as origin: " + self.accountPBK)

    def sign_tx(self,contractFunc,options=None): # This will generate a signed tx with the private key of the service
        nonce = self.eth.getTransactionCount(self.accountPBK)
        tx = contractFunc.buildTransaction({
            'nonce':nonce,
            'gasPrice': self.w3.toWei('21', 'gwei')
        })
        pk = os.environ.get('PK')
        signedTx = self.eth.account.signTransaction(tx,private_key=pk)
        return signedTx
