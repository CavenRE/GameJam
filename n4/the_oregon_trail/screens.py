# 🟢 🖥️ Base class for all screens
import os
from kb import KB

kb = KB()
# 🟢 🖥️
class Screen:
    def __init__(self, key, screen_dict, player):
        self.key = key
        self.name = screen_dict["name"]
        self.text = screen_dict["text"]
        self.menu = screen_dict["menu"]                
        self.player = player
    # menu
    def display_menu(self):
        max_menu = 7
        if self.menu:
            for i, option in enumerate(self.menu):
                print(f"    {i + 1}. {option['label']}")
        
            # fill remaining space below the menu            
            space = max_menu - len(self.menu)       
            for i in range(space):
                print()
        else:
            # no menu, fill with blank
            for i in range(max_menu):
                print()
    
    def display_text(self):
        print(self.text)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self, pad_bottom=1):
        # header
        print(f"---=[ {self.name} ]=---")
        for i in range(pad_bottom):
            print()

    # display
    def display_screen(self):
        self.clear_screen()
        
        self.display_header()
        print()
        print()

        # menu
        self.display_menu()
        print()

        # text
        self.display_text()
        
        # stats header
        print("stats:")
        # player stats
        self.player.display()
        
# 🟣🖥️ Screen manager to handle transitions
class ScreenManager:
    def __init__(self):
        self.screens = {}
    
    def add_screen(self, screen:Screen):                
        self.screens[screen.key] = screen

    def transition_to(self, key):
        if key in self.screens:
            self.current_screen = self.screens.get(key)
    # 🔴
    def handle_menu_input(self, options, screens=None): ##TODO TODO TODO
        
        # get key
        key_index = kb.get_key() #1️⃣2️⃣3️⃣🔢
        
        num_options = len(options)
        # process key
        if options:
            try:
                index = int(key_index) - 1
                if 0 <= index < num_options:                    
                    return options[index]
            except ValueError:
                pass
        return None

    def run(self):
        
        # setup first and previous screens
        first_key = "main_menu"#next(iter(self.screens))
        cur_screen = self.screens[first_key]
        prev_screen = None        

        # display the screen and handle user input
        while True:            
            cur_screen.display_screen()            
            
            
            if cur_screen.menu:   # 🔴
                input_result = self.handle_menu_input(cur_screen.menu)

                if isinstance(input_result, dict):
                    # did we get an "action" back?
                    if "action" in input_result:
                        action = input_result["action"] # 🏃 💨
                        response = action() # 📞
                        
                        if response == "back": # 👈️
                            cur_screen = prev_screen
                            continue

                    # did we get a "screen" back?
                    if "screen" in input_result: # 🟣🖥️
                        screen_key = input_result['screen']                
                        prev_screen = cur_screen
                        cur_screen = self.screens[screen_key]
                        continue
            else:                
                input() # wait for enter press
                cur_screen = cur_screen.screen
