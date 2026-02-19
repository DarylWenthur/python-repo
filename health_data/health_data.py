def menu():
    print("\n| Health Calculator Menu |")
    print("1. Calculate age in minutes and seconds")
    print("2. Calculate total heartbeats")
    print("3. Calculate total sneezes")
    print("4. Calculate total calories consumed")
    print("5. Calculate burgers burned")
    print("6. Display all calculations")
    print("7. Exit")

def age_in_min_sec(age_years)-> tuple[int, int]:
    minutes_in_year = 525600  # 60 * 24 * 365
    seconds_in_year = 31536000  # 60 * 60 * 24 * 365
    age_minutes = age_years * minutes_in_year
    age_seconds = age_years * seconds_in_year
    return age_minutes, age_seconds

def heart_beats(age_years: int, beats_per_minute: int = 72) -> int:
    minutes_in_year = 525600
    total_minutes = age_years * minutes_in_year
    return total_minutes * beats_per_minute

def lifetime_sneezes(age_years: int, sneezes_per_day: int = 4) -> int:
    days_in_year = 365
    total_days = age_years * days_in_year
    return total_days * sneezes_per_day

def lifetime_calories(age_years: int, calories_per_day: int = 2000) -> int:
    days_in_year = 365
    total_days = age_years * days_in_year
    return total_days * calories_per_day

def burger_burned(age_years) -> int:
    calories_per_burger = 354
    total_calories = lifetime_calories(age_years)
    return total_calories // calories_per_burger

def main():
    print("\n~ Welcome to the Health Data Calculator! ~\n")
    age_years = int(input("Enter your age in years: "))
    while True:
        menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':  
            minutes, seconds = age_in_min_sec(age_years)
            print(f"\nYou have lived for approximately {minutes} minutes or {seconds} seconds.")
        elif choice == '2':
            beats = heart_beats(age_years)
            print(f"\nYou have had approximately {beats} heartbeats in your lifetime.")
        elif choice == '3':
            sneezes = lifetime_sneezes(age_years)
            print(f"\nYou have sneezed approximately {sneezes} times in your lifetime.")
        elif choice == '4':
            calories = lifetime_calories(age_years)
            print(f"\nYou have consumed approximately {calories} calories in your lifetime.")
        elif choice == '5':
            burgers = burger_burned(age_years)
            print(f"\nYou have burned approximately {burgers} burgers in your lifetime.")
        elif choice == '6':
            minutes, seconds = age_in_min_sec(age_years)
            beats = heart_beats(age_years)
            sneezes = lifetime_sneezes(age_years)
            calories = lifetime_calories(age_years)
            burgers = burger_burned(age_years)
            print(f"\nYou have lived for approximately {minutes} minutes or {seconds} seconds.")
            print(f"You have had approximately {beats} heartbeats in your lifetime.")
            print(f"You have sneezed approximately {sneezes} times in your lifetime.")
            print(f"You have consumed approximately {calories} calories in your lifetime.")
            print(f"You have burned approximately {burgers} burgers in your lifetime.")
        elif choice == '7':
            print("\nExiting the Health Calculator. Stay healthy!\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()