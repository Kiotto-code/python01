from PIL import Image

# Open the image
image = Image.open("animal.jpeg")

# Rotate the image by 90 degrees clockwise
rotated_image = image.rotate(90)

rotated_image.show()

# Save the rotated image

# Close the original and rotated images
image.close()
rotated_image.close()
