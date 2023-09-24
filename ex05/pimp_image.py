import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """flips the bits the opposite the colors"""
    array = 255 - array
    array = array.astype(np.uint8)
    plt.imshow(array)
    plt.axis('off')
    plt.savefig("inverted_image.png", bbox_inches='tight', pad_inches=0)
    plt.show()
    return array


def ft_red(array) -> np.ndarray:
    """shut the green and blue channels"""
    array = array.astype(np.uint8)
    # print(array[:, :, 1])
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    plt.imshow(array)
    plt.axis('off')
    plt.savefig("red_image.png", bbox_inches='tight', pad_inches=0)
    plt.show()


def ft_green(array) -> np.array:
    """shut the red and blue channels"""
    array = array.astype(np.uint8)
    # print(array[:, :, 1])
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    plt.imshow(array)
    plt.axis('off')
    plt.savefig("green_image.png", bbox_inches='tight', pad_inches=0)
    plt.show()


def ft_blue(array) -> np.array:
    """shut the red and green channels"""
    array = array.astype(np.uint8)
    # print(array[:, :, 1])
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    plt.imshow(array)
    plt.axis('off')
    plt.savefig("blue_image.png", bbox_inches='tight', pad_inches=0)
    plt.show()


# def ft_grey(array):
#     """make the image grey using the mean of the RGB channels"""
#     array = array.astype(np.uint8)

#     if len(array.shape) == 3 and array.shape[2] == 3:
#         height, width, _ = array.shape
#         grey_image = np.array([[np.mean(array[i, row])
#                                for i in row] for row in array])
#         # print(grey_image)
#         # grey_image = np.array(array[:, :, :].mean)
#         # print(grey_image)
#         print(grey_image)

#         # So, essentially, taking the mean of the RGB channels at each pixel
#         # location collapses the color information into a single channel
#         # representing brightness, resulting in a grayscale image where each
#         # pixel's color is determined by its intensity.


#         # grey_image = grey_image.reshape(height, width).astype(np.uint8)
#         grey_image = grey_image.reshape(height, width).astype(np.uint8)
#         plt.imshow(grey_image, cmap="gray")
#         plt.axis('off')
#         plt.savefig("grey_image1.png", bbox_inches='tight', pad_inches=0)
#         plt.show()
#         return grey_image
#     else:
#         raise ValueError("Input array must be a color image with three \
#             channels (e.g., RGB).")

# import numpy as np
# import matplotlib.pyplot as plt

def ft_grey(array):
    """Convert a color image to grayscale using the mean of the RGB channels."""
    array = array.astype(np.uint8)

    if len(array.shape) == 3 and array.shape[2] == 3:
        array[:] = array.mean(axis=2,keepdims=1)
        grey_image = array

        plt.imshow(grey_image)
        plt.axis('off')
        plt.savefig("ghuh2.png", bbox_inches='tight', pad_inches=0)
        plt.show()
        
        return grey_image
    else:
        raise ValueError("Input array must be a color image with three channels (e.g., RGB).")


# def ft_grey(array) -> np.array:
#     """Convert an RGB image to grayscale."""
#     array = np.dot(array[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
#     array = array[:, :, np.newaxis]
#     print(array)
#     array = np.repeat(array, 3, axis=2)
#     print(array)
#     plt.imsave("landscape_grey.jpg", array)
#     return array
