import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) != 5:
    sys.exit("You must write the input like this: image_name.extension new_image_name.extension width height")
else:
    try:
        bank_of_images_path = "bank_of_images/"
        input_image_path = os.path.join(bank_of_images_path, sys.argv[1])
        image_under_change = Image.open(input_image_path)
    except FileNotFoundError:
        sys.exit("The specified image does not exist in bank_of_images")

inputs_spliter = os.path.splitext(sys.argv[1])
outputs_spliter = os.path.splitext(sys.argv[2])
if inputs_spliter[1].lower() != outputs_spliter[1].lower():
    sys.exit("Images need to have the same extension")

valid_extensions = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
if inputs_spliter[1] not in valid_extensions:
    sys.exit("Input image with invalid extension (jpg - jpeg - png")

width = int(sys.argv[3])
height = int(sys.argv[4])
size = (width, height)
sized_image = ImageOps.fit(image_under_change, size)

resized_images_path = "resized_images/"
output_image_path = os.path.join(resized_images_path, sys.argv[2])
sized_image.save(output_image_path)
