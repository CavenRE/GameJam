import os
import json
import random
import datetime
from game.pawn import Pawn
from game.caravan import Caravan

class Convoy:
    def __init__(self, size="random", provided_names=None):
        self.id = int(datetime.datetime.now().timestamp())
        self.state = "stationary"
        self.size = size if size != "random" else random.choice(["small", "normal", "large"])
        self.caravans = self.initialize_caravans()
        self.leader = None
        self.pawns = self.initialize_pawns(provided_names)
        self.assign_pawns_to_caravan(self.pawns)

    # This function initializes the caravans based on the convoy size
    def initialize_caravans(self):
        caravans = []
        if self.size == "small":
            num_caravans = random.randint(2, 3)
            caravans = [Caravan(type="mixed") for _ in range(num_caravans)]
        elif self.size == "normal":
            num_caravans = random.randint(4, 6)
            for i in range(num_caravans):
                if i < 3:
                    caravans.append(Caravan(type="mixed"))
                else:
                    # Wanted to add some spice here, so added a random chance for a storage caravan
                    caravans.append(Caravan(type=random.choice(["mixed", "storage"])))
        elif self.size == "large":
            num_caravans = random.randint(7, 10)
            for i in range(num_caravans):
                if i < 6:
                    caravans.append(Caravan(type="mixed"))
                else:
                    # Even more spice here as we can get full people caravans here as well in large convoys
                    caravans.append(Caravan())
        return caravans

    # This function initializes the pawns in the convoy
    def initialize_pawns(self, provided_names):
        total_capacity = sum(caravan.passenger_capacity for caravan in self.caravans)
        min_pawns = sum(min(caravan.passenger_capacity, 3) for caravan in self.caravans)
        max_pawns = total_capacity + 3

        num_pawns = random.randint(min_pawns, max_pawns)
        pawns = []

        # Ensure we have at least one leader
        if provided_names and len(provided_names) > 0:
            name, age, gender = provided_names.pop(0)
            self.leader = Pawn(name=name, age=age, gender=gender, role="Leader")
        else:
            self.leader = Pawn(role="Leader")
        
        pawns.append(self.leader)

        # Create user-provided pawns
        if provided_names:
            for name, age, gender in provided_names:
                if len(pawns) >= num_pawns:
                    break
                pawn = Pawn(name=name, age=age, gender=gender)
                pawns.append(pawn)

        # Create random pawns
        while len(pawns) < num_pawns:
            pawn = Pawn()
            pawns.append(pawn)
        return pawns

    # This function assigns pawns to caravans
    def assign_pawns_to_caravan(self, pawns):
        total_capacity = sum(caravan.passenger_capacity for caravan in self.caravans)
        assigned_pawns = 0
        for caravan in self.caravans:
            while len(caravan.pawns) < caravan.passenger_capacity:
                pawn = pawns[assigned_pawns]
                pawn.assigned_caravan = caravan.id
                caravan.pawns.append(pawn.id)
                assigned_pawns += 1

    # This function saves the convoy data to a JSON file
    def save_to_json(self):
        os.makedirs('saves', exist_ok=True)
        convoy_dict = {
            "id": self.id,
            "state": self.state,
            "size": self.size,
            "total_caravans": len(self.caravans),
            "leader": json.loads(self.leader.to_json()),  # Add leader to the save
            "caravans": [json.loads(caravan.to_json()) for caravan in self.caravans],
            "total_pawns": len(self.pawns),
            "pawns": [json.loads(pawn.to_json()) for pawn in self.pawns]
        }
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        filename = f"saves/convoy - {timestamp}.json"
        with open(filename, 'w') as file:
            json.dump(convoy_dict, file, indent=4)
        print(f"Convoy saved to {filename}")
        return filename

    # This function returns the JSON representation of the convoy
    def to_json(self):
        return {
            "id": self.id,
            "state": self.state,
            "size": self.size,
            "total_caravans": len(self.caravans),
            "leader": json.loads(self.leader.to_json()),  # Add leader to the JSON representation
            "caravans": [json.loads(caravan.to_json()) for caravan in self.caravans],
            "total_pawns": len(self.pawns),
            "pawns": [json.loads(pawn.to_json()) for pawn in self.pawns]
        }