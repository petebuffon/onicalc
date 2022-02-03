"""General tree structure of oni's food."""
from collections import deque


class Node():
    """Base general tree class"""
    def __init__(self, name):
        """name and children"""
        self.name = name
        self.children = []

    def insert(self, name, node):
        """Inserts defined node into tree at named node."""
        parent_node = search(self, name)
        parent_node.children.append(node)

    def __repr__(self):
        """Node represented by name."""
        return str(self.name)


class Recipe(Node):
    """Recipe node"""
    def __init__(self, name, calories):
        """name, children, calories"""
        super().__init__(name)
        self.calories = calories


class Food(Node):
    """Food node"""
    def __init__(self, name, quantity):
        """name, children, quantity"""
        super().__init__(name)
        self.quantity = quantity


class Resource(Node):
    """Resource node"""
    def __init__(self, name, quantity):
        """name, children, quantity"""
        super().__init__(name)
        self.quantity = quantity


class Plant(Node):
    """Plant node"""
    def __init__(self, name, growth, production):
        """name, children, growth, production, quantity"""
        super().__init__(name)
        self.growth = growth
        self.production = production
        self.quantity = 1


def search(root, name):
    """Search root general tree for child node with name."""
    stack = deque([root])
    while stack:
        node = stack.popleft()
        if node.name == name:
            return node
        stack.extend(node.children)


def preorder(node, quantity, values):
    """Preorder traversal to produce dict of resources."""
    if type(node) == Food:
        quantity *= node.quantity
    elif type(node) == Resource:
        values[node.name] += round(quantity * node.quantity, 2)
    elif type(node) == Plant:
        quantity *= node.growth / node.production
        values[node.name] += round(quantity, 2)
    if node.children:
        stack = deque(node.children)
        while stack:
            temp = stack.popleft()
            preorder(temp, quantity, values)


bristle_blossom = Plant("Bristle Blossom", 6, 1)
bristle_blossom.insert("Bristle Blossom", Resource("Water", 20))

dusk_cap = Plant("Dusk Cap", 7.5, 1)
dusk_cap.insert("Dusk Cap", Resource("Slime", 4))

nosh_sprout = Plant("Nosh Sprout", 21, 12)
nosh_sprout.insert("Nosh Sprout", Resource("Ethanol", 20))
nosh_sprout.insert("Nosh Sprout", Resource("Dirt", 5))

bog_bucket = Plant("Bog Bucket", 6.6, 1)
bog_bucket.insert("Bog Bucket", Resource("Polluted Water", 40))

mealwood = Plant("Mealwood", 3, 1)
mealwood.insert("Mealwood", Resource("Dirt", 10))

pincha_pepper = Plant("Pincha Pepper", 8, 4)
pincha_pepper.insert("Pincha Pepper", Resource("Polluted Water", 35))
pincha_pepper.insert("Pincha Pepper", Resource("Phosphorite", 1))

bristle_berry = Recipe("Bristle Berry", 1600)
bristle_berry.insert("Bristle Berry", bristle_blossom)

grubfruit_plant = Plant("Grubfruit Plant", 8, 8)
grubfruit_plant.insert("Grubfruit Plant", Resource("Sulfur", 10))

spindly_grubfruit_plant = Plant("Spindly Grubfruit Plant", 4, 1)
grubfruit_plant.insert("Grubfruit Plant", Resource("Sulfur", 10))

sleet_wheat = Plant("Sleet Wheat", 18, 18)
sleet_wheat.insert("Sleet Wheat", Resource("Water", 20))
sleet_wheat.insert("Sleet Wheat", Resource("Dirt", 5))

waterweed = Plant("Waterweed", 12, 12)
waterweed.insert("Waterweed", Resource("Salt Water", 5))
waterweed.insert("Waterweed", Resource("Bleach Stone", 0.5))

lettuce = Recipe("Lettuce", 400)
lettuce.insert("Lettuce", waterweed)

mushroom_wrap = Recipe("Mushroom Wrap", 4800)
mushroom_wrap.insert("Mushroom Wrap", Food("Fried Mushroom", 1))
mushroom_wrap.insert("Fried Mushroom", Food("Mushroom", 1))
mushroom_wrap.insert("Mushroom", dusk_cap)
mushroom_wrap.insert("Mushroom Wrap", Food("Lettuce", 4))
mushroom_wrap.insert("Lettuce", waterweed)

