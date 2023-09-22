import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    assert str is not None, 'path must be a string'
    assert isinstance(path, str), 'path must be a string'
    assert path.endswith(('.jpg', 'jpeg')), 'path must be a jpg file'

    img = Image.open(path)
    pixels = np.array(img)

    shape = pixels.shape

    print("The shape of image is: ", shape)
    return pixels
