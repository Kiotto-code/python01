from load_image import zoom, ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# def ft_rotate(path: str) -> list:
#     image = plt.imread(path)
#     # print(image)
#     rotated_image = [t for t in zip(*image)]
#     # image_3d = np.expand_dims(rotated_image, axis=2)
#     plt.imshow(rotated_image, cmap="gray")
#     # plt.axis('off')
#     plt.savefig("rotated_image.jpeg", bbox_inches='tight', pad_inches=0)
#     plt.show()
#     return np.array(rotated_image)

def ft_rotate(path: str) -> list:
    # Read the image
    # image = Image.open(path)
    image = plt.imread(path)


    # Transpose the image (rotate 90 degrees counterclockwise)
    rotated_image = [t for t in zip(*image)]

    # Convert the rotated image to a NumPy array
    rotated_image_array = np.array(rotated_image)

    # Save the rotated image
    plt.axis('off')
    plt.imsave("rotated_image.jpeg", rotated_image_array, cmap="gray")

    # Display the rotated image
    plt.imshow(rotated_image_array, cmap="gray")
    plt.axis('on')
    plt.show()

    return rotated_image_array


def main():
    zoom_arr = zoom("animal.jpeg")
    print("The shape of the image is: ", zoom_arr.shape)
    print(zoom_arr)

    rotated_arr = ft_rotate("cropped_image.jpeg")
    print("The new shape after Transpose is: ", rotated_arr.shape)
    print(rotated_arr)


if __name__ == "__main__":
    main()
