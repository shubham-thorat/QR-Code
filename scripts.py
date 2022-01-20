import qrcode
import cv2


def QRGenerator():
    input_data = input()
    img = qrcode.make(input_data)    
    img.save('qrcode.jpg')


def QRDecoder():
    code = cv2.QRCodeDetector()
    data,points,straight_qrcode =  code.detectAndDecode(cv2.imread('qrcode.jpg'))
    return data
