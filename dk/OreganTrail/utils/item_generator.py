import os
import json
import random

# Want to add i more, but this will suffice for now

# Instruments
instruments = [
    {"name": "Acoustic Guitar", "storage_size": 4, "value": 25},
    {"name": "Harmonica", "storage_size": 1, "value": 10},
    {"name": "Flute", "storage_size": 1, "value": 15},
    {"name": "Drum", "storage_size": 3, "value": 20},
    {"name": "Violin", "storage_size": 3, "value": 30}
]

# Clothing
clothing = [
    {"name": "Shirt", "storage_size": 1, "value": 5},
    {"name": "T-shirt", "storage_size": 1, "value": 3},
    {"name": "Jacket", "storage_size": 2, "value": 10},
    {"name": "Pants", "storage_size": 2, "value": 8},
    {"name": "Shorts", "storage_size": 1, "value": 4},
    {"name": "Skirt", "storage_size": 1, "value": 4},
    {"name": "Dress", "storage_size": 2, "value": 8},
    {"name": "Hat", "storage_size": 1, "value": 3},
    {"name": "Scarf", "storage_size": 1, "value": 2},
    {"name": "Gloves", "storage_size": 1, "value": 3},
    {"name": "Boots", "storage_size": 2, "value": 10},
    {"name": "Shoes", "storage_size": 2, "value": 7}
]

# Animal Skins
animal_skins = [
    {"name": "Ox Skin", "storage_size": 2, "value": 15},
    {"name": "Cow Skin", "storage_size": 2, "value": 14},
    {"name": "Horse Skin", "storage_size": 2, "value": 12},
    {"name": "Chicken Skin", "storage_size": 1, "value": 6},
    {"name": "Goat Skin", "storage_size": 2, "value": 10},
    {"name": "Lamb Skin", "storage_size": 2, "value": 11},
    {"name": "Giraffe Skin", "storage_size": 3, "value": 20},
    {"name": "Kudu Skin", "storage_size": 3, "value": 18},
    {"name": "Springbok Skin", "storage_size": 2, "value": 13},
    {"name": "Impala Skin", "storage_size": 2, "value": 12},
    {"name": "Warthog Skin", "storage_size": 2, "value": 9},
    {"name": "Blesbok Skin", "storage_size": 2, "value": 12},
    {"name": "Guinea Fowl Skin", "storage_size": 1, "value": 5},
    {"name": "Ostrich Skin", "storage_size": 2, "value": 14},
    {"name": "Buffalo Skin", "storage_size": 3, "value": 19}
]

# Containers
containers = [
    {"name": "Bucket", "storage_size": 2, "value": 5},
    {"name": "Barrel", "storage_size": 5, "value": 20},
    {"name": "Water Drum", "storage_size": 5, "value": 25},
    {"name": "Cooler Box (Small)", "storage_size": 3, "value": 10},
    {"name": "Cooler Box (Medium)", "storage_size": 4, "value": 15},
    {"name": "Cooler Box (Large)", "storage_size": 5, "value": 20}
]

# Valuable Items
valuable_items = [
    {"name": "Books", "storage_size": 2, "value": 5},
    {"name": "Jewelry", "storage_size": 1, "value": 25},
    {"name": "Coins", "storage_size": 1, "value": 10},
    {"name": "Precious Metals", "storage_size": 2, "value": 30},
    {"name": "Gems", "storage_size": 1, "value": 50},
    {"name": "Artwork", "storage_size": 3, "value": 40},
    {"name": "Tools", "storage_size": 3, "value": 20},
    {"name": "Seeds", "storage_size": 1, "value": 5},
    {"name": "Maps", "storage_size": 1, "value": 10},
    {"name": "Diaries", "storage_size": 1, "value": 5},
    {"name": "Photographs", "storage_size": 1, "value": 4},
    {"name": "Antiques", "storage_size": 2, "value": 30},
    {"name": "Watches", "storage_size": 1, "value": 20},
    {"name": "Musical Instrument", "storage_size": 4, "value": 35},
    {"name": "Writing Supplies", "storage_size": 1, "value": 3},
    {"name": "Fishing Gear", "storage_size": 3, "value": 15},
    {"name": "Camping Gear", "storage_size": 3, "value": 25},
    {"name": "Hunting Gear", "storage_size": 3, "value": 30},
    {"name": "Cooking Gear", "storage_size": 3, "value": 20},
    {"name": "Handmade Crafts", "storage_size": 2, "value": 10},
    {"name": "Rare Stones", "storage_size": 1, "value": 25},
    {"name": "Collectible Items", "storage_size": 2, "value": 20},
    {"name": "Vintage Clothing", "storage_size": 2, "value": 15},
    {"name": "Historical Documents", "storage_size": 1, "value": 20}
]

# Add category to each item in the respective lists
instruments = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Instrument"} for item in instruments]
clothing = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Clothing"} for item in clothing]
animal_skins = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Animal Skin"} for item in animal_skins]
containers = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Container"} for item in containers]
valuable_items = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Valuables"} for item in valuable_items]

# Combine all miscellaneous items into a single list
all_items = instruments + clothing + animal_skins + containers + valuable_items

# Function to save items to a JSON file
def save_items_to_json(item_list, filename="data/generated/items.json"):
    with open(filename, 'w') as file:
        json.dump(item_list, file, indent=4)

# Check if file exists, if not, create it with the full list of items
def initialize_items_file(filename="data/generated/items.json"):
    if not os.path.exists(filename):
        save_items_to_json(all_items, filename)