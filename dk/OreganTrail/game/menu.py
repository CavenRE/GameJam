import os
import sys
import json
import datetime
from glob import glob
from game.convoy import Convoy
from game.interface import Interface
from game.journey import start_journey

# Need variables for the things we need to do
SAVE_DIR = 'saves'
HIGH_SCORES_FILE = 'data/high_scores.json'
interface = Interface()

# The main menu before the game starts
def main_menu():
    while True:
        options = ["New Game", "Exit"]

        if any(glob(os.path.join(SAVE_DIR, '*.json'))):
            options.insert(0, "Load Game")
            options.insert(0, "Continue")
        
        if os.path.exists(HIGH_SCORES_FILE):
            options.append("High Scores")
        
        interface.display(title="Main Menu", options=options)
        choice = interface.get_user_input()

        if choice == "1" and "Continue" in options:
            latest_save = get_latest_save()
            if latest_save:
                continue_game(latest_save)
            else:
                interface.print_message("No saved games found.")
        elif choice == "2" and "Load Game" in options:
            load_game()
        elif choice == "1" or (choice == "3" and "Load Game" in options):
            new_game()
        elif choice == "3" or (choice == "3" and "High Scores" in options):
            show_high_scores()
        elif choice == "4" or (choice == "2" and "Exit" in options):
            exit_game()
        else:
            interface.print_message("Invalid option. Please try again.")

# Get the latest save file
def get_latest_save():
    save_files = glob(os.path.join(SAVE_DIR, '*.json'))
    if save_files:
        latest_save = max(save_files, key=os.path.getctime)
        return latest_save
    return None

# Load a saved game
def load_game():
    save_files = glob(os.path.join(SAVE_DIR, '*.json'))
    if not save_files:
        interface.print_message("No saved games found.")
        return

    while True:
        options = [os.path.basename(save_file) for save_file in save_files] + ["Back"]
        interface.display(title="Load Game", options=options)
        choice = interface.get_user_input()

        if choice == str(len(options)):
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(save_files):
            chosen_save = save_files[int(choice) - 1]
            sub_choice = input("L. Load, D. Delete, B. Back: ").upper()
            if sub_choice == 'L':
                continue_game(chosen_save)
            elif sub_choice == 'D':
                delete_save(chosen_save)
                save_files = glob(os.path.join(SAVE_DIR, '*.json'))
            elif sub_choice == 'B':
                continue
            else:
                interface.print_message("Invalid choice. Returning to save file list.")
        else:
            interface.print_message("Invalid choice. Please try again.")

# Delete save files
def delete_save(save_file):
    try:
        os.remove(save_file)
        interface.print_message(f"Save file {os.path.basename(save_file)} deleted.")
    except OSError as e:
        interface.print_message(f"Error deleting save file: {e}")

# Continue from the latest game file (Kinda borked cause of how I handle save files, should be fixed later)
def continue_game(save_file):
    interface.print_message("Continuing your journey from the last save point...")
    start_journey(save_file)

# Start a new game loop
def new_game():
    interface.display(title="New Game", messages=["Starting a new game..."])

    convoy_sizes = {
        '1': ('small', 3),
        '2': ('normal', 5),
        '3': ('large', 7)
    }

    while True:
        options = [f"{size.capitalize()} ({members} members)" for size, members in convoy_sizes.values()] + ["Back"]
        interface.display(title="Select Caravan Size", options=options)
        choice = interface.get_user_input()

        if choice == '4':
            return
        elif choice in convoy_sizes:
            selected_size, member_count = convoy_sizes[choice]
            break
        else:
            interface.print_message("Invalid choice. Please try again.")

    provided_details = []
    for i in range(member_count):
        name = input(f"Enter the name of member {i+1} (or type 'skip' to skip the rest): ")
        if name.lower() == 'skip':
            break
        age = input(f"Enter the age of {name}: ")
        gender = input(f"Enter the gender of {name} (Male/Female): ")
        provided_details.append((name, int(age), gender))

    details = provided_details if provided_details else None
    convoy = Convoy(size=selected_size, provided_names=details)
    save_file = convoy.save_to_json()

    interface.print_message("New game started. Your progress has been saved.")
    start_journey(save_file)

# Show high scores
def show_high_scores():
    if os.path.exists(HIGH_SCORES_FILE):
        with open(HIGH_SCORES_FILE, 'r') as file:
            high_scores = json.load(file)
        interface.display(title="High Scores", messages=[f"{score['name']}: {score['score']}" for score in high_scores])
    else:
        interface.print_message("No high scores available.")

# Exit the game
def exit_game():
    interface.display(title="Exit", messages=["Exiting the game. Goodbye!"])
    sys.exit()