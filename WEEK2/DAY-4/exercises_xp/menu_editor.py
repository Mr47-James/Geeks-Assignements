# ============================================
# PART 2 : menu_editor.py
# ============================================

from menu_item import MenuItem
from menu_manager import MenuManager

def add_item_to_menu():
    name = input("Enter the name of the item: ").strip()
    price = input("Enter the price of the item: ").strip()
    try:
        price = int(price)
        item = MenuItem(name, price)
        item.save()
        print(f"{name} was added successfully.")
    except Exception as e:
        print("Error adding item:", e)

--s--

def remove_item_from_menu():
    name = input("Enter the name of the item to delete: ").strip()
    item = MenuItem(name, 0)
    try:
        if MenuManager.get_by_name(name):
            item.delete()
            print(f"{name} was deleted successfully.")
        else:
            print("Error: Item not found.")
    except Exception as e:
        print("Error deleting item:", e)

--s--

def update_item_from_menu():
    old_name = input("Enter the name of the item to update: ").strip()
    new_name = input("Enter the new name: ").strip()
    new_price = input("Enter the new price: ").strip()
    try:
        new_price = int(new_price)
        if MenuManager.get_by_name(old_name):
            item = MenuItem(old_name, 0)
            item.update(new_name, new_price)
            print(f"{old_name} was updated successfully.")
        else:
            print("Error: Item not found.")
    except Exception as e:
        print("Error updating item:", e)

--s--

def show_restaurant_menu():
    print("\n---- RESTAURANT MENU ----")
    items = MenuManager.all_items()
    if not items:
        print("The menu is currently empty.")
    else:
        for item in items:
            print(f"{item['item_name']} - ${item['item_price']}")
    print("--------------------------\n")

--s--

def show_user_menu():
    while True:
        print("""
========= MENU EDITOR =========
(V) View an Item
(A) Add an Item
(D) Delete an Item
(U) Update an Item
(S) Show the Menu
(Q) Quit
===============================
        """)
        choice = input("Select an option: ").strip().upper()

        if choice == 'V':
            name = input("Enter item name to view: ").strip()
            item = MenuManager.get_by_name(name)
            if item:
                print(f"Item found: {item['item_name']} - ${item['item_price']}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'Q':
            print("\nExiting program...")
            show_restaurant_menu()
            break
        else:
            print("Invalid option. Please try again.")

--s--

if __name__ == "__main__":
    show_user_menu()
