import json
import random

class Shop:
    def __init__(self, shop_type, items=None, money=1000, buy_sell_flag='sell'):
        self.shop_type = shop_type
        self.money = money
        self.buy_sell_flag = buy_sell_flag
        self.inventory = self.load_inventory(items)

    # This function loads the inventory of the shop, needs major work! 
    def load_inventory(self, items):
        inventory = []
        if items:
            for item in items:
                inventory.append(item)
        else:
            if self.shop_type == 'weapons':
                inventory += self.load_items_from_file('data/generated/weapons.json')
            elif self.shop_type == 'foods':
                inventory += self.load_items_from_file('data/generated/foods.json')
            elif self.shop_type == 'health':
                inventory += self.load_items_from_file('data/generated/health.json')
            elif self.shop_type == 'general':
                inventory += self.load_items_from_file('data/generated/items.json')
                inventory += random.sample(self.load_items_from_file('data/generated/foods.json'), 5)
                inventory += random.sample(self.load_items_from_file('data/generated/health.json'), 5)
                inventory += random.sample(self.load_items_from_file('data/generated/weapons.json'), 3)
        return inventory

    # This function loads the items from a file, so much work to be done here
    def load_items_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return []

    # Show teh inventory of the shop, at least this is simple enough
    def show_inventory(self):
        for index, item in enumerate(self.inventory, start=1):
            print(f"{index}. {item['name']} - {item['price']}")

    # Buy an item from the shop, works?
    def buy_item(self, item_index, player_money):
        if self.buy_sell_flag in ['sell', 'buy_sell']:
            if 0 <= item_index < len(self.inventory):
                item = self.inventory[item_index]
                if player_money >= item['price']:
                    player_money -= item['price']
                    self.money += item['price']
                    self.inventory.pop(item_index)
                    print(f"Bought {item['name']} for {item['price']}.")
                    return item, player_money
                else:
                    print("Not enough money.")
                    return None, player_money
            else:
                print("Invalid item index.")
                return None, player_money
        else:
            print("This shop does not sell items.")
            return None, player_money

    # Sell an item to the shop
    def sell_item(self, item, player_money):
        if self.buy_sell_flag in ['buy', 'buy_sell']:
            if self.money >= item['price']:
                player_money += item['price']
                self.money -= item['price']
                self.inventory.append(item)
                print(f"Sold {item['name']} for {item['price']}.")
                return player_money
            else:
                print("The shop does not have enough money.")
                return player_money
        else:
            print("This shop does not buy items.")
            return player_money