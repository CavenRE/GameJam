import os
import json
import random

# Ok I may or may not have a goen a little made with generators....

# Load journey data
with open('data/journey.json', 'r') as file:
    journey_data = json.load(file)

# Detour types
detour_types = ["market", "bandits", "settlement", "town", "poi", "vault", "farm", "ruins", "shopping center", "trading post", "camp", "mine", "bunker", "bridge", "village"]

# Directions
directions = ["north", "south", "east", "west", "northeast", "northwest", "southeast", "southwest"]

# Names based on types
type_names = {
    "market": ["Old Market", "Trading Post", "Merchants' Haven"],
    "bandits": ["Bandit Camp", "Outlaw's Den", "Rogue Encampment"],
    "settlement": ["Refugee Camp", "Survivor's Enclave", "Resettlement Zone"],
    "town": ["Ghost Town", "Ruined Hamlet", "Deserted Village"],
    "poi": ["Historic Landmark", "Ancient Monument", "Mysterious Ruins"],
    "vault": ["Secret Vault", "Hidden Treasure", "Forgotten Bunker"],
    "farm": ["Abandoned Farm", "Overgrown Fields", "Desolate Homestead"],
    "ruins": ["Ruined City", "Collapsed Building", "Wreckage Site"],
    "shopping center": ["Deserted Mall", "Empty Plaza", "Looted Store"],
    "trading post": ["Merchant's Post", "Trading Hub", "Barter Grounds"],
    "camp": ["Survivor Camp", "Makeshift Encampment", "Temporary Shelter"],
    "mine": ["Abandoned Mine", "Collapsed Tunnel", "Ore Deposit"],
    "bunker": ["Military Bunker", "Shelter Bunker", "Underground Safehouse"],
    "bridge": ["Collapsed Bridge", "Old Crossing", "Broken Span"],
    "village": ["Small Hamlet", "Tiny Settlement", "Rural Outpost"]
}

# Conflicting types
conflicting_types = {
    "market": ["bandits"],
    "vault": ["farm"],
    "bunker": ["shopping center"],
    "bridge": ["mine"]
}

# Function to generate a random detour
def generate_random_detour(town_name):
    detour_type = random.choice(detour_types)
    additional_type = None

    # Check for conflicting types
    if detour_type in conflicting_types:
        additional_type = random.choice([t for t in detour_types if t not in conflicting_types[detour_type]])

    types = [detour_type]
    if additional_type:
        types.append(additional_type)

    name = f"{random.choice(type_names[detour_type])} near {town_name}"
    description = f"A {', '.join(types)} located near {town_name}."
    distance_km = random.randint(1, 100)
    direction = random.choice(directions)
    
    return {
        "name": name,
        "type": types,
        "description": description,
        "closest": town_name,
        "distance_km": distance_km,
        "direction": direction
    }

# Generate detours based on journey data
def generate_detours(journey_data, detours_max=3):
    detours = []
    for place in journey_data["journey"]:
        if place["name"] not in ["Gauteng", "Cape Town"]:  # Exclude start and end points
            num_detours = random.randint(0, detours_max)  # Random number of detours per place
            for _ in range(num_detours):
                detour = generate_random_detour(place["name"])
                detours.append(detour)
    return detours

# Save detours to a JSON file
def save_detours_to_json(detours, filename="data/generated/detours.json"):
    with open(filename, 'w') as file:
        json.dump(detours, file, indent=4)

# Check if file exists, if not, create it with the generated detours
def initialize_detours_file(filename="data/generated/detours.json"):
    if not os.path.exists(filename):
        detours = generate_detours(journey_data, 5)
        save_detours_to_json(detours, filename)