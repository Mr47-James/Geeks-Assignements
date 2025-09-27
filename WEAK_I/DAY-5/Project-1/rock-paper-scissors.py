from game import Game


def get_user_menu_choice():
    """Display the menu and get user choice with validation (no loop here)."""
    print("\n--- Main Menu ---")
    print("(g) Play a new game")
    print("(s) Show scores")
    print("(q) Quit")
    choice = input("Enter your choice: ").strip().lower()
    if choice in ["g", "s", "q"]:
        return choice
    else:
        print("Invalid choice. Please enter g, s, or q.")
        return None


def print_results(results):
    """Display results of all games played."""
    print("\n--- Game Results ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice is None:
            continue  # Ask again

        if choice == "g":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "s":
            print_results(results)

        elif choice == "q":
            print_results(results)
            break


if __name__ == "__main__":
    main()
