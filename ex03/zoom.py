import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from PIL import Image


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


def main():
    """subject test"""
    load_arr = ft_load("animal.jpeg")
    # print("The shape of image is: ", load_arr.shape)
    print(load_arr)
    zoom_arr = zoom("animal.jpeg")
    print("The new shape after slicing is: ", zoom_arr.shape)
    print(zoom_arr)


if __name__ == "__main__":
    main()
