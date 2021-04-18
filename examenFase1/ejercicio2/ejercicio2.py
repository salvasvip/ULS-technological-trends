# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 

# String which represents the QR code 
s = """
    n = int(input("cuantos numeros fibonacci?"))
    a = 0
    b = 1
    d = 0
    for x in range(n):
        c = b+a
        a = b
        d += a
        b = c    
        print (a)
    print (f'Suma total {d}')
    """

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 6) 

# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 
