import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_load(path: str) -> list:
    """load an image from a path and return a list of pixels"""
    try:
        assert str is not None, 'path must be a string'
        assert isinstance(path, str), 'path must be a string'
        assert path.endswith(('.jpg', 'jpeg')), 'path must be a jpg file'

        img = plt.imread(path)
        shape = img.shape

        print("The shape of image is: ", shape)
        return img
    except AssertionError as e:
        print(e)
        return None


def zoom(path: str) -> np.ndarray:
    """crop the image and return a 3d array"""
    image_data = plt.imread(path)
    cropped_image_data = image_data[100:500, 450:850, 1]
    # cropped_image_data = image_data[114:514, 452:852, 1]
    cropped_image = Image.fromarray(cropped_image_data)
    image_3d = np.expand_dims(cropped_image, axis=2)
    resized_image = cropped_image.resize((400, 400))
    resized_image.save("cropped_image.jpeg")

    plt.imshow(resized_image, cmap="gray")
    plt.axis('on')
    plt.show()
    return image_3d
