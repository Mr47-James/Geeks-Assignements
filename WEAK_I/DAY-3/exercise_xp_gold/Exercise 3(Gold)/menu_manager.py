import re

class MenuManager:
    dictionaries = {
        "Item1": {"name": "Soup", "Price": 10, "spice": "B", "gluten": False},
        "Item2": {"name": "Hamburger", "Price": 15, "spice": "A", "gluten": True},
        "Item3": {"name": "Salad", "Price": 18, "spice": "A", "gluten": False},
        "Item4": {"name": "French Fries", "Price": 5, "spice": "C", "gluten": False},
        "Item5": {"name": "Beef bourguignon", "Price": 25, "spice": "B", "gluten": True},
    }

    def __init__(self, name=None, price=None, spice=None, gluten=None):
        self.menu = MenuManager.dictionaries
        self.name = name
        self.price = price
        self.spice = spice
        self.gluten = gluten
        
    def add_item(self, name, price, spice, gluten):
        keys_list = list(self.menu.keys())
        Last_item = keys_list[-1]
        num = ""
        for ch in Last_item:
            if ch.isdigit():
                num += ch
        if num:
            string = int(num)
            string += 1
        digit = f"Item{string}"
        self.menu[digit] = {}
        self.menu[digit]["name"] = name  
        self.menu[digit]["Price"] = int(price)
        self.menu[digit]["spice"] = spice  
        self.menu[digit]["gluten"] = gluten 
        print(f"[*] Item {name} added successfully.")

    def update_item(self, name, price=None, spice=None, gluten=None):
        for key, item in self.menu.items():
            if item["name"].lower() == name.lower():
                if price:  item["Price"] = int(price)
                if spice:  item["spice"] = spice
                if gluten is not None: item["gluten"] = gluten
                print(f"[*] {name} updated successfully → {item}")
                return
        print(f"[!] Dish '{name}' not found in the menu.")

    def remove_item(self, name):
        for key, item in list(self.menu.items()):  
            if item["name"].lower() == name.lower():
                self.menu.pop(key)
                print(f"[!] Your Item has been removed: {name}")
                return
        print(f"[!] Dish '{name}' not found in the menu.")


mode = input("[!] Put in your mode (Update=0, Add=1, Remove=2): ")
manager = MenuManager()

match mode:
    case "0":
        name = input("\n[?] Put in the name of your dish: ")
        price = input("\n[?] Put in the new price (or leave empty): ") or None
        spice = input("\n[?] Put in the new spice level (or leave empty): ") or None
        gluten_in = input("\n[?] Gluten? (True/False or leave empty): ") or None
        gluten = gluten_in.lower() == "true" if gluten_in else None
        manager.update_item(name, price, spice, gluten)

    case "1":
        name = input("\n[?] Put in the name of your dish: ")
        price = input("\n[?] Put in the price of your dish: ")
        spice = input("\n[?] Put in the spice level of your dish: ")
        gluten = input("\n[?] Gluten? (True/False): ").lower() == "true"
        manager.add_item(name, price, spice, gluten)

    case "2":
        name = input("\n[?] Put in the name of your dish to remove: ")
        manager.remove_item(name)
