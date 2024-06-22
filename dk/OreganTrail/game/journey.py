import os
import json
from game.shop import Shop
from game.interface import Interface

interface = Interface()

SAVE_DIR = 'saves'
JOURNEY_FILE = 'data/journey.json'

# Loads journey, generally passed a file name, this grabs it
def load_journey():
    if not os.path.exists(JOURNEY_FILE):
        raise FileNotFoundError(f"{JOURNEY_FILE} not found.")
    with open(JOURNEY_FILE, 'r') as file:
        return json.load(file)

# Gets the slowest speed of the convoy, because you are only as fast as your slowest member
def get_slowest_speed(convoy):
    return min(caravan["speed"] for caravan in convoy["caravans"])

# Calculate travel distance, checked online for this, to what the travel distance a day for X animals are and seems it's around double the travel speed. Want to come back and rework condition modifiers for rough roads, and what not
def calculate_travel_distance(speed, terrain_modifier=1.0, weather_modifier=1.0):
    return speed * 2 * terrain_modifier * weather_modifier

# Loads the file into an actual usable object, separated it just in case I want to do future weirdness here
def load_convoy(save_file):
    with open(save_file, 'r') as file:
        return json.load(file)

# Save the file! Might need to come back here and update the save file name? Or I just need to add a tag stating save date to get the latest within the save files
def save_convoy(save_file, convoy):
    with open(save_file, 'w') as file:
        json.dump(convoy, file, indent=4)
    interface.print_message(f"Convoy progress saved to {save_file}")

# Initialize the journey data, add inventory and initial setup
def initialize_journey(save_file):
    convoy = load_convoy(save_file)
    journey_data = load_journey()

    # I think these would work? Can always come back and add more stuff here
    convoy["money"] = 500
    convoy["current_distance"] = 0
    convoy["total_distance_traveled"] = 0
    convoy["day"] = 0
    convoy["history"] = []
    convoy["current_location"] = journey_data["journey"][0]["name"]
    convoy["goal_location"] = journey_data["journey"][-1]["name"]
    convoy["next_location"] = journey_data["journey"][1]["name"]
    convoy["distance_to_next"] = journey_data["journey"][1]["distance_km"]

    # Initialize starting inventory (Will flesh this out as we go along)
    initial_inventory = [
        {"name": "Ox Meat", "category": "Meat", "storage_size": 4, "value": 10, "quantity": 5},
        {"name": "Potato", "category": "Vegetable", "storage_size": 2, "value": 3, "quantity": 10},
        {"name": "Rice", "category": "Other", "storage_size": 2, "value": 3, "quantity": 5},
        {"name": "Bow", "category": "Ranged Weapon", "storage_size": 3, "value": 20, "quantity": 2},
        {"name": "Knife", "category": "Melee Weapon", "storage_size": 1, "value": 10, "quantity": 3},
        {"name": "Small First Aid Kit", "category": "First Aid Kit", "storage_size": 2, "value": 16, "quantity": 2},
        {"name": "Bucket", "category": "Container", "storage_size": 2, "value": 5, "quantity": 3},
        {"name": "Cooler Box (Small)", "category": "Container", "storage_size": 3, "value": 10, "quantity": 2},
        {"name": "Medium Bandage", "category": "Bandage", "storage_size": 2, "value": 3, "quantity": 5},
        {"name": "Pain Killers", "category": "Basic Medications", "storage_size": 1, "value": 10, "quantity": 3}
    ]
    convoy["inventory"] = initial_inventory
    
    save_convoy(save_file, convoy)
    return convoy

# Start the journey, initial menu options
def start_journey(save_file):
    convoy = initialize_journey(save_file)
    journey_data = load_journey()

    interface.clear_screen()
    interface.print_journey_status(convoy["day"], "Morning", convoy["current_distance"])
    interface.print_header("We are about to embark", sub=f"Current Location: {convoy['current_location']} | Goal: {convoy['goal_location']}")
    while True:
        interface.print_line_break()
        options = ["Start Journey", "Visit Merchant", "Quit"]
        interface.print_options(options)
        choice = interface.get_user_input()

        if choice == '1':
            interface.print_message("The journey begins...")
            break
        elif choice == '2':
            shop = Shop()
            shop.open_shop()
        elif choice == '3':
            save_convoy(save_file, convoy)
            interface.print_message("Game saved. Returning to main menu.")
            return
        else:
            interface.print_message("Invalid choice. Please choose a valid option.")

    # Start daily travel loop
    while convoy["current_location"] != convoy["goal_location"]:
        interface.clear_screen()
        interface.print_journey_status(convoy["day"], "Morning", convoy["total_distance_traveled"])

        next_poi = next((poi for poi in journey_data["journey"] if poi["name"] == convoy["next_location"]), None)
        interface.print_header(f"On the road to {next_poi['name']}", sub=f"Day {convoy['day']} | Previous Location: {convoy['current_location']}")

        travel_distance = get_slowest_speed(convoy) * 2  # Simplified travel distance for now
        convoy["total_distance_traveled"] += travel_distance
        convoy["current_distance"] += travel_distance
        convoy["day"] += 1

        if convoy["current_distance"] >= convoy["distance_to_next"]:
            convoy["history"].append({"location": convoy["current_location"], "day_arrived": convoy["day"]})
            convoy["current_location"] = convoy["next_location"]
            current_poi_index = journey_data["journey"].index(next_poi)
            next_poi = journey_data["journey"][current_poi_index + 1] if current_poi_index + 1 < len(journey_data["journey"]) else None
            convoy["next_location"] = next_poi["name"] if next_poi else None
            convoy["distance_to_next"] = next_poi["distance_km"] if next_poi else 0
            convoy["current_distance"] = 0

        save_convoy(save_file, convoy)

        options = ["Continue", "Save", "Exit (Main Menu)"]
        interface.print_options(options)
        choice = interface.get_user_input()

        if choice == '1':
            continue
        elif choice == '2':
            save_convoy(save_file, convoy)
        elif choice == '3':
            save_convoy(save_file, convoy)
            interface.print_message("Game saved. Returning to main menu.")
            break
        else:
            interface.print_message("Invalid choice. Please choose a valid option.")

    if convoy["current_location"] == convoy["goal_location"]:
        interface.print_message("Congratulations! You have reached Cape Town!")

