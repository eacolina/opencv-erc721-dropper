abi = [{
   "constant": True,
   "inputs": [{
     "name": "interfaceId",
     "type": "bytes4"
   }],
   "name": "supportsInterface",
   "outputs": [{
     "name": "",
     "type": "bool"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [],
   "name": "name",
   "outputs": [{
     "name": "",
     "type": "string"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "getApproved",
   "outputs": [{
     "name": "",
     "type": "address"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "to",
     "type": "address"
   }, {
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "approve",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [],
   "name": "totalSupply",
   "outputs": [{
     "name": "",
     "type": "uint256"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "from",
     "type": "address"
   }, {
     "name": "to",
     "type": "address"
   }, {
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "transferFrom",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "owner",
     "type": "address"
   }, {
     "name": "index",
     "type": "uint256"
   }],
   "name": "tokenOfOwnerByIndex",
   "outputs": [{
     "name": "",
     "type": "uint256"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "from",
     "type": "address"
   }, {
     "name": "to",
     "type": "address"
   }, {
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "safeTransferFrom",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "index",
     "type": "uint256"
   }],
   "name": "tokenByIndex",
   "outputs": [{
     "name": "",
     "type": "uint256"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "to",
     "type": "address"
   }, {
     "name": "tokenId",
     "type": "uint256"
   }, {
     "name": "tokenURI",
     "type": "string"
   }],
   "name": "mintWithTokenURI",
   "outputs": [{
     "name": "",
     "type": "bool"
   }],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "ownerOf",
   "outputs": [{
     "name": "",
     "type": "address"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "owner",
     "type": "address"
   }],
   "name": "balanceOf",
   "outputs": [{
     "name": "",
     "type": "uint256"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "to",
     "type": "address"
   }, {
     "name": "tokenURI",
     "type": "string"
   }],
   "name": "mintNextTokenWithTokenURI",
   "outputs": [{
     "name": "",
     "type": "bool"
   }],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [],
   "name": "symbol",
   "outputs": [{
     "name": "",
     "type": "string"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "account",
     "type": "address"
   }],
   "name": "addMinter",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [],
   "name": "renounceMinter",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "to",
     "type": "address"
   }, {
     "name": "approved",
     "type": "bool"
   }],
   "name": "setApprovalForAll",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "account",
     "type": "address"
   }],
   "name": "isMinter",
   "outputs": [{
     "name": "",
     "type": "bool"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": False,
   "inputs": [{
     "name": "from",
     "type": "address"
   }, {
     "name": "to",
     "type": "address"
   }, {
     "name": "tokenId",
     "type": "uint256"
   }, {
     "name": "_data",
     "type": "bytes"
   }],
   "name": "safeTransferFrom",
   "outputs": [],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "tokenURI",
   "outputs": [{
     "name": "",
     "type": "string"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "constant": True,
   "inputs": [{
     "name": "owner",
     "type": "address"
   }, {
     "name": "operator",
     "type": "address"
   }],
   "name": "isApprovedForAll",
   "outputs": [{
     "name": "",
     "type": "bool"
   }],
   "payable": False,
   "stateMutability": "view",
   "type": "function"
 }, {
   "inputs": [{
     "name": "name",
     "type": "string"
   }, {
     "name": "symbol",
     "type": "string"
   }],
   "payable": False,
   "stateMutability": "nonpayable",
   "type": "constructor"
 }, {
   "anonymous": False,
   "inputs": [{
     "indexed": True,
     "name": "account",
     "type": "address"
   }],
   "name": "MinterAdded",
   "type": "event"
 }, {
   "anonymous": False,
   "inputs": [{
     "indexed": True,
     "name": "account",
     "type": "address"
   }],
   "name": "MinterRemoved",
   "type": "event"
 }, {
   "anonymous": False,
   "inputs": [{
     "indexed": True,
     "name": "from",
     "type": "address"
   }, {
     "indexed": True,
     "name": "to",
     "type": "address"
   }, {
     "indexed": True,
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "Transfer",
   "type": "event"
 }, {
   "anonymous": False,
   "inputs": [{
     "indexed": True,
     "name": "owner",
     "type": "address"
   }, {
     "indexed": True,
     "name": "approved",
     "type": "address"
   }, {
     "indexed": True,
     "name": "tokenId",
     "type": "uint256"
   }],
   "name": "Approval",
   "type": "event"
 }, {
   "anonymous": False,
   "inputs": [{
     "indexed": True,
     "name": "owner",
     "type": "address"
   }, {
     "indexed": True,
     "name": "operator",
     "type": "address"
   }, {
     "indexed": False,
     "name": "approved",
     "type": "bool"
   }],
   "name": "ApprovalForAll",
   "type": "event"
 }]