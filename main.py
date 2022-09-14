import pyqrcode
import png
from pyqrcode import QRCode

QRString ='https://www.instagram.com/rgil.guitars/?r=nametag'

url = pyqrcode.create(QRString)

url.png(r'qrinsta.png',scale = 8)

