import pyqrcode
import png
from pyqrcode import QRCode

QRString =''#put the link here

url = pyqrcode.create(QRString)

url.png(r'qr.png',scale = 8)
  #change the name of the archive if you desire 
