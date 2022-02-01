"""Food Calculator for Oxygen Not Included"""
from collections import defaultdict
from food import preorder, food_dict


def foodcalc(dupes, name):
    """Calculates resource cost of specified food.
    >>>foodcalc(4, "Gristle Berry")
    {'Gristle Berry': 2.0, 'Bristle Blossom': 12.0, 'Water': 240.0}"""
    food = food_dict[name]
    kcal = dupes * 1000
    values = defaultdict(int)
    values[name] += round(kcal / food.calories, 2)
    preorder(food, kcal / food.calories, values)
    return dict(values)
