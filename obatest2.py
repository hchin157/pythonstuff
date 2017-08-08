from PIL import Image

# For recoloring.
darkGreen = (69, 114, 89)
orange = (248, 146, 33)
lightPurple = (188, 136, 233)
taupe = (222, 218, 187)

# Load the image and turn the image into a list of tuples.
my_image = Image.open("brooklyn.jpg")
image_list = my_image.getdata()
image_list = list(image_list)


# Check the intensity of each pixel, determine how to recolor it, and save it in a new list.
recolored = []
for pixel in image_list:

    intensity = pixel[0] + pixel[1] + pixel[2]

    if intensity < 182:
        recolored.append(darkGreen)

    elif intensity >= 182 and intensity < 364:
        recolored.append(orange)

    elif intensity >= 364 and intensity < 546:
        recolored.append(lightPurple)

    elif intensity >=546:
        recolored.append(taupe)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
