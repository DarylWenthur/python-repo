import random
import time

balance = 1000.00
wins = 0
losses = 0

def menu():
    global balance

    print("\n=== CASINO MENU ===")
    print(f"Balance: ${balance:.2f}\n")
    print("1. Play Slot Machine")
    print("2. Play Roulette")
    print("3. Play Blackjack")
    print("4. Exit")
    choice = input("Select an option: ")
    return choice

def play_slot_machine():
    global balance
    global wins
    global losses
    result = ""

    while True:
        print("Enter your bet for Slot Machine")
        bet = float(input("Enter a negative bet amount to quit: $"))
        if bet < 0:
            print("\nExiting Slot Machine...\n")
            break
        elif bet == 0:
            print("\nInvalid bet amount.\n")
        elif bet > balance:
            print("\nInsufficient funds for this bet.\n")
        else:
            print("Spinning...")
            time.sleep(2)
            result = ""
            for i in range(3):
                result += random.choice(['🍒', '🍋', '🔔', '7️⃣']) + " "
            print(f"Result: {result}\n")
            if result.count('7️⃣') == 3:
                winnings = bet * 100
                print(f"Jackpot! You win ${winnings:.2f}!\n")
                balance += winnings
                wins += 1
            elif result.count('🔔') == 3:
                winnings = bet * 50
                print(f"Great! You win ${winnings:.2f}!\n")
                balance += winnings
                wins += 1
            elif result.count('🍋') == 3:
                winnings = bet * 20
                print(f"Good! You win ${winnings:.2f}!\n")
                balance += winnings
                wins += 1
            elif result.count('🍒') == 3:
                winnings = bet * 10
                print(f"Nice! You win ${winnings:.2f}!\n")
                balance += winnings
                wins += 1
            else:
                print("No win. Better luck next time!\n")
                balance -= bet
                losses += 1
                if balance <= 0:
                    print("You are out of money.\n")
                    print("Game Over.\n")
                    exit()
                time.sleep(1)
        print(f"Current balance: ${balance:.2f}\n")

def play_roulette():
    global balance
    global wins
    global losses

    while True:
        print("Enter your bet for Roulette")
        bet = float(input("Enter a negative bet amount to quit: $"))
        if bet < 0:
            print("\nExiting Roulette...\n")
            break
        elif bet == 0:
            print("\nInvalid bet amount.\n")
        elif bet > balance:
            print("\nInsufficient funds for this bet.\n")
        else:
            number = int(input("Bet on a number (0-36): "))
            print("Spinning the wheel...")
            time.sleep(2)
            outcome = random.randint(0, 36)
            print(f"The ball landed on: {outcome}\n")
            if number == outcome:
                winnings = bet * 35
                print(f"Congratulations! You win ${winnings:.2f}!\n")
                balance += winnings
                wins += 1
            else:
                print("No win. Better luck next time!\n")
                balance -= bet
                losses += 1
                if balance <= 0:
                    print("You are out of money.\n")
                    print("Game Over.\n")
                    exit()
                time.sleep(1)
        print(f"Current balance: ${balance:.2f}\n")

def play_blackjack():
    global balance
    global wins
    global losses

    while True:
        print("Enter your bet for Blackjack")
        bet = float(input("Enter a negative bet amount to quit: $"))
        if bet < 0:
            print("\nExiting Blackjack...\n")
            break
        elif bet == 0:
            print("\nInvalid bet amount.\n")
        elif bet > balance:
            print("\nInsufficient funds for this bet.\n")
        else:
            player_score = random.randint(15, 21)
            dealer_score = random.randint(15, 21)
            print(f"Your score: {player_score}")
            print(f"Dealer's score: {dealer_score}\n")
            if player_score > dealer_score:
                winnings = bet * 2
                print(f"You win ${winnings:.2f}!\n")
                balance += winnings
                wins += 1
            elif player_score < dealer_score:
                print("You lose. Better luck next time!\n")
                balance -= bet
                losses += 1
                if balance <= 0:
                    print("You are out of money.\n")
                    print("Game Over.\n")
                    exit()
            else:
                print("It's a tie! Your bet is returned.\n")
        time.sleep(1)
        print(f"Current balance: ${balance:.2f}\n")

def main():
    print("\n~ Welcome to the Casino Simulator! ~")
    
    while True:
        if balance <= 0:
            print("\nYou are out of money.\n")
            break
        choice = menu()
        if choice == '1':
            print("\nPlaying Slot Machine...\n")
            play_slot_machine()
        elif choice == '2':
            print("\nPlaying Roulette...\n")
            play_roulette()
        elif choice == '3':
            print("\nPlaying Blackjack...\n")
            play_blackjack()
        elif choice == '4':
            print(f"\nFinal balance: ${balance:.2f}")
            print(f"Total wins: {wins}")
            print(f"Total losses: {losses}")
            print("\nThank you for visiting the casino. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

if __name__ == "__main__":
    main()