def menu():
    print("\n~ Python Bank Menu ~\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def account_setup():
    print("\n~ Welcome to Python Bank ~\n")
    account = {"name": "", "balance": 0.0}
    account["name"] = input("Please enter your name: ").title()
    account["balance"] = float(input("Please enter your initial deposit: $"))
    return account

def balance(account):
    print(f"\nYour current balance is: ${account['balance']:.2f}")

def deposit(account):
    amount = float(input("\nEnter the amount to deposit: $"))
    account['balance'] += amount
    print(f"Deposit successful! Your new balance is: ${account['balance']:.2f}")

def withdraw(account):
    amount = float(input("\nEnter the amount to withdraw: $"))
    if amount > account['balance']:
        print("Insufficient funds! Please try again.")
    else:
        account['balance'] -= amount
        print(f"Withdrawal successful! Your new balance is: ${account['balance']:.2f}")

def quit():
    print("\nThank you for banking with Python Bank! Have a great day!\n")

def main():
    account = account_setup()
    while True:
        menu()
        choice = input("Please select an option (1-4): ")
        if choice == "1":
            balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            quit()
            break
        else:
            print("Invalid option! Please try again.")
        
if __name__ == "__main__":
    main()