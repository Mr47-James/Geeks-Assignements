import random


class Game:
    def get_user_item(self):
        """Ask the user to select rock/paper/scissors, validate input."""
        while True:
            choice = input("Select (rock/paper/scissors): ").strip().lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        """Randomly select rock/paper/scissors for the computer."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Compare user and computer items, return win/draw/loss."""
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        """Play one round of Rock-Paper-Scissors."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # Print outcome
        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")

        return result
