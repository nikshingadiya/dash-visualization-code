import numpy as np

from PIL import Image

img = Image.open('C:/Users/nikhil/Pictures/Saved Pictures/Girnar.jpg')
# print(img.format)
print(img.size)
# print(img.mode)
#
# newImage = img.resize((440, 600))
# newImage.show()
# img.rotate(0).show()
Matrix = np.array([[1, 0], [-4, 8]])
mt = np.array([[1, 0],
               [-4, 8]])
# print(img.size[0])
# print(img.size[1])
pixels = []
new_co = []
for i in range(img.size[1]):
    pixel = []
    for j in range(img.size[0]):
        pixel.append(img.getpixel((j, i)))
        k = np.array([j, i])
        new_co.append(tuple(mt.dot(k)))
    pixels.append(pixel)

array = np.array(pixels, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.show()
