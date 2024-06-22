import os
import json

# Repair Items
repair_items = [
    {"name": "Wheels", "storage_size": 3},
    {"name": "Axles", "storage_size": 3},
    {"name": "Shocks", "storage_size": 2},
    {"name": "Cover", "storage_size": 2},
    {"name": "Weapon Repair Kit", "storage_size": 1},
    {"name": "Armor Repair Kit", "storage_size": 1},
    {"name": "Tire Patch Kit", "storage_size": 1}
]

# Upgrade Items
upgrade_items = [
    {"name": "Outer Armor", "storage_size": 4},
    {"name": "Reinforced Wheels", "storage_size": 3},
    {"name": "Advanced Shocks", "storage_size": 3},
    {"name": "Weatherproof Cover", "storage_size": 2},
    {"name": "Enhanced Axles", "storage_size": 3},
    {"name": "Storage Expansion", "storage_size": 5},
    {"name": "Water Purification System", "storage_size": 3},
    {"name": "Off-road Tires", "storage_size": 3}
]

# Add category to each item in the respective lists
repair_items = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Repair"} for item in repair_items]
upgrade_items = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Upgrade"} for item in upgrade_items]

# Combine all repair and upgrade items into a single list
all_items = repair_items + upgrade_items

# Function to save items to a JSON file
def save_items_to_json(item_list, filename="data/generated/repair.json"):
    with open(filename, 'w') as file:
        json.dump(item_list, file, indent=4)

# Check if file exists, if not, create it with the full list of items
def initialize_repairs_file(filename="data/generated/repair.json"):
    if not os.path.exists(filename):
        save_items_to_json(all_items, filename)