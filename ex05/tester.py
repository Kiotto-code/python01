from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    try:
        array = ft_load("landscape.jpg")
        if array is None:
            print("Error: ft_load returned None")
            exit()

        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except Exception as e:
        print(e.__class__.__name__ + ": " + str(e))
        return None


if __name__ == "__main__":
    main()
