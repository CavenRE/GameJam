import os
import json
import random

# Meats
meats = [
    {"name": "Ox Meat", "storage_size": 4, "value": 10},
    {"name": "Cow Meat", "storage_size": 4, "value": 9},
    {"name": "Horse Meat", "storage_size": 4, "value": 8},
    {"name": "Chicken Meat", "storage_size": 2, "value": 5},
    {"name": "Goat Meat", "storage_size": 2, "value": 7},
    {"name": "Lamb Meat", "storage_size": 4, "value": 12},
    {"name": "Giraffe Meat", "storage_size": 4, "value": 15},
    {"name": "Kudu Meat", "storage_size": 4, "value": 11},
    {"name": "Springbok Meat", "storage_size": 2, "value": 8},
    {"name": "Impala Meat", "storage_size": 4, "value": 10},
    {"name": "Warthog Meat", "storage_size": 2, "value": 6},
    {"name": "Blesbok Meat", "storage_size": 4, "value": 9},
    {"name": "Guinea Fowl Meat", "storage_size": 2, "value": 7},
    {"name": "Ostrich Meat", "storage_size": 4, "value": 10},
    {"name": "Buffalo Meat", "storage_size": 4, "value": 14}
]

# Vegetables
vegetables = [
    {"name": "Potato", "storage_size": 2, "value": 3},
    {"name": "Carrot", "storage_size": 1, "value": 2},
    {"name": "Tomato", "storage_size": 2, "value": 3},
    {"name": "Cabbage", "storage_size": 2, "value": 2},
    {"name": "Spinach", "storage_size": 2, "value": 3},
    {"name": "Peas", "storage_size": 1, "value": 2},
    {"name": "Corn", "storage_size": 2, "value": 3},
    {"name": "Pumpkin", "storage_size": 2, "value": 4},
    {"name": "Onion", "storage_size": 1, "value": 2},
    {"name": "Sweet Potato", "storage_size": 2, "value": 3},
    {"name": "Butternut Squash", "storage_size": 2, "value": 3},
    {"name": "Green Beans", "storage_size": 1, "value": 2},
    {"name": "Bell Pepper", "storage_size": 1, "value": 2},
    {"name": "Chili Pepper", "storage_size": 1, "value": 2},
    {"name": "Zucchini", "storage_size": 2, "value": 3},
    {"name": "Beetroot", "storage_size": 1, "value": 2},
    {"name": "Radish", "storage_size": 1, "value": 2}
]

# Fruits
fruits = [
    {"name": "Apple", "storage_size": 1, "value": 2},
    {"name": "Banana", "storage_size": 1, "value": 2},
    {"name": "Orange", "storage_size": 1, "value": 2},
    {"name": "Mango", "storage_size": 1, "value": 3},
    {"name": "Pineapple", "storage_size": 1, "value": 3},
    {"name": "Grapes", "storage_size": 1, "value": 3},
    {"name": "Strawberry", "storage_size": 1, "value": 2},
    {"name": "Peach", "storage_size": 1, "value": 2},
    {"name": "Watermelon", "storage_size": 2, "value": 4},
    {"name": "Papaya", "storage_size": 1, "value": 3},
    {"name": "Guava", "storage_size": 1, "value": 2},
    {"name": "Pawpaw", "storage_size": 1, "value": 3},
    {"name": "Granadilla", "storage_size": 1, "value": 3},
    {"name": "Marula Fruit", "storage_size": 1, "value": 3},
    {"name": "Naartjie", "storage_size": 1, "value": 2},
    {"name": "Litchi", "storage_size": 1, "value": 3},
    {"name": "Plum", "storage_size": 1, "value": 2},
    {"name": "Apricot", "storage_size": 1, "value": 2},
    {"name": "Mulberry", "storage_size": 1, "value": 3},
    {"name": "Kiwi", "storage_size": 1, "value": 3}
]

# Produce
produce = [
    {"name": "Eggs", "storage_size": 2, "value": 4},
    {"name": "Milk", "storage_size": 2, "value": 3},
    {"name": "Cheese", "storage_size": 2, "value": 5},
    {"name": "Butter", "storage_size": 1, "value": 3},
    {"name": "Yogurt", "storage_size": 1, "value": 2},
    {"name": "Sour Cream", "storage_size": 1, "value": 2},
    {"name": "Cottage Cheese", "storage_size": 1, "value": 3},
    {"name": "Cream", "storage_size": 2, "value": 4},
    {"name": "Mealie Meal", "storage_size": 2, "value": 3},
    {"name": "Flour", "storage_size": 2, "value": 3},
    {"name": "Sunflower Oil", "storage_size": 2, "value": 4}
]

# Canned Goods
canned_goods = [
    {"name": "Canned Beef", "storage_size": 1, "value": 6},
    {"name": "Canned Chicken", "storage_size": 1, "value": 6},
    {"name": "Canned Fish", "storage_size": 1, "value": 6},
    {"name": "Canned Beans", "storage_size": 1, "value": 4},
    {"name": "Canned Peas", "storage_size": 1, "value": 4},
    {"name": "Canned Corn", "storage_size": 1, "value": 4},
    {"name": "Canned Tomatoes", "storage_size": 1, "value": 4},
    {"name": "Canned Carrots", "storage_size": 1, "value": 4},
    {"name": "Canned Potatoes", "storage_size": 1, "value": 4},
    {"name": "Canned Spinach", "storage_size": 1, "value": 4},
    {"name": "Canned Pumpkin", "storage_size": 1, "value": 4},
    {"name": "Canned Pineapple", "storage_size": 1, "value": 6},
    {"name": "Canned Peaches", "storage_size": 1, "value": 6},
    {"name": "Canned Apricots", "storage_size": 1, "value": 6},
    {"name": "Canned Mixed Fruit", "storage_size": 1, "value": 6},
    {"name": "Canned Soup", "storage_size": 1, "value": 6}
]

# Other foods that don't really fit
other = [
    {"name": "Peanut Butter", "storage_size": 1, "value": 3},
    {"name": "Honey", "storage_size": 1, "value": 4},
    {"name": "Jam", "storage_size": 1, "value": 3},
    {"name": "Bread", "storage_size": 1, "value": 2},
    {"name": "Rice", "storage_size": 2, "value": 3},
    {"name": "Pasta", "storage_size": 2, "value": 3},
    {"name": "Sugar", "storage_size": 1, "value": 2},
    {"name": "Salt", "storage_size": 1, "value": 1},
    {"name": "Pepper", "storage_size": 1, "value": 2},
    {"name": "Animal Feed", "storage_size": 1, "value": 4}
]


# Add category to each item in the respective lists
meats = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Meat"} for item in meats]
vegetables = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Vegetable"} for item in vegetables]
fruits = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Fruit"} for item in fruits]
produce = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Produce"} for item in produce]
canned_goods = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Canned Good"} for item in canned_goods]
other = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Other"} for item in other]

# Combine all food items into a single list
all_foods = meats + vegetables + fruits + produce + canned_goods + other

# Function to save foods to a JSON file
def save_foods_to_json(food_list, filename="data/generated/foods.json"):
    with open(filename, 'w') as file:
        json.dump(food_list, file, indent=4)

# Check if file exists, if not, create it with the full list of items
def initialize_foods_file(filename="data/generated/foods.json"):
    if not os.path.exists(filename):
        save_foods_to_json(all_foods, filename)
