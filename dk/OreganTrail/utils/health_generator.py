import os
import json
import random

# Splints
splints = [
    {"name": "Leg Splint", "storage_size": 3, "value": 10},
    {"name": "Arm Splint", "storage_size": 2, "value": 7}
]

# Bandages
bandages = [
    {"name": "Small Bandage", "storage_size": 1, "value": 2},
    {"name": "Medium Bandage", "storage_size": 2, "value": 3},
    {"name": "Large Bandage", "storage_size": 3, "value": 4}
]

# First Aid Kits
first_aid_kits = [
    {"name": "Small First Aid Kit", "storage_size": 2, "value": 16},
    {"name": "Medium First Aid Kit", "storage_size": 3, "value": 24},
    {"name": "Large First Aid Kit", "storage_size": 4, "value": 32}
]

# Basic Medications
basic_medications = [
    {"name": "Pain Killers", "storage_size": 1, "value": 10},
    {"name": "Antibiotics", "storage_size": 1, "value": 25},
    {"name": "Antiseptic", "storage_size": 1, "value": 25},
    {"name": "Medicine", "storage_size": 1, "value": 15}
]

# Add category to each item in the respective lists
splints = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Splint"} for item in splints]
bandages = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Bandage"} for item in bandages]
first_aid_kits = [{"name": item["name"], "storage_size": item["storage_size"], "category": "First Aid Kit"} for item in first_aid_kits]
basic_medications = [{"name": item["name"], "storage_size": item["storage_size"], "category": "Medication"} for item in basic_medications]

# Combine all health health into a single list
health_items = splints + bandages + first_aid_kits + basic_medications

# Function to save health to a JSON file
def save_health_to_json(item_list, filename="data/generated/health.json"):
    with open(filename, 'w') as file:
        json.dump(item_list, file, indent=4)

# Check if file exists, if not, create it with the full list of health
def initialize_health_file(filename="data/generated/health.json"):
    if not os.path.exists(filename):
        save_health_to_json(health_items, filename)
