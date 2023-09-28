import matplotlib.pyplot as plt


def ft_load(path: str) -> list:
    """load an image from a path and return a list of pixels"""
    try:
        assert str is not None, 'path must be a string'
        assert isinstance(path, str), 'path must be a string'
        assert path.endswith(('.jpg', '.jpeg')), 'path must be a jpg file'

        img = plt.imread(path)
        shape = img.shape

        print("The shape of image is: ", shape)
        return img
    except AssertionError as e:
        print(e)
        return None
