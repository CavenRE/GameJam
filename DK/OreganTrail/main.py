import os
import time
from game.menu import main_menu
from utils.name_generator import initialize_names_file
from utils.food_generator import initialize_foods_file
from utils.item_generator import initialize_items_file
from utils.health_generator import initialize_health_file
from utils.weapon_generator import initialize_weapons_file
from utils.detour_generator import initialize_detours_file
from utils.repair_generator import initialize_repairs_file

def main():
    # Initialize the JSON files for items if not created yet
    initialize_items_file()
    initialize_names_file()
    initialize_foods_file()
    initialize_health_file()
    initialize_weapons_file()
    initialize_detours_file()
    initialize_repairs_file()

    # Ensure that the necessary files are created before proceeding, because somehow they are not created in time?
    while not os.path.exists('data/generated/pawns.json'):
        time.sleep(1)

    main_menu()

if __name__ == "__main__":
    main()