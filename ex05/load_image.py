import numpy as np
import matplotlib.pyplot as plt
# from PIL import Image


def ft_load(path: str) -> list:
    assert str is not None, 'path must be a string'
    assert isinstance(path, str), 'path must be a string'
    assert path.endswith(('.jpg', 'jpeg', 'png')), 'path must be a png file'

    img = plt.imread(path)
    pixels = np.array(img)

    return pixels


def zoom(path: str) -> np.ndarray:
    image_data = plt.imread(path)
    cropped_image_data = image_data[114:514, 452:852, 1]
    image_3d = np.expand_dims(cropped_image_data, axis=2)
    # cropped_image = Image.fromarray(cropped_image_data)
    fig, ax = plt.subplots()
    plt.imshow(cropped_image_data, cmap="gray")
    ax.axis('off')
    fig.savefig("cropped_image.jpeg", bbox_inches='tight', pad_inches=0)
    plt.show()
    return image_3d
