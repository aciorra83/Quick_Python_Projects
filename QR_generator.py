# import the appropriate module
import qrcode

# data that the qrcode is linked to
data = 'Don\'t forget to subscribe'

# creating and instance of qr class
qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('/home/alex/Desktop/quick_python_projects/myqrcode1.png')

# # constructing method and variable declaration of the qrcode
# img = qrcode.make(data)

# # path were the qrcode .png file is saved
# img.save('/home/alex/Desktop/quick_python_projects/myqrcode.png')
