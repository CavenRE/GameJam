import os
import json
import random
import datetime

class Pawn:
    def __init__(self, name="random", age="random", gender="random", role="random", skills="random", health=None, stamina=None, body_conditions=None, status_effects=None):
        # Unique ID based on the current timestamp and some random number, wanted to get a little fancy here
        self.id = int(datetime.datetime.now().timestamp() * 1000) + random.randint(0, 999)
        if name == "random":
            names_list = self.load_names_from_json('data/generated/pawns.json')
            random_pawn = random.choice(names_list)
            self.name = random_pawn["name"]
            self.age = random_pawn["age"] if age == "random" else age
            self.gender = random_pawn["gender"] if gender == "random" else gender
        else:
            self.name = name
            self.age = age if age != "random" else random.randint(18, 60)
            self.gender = gender if gender != "random" else random.choice(["Male", "Female"])

        self.role = role if role != "random" else random.choice(self.get_roles())
        self.skills = self.initialize_skills(skills)
        self.health = health if health is not None else random.randint(50, 100)
        self.stamina = stamina if stamina is not None else random.randint(50, 100)
        self.body_conditions = body_conditions if body_conditions is not None else self.default_body_conditions()
        self.status_effects = status_effects if status_effects is not None else []

        self.job = None
        self.assigned_caravan = None
        self.tasks = []
        self.current_task = None

    # This function loads the names from a JSON file
    def load_names_from_json(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found.")
        with open(filename, 'r') as file:
            return json.load(file)

    # This function returns the possible roles for a pawn
    def get_roles(self):
        return ["Leader", "Scout", "Medic", "Cook", "Hunter", "Gatherer", "Engineer", "Mechanic", "Guard", "Drifter"]

    # This function initializes the pawn's skills based on the role
    def initialize_skills(self, skills):
        role_skill_weightings = {
            "Leader": {"Leadership": 5, "Navigation": 3, "Medical": 1, "Cooking": 1, "Hunting": 1, "Mechanics": 1, "Combat": 3, "Foraging": 1, "Research": 1},
            "Scout": {"Leadership": 1, "Navigation": 5, "Medical": 1, "Cooking": 1, "Hunting": 3, "Mechanics": 1, "Combat": 3, "Foraging": 3, "Research": 1},
            "Medic": {"Leadership": 1, "Navigation": 1, "Medical": 5, "Cooking": 3, "Hunting": 1, "Mechanics": 1, "Combat": 1, "Foraging": 3, "Research": 1},
            "Cook": {"Leadership": 1, "Navigation": 1, "Medical": 3, "Cooking": 5, "Hunting": 1, "Mechanics": 1, "Combat": 1, "Foraging": 3, "Research": 1},
            "Hunter": {"Leadership": 1, "Navigation": 3, "Medical": 1, "Cooking": 1, "Hunting": 5, "Mechanics": 1, "Combat": 3, "Foraging": 1, "Research": 1},
            "Gatherer": {"Leadership": 1, "Navigation": 3, "Medical": 1, "Cooking": 1, "Hunting": 1, "Mechanics": 1, "Combat": 3, "Foraging": 5, "Research": 1},
            "Engineer": {"Leadership": 1, "Navigation": 1, "Medical": 1, "Cooking": 1, "Hunting": 1, "Mechanics": 1, "Combat": 1, "Foraging": 1, "Research": 5},
            "Mechanic": {"Leadership": 1, "Navigation": 1, "Medical": 1, "Cooking": 1, "Hunting": 1, "Mechanics": 5, "Combat": 3, "Foraging": 1, "Research": 1},
            "Guard": {"Leadership": 1, "Navigation": 1, "Medical": 1, "Cooking": 1, "Hunting": 1, "Mechanics": 3, "Combat": 5, "Foraging": 1, "Research": 1},
            "Drifter": {"Leadership": 1, "Navigation": 1, "Medical": 1, "Cooking": 1, "Hunting": 1, "Mechanics": 1, "Combat": 1, "Foraging": 1, "Research": 1}
        }

        if skills == "random":
            return self.allocate_random_skills(role_skill_weightings[self.role])
        else:
            all_skills = {skill: 0 for skill in role_skill_weightings[self.role].keys()}
            for skill, value in skills.items():
                all_skills[skill] = value
            return all_skills

    # This function is a bit complex, but it's just a way to allocate random skill points to the pawn based on the role's skill weightings
    def allocate_random_skills(self, weightings):
        total_skill_points = random.randint(15, 25)
        skills = {skill: 0 for skill in weightings}
        
        # Weights for random points allocation, favoring lower numbers
        point_weights = [10, 8, 6, 4, 2]

        while total_skill_points > 0:
            skill = random.choices(list(skills.keys()), weights=weightings.values(), k=1)[0]
            max_points_to_add = min(1, total_skill_points, 7 - skills[skill])  # Ensure no skill exceeds 7
            if max_points_to_add > 0:
                #This can be confusing but it's just a way to randomly choose a number between 1 and max_points_to_add, using the point_weights list to favor lower numbers and splice from the decide on the possible values to add
                points_to_add = random.choices(list(range(1, max_points_to_add + 1)), weights=point_weights[:max_points_to_add], k=1)[0]
                skills[skill] += points_to_add
                total_skill_points -= points_to_add
        return skills

    # This function initializes the body conditions of the pawn
    def default_body_conditions(self):
        body_parts = ["Head", "Left Eye", "Right Eye", "Left Ear", "Right Ear", "Nose", "Mouth", "Neck", "Torso", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
        return {part: "Normal" for part in body_parts}

    # This function returns a JSON representation of the pawn
    def to_json(self):
        return json.dumps(self.__dict__, indent=4)