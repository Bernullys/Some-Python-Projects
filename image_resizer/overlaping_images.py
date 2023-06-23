import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

#open the background image
#background_image = Image.open(sys.argv[1])

try:
    background_image = Image.open(f"bank_of_images/{sys.argv[1]}")
    rgba_background_image = background_image.convert("RGBA")
except FileNotFoundError:
    sys.exit("The specified image does not exist in the folder bank_of_images")

first_condition = input("Do you want to fix default images to your background image? ")
if first_condition == "yes" or first_condition == "y":
    rigth_arrow = Image.open("assets_images/flechaderecha.png")
    left_arrow = Image.open("assets_images/flechaizquierda.png")
    logo = Image.open("assets_images/logoinstelecsa.png")

    arrows_size = (150, 150)
    logo_size = (200, 80)
    rz_rigth_arrow = rigth_arrow.resize(arrows_size)
    rz_left_arrow = left_arrow.resize(arrows_size)
    rz_logo = logo.resize(logo_size)

    rgba_rigth_arrow = rz_rigth_arrow.convert("RGBA")
    rgba_left_arrow = rz_left_arrow.convert("RGBA")
    rgba_logo = rz_logo.convert("RGBA")

    rgba_background_image.paste(rgba_rigth_arrow, (0, 225))
    rgba_background_image.paste(rgba_left_arrow, (949, 225))
    rgba_background_image.paste(rgba_logo, (874, 10))

# Calculate the position to paste the overlay image at the center
# position = (
#     (background_image.width - overlay_image.width) // 2,
#     (background_image.height - overlay_image.height) // 2
# )

# Paste the overlay image onto the new image at the calculated position
# overlapped_image.paste(front_image, (position_x, position_y), mask=front_image)

# # Create a drawing context
# draw = ImageDraw.Draw(overlapped_image)

# # Specify the font style ans size
# #font = ImageFont.truetype("arial.ttf", 30)

# # Defined the text content, position and color
# text = "Hello Iddero HC3"
# text_position = (50, 50)
# text_color = (255, 255, 255)

# # Draw the text onto the image
# draw.text(text_position, text, fill = text_color)


# Save the overlapped image
rgba_background_image.save(sys.argv[2])