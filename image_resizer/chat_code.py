from PIL import Image

# Load the images
background_image = Image.open('SUBTE-Losa.png')
overlay_image = Image.open('flecha.png')

# Resize the overlay image to the desired size
new_size = (500, 500)
overlay_image = overlay_image.resize(new_size)

# Convert the overlay image to RGBA mode
overlay_image = overlay_image.convert('RGBA')

# Create a new image with the size of the background image
overlapped_image = Image.new('RGBA', background_image.size)

# Paste the background image onto the new image
overlapped_image.paste(background_image, (0, 0))

# Calculate the position to paste the overlay image at the center
position = (
    (background_image.width - overlay_image.width) // 2,
    (background_image.height - overlay_image.height) // 2
)

# Paste the overlay image onto the new image at the calculated position
overlapped_image.paste(overlay_image, position, mask=overlay_image)

# Save or display the overlapped image
overlapped_image.save('overlapped_image.png')
overlapped_image.show()