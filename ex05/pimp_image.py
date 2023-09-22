import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    array = 255 - array
    array = array.astype(np.uint8)
    plt.imshow(array)
    plt.show()
    return array


def ft_red(array) -> np.ndarray:
    array = array.astype(np.uint8)
    # print(array[:, :, 1])
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    plt.imshow(array)
    plt.show()


def ft_green(array) -> np.array:
    array = array.astype(np.uint8)
    # print(array[:, :, 1])
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    plt.imshow(array)
    plt.show()


def ft_blue(array) -> np.array:
    array = array.astype(np.uint8)
    # print(array[:, :, 1])
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    plt.imshow(array)
    plt.show()


def ft_grey(array) -> np.array:
    if len(array.shape) == 3 and array.shape[2] == 3:
        grey_image = np.mean(array, axis=2).astype(np.uint8)
        plt.imshow(grey_image)
        plt.show()
        return grey_image
    else:
        raise ValueError("Input array must be a color image with three channels (e.g., RGB).")
