

class Player:
    def __init__(self, player_dict):
        self.player_dict = player_dict

    def display(self):
        for section_key in self.player_dict:
            # Utility function to print a player section        
            maxwidth = len("inventory")      
            tmp_str = f"{section_key:<{maxwidth}}: "
            tmp_str = "" # disabled labels for now

            # build the section display
            section = self.player_dict[section_key]
            for key, item in section.items():
                icon = item['lbl'][0]
                val = item['val']

                if item['lbl'] in ["water", "spares"]:
                    icon += " " # weird emoji bug

                tmp_str += f"{icon} {val}".ljust(7)
            
            # display
            print(tmp_str)