## Copy in case, started fresh cause I'm an idiot
# import os
# import json
# from game.interface import Interface

# interface = Interface()

# SAVE_DIR = 'saves'
# JOURNEY_FILE = 'data/journey.json'

# # Loads journey, generaly passed a file name, this grabs it
# def load_journey():
#     if not os.path.exists(JOURNEY_FILE):
#         raise FileNotFoundError(f"{JOURNEY_FILE} not found.")
#     with open(JOURNEY_FILE, 'r') as file:
#         return json.load(file)

# # So gets the slowest speed of the convoy, cause you only as fast as your slowest member
# def get_slowest_speed(convoy):
#     return min(caravan["speed"] for caravan in convoy["caravans"])

# # Calculate travel distance, so checked on line for this, to what teh travel distancea  day for X aimals are and seems it's around double the travel speed. Want to come back and rework condition modifiers for rough roads, and what not
# def calculate_travel_distance(speed, terrain_modifier=1.0, weather_modifier=1.0):
#     return speed * 2 * terrain_modifier * weather_modifier

# # Loads the file into an actual usabke object, separated it just in case I want to do future weirdnes here
# def load_convoy(save_file):
#     with open(save_file, 'r') as file:
#         return json.load(file)

# # Save the file! Might need to come back here and update the save file name? Or I just need ot add a tag stating save date to get latest within teh save files
# def save_convoy(save_file, convoy):
#     with open(save_file, 'w') as file:
#         json.dump(convoy, file, indent=4)
#     interface.print_message(f"Convoy progress saved to {save_file}")

# # Start the journey, this is where the magic happens and my god does it need work, but it's a start
# def start_journey(save_file):
#     journey_data = load_journey()
#     convoy = load_convoy(save_file)
#     total_distance = journey_data["total_distance"]
#     current_distance = convoy.get("current_distance", 0)
#     current_day = convoy.get("day", 0)

#     interface.print_header("Journey")
#     interface.print_line_break()
#     interface.print_message("Your journey begins...")

#     # Works, but I need to rework this, I want to add a stop of sorts and the journey never starts till the user decides to start, so wording may need to change
#     if current_distance == 0:
#         current_poi = journey_data["journey"][0]
#         interface.print_message(f"Day {current_day}: Reached {current_poi['name']} ({current_poi['description']})")

#     # This is super simplistic, and it does wierd things from time to time, so need to add a bunch of stuff here
#     while current_distance < total_distance:
#         # Find the next point of interest based on current distance
#         for poi in journey_data["journey"]:
#             if current_distance < poi["distance_km"]:
#                 current_poi = poi
#                 break

#         interface.print_message(f"Day {current_day}: Reached {current_poi['name']} ({current_poi['description']})")

#         slowest_speed = get_slowest_speed(convoy)
#         terrain_modifier = 1.0  # Placeholderm ideally I want this to be set in teh journey maybe? Or road modifier
#         weather_modifier = 1.0  # Placeholder, this I need to set up a super simple weather system for
#         travel_distance = calculate_travel_distance(slowest_speed, terrain_modifier, weather_modifier)

#         current_distance += travel_distance
#         current_day += 1

#         convoy["current_distance"] = current_distance
#         convoy["day"] = current_day

#         save_convoy(save_file, convoy)

#         # I suppose it works, not to happy with this loop
#         if current_distance >= total_distance:
#             interface.print_message("Congratulations! You have reached Cape Town!")
#             break

#         # I'm  an idiiot, while goign through commenting, I remember I add in convoy states for this fucking purpose!! !GAH! Need to use them
#         interface.print_line_break()
#         options = ["Continue", "Save", "Exit (Main Menu)"]
#         interface.print_options(options)
#         interface.print_line_break()
#         choice = interface.get_user_input()

#         if choice == '1':
#             continue
#         elif choice == '2':
#             save_convoy(save_file, convoy)
#         elif choice == '3':
#             save_convoy(save_file, convoy)
#             interface.print_message("Game saved. Returning to main menu.")
#             break
#         else:
#             interface.print_message("Invalid choice. Please choose a valid option.")