meal_lice = Recipe("Meal Lice", 600)
meal_lice.insert("Meal Lice", mealwood)

meat = Recipe("Meat", 1600)

liceloaf = Recipe("Liceloaf", 1700)
liceloaf.insert("Liceloaf", Food("Meal Lice", 2))
liceloaf.insert("Meal Lice", mealwood)
liceloaf.insert("Liceloaf", Resource("Water", 50))

pickled_meal = Recipe("Pickled Meal", 1800)
pickled_meal.insert("Pickled Meal", Food("Meal Lice", 3))
pickled_meal.insert("Meal Lice", mealwood)

mush_bar = Recipe("Mush Bar", 800)
mush_bar.insert("Mush Bar", Resource("Water", 75))
mush_bar.insert("Mush Bar", Resource("Dirt", 75))

mush_fry = Recipe("Mush Fry", 1050)
mush_fry.insert("Mush Fry", Food("Mush Bar", 1))
mush_fry.insert("Mush Bar", Resource("Water", 75))
mush_fry.insert("Mush Bar", Resource("Dirt", 75))

omelette = Recipe("Omelette", 2800)
omelette.insert("Omelette", Resource("Raw Egg", 1))

roast_grubfruit_nut = Recipe("Roast Grubfruit Nut", 1200)
roast_grubfruit_nut.insert("Roast Grubfruit Nut",
                           Food("Spindly Grubfruit", 1))
roast_grubfruit_nut.insert("Spindly Grubfruit", grubfruit_plant)

pepper_bread = Recipe("Pepper Bread", 4000)
pepper_bread.insert("Pepper Bread", Food("Sleet Wheat Grain", 10))
pepper_bread.insert("Sleet Wheat Grain", sleet_wheat)
pepper_bread.insert("Pepper Bread", Food("Pincha Peppernut", 1))
pepper_bread.insert("Pincha Peppernut", pincha_pepper)

barbeque = Recipe("Barbeque", 4000)
barbeque.insert("Barbeque", Resource("Meat", 2))

cooked_fish = Recipe("Cooked Fish", 1600)
cooked_fish.insert("Cooked Fish", Resource("Pacu Fillet", 1))

pacu_fillet = Recipe("Pacu Fillet", 1000)

frost_burger = Recipe("Frost Burger", 6000)
frost_burger.insert("Frost Burger", Food("Lettuce", 1))
frost_burger.insert("Lettuce", waterweed)
frost_burger.insert("Frost Burger", Food("Frost Bun", 1))
frost_burger.insert("Frost Bun", Food("Sleet Wheat Grain", 3))
frost_burger.insert("Sleet Wheat Grain", sleet_wheat)
frost_burger.insert("Frost Burger", Food("Barbeque", 1))
frost_burger.insert("Barbeque", Resource("Meat", 2))

gristle_berry = Recipe("Gristle Berry", 2000)
gristle_berry.insert("Gristle Berry", Food("Bristle Berry", 1))
gristle_berry.insert("Bristle Berry", bristle_blossom)

tofu = Recipe("Tofu", 3600)
tofu.insert("Tofu", Food("Nosh Bean", 6))
tofu.insert("Nosh Bean", nosh_sprout)
tofu.insert("Tofu", Resource("Water", 50))

fried_mushroom = Recipe("Fried Mushroom", 2800)
fried_mushroom.insert("Fried Mushroom", Food("Mushroom", 1))
fried_mushroom.insert("Mushroom", dusk_cap)

mushroom = Recipe("Mushroom", 2400)
mushroom.insert("Mushroom", dusk_cap)

frost_bun = Recipe("Frost Bun", 1200)
frost_bun.insert("Frost Bun", Food("Sleet Wheat Grain", 3))
frost_bun.insert("Sleet Wheat Grain", sleet_wheat)

swampy_delights = Recipe("Swampy Delights", 2240)
swampy_delights.insert("Swampy Delights", Food("Bog Jelly", 1))
swampy_delights.insert("Bog Jelly", bog_bucket)

grubfruit = Recipe("Grubfruit", 250)
grubfruit.insert("Grubfruit", grubfruit_plant)

spindly_grubfruit = Recipe("Spindly Grubfruit", 800)
spindly_grubfruit.insert("Spindly Grubfruit", spindly_grubfruit_plant)

