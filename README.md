# library

- pip install qrcode
- pip install opencv-python

# methods

- generate QR code : QRGenerator()
- decode QR code : QRDecoder()

# QRGenerator()

    - take input as string
    - encode the string
    - save as qrcode.jpg

# QRDecoder()

    - decode image present in current directory as qrcode.jpg
    - return encoded string
