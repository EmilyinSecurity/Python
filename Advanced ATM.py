# ATM SIMULATOR

import time

# Define User Data
userID = [
    {"account": "12345600", "full_name": "Alice Johnson", "pin": "1234", "acc_balance": 1500.00},
    {"account": "78910000", "full_name": "Emily Mankge", "pin": "7891", "acc_balance": 3500.00},
    {"account": "24681000", "full_name": "Roronoa Zoro", "pin": "2468", "acc_balance": 10000.00},
    {"account": "13579100", "full_name": "Nico Robin", "pin": "1357", "acc_balance": 800.00}
]

# Extract all account numbers for lookup
account_numbers = [user["account"] for user in userID]

Zar = "R"
trials = 3


def delay():
    print("==== ==== ==== " * 2)
    time.sleep(2)


def greetings():
    print("Welcome to Optimum Bank, How can we help you today?")
    delay()


def get_user():
    global trials
    
    get_account_number = input("Enter your account Number: \n").strip()
    delay()

    if get_account_number in account_numbers:
        user_id = account_numbers.index(get_account_number)
        confirm_pin(user_id)
    else:
        print("Account Not found. Try again...")
        delay()
        get_user()


def confirm_pin(user_id):
    global trials
    
    while trials > 0:
        get_pin = input("Enter your 4-digit pin: \n").strip()
        delay()
        
        user = userID[user_id]  # Retrieve user details

        if get_pin == user["pin"]:
            print(f"Welcome {user['full_name']}!")
            delay()
            transaction_menu(user_id)
            return
        else:
            trials -= 1
            if trials == 0:
                print("You've exceeded maximum attempts. Exiting...")
                quit()
            else:
                print(f"Incorrect pin. {trials} attempts left. Try again.")
                continue


def transaction_menu(user_id):
    while True:
        print("What would you like to do today? \n",
              "1. Deposit \n",
              "2. Withdrawal \n",
              "3. Check Balance \n",
              "4. Change Pin\n",
              "5. Exit \n")

        transaction = input(">> ").strip().lower()

        if transaction in ["1", "deposit"]:
            deposit(user_id)
        elif transaction in ["2", "withdrawal"]:
            withdrawal(user_id)
        elif transaction in ["3", "check balance"]:
            check_balance(user_id)
        elif transaction in ["4", "change pin"]:
            change_pin(user_id)
        elif transaction in ["5", "exit"]:
            confirm_exit()
        else:
            print("Invalid option. Try again.")


def deposit(user_id):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            userID[user_id]["acc_balance"] += amount
            print(f"Deposit successful! New balance: {Zar}{userID[user_id]['acc_balance']:.2f}")
        else:
            print("Invalid amount. Deposit must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def withdrawal(user_id):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= userID[user_id]["acc_balance"]:
            userID[user_id]["acc_balance"] -= amount
            print(f"Withdrawal successful! New balance: {Zar}{userID[user_id]['acc_balance']:.2f}")
        else:
            print("Insufficient funds or invalid amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def check_balance(user_id):
    print(f"Your current balance is {Zar}{userID[user_id]['acc_balance']:.2f}")


def change_pin(user_id):
    new_pin = input("Enter a new 4-digit PIN: ").strip()
    if len(new_pin) == 4 and new_pin.isdigit():
        userID[user_id]["pin"] = new_pin
        print("PIN successfully changed!")
    else:
        print("Invalid PIN format. Must be exactly 4 digits.")


def confirm_exit():
    confirm_response = input("Do you want to perform another transaction? (yes/no) \n>> ").strip().lower()

    if confirm_response in ["yes", "y"]:
        get_user()
    else:
        print("Thank you for banking with us...")
        quit()


def main():
    greetings()
    get_user()


main()
