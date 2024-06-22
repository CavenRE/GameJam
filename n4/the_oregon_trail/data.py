import sys


screen_text = {
"main_menu" :
"""
╔══  🏡 Welcome to the Oregon Trail!   ════════════════════╗
║ In 1848, your family journeyS from Missouri to Oregon.   ║
║ Face rugged terrain and dangerous rivers.                ║
║ Endure scarce supplies and tough decisions.              ║
║                                                          ║
║ [1,2,3..] Choose an option                               ║
╚══════════════════════════════════════════════════════════╝
""",

"shop" :
"""
╔══  🛒 Welcome to the Shop            ════════════════════╗ 
║ Here you can stock up on supplies.                       ║
║ Make sure you have enough supplies for your journey      ║
║                                                          ║
║                                                          ║
║ [1,2,3..] Buy supplies                                   ║
╚══════════════════════════════════════════════════════════╝
""",

"story_01":
"""
╔══  🌄 (1) The Journey Begins     🌲⛰️ 🌲⛰️═════════════════╗ 
║ Stocked up on supplies, said goodbye to loved ones,     ║
║ and now it's time to start your journey.                ║
║ Get ready for the long and treacherous road ahead!      ║
║                                                         ║
║ [ ] The Oregon Trail Ahead...                           ║
╚═════════════════════════════════════════════════════════╝
""",

"story_02":
"""
╔══  ⛺️ (2) Halfway There 🦅🕊️   🪵🌳🌲  ═══════════════════╗ 
║ xxx                                                     ║
║ xxx                                                     ║
║ xxx                                                     ║
║                                                         ║
║ [ ] The Oregon Trail Ahead...                           ║
╚═════════════════════════════════════════════════════════╝
""",

"story_03":
"""
╔══  🌄 Your Arrival               🎊🎉🥳  ═══════════════╗ 
║ xxx                                                     ║
║ xxx                                                     ║
║ xxx                                                     ║
║                                                         ║
║ [ ] The Oregon Trail Ahead...                           ║
╚═════════════════════════════════════════════════════════╝
""",

}


shop_prices = {
    "oxen":     { "price":20, "stock":5},
    "food":     { "price":10, "stock":5},
    "water":    { "price":5 , "stock":5},
    "clothes":  { "price":5 , "stock":5},
    "ammo":     { "price":5 , "stock":5},
    "spares":   { "price":0 , "stock":5}
}

# __🏃 💨__
def buy(item, player):
    def buy_action():
        
        stock = shop_prices[item]["stock"]
        price = shop_prices[item]["price"]
        inv_item = player["inventory"][item]
        money = player["stats"]["money"]

        # check stock
        if stock == 0: return

        if(money["val"] - price > 0):
            money["val"] -= price
            inv_item["val"] += 1                
            shop_prices[item]["stock"] -= 1
    return buy_action

# __🏃 💨__
def back():
    def back_action():                        
        return "back"            
    return back_action

# __🏃 💨__
def noop():
    def continue_action():
        return "noop"
    return noop()

# __🏃 💨__
def exit(msg):
    def k():            
        print(f"\n{msg}\n")
        sys.exit(0)
    return k

def end_game():
    def f():
        sys.exit(0)    
    return f

# __🏃__
player = {   
    "stats": {
        "money" : { "lbl": "🪙 money ", "val": 500 },
        "hp"    : { "lbl": "🩸 hp    ", "val": 100 },
        "morale": { "lbl": "😐️ morale", "val": 50  },
        "wagon" : { "lbl": "🟫 wagon",  "val": 3   }
    },
    "inventory": {            
        "oxen"   : { "lbl": "🐂  oxen",    "val": 1  },
        "food"   : { "lbl": "🍲  food",    "val": 10 },
        "water"  : { "lbl": "🫙   water",  "val": 10 },
        "clothes": { "lbl": "👗  clothes", "val": 10 },
        "ammo"   : { "lbl": "🔫  ammo",    "val": 10 },
        "spares" : { "lbl": "🧰  spares",  "val": 10 }
    }
}

# 📊 Data
menu_options = {
    # 📜
    "main_menu": [
        { "label": "🎮️ start", "screen": "story_01"        },
        { "label": "💰️ shop" , "screen": "shop"            },
        { "label": "🚪 exit" , "action": exit("Good Bye.") }
    ],
    # 💰️
    "shop": [
        { "label": "🐂 oxen"    , "action":  buy("oxen", player)    },
        { "label": "🍲 food"    , "action":  buy("food", player)    },
        { "label": "🫙  water"  , "action":  buy("water", player)   },
        { "label": "👗 clothes" , "action":  buy("clothes", player) },
        { "label": "🔫 ammo"    , "action":  buy("ammo", player)    },
        { "label": "🛠️  spares" , "action":  buy("spares", player)  },
        { "label": "👈️ back"    , "action":  back()                 }
    ],
    "story_01": [
        { "label": "🐂 continue...", "screen": "story_02" }
    ],
    "story_02": [
        { "label": "🐂 continue...", "screen": "story_03" }
    ],
    "story_03": [
        { "label": "🐂 continue...", "event": end_game()  }
    ],
}


# 🟣🖥️
screens = {        
    "main_menu":  {
        "name": "🐂 The Oregon Trail",
        "text": screen_text["main_menu"],
        "menu": menu_options["main_menu"],
        "event": None
    },
    "shop": {
        "name": "💰️ Shop",
        "text": screen_text["shop"],
        "menu": menu_options["shop"],
        "event": None
    },
    "story_01": {
        "name": "📖 story_01",
        "text": screen_text["story_01"],
        "menu": menu_options["story_01"],
        "event": None
    },
    "story_02": {
        "name": "📖 story_02",
        "text": screen_text["story_02"],
        "menu": menu_options["story_02"],
        "event": None
    }, 
    "story_03": {
        "name": "📖 story_03",
        "text": screen_text["story_03"],
        "menu": menu_options["story_03"],
        "event": None
    },    
}