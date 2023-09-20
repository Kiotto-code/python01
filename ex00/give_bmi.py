def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    assert len(height) == len(weight), \
        'height weight must have the same length'
    for item in height:
        assert isinstance(item, (int, float)), \
            'height weight must be a list of numbers'
    for item in weight:
        assert isinstance(item, (int, float)), \
            'height weight must be a list of numbers'

    def bodymassindex(weight, height): return (weight / height**2)

    bmi = []

    for h, w in zip(height, weight):
        print(h, w)
        bmi.append(bodymassindex(w, h))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert isinstance(limit, int), 'limit must be an integer'
    for item in bmi:
        assert isinstance(item, (int, float)), 'bmi must be a list of numbers'

    def check_limit(bmi, limit): return (bmi > limit)
    apply_limit = []

    for b in bmi:
        apply_limit.append(check_limit(b, limit))
    return apply_limit


# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
