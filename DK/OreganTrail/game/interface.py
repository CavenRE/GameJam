import os

class Interface:
    def __init__(self):
        self.width = 80

    # This function clears the screen so I dont have to do all the ho ha you see below each and every single time
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # So text has a nice centering function, give it a width and it will center it accordingly, kinda neat
    def center_text(self, text):
        return text.center(self.width)

    # My fancy header output
    def print_header(self, title, sub=None):
        print()
        print(self.center_text(f"╌╌╍ {title} ╍╌╌"))
        if sub:
            print(self.center_text(sub))
        print()

    # Line break wiht the border
    def print_line_break(self):
        print("╾" + ("╶" * (self.width - 2)) + "╼")

    # Can't remember why I have this... I know it centers my messages, not sure why I separeted it from the print_message function again
    def print_message(self, message):
        print(self.center_text(message))
        print()

    # Prints the options that user can select, may need to add in pagination here for longer lists (Which I had, no idea where that code went)
    def print_options(self, options):
        print()
        for i, option in enumerate(options, start=1):
            print(f"        × {i}: {option}")
        print()

    # Overview of the convoy, this is a bit of a mess, need to clean it up as it kinda doesn't work right now and yeah, might make it more dynamic
    def print_overview(self, convoy):
        self.print_header("Overview")
        print(f"    Caravans: {len(convoy.caravans)}")
        print(f"    Leader: {convoy.leader.name}")
        print(f"    Pawns: {len(convoy.pawns)}")
        print(f"    Total Storage: {convoy.total_storage}")
        print(f"    Used Storage: {convoy.used_storage}")
        print(f"    Food: {convoy.food}")
        print(f"    Water: {convoy.water}")
        print(f"    Money: {convoy.money}")
        print(f"    Hydration: {convoy.hydration}")

    # Basic user input, I might add in a var to allow for text before the selection? Maybe
    def get_user_input(self):
        return input("\n> ")

    # Print message function, want to maybe turn this into a typewriter of sorts? Could be cool?
    def show_messages(self, messages):
        for message in messages:
            self.print_message(message)
            self.print_line_break()

    # Print the journey status, want to come back and work on this
    def print_journey_status(self, day, time, traveled):
        left = f"Day: {day} Time: {time}"
        right = f"Total Traveled: {traveled}km"
        print(f"{left}{' ' * (self.width - len(left) - len(right))}{right}")
        self.print_line_break()

    # Display function, this is the main function that will be called to display the interface, basically a wrapper for all the other functions so we only need to call one function instead of several
    def display(self, title=None, messages=None, options=None, day=None, time=None, traveled=None):
        self.clear_screen()
        if day is not None and time is not None and traveled is not None:
            self.print_journey_status(day, time, traveled)
        
        if title:
            self.print_header(title)
            self.print_line_break()
        
        if messages:
            self.show_messages(messages)
        
        if options:
            self.print_options(options)
            self.print_line_break()