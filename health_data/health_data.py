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
    print("\nWelcome to the Health Data Calculator!\n")
    user_age_years = int(input("Enter your age in years: "))
    minutes, seconds = age_in_min_sec(user_age_years)
    print(f"Your age in minutes: {minutes}")
    print(f"Your age in seconds: {seconds}")
    print(f"Your heart has beaten approximately {heart_beats(user_age_years)} times.")
    print(f"You have sneezed approximately {lifetime_sneezes(user_age_years)} times in your lifetime.")
    print(f"You have consumed approximately {lifetime_calories(user_age_years)} calories in your lifetime.")
    print(f"You have burned approximately {burger_burned(user_age_years)} burgers in your lifetime.")

main()