grubfruit_preserve = Recipe("Grubfruit Preserve", 2400)
grubfruit_preserve.insert("Grubfruit Preserve", Resource("Sucrose", 4))
grubfruit_preserve.insert("Grubfruit Preserve", Food("Grubfruit", 8))
grubfruit_preserve.insert("Grubfruit", grubfruit_plant)

mixed_berry_pie = Recipe("Mixed Berry Pie", 4200)
mixed_berry_pie.insert("Mixed Berry Pie", Food("Grubfruit", 4))
mixed_berry_pie.insert("Grubfruit", grubfruit_plant)
mixed_berry_pie.insert("Grubfruit Plant", Resource("Sulfur", 10))
mixed_berry_pie.insert("Mixed Berry Pie", Food("Gristle Berry", 1))
mixed_berry_pie.insert("Gristle Berry", Food("Bristle Berry", 1))
mixed_berry_pie.insert("Bristle Berry", bristle_blossom)
mixed_berry_pie.insert("Mixed Berry Pie", Food("Sleet Wheat Grain", 3))
mixed_berry_pie.insert("Sleet Wheat Grain", sleet_wheat)

berry_sludge = Recipe("Berry Sludge", 4000)
berry_sludge.insert("Berry Sludge", Food("Sleet Wheat Grain", 5))
berry_sludge.insert("Sleet Wheat Grain", sleet_wheat)
berry_sludge.insert("Berry Sludge", Food("Bristle Berry", 1))
berry_sludge.insert("Bristle Berry", bristle_blossom)

spicy_tofu = Recipe("Spicy Tofu", 4000)
spicy_tofu.insert("Spicy Tofu", Food("Tofu", 1))
spicy_tofu.insert("Spicy Tofu", Food("Pincha Peppernut", 1))
spicy_tofu.insert("Pincha Peppernut", pincha_pepper)
spicy_tofu.insert("Tofu", Food("Nosh Bean", 6))
spicy_tofu.insert("Nosh Bean", nosh_sprout)
spicy_tofu.insert("Tofu", Resource("Water", 50))

stuffed_berry = Recipe("Stuffed Berry", 4400)
stuffed_berry.insert("Stuffed Berry", Food("Pincha Peppernut", 2))
stuffed_berry.insert("Pincha Peppernut", pincha_pepper)
stuffed_berry.insert("Stuffed Berry", Food("Gristle Berry", 2))
stuffed_berry.insert("Gristle Berry", Food("Bristle Berry", 1))
stuffed_berry.insert("Bristle Berry", bristle_blossom)

surf_n_turf = Recipe("Surf'n'Turf", 6000)
surf_n_turf.insert("Surf'n'Turf", Food("Barbeque", 1))
surf_n_turf.insert("Barbeque", Resource("Meat", 2))
surf_n_turf.insert("Surf'n'Turf", Food("Cooked Fish", 1))
surf_n_turf.insert("Cooked Fish", Resource("Pacu Fillet", 1))

bog_jelly = Recipe("Bog Jelly", 1840)
bog_jelly.insert("Bog Jelly", bog_bucket)

food_dict = {
    "Gristle Berry": gristle_berry,
    "Tofu": tofu,
    "Fried Mushroom": fried_mushroom,
    "Swampy Delights": swampy_delights,
    "Grubfruit Preserve": grubfruit_preserve,
    "Mixed Berry Pie": mixed_berry_pie,
    "Berry Sludge": berry_sludge,
    "Frost Bun": frost_bun,
    "Stuffed Berry": stuffed_berry,
    "Spicy Tofu": spicy_tofu,
    "Surf'n'Turf": surf_n_turf,
    "Barbeque": barbeque,
    "Bristle Berry": bristle_berry,
    "Mushroom Wrap": mushroom_wrap,
    "Meal Lice": meal_lice,
    "Liceloaf": liceloaf,
    "Pickled Meal": pickled_meal,
    "Mush Bar": mush_bar,
    "Mush Fry": mush_fry,
    "Omelette": omelette,
    "Pepper Bread": pepper_bread,
    "Cooked Fish": cooked_fish,
    "Frost Burger": frost_burger,
    "Frost Bun": frost_bun,
    "Swampy Delights": swampy_delights,
    "Roast Grubfruit Nut": roast_grubfruit_nut,
    "Pacu Fillet": pacu_fillet,
    "Mushroom": mushroom,
    "Lettuce": lettuce,
    "Meat": meat,
    "Grubfruit": grubfruit,
    "Spindly Grubfruit": spindly_grubfruit,
    "Bog Jelly": bog_jelly
}
