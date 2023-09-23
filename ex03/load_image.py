import numpy as np
import matplotlib.pyplot as plt
# from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """load an image from a path and return a list of pixels"""
    assert str is not None, 'path must be a string'
    assert isinstance(path, str), 'path must be a string'
    assert path.endswith(('.jpg', 'jpeg', 'png')), 'path must be a jpg file'

    img = plt.imread(path)
    pixels = np.array(img)

    return pixels
