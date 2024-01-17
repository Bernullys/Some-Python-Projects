import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

#open the background image
#background_image = Image.open(sys.argv[1])

try:
    background_image = Image.open(f"resized_images/{sys.argv[1]}")
    rgba_background_image = background_image.convert("RGBA")
except FileNotFoundError:
    sys.exit("The specified image does not exist in the folder bank_of_images")

first_condition = input("Do you want to fix default images to your background image? ")
if first_condition == "yes" or first_condition == "y":
    rigth_arrow = Image.open("assets_images/flechaizquierda.png")
    left_arrow = Image.open("assets_images/flechaderecha.png")
    logo = Image.open("assets_images/logoinstelecsa.png")
    background_button1 = Image.open("assets_images/orange_button.png")
    background_button2 = Image.open("assets_images/orange_button.png")

    arrows_size = (150, 100)
    logo_size = (200, 80)
    background_button_size = (300, 150)
    rz_rigth_arrow = rigth_arrow.resize(arrows_size)
    rz_left_arrow = left_arrow.resize(arrows_size)
    rz_logo = logo.resize(logo_size)
    rz_background_button1 = background_button1.resize(background_button_size)
    rz_background_button2 = background_button1.resize(background_button_size)

    rgba_rigth_arrow = rz_rigth_arrow.convert("RGBA")
    rgba_left_arrow = rz_left_arrow.convert("RGBA")
    rgba_logo = rz_logo.convert("RGBA")
    rgba_background_button1 = rz_background_button1.convert("RGBA")
    rgba_background_button2 = rz_background_button2.convert("RGBA")

    rgba_background_image.paste(rgba_rigth_arrow, (0, 250))
    rgba_background_image.paste(rgba_left_arrow, (874, 250))
    rgba_background_image.paste(rgba_logo, (814, 80))
    rgba_background_image.paste(rgba_background_button1, (362, 100))
    rgba_background_image.paste(rgba_background_button2, (362, 300))


# Calculate the position to paste the overlay image at the center
# position = (
#     (background_image.width - overlay_image.width) // 2,
#     (background_image.height - overlay_image.height) // 2
# )

# Paste the overlay image onto the new image at the calculated position
# overlapped_image.paste(front_image, (position_x, position_y), mask=front_image)


# Specify the rectangle dimensions
# rect_x = 50
# rect_y = 50
# rect_width = 400
# rect_height = 150

# # Draw the rectangle
# draw = ImageDraw.Draw(rgba_background_image)

# draw.rectangle((rect_x, rect_y, rect_x + rect_width, rect_y + rect_height), outline=(0, 0, 0), fill=None)








#Create a drawing context
draw1 = ImageDraw.Draw(rgba_background_image)
draw2 = ImageDraw.Draw(rgba_background_image)

# # Specify the font style ans size
font = ImageFont.truetype("DejaVuSans.ttf", 34)
# # Defined the text content, position and color
text1 = " Emplazamiento"
text2 = " Emplazamiento"
text_position1 = (362, 158)
text_position2 = (362, 358)

text_color = (0, 0, 0)
text_color2 = (255, 0, 0)

# # Draw the text onto the image
draw1.text(text_position1, text1, font = font, fill = text_color)
draw2.text(text_position2, text2, font = font, fill = text_color2)



# Save the overlapped image
rgba_background_image.save(sys.argv[2])