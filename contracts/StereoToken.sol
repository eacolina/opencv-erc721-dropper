pragma solidity >=0.4.21 <0.6.0;

import "openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";
import "openzeppelin-solidity/contracts/ownership/Ownable.sol";

contract StereoToken is ERC721Full, Ownable {
    /***
        @param _name string of the contract
        @param _symbol string of the token 
        @dev constructor function, sets name and symbol of the token  
    */
    constructor (string memory _name, string memory _symbol) ERC721Full(_name, _symbol) public{
    }
    
    event ModifyRights(uint indexed version, address indexed author, uint indexed tokenID, string hash, string URL); // event to record the mod of a song
    
    struct Right {
        uint version;
        string integrityHash;
        string URL;
    }
    mapping(uint => Right) public rightsInfo;
    mapping(uint => string) public songTitles;

    function createSong(uint _tokenID, string memory _hash, string memory _URL, string memory _title) public {
        _mint(msg.sender, _tokenID);
        rightsInfo[_tokenID] = Right(0,_hash, _URL);
        songTitles[_tokenID] = _title;
        emit ModifyRights(0, msg.sender,  _tokenID, _hash, _URL);
    }
    function getOwnedSongs() public view returns (uint[] memory)  {
        return _ownedTokens[msg.sender];
    }
    function updateRightsInfo(uint _tokenID, string memory _newHash, string memory _newURL) public {
        emit ModifyRights(rightsInfo[_tokenID].version + 1,msg.sender, _tokenID, _newHash, _newURL);
        rightsInfo[_tokenID].version += 1;
        rightsInfo[_tokenID].integrityHash = _newHash;
        rightsInfo[_tokenID].URL = _newURL;
    }
    function getURL(uint _tokenID) public view returns (string memory) {
        return (rightsInfo[_tokenID].URL);
    }
    function getAllTokens() public view returns (uint[] memory){
        return _allTokens;
    }
}
