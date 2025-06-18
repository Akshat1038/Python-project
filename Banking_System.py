import hashlib
import json
import os

ACCOUNTS_FILE = "accounts.json"

def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            return json.load(file)
    return{}

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_account():
    accounts = load_accounts()
    username = input("Enter Your Username : ")
    if username in accounts:
        print("Username already exists . Please try another account !")
        return
    
    password = input("Set a password: ")
    
    account_type = input("Enter account type (saving/current): ").lower()
    if account_type not in ["saving", "current"]:
        print("Invalid account type. Choose 'saving' or 'current'.")
        return
    
    accounts[username] = {
        "password" : hash_password(password),
        "type" : account_type,
        "balance" : 0.0,
        "transactions" : []
    }
    save_accounts(accounts)
    print("Account succesfully created !!")

def login():
    accounts = load_accounts()
    username = input("Enter Your Username : ")
    if username not in accounts:
        print("Username not found ! please try agian !")
        return None
    
    password = input("Enter Your Password : ")
    if accounts[username]["password"] != hash_password(password):
        print("Incorrect password.")
        return None
    
    print("Login succesful !")
    return username

def deposit(username):
    accounts = load_accounts()
    amount = float(input("Enter amount to deposit : "))
    accounts[username]["balance"] += amount
    accounts[username]["transactions"].append(f"Deposited : {amount}")
    save_accounts(accounts)
    print(f"Deposited {amount} Successfully.")

def withdrew(username):
    accounts = load_accounts()
    amount = float(input("Enter amount to withdrew : "))
    if accounts[username]["balance"] < amount:
        print("Insufficient balance.")
        return
    
    accounts[username]["balance"] -= amount
    accounts[username]["transactions"].append(f"WIthdrew : {amount}")
    save_accounts(accounts)
    print(f"Withdrew {amount} Successfully.")

def view_transaction(username):
    accounts = load_accounts()
    print("Transaction History : ")
    for transaction in accounts[username]["transactions"]:
        print(transaction)

def check_balance(username):
    accounts = load_accounts()
    print(f"Current Balance : {accounts[username]["balance"]}")

def main_manu(username):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Transactions\n5. Logout")
        choice = input("Enter Your Chioce : ")

        if choice == "1":
            deposit(username)
        elif choice == "2":
            withdrew(username)
        elif choice == "3":
            check_balance(username)
        elif choice == "4":
            view_transaction(username)
        elif choice == "5":
            print("Logged Out.")
            break
        else:
            print("invaild Choice ! Please Try Again !")

def main():
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter Your Choice : ")

        if choice == "1":
            create_account()
        elif choice == "2":
            username = login()
            if username:
                main_manu(username)
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invaild choice. Please Try Again.")

if __name__ == "__main__":
    main()