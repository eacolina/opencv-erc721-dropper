# ERC 721 Token Air Droper 

NFTs are great, you can't argue that! Everything started back when CryptoKitties clogged the Ethereum network. And virtual collectibles on Ethereum have been on the rise since.
This project focuses on memorabilia use. Some projects and companies have started using NFT's to promote brand awareness. Take the great example of Bitcoin's Kudos. 

We could use the analogy of stickers at an event booth. People go to your booth and they would take home your super cool company sticker and show it off to their friends. We could also do that we 721 tokens but it would be a pain. They would have to ask you to pull up their wallet, you would have to be sure that that wallet has the tokens get their address and send it to them.

With this project, we aimed to automate this. You only need a computer with a camera and you can start giving away badges like candy!🍩🍭🍬

## How to claim a badge:
Just show your QR address to the camera and get your token. It's that simple!

## Requirements:
- Python 3.6 (or higher)
- OpenCV ([Install guide](https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/))
- ZBar
    - Linux: `$ sudo apt-get install libzbar0`
    - MacOS: `$ brew install zbar`
## Getting started
- Clone this repo
- Set enviroment variables:
    - `export BADGE_DROPER_PK=<PRIVATE KEY OF ACCOUNT THAT HOLDS THE TOKENS>`
    - `export CONTRACT_ADDRESS=<ADDRESS OF THE 721 TOKEN CONTRACT>`
- Install dependecies:
    - `pip3 install -r requirements.txt`

To start it up, just run: `python3 main.py`