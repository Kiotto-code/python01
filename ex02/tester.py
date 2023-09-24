from load_image import ft_load


def main():
    """Main function"""
    try:
        print(ft_load("landscape.jpg"))
    except AssertionError as error:
        print(error)
    except Exception as exception:
        print(exception)


if __name__ == '__main__':
    main()
