from pyzbar import pyzbar
import numpy as np
import cv2
from web3 import Web3, HTTPProvider
from web3.auto.infura import w3
from components.BadgeDroper import BadgeDropper
from threading import Timer

class VideoProcessor:
    should_capture = True
    font = cv2.FONT_HERSHEY_SIMPLEX
    def __init__(self, videoSource, badge_dropper: BadgeDropper):
        self.source = cv2.VideoCapture(videoSource)
        self.badge_dropper = badge_dropper
        self.sent = False
        self.processed_addresses = []
        self.tokenImage = cv2.imread(self.badge_dropper.badge_image_path,cv2.IMREAD_UNCHANGED)
        self.tokenImage = cv2.resize(self.tokenImage, (200,200)) 
        print("Started VideoProcessor")
    
    # Calback function used to reset the should_capture flag and decode the frame again
    def resetCapture(self):
        self.should_capture = True
        
    def lookForQR(self):
        while(True):
            ret,frame = self.source.read()
            barcodes = pyzbar.decode(frame)
            if(len(barcodes) > 1):
                print(barcodes[0].type)
                cv2.putText(frame,"Please only show ONE QR code",(100,100), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
                continue
            if(len(barcodes) == 1):
                if (barcodes[0].type == 'QRCODE'):
                    frame = self.parseQR(barcodes,frame)
            #frame[50:50+self.tokenImage.shape[0],50:50+self.tokenImage.shape[1]] = self.tokenImage
            y_offset = 100
            x_offset = 100

            y1, y2 = y_offset, y_offset + self.tokenImage.shape[0]
            x1, x2 = x_offset, x_offset + self.tokenImage.shape[1]

            alpha_s = self.tokenImage[:, :, 2] / 255.0
            alpha_l = 1.0 - alpha_s

            for c in range(0, 3):
                frame[y1:y2, x1:x2, c] = (alpha_s * self.tokenImage[:, :, c] +
                                        alpha_l * frame[y1:y2, x1:x2, c])
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
                token_id = self.badge_dropper.getNextTokenID()
                self.badge_dropper.send721Token(token_id,eth_address)          
                cv2.putText(frame,"Badge was sent succesfully",(x,y), self.font, 1, (255,0,0), 3, cv2.LINE_AA)
                self.should_capture = False
                Timer(2.5,self.resetCapture).start()
        return frame

    def overlay_image_alpha(self,img, img_overlay, pos, alpha_mask):
        """Overlay img_overlay on top of img at the position specified by
        pos and blend using alpha_mask.

        Alpha mask must contain values within the range [0, 1] and be the
        same size as img_overlay.
        """

        x, y = pos

        # Image ranges
        y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
        x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

        # Overlay ranges
        y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
        x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

        # Exit if nothing to do
        if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
            return

        channels = img.shape[2]

        alpha = alpha_mask[y1o:y2o, x1o:x2o]
        alpha_inv = 1.0 - alpha

        for c in range(channels):
            img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                    alpha_inv * img[y1:y2, x1:x2, c])