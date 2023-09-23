from load_image import zoom
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
    """rotates the image by 90 degrees clockwise, saves it as rotated_image"""
    image = plt.imread(path)

    rotated_image = [t for t in zip(*image)]
    rotated_image_array = np.array(rotated_image)

    plt.axis('off')
    plt.imsave("rotated_image.jpeg", rotated_image_array, cmap="gray")

    plt.imshow(rotated_image_array, cmap="gray")
    plt.axis('on')
    plt.show()

    return rotated_image_array


def main():
    """subject test"""
    zoom_arr = zoom("animal.jpeg")
    print("The shape of the image is: ", zoom_arr.shape)
    print(zoom_arr)

    rotated_arr = ft_rotate("cropped_image.jpeg")
    print("The new shape after Transpose is: ", rotated_arr.shape)
    print(rotated_arr)
    # rotated_arr.reshape(rotated_arr.shape[0], rotated_arr.shape[1], 4)
    # print(rotated_arr)


if __name__ == "__main__":
    main()
