import os
import json
import random
import datetime

class Caravan:
    ANIMAL_SPEEDS = { # Speeds of different animals that can be used in the caravan
        "Horse": 2.5,
        "Mule": 2,
        "Ox": 1,
        "Donkey": 1.5
    }

    def __init__(self, type="random", animals="random", num_animals="random", storage_capacity="random", passenger_capacity="random", wheels="random", axles="random", shocks="random", cover="random", status="random", speed="random", health="random"):
        # Unique ID based on the current timestamp and some random number, wanted to get a little fancy here - Stolen from pawns
        self.id = int(datetime.datetime.now().timestamp() * 1000) + random.randint(0, 999)
        self.type = type if type != "random" else random.choice(["people", "storage", "mixed"])
        self.num_animals = num_animals if num_animals != "random" else random.randint(1, 2)

        if animals == "random":
            self.animals = self.random_animals()
        else:
            self.animals = animals

        self.storage_capacity = storage_capacity if storage_capacity != "random" else self.default_storage_capacity()
        self.passenger_capacity = passenger_capacity if passenger_capacity != "random" else self.default_passenger_capacity()

        self.wheels = wheels if wheels != "random" else self.default_wheels()
        self.axles = axles if axles != "random" else self.default_axles()
        self.shocks = shocks if shocks != "random" else self.default_shocks()
        self.cover = cover if cover != "random" else self.default_cover()

        self.status = status if status != "random" else "Good"
        self.speed = speed if speed != "random" else self.calculate_speed()
        self.health = health if health != "random" else 100

        self.pawns = []

    # This function generates a random list of animals
    def random_animals(self):
        animal_type = random.choice(list(self.ANIMAL_SPEEDS.keys()))
        return [animal_type] * self.num_animals

    # These functions provide default values for the attributes of storage, assume 1 person is worth 50 units of storage
    def default_storage_capacity(self):
        if self.type == "storage":
            return random.randint(4, 10) * 50  # Assuming 1 person's worth of storage is 50 units
        elif self.type == "mixed":
            return random.randint(2, 4) * 50
        else:
            return 0

    # These functions provide default values for the attributes of passenger capacity
    def default_passenger_capacity(self):
        if self.type == "people":
            return random.randint(4, 10)
        elif self.type == "mixed":
            return random.randint(3, 4)
        else:
            return 1

    # These functions provide default values for the attributes of wheels and their status
    def default_wheels(self):
        return {"Front Left": "Good", "Front Right": "Good", "Rear Left": "Good", "Rear Right": "Good"}

    # These functions provide default values for the attributes of axles and their status
    def default_axles(self):
        return {"Front": "Good", "Rear": "Good"}

    # These functions provide default values for the attributes of shocks and their status
    def default_shocks(self):
        return {"Front Left": "Good", "Front Right": "Good", "Rear Left": "Good", "Rear Right": "Good"}

    # These functions provide default values for the attributes of cover
    def default_cover(self):
        return "Intact"

    # This function calculates the speed of the caravan based on the number of animals and the condition of the wheels
    def calculate_speed(self):
        base_speed = 10
        animal_speed_sum = sum(self.ANIMAL_SPEEDS[animal] for animal in self.animals)
        average_animal_speed = animal_speed_sum / self.num_animals
        speed = base_speed + average_animal_speed - (4 - len(self.wheels)) * 2
        return max(0, speed)

    # This function returns the JSON representation of the caravan
    def to_json(self):
        return json.dumps(self.__dict__, indent=4)