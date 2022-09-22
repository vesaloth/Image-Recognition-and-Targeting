#Image.jpg is the image you are encrypting/decrypting
file = open('image.jpg', "rb")

image = file.read()
file.close()

image = bytearray(image)

key = 48

for i,j in enumrate(image):
    image[i] = j^key

#Switch encrypted to decrypted to decrypt image.jpg
file = open("encrypted.jpg", "wb")
file.write(image)
file.close()
