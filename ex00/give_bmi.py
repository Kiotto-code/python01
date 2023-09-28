import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> \
            list[int | float]:
    """give the bmi of a person"""
    try:
        assert type(height) is list, 'height must be a list'
        assert type(weight) is list, 'weight must be a list'
        assert len(height) == len(weight), \
            'height weight must have the same length'

        return (np.array(weight) / np.array(height)**2).tolist()
    except ZeroDivisionError as error:
        print("ZeroDivisionError", error)
    except AssertionError as error:
        print("AssertionError", error)
    except Exception as exception:
        print(exception)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """limit the bmi of a person"""
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
