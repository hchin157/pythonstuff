from PIL import Image

black = (0, 0, 0)
darkGrey = (64, 64, 64)
grey = (128, 128, 128)
lightGrey = (192, 192, 192)
white = (255, 255, 255)

my_image = Image.open("brooklyn.jpg")
image_list = my_image.getdata()
image_list = list(image_list)

recolored = []
for pixel in image_list:
    bright = pixel[0] + pixel[1] + pixel[2]

    if bright < 153:
        recolored.append(white)
    elif bright >= 153 and bright < 306:
        recolored.append(lightGrey)
    elif bright >= 306 and bright < 459:
        recolored.append(grey)
    elif bright >= 459 and bright < 612:
        recolored.append(darkGrey)
    elif bright >= 612 and bright <= 765:
        recolored.append(black)

new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
