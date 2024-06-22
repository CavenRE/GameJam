from data import player as player_dict, screens as screens_dict
from screens import Screen, ScreenManager
from player import Player








# 🐍 __MAIN__
if __name__ == "__main__":
    
    # 🏃 player
    player = Player(player_dict)

    # 🖥️ screens
    screen_manager = ScreenManager()
    for screen_key, screen_dict in screens_dict.items():        
        # 🟢 🖥️
        screen = Screen(screen_key, screen_dict, player)  
        screen_manager.add_screen(screen)
    
    # 🟣 🖥️
    screen_manager.run() #




