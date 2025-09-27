class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            print(f"{self.username} authenticated successfully.")
        else:
            raise Exception("Authentication failed.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must authenticate before depositing.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must authenticate before withdrawing.")
        if amount <= 0:
            raise Exception("Withdraw amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must authenticate before withdrawing.")
        if amount <= 0:
            raise Exception("Withdraw amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: would go below minimum balance.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


class ATM:
    def __init__(self, account_list, try_limit=2):
     
        if not isinstance(account_list, list) or not all(
            isinstance(acc, BankAccount) for acc in account_list
        ):
            raise Exception("account_list must be a list of BankAccount instances.")

        
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit. Setting try_limit to 2 by default.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\nATM Main Menu")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                if account.authenticated:
                    print(f"Welcome {account.username}!")
                    self.show_account_menu(account)
                    return
            except Exception:
                continue

        self.current_tries += 1
        print("Invalid credentials. Try again.")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down ATM.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\nAccount Menu for {account.username}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit to Main Menu")

            choice = input("Select an option: ").strip()

            if choice == "1":
                try:
                    amount = int(input("Enter deposit amount: "))
                    account.deposit(amount)
                except Exception as e:
                    print("Error:", e)

            elif choice == "2":
                try:
                    amount = int(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except Exception as e:
                    print("Error:", e)

            elif choice == "3":
                print(f"Current balance: {account.balance}")

            elif choice == "4":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    acc1 = BankAccount("john", "1234", balance=500)
    acc2 = MinimumBalanceAccount("jane", "abcd", balance=1000, minimum_balance=200)

    atm = ATM([acc1, acc2], try_limit=3)
