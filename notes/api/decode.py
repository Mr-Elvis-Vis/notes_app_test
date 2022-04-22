import base64
image = open('/home/mr-elvis-vis/Загрузки/123.jpg', 'rb') #open binary file in
# read mode
image_read = image.read()
image_64_encode = base64.encodebytes(image_read)
with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(image_64_encode))