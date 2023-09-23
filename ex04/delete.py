import matplotlib.pyplot as plt
from PIL import Image

# Load the image using Pillow
path = "animal.jpeg"
image = Image.open(path)

# Define the new dimensions (width, height)
new_width = 200
new_height = 150

# Resize the image using Pillow
resized_image = image.resize((new_width, new_height))

# Save or display the resized image
resized_image.save("resized_image.png")
plt.imshow(resized_image)
plt.axis('on')
plt.show()
