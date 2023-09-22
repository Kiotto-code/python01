import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert type(height) == list, 'height must be a list'
        assert type(weight) == list, 'weight must be a list'
        assert len(height) == len(weight), \
            'height weight must have the same length'

        return (np.array(weight) / np.array(height)**2).tolist()
    except AssertionError as error:
        print("AssertionError", error)
    except Exception as exception:
        print(exception)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert isinstance(bmi, list), 'bmi must be a list'
        assert isinstance(limit, int), 'limit must be an integer'
        for item in bmi:
            assert isinstance(item, (int, float)), 'bmi must be a list of \
            numbers'

        def check_limit(bmi, limit): return (bmi > limit)
        apply_limit = []

        for b in bmi:
            apply_limit.append(check_limit(b, limit))
        return apply_limit
    except AssertionError as error:
        print("AssertionError", error)
    except Exception as exception:
        print(exception)


# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
