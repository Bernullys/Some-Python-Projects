import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

#open the background image
background_image = Image.open(sys.argv[1])

#open overlay image
front_image = Image.open(sys.argv[2])

# Resize the overlay image to the desired size
new_size = (150, 150)
front_image = front_image.resize(new_size)

# Convert the overlay image to RGBA mode
# This is to have a transparency

front_image = front_image.convert("RGBA")

#defining position on witch front_image is goint to be
position_x = int(sys.argv[3])
position_y = int(sys.argv[4])

# Create a new image with the size of the background image
# This is to have a transparency
overlapped_image = Image.new('RGBA', background_image.size)

# Paste the background image onto the new image
overlapped_image.paste(background_image, (0, 0))

# Calculate the position to paste the overlay image at the center
# position = (
#     (background_image.width - overlay_image.width) // 2,
#     (background_image.height - overlay_image.height) // 2
# )

# Paste the overlay image onto the new image at the calculated position
overlapped_image.paste(front_image, (position_x, position_y), mask=front_image)

# Create a drawing context
draw = ImageDraw.Draw(overlapped_image)

# Specify the font style ans size
#font = ImageFont.truetype("arial.ttf", 30)

# Defined the text content, position and color
text = "Hello Iddero HC3"
text_position = (50, 50)
text_color = (255, 255, 255)

# Draw the text onto the image
draw.text(text_position, text, fill = text_color)


# Save the overlapped image
overlapped_image.save(sys.argv[5])