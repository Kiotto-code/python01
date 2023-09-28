import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    try:
        assert isinstance(array, np.ndarray)
        array = 255 - array
        array = array.astype(np.uint8)
        plt.imshow(array)
        plt.axis('off')
        plt.savefig("inverted_image.png", bbox_inches='tight', pad_inches=0)
        plt.show()
        return array
    except AssertionError:
        raise ValueError("Input array must be a color image with three \
            channels (e.g., RGB).")


def ft_red(array) -> np.ndarray:
    """shut the green and blue channels"""
    try:
        assert isinstance(array, np.ndarray)
        array = array.astype(np.uint8)
        array[:, :, 1] = 0
        array[:, :, 2] = 0
        plt.imshow(array)
        plt.axis('off')
        plt.savefig("red_image.png", bbox_inches='tight', pad_inches=0)
        plt.show()
    except AssertionError:
        raise ValueError("Input array must be a color image with three \
            channels (e.g., RGB).")


def ft_green(array) -> np.array:
    """shut the red and blue channels"""
    try:
        assert isinstance(array, np.ndarray)
        array = array.astype(np.uint8)
        array[:, :, 0] = 0
        array[:, :, 2] = 0
        plt.imshow(array)
        plt.axis('off')
        plt.savefig("green_image.png", bbox_inches='tight', pad_inches=0)
        plt.show()
    except AssertionError:
        raise ValueError("Input array must be a color image with three \
            channels (e.g., RGB).")


def ft_blue(array) -> np.array:
    """shut the red and green channels"""
    try:
        assert isinstance(array, np.ndarray)
        array = array.astype(np.uint8)
        array[:, :, 0] = 0
        array[:, :, 1] = 0
        plt.imshow(array)
        plt.axis('off')
        plt.savefig("blue_image.png", bbox_inches='tight', pad_inches=0)
        plt.show()
    except AssertionError:
        raise ValueError("Input array must be a color image with three \
            channels (e.g., RGB).")


def ft_grey(array):
    """make the image grey using the mean of the RGB channels"""
    try:
        assert isinstance(array, np.ndarray)
        array = array.astype(np.uint8)

        if len(array.shape) == 3 and array.shape[2] == 3:
            grey_image = np.full(array.shape, 0)
            grey_image[:] = np.mean(array, axis=2, keepdims=True).\
                astype(np.uint8)
            plt.imshow(grey_image)
            plt.axis('off')
            plt.savefig("grey_image1.png", bbox_inches='tight', pad_inches=0)
            plt.show()
            return grey_image
        else:
            raise ValueError("Input array must be a color image with three \
                channels (e.g., RGB).")
    except AssertionError:
        raise ValueError("Input array must be a color image with three \
            channels (e.g., RGB).")
