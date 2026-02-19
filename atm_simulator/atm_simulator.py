def pin_login():
    for i in range(3):
        pin = input("Enter your 4-digit PIN: ")
        if pin == "1234":
            print("Login successful!\n")
            return True
        else:
            print("Incorrect PIN. Try again.")
    print("Account locked.\n")

def menu():
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = input("Select an option: ")
    return choice

def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}\n")

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("\nInsufficient funds.")
    else:
        balance -= amount
        print(f"\n${amount:.2f} withdrawal successful.")
        print(f"New balance: ${balance:.2f}\n")
    return balance

def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    balance += amount
    print(f"\n${amount:.2f} deposit successful.")
    print(f"New balance: ${balance:.2f}\n")
    return balance

def exit_atm():
    print("\nThank you for using the ATM. Goodbye!\n")

def main():
    print("\n~ Welcome to the ATM Simulator! ~\n")
    balance = 1000.00
    if pin_login():
        while True:
            choice = menu()
            if choice == '1':
                check_balance(balance)
            elif choice == '2':
                balance = withdraw(balance)
            elif choice == '3':
                balance = deposit(balance)
            elif choice == '4':
                exit_atm()
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()