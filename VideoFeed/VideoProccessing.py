from pyzbar import pyzbar
import numpy as np
import cv2
from web3 import Web3, HTTPProvider
from web3.auto.infura import w3
from components.BadgeDroper import BadgeDropper
from threading import Timer

#
class VideoProcessor:
    should_capture = True
    font = cv2.FONT_HERSHEY_SIMPLEX
    def __init__(self, videoSource, badge_dropper: BadgeDropper):
        self.source = cv2.VideoCapture(videoSource)
        self.badge_dropper = badge_dropper
        self.sent = False
        self.processed_addresses = []
        print("Started VideoProcessor")
    
    def resetCapture(self):
        print("Callback fired")
        self.should_capture = True
        
    def lookForQR(self):
        while(True):
            ret,frame = self.source.read()
            barcodes = pyzbar.decode(frame)
            if(len(barcodes) > 1):
                cv2.putText(frame,"Please only show ONE QR code",(100,100), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
                continue
            if(len(barcodes) == 1):
                frame = self.parseQR(barcodes,frame)
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def parseQR(self,barcodes,frame):
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect # get cordinates of QR code
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # draw rectangle around code
            cv2.imshow('frame',frame)
            eth_address = barcode.data.decode("utf-8") # decode qr code
            if (not self.should_capture):
                cv2.putText(frame,"Badge was sent succesfully",(x,y), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
                return frame
            if eth_address in self.processed_addresses:
                cv2.putText(frame,"You already claimed this badge",(x,y), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
            else:
                self.processed_addresses.append(eth_address)
                token_id = self.badge_dropper.getNexTokenID()
                self.badge_dropper.send721Token(token_id,eth_address)          
                cv2.putText(frame,"Badge was sent succesfully",(x,y), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
                self.should_capture = False
                Timer(2.5,self.resetCapture).start()
        return frame


