from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
# height = ['asd', 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
# bmi = give_bmi(height, None)
# bmi = give_bmi(None, None)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
