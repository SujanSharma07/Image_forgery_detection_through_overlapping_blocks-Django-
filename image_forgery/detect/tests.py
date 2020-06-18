from django.test import TestCase

# Create your tests here.
allowed_extention = ["jpeg","jpg","png"]

image = "image.jpesg"
img,extention = image.split(".")
if extention in allowed_extention:
    print(extention)
    print(img)