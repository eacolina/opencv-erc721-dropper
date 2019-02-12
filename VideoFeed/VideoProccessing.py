from pyzbar import pyzbar
import numpy as np
import cv2
from web3 import Web3, HTTPProvider
from web3.auto.infura import w3
from components.BadgeDroper import BadgeDropper

#
class VideoProcessor:
    should_capture = True
    font = cv2.FONT_HERSHEY_SIMPLEX
    def __init__(self, videoSource, badge_dropper: BadgeDropper):
        self.source = cv2.VideoCapture(videoSource)
        self.badge_dropper = badge_dropper
        self.sent = False
        print("Started VideoProcessor")
        
    def lookForQR(self):
        while(True):
            ret,frame = self.source.read()
            barcodes = pyzbar.decode(frame)
            if(len(barcodes) > 0):
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
            if(self.should_capture):
                token_id = self.badge_dropper.getNexTokenID()
                self.badge_dropper.send721Token(token_id,eth_address)
                self.should_capture = False
                self.sent = True
            if(self.sent):
                cv2.putText(frame,"Badge was succesfully sent",(x,y), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
                
            #drop badge logic
            
        return frame


