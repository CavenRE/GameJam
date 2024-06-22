import json
import random
import os
from datetime import datetime

# Function to load games from the JSON file
def load_games():
    with open('games.json', 'r') as file:
        return json.load(file)

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to randomly select games from the list
def select_random_games(games, num=10):
    return random.sample(games, num)

# Function to select games randomly based on weights
def weighted_random_sample(games, num=3):
    total_weight = sum(game["weight"] for game in games)
    chosen_indices = set()

    while len(chosen_indices) < num:
        rand_value = random.uniform(0, total_weight)
        cumulative_weight = 0
        for i, game in enumerate(games):
            if i in chosen_indices:
                continue
            cumulative_weight += game["weight"]
            if rand_value < cumulative_weight:
                chosen_indices.add(i)
                total_weight -= game["weight"]
                break

    return [games[i] for i in chosen_indices]


# Function to select a game randomly based on weights
def select_game(games):
    total_weight = sum(game["weight"] for game in games)
    rand_value = random.uniform(0, total_weight)
    cumulative_weight = 0
    selected_game = None

    for game in games:
        cumulative_weight += game["weight"]
        if rand_value < cumulative_weight:
            selected_game = game
            break

    return selected_game, rand_value

# Function to print a decorative border
def print_border(width):
    print("╾" + ("╶" * (width - 2)) + "╼")

# Function to print game options
def print_game_options(games):
    print_border(80)
    for i, game in enumerate(games):
        description = game.get("description", "No description available.")
        tag = game.get("tag", ["No tag specified."])
        weight = game.get("weight", 1)
        print(f"{i + 1}. {game['name']}\n   Description: {description}\n   Tag: {', '.join(tag)}\n   Weight: {weight}")
        print_border(80)

# Function to append the winner to README.md
def append_winner_to_readme(winner):
    with open('README.md', 'a') as file:
        file.write(f"\n- {datetime.now().strftime('%Y-%m-%d')}: **{winner['name']}** - {winner['description']}\n")
        file.write(f"  - **Tags/Mechanics**: {', '.join(winner['tag'])}\n")

# Function to update and display the current state
def update_display(title, games):
    clear_screen()
    print(title)
    print_game_options(games)

# Function for round-robin voting
def round_robin_voting(selected_games, voters, num_votes=3):
    total_votes = {voter: 0 for voter in voters}
    vote_index = {voter: 0 for voter in voters}
    valid_vote = True
    voter_index = 0

    while any(votes < num_votes for votes in total_votes.values()):
        current_voter = voters[voter_index % len(voters)]
        vote = input(f"{current_voter}, enter the number of the game to vote for (1-10): ").strip()
        if not vote.isdigit() or int(vote) < 1 or int(vote) > 10:
            print("Invalid vote. Please enter a number between 1 and 10.")
            valid_vote = False
            continue
        vote_index[current_voter] = int(vote) - 1
        selected_games[vote_index[current_voter]]["weight"] += 1  # Update weight immediately
        total_votes[current_voter] += 1
        update_display("Round 1 Voting:", selected_games)  # Refresh display after each vote
        voter_index += 1

    return valid_vote

def main():
    games = load_games()

    while True:
        # Randomly select 10 games
        selected_games = select_random_games(games, 10)
        update_display("Selected Games:", selected_games)

        command = input("Type 'Start' or 'Go' to begin the voting process or 'Roll' to select new games: ").strip().lower()
        if command in ["start", "go"]:
            break
        elif command == "roll":
            continue

    while True:
        # Round 1: Bob and Frank vote using round-robin method
        voters = ["Bob", "Frank"]
        if round_robin_voting(selected_games, voters):
            break

    clear_screen()
    print("Weights after Round 1 Voting:")
    print_game_options(selected_games)

    # Select 3 games based on weights after Round 1
    round_2_games = weighted_random_sample(selected_games, 3)

    # Final vote: Bob and Frank vote again using round-robin method
    while True:
        update_display("Final Voting:", round_2_games)

        votes = {"Bob": 0, "Frank": 0}
        valid_vote = True
        for voter in ["Bob", "Frank"]:
            vote = input(f"{voter}, enter the number of the game to vote for (1-3): ").strip()
            if not vote.isdigit() or int(vote) < 1 or int(vote) > 3:
                print("Invalid vote. Please enter a number between 1 and 3.")
                valid_vote = False
                break
            votes[voter] = int(vote) - 1
            round_2_games[votes[voter]]["weight"] += 1  # Update weight immediately
            update_display("Final Voting:", round_2_games)  # Refresh display after each vote
        if valid_vote:
            break

    clear_screen()
    print("Weights after Final Voting:")
    print_game_options(round_2_games)

    # Select the final game based on weights after Final Voting
    final_game, roll_value = select_game(round_2_games)
    clear_screen()
    print(f"\nThe roll value was: {roll_value:.2f}")
    print(f"The selected game to build next is: {final_game['name']} with weight {final_game['weight']}")

    # Append the winner to README.md
    append_winner_to_readme(final_game)

if __name__ == "__main__":
    main()