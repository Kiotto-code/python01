import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice a list and return a new one"""
    try:
        assert isinstance(family, list), 'family must be a list'
        assert isinstance(start, int), 'start must be an integer'
        assert all(len(element) == len(family[0]) for element in family), \
            'all elements of the list must have the same size'
        family_n = np.array(family)
        print("My shape is : ", family_n.shape)
        newshape = family_n[start:end]
        print("My newshape is : ", newshape.shape)
        return (family[start:end])
    except AssertionError as error:
        print("AssertionError", error)
    except Exception as exception:
        print(exception)

# family =[[1.80, 78.4],
# 		 [2.15, 102.7],
# 		 [2.10, 98.5],
# 		 [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))

# family = [[1.80, 78.4],
# [2.15, 102.7],
# [2.10, 98.5],
# [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
