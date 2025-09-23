sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    finished_sandwiches.append(current_order)
    print(f"I made your {current_order}")
