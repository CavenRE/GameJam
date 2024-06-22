import os
import json
import random

# Ranged Weapons
ranged_weapons = [
    {"name": "Bow", "storage_size": 3, "value": 20},
    {"name": "Crossbow", "storage_size": 3, "value": 25},
    {"name": "Compound Bow", "storage_size": 3, "value": 30},
    {"name": "Hunting Rifle", "storage_size": 4, "value": 50},
    {"name": "Handgun", "storage_size": 2, "value": 40},
    {"name": "Shotgun", "storage_size": 4, "value": 60},
    {"name": "Longbow", "storage_size": 3, "value": 20},
    {"name": "Recurve Bow", "storage_size": 3, "value": 25},
    {"name": "Throwing Knives", "storage_size": 1, "value": 15},
    {"name": "Spear Gun", "storage_size": 3, "value": 35},
    {"name": "Bolt-Action Rifle", "storage_size": 4, "value": 55},
    {"name": "Sawed-Off Shotgun", "storage_size": 3, "value": 50}
]

# Melee Weapons
melee_weapons = [
    {"name": "Knife", "storage_size": 1, "value": 10},
    {"name": "Machete", "storage_size": 2, "value": 15},
    {"name": "Sword", "storage_size": 3, "value": 25},
    {"name": "Axe", "storage_size": 3, "value": 20},
    {"name": "Hatchet", "storage_size": 2, "value": 15},
    {"name": "Club", "storage_size": 2, "value": 10},
    {"name": "Baseball Bat", "storage_size": 3, "value": 15},
    {"name": "Crowbar", "storage_size": 2, "value": 10},
    {"name": "Hammer", "storage_size": 1, "value": 8},
    {"name": "Tire Iron", "storage_size": 2, "value": 10},
    {"name": "Sledgehammer", "storage_size": 4, "value": 25},
    {"name": "Scythe", "storage_size": 3, "value": 20},
    {"name": "Spear", "storage_size": 3, "value": 15},
    {"name": "Chain", "storage_size": 2, "value": 10},
    {"name": "Pipe Wrench", "storage_size": 2, "value": 12},
    {"name": "Cleaver", "storage_size": 1, "value": 8}
]

# Defense weapons
defense_weapons = [
    {"name": "Makeshift Shield", "storage_size": 3, "value": 15},
    {"name": "Shield", "storage_size": 4, "value": 20},
    {"name": "Riot Shield", "storage_size": 5, "value": 25},
    {"name": "Basic Armor Vest", "storage_size": 3, "value": 30},
    {"name": "Bullet Proof Vest", "storage_size": 4, "value": 40},
    {"name": "Leg Armor", "storage_size": 2, "value": 20},
    {"name": "Gas Mask", "storage_size": 1, "value": 15},
    {"name": "Helmet", "storage_size": 2, "value": 25},
    {"name": "Kneepads", "storage_size": 1, "value": 10},
    {"name": "Elbow Pads", "storage_size": 1, "value": 10},
    {"name": "Arm Guards", "storage_size": 1, "value": 15},
    {"name": "Leg Guards", "storage_size": 2, "value": 20}
]

# Ammo
ammo = [
    {"name": "Arrow", "storage_size": 1, "value": 5, "quantity": 10},
    {"name": "Bolt", "storage_size": 1, "value": 15, "quantity": 6},
    {"name": "Rifle Bullet", "storage_size": 1, "value": 30, "quantity": 3},
    {"name": "Handgun Bullet", "storage_size": 1, "value": 25, "quantity": 5},
    {"name": "Shotgun Shell", "storage_size": 1, "value": 40, "quantity": 5},
    {"name": "Spear Bolt", "storage_size": 1, "value": 25, "quantity": 1}
]

# Add category to each item in the respective lists
ranged_weapons = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Ranged Weapon"} for item in ranged_weapons]
melee_weapons = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Melee Weapon"} for item in melee_weapons]
defense_weapons = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Armour"} for item in defense_weapons]
ammo = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Ammo"} for item in ammo]

# Combine all weapon weapons into a single list
all_weapon_weapons = ranged_weapons + melee_weapons + defense_weapons + ammo

# Function to save weapons to a JSON file
def save_weapons_to_json(item_list, filename="data/generated/weapons.json"):
    with open(filename, 'w') as file:
        json.dump(item_list, file, indent=4)

# Check if file exists, if not, create it with the full list of weapons
def initialize_weapons_file(filename="data/generated/weapons.json"):
    if not os.path.exists(filename):
        save_weapons_to_json(all_weapon_weapons, filename)