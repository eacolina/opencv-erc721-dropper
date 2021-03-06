from services.Web3Service import Web3Service
from services.TokenABI import abi
import requests
import shutil
import os

class BadgeDropper:

    def __init__(self, Web3Service: Web3Service):
        self.w3Service = Web3Service
        self.tokenContract = self.w3Service.eth.contract(address=self.w3Service.w3.toChecksumAddress('0xabe71e6a260c2eea3c30864dc50639100aa315f6'),abi=abi)
        self.getOwnedTokens()
        self.badge_image_path = 'burnerlogo.png' 
        self.getTokenMetadata(self.ownedTokens[0])
        print("Started badge dropper")
    
    def getOwnedTokens(self):
        self.tokenCount = self.tokenContract.functions.balanceOf(self.w3Service.accountPBK).call() # get amount of owned tokens
        if(self.tokenCount == 0):
             raise NameError("The badge dropper ran out of tokens!!")
        self.ownedTokens = [] # list used to keep track of the owned tokens
        for i in range(0, self.tokenCount):
            # iterate through the ownedTokens array of the contract
            tokenID = self.tokenContract.functions.tokenOfOwnerByIndex(self.w3Service.accountPBK,i).call()
            self.ownedTokens.append(tokenID) # add each tokenID to the list

    # Get the next tokenID in the list to send and delete from list
    def getNextTokenID(self):
        if (len(self.ownedTokens) == 0):
            print("Ran out of tokens")
            return 
        return self.ownedTokens.pop()

    def send721Token(self, token_ID, dest_address):
        dest_address = self.w3Service.w3.toChecksumAddress(dest_address)
        safe_transfer = self.tokenContract.functions.safeTransferFrom(self.w3Service.accountPBK,dest_address,token_ID) # build the function to send tx
        signed_tx = self.w3Service.sign_tx(safe_transfer)
        txReceipt = self.w3Service.eth.sendRawTransaction(signed_tx.rawTransaction)
        txHash = self.w3Service.w3.toHex(txReceipt)
        print(txHash)
    
    def getTokenMetadata(self, tokenID):
        metadata_uri = self.tokenContract.functions.tokenURI(tokenID).call()
        req = requests.get(metadata_uri)
        data = req.json()
        print(data)
        self.badge_name = data['name']
        self.downloadImage(data['image'])
    
    def downloadImage(self,url):
        response = requests.get(url, stream=True)
        with open(self.badge_image_path , 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        