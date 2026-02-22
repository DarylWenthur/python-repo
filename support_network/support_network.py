import csv
import random

# Global variable to store student profiles in memory
students = {}

def read_from_file() -> dict: # Reads student profiles from a CSV file and returns a dictionary of profiles
    students_dict = {}

    try:
        with open("support_network/students.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row

            # Read each row and create a profile dictionary for each student, using the name as the key
            for row in reader: 
                if len(row) >= 7:
                    name = row[0]
                    students_dict[name] = {
                        "Name": name,
                        "Age": int(row[1]),
                        "Condition": row[2],
                        "College Year": row[3],
                        "Major": row[4],
                        "Stress Level": int(row[5]) if row[5] else None,
                        "Average Sleep Hours": float(row[6]) if row[6] else None
                    }
    except FileNotFoundError:
        print("students.csv not found.")
    except IOError:
        print("Error reading file.")

    return students_dict

# Load all students into the global dictionary when the program starts
students = read_from_file()

def save_profile_to_file(profile): # Appends a new student profile to the CSV file
    try:
        with open("support_network/students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                profile["Name"],
                profile["Age"],
                profile["Condition"],
                profile["College Year"],
                profile["Major"],
                profile.get("Stress Level", ""),
                profile.get("Average Sleep Hours", "")
            ])
    except IOError:
        print("Error: An error occurred while writing to the file.")

def rewrite_file(): # Writes the entire students dictionary back to the CSV file, used for updates and deletions
    try:
        with open("support_network/students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(["Name", 
                             "Age", 
                             "Condition", 
                             "College Year", 
                             "Major", 
                             "Stress Level", 
                             "Average Sleep Hours"])
            
            # Write each student's profile as a row in the CSV file
            for student in students.values():
                writer.writerow([
                    student["Name"],
                    student["Age"],
                    student["Condition"],
                    student["College Year"],
                    student["Major"],
                    student.get("Stress Level", ""),
                    student.get("Average Sleep Hours", "")
                ])
    except IOError:
        print("Error: An error occurred while writing to the file.")

def display_welcome_message(): # Displays a welcome message to the user when they start the program
    print("\n~ Welcome to the Neurodivergent Education Resource Database! - N.E.R.D. ~\n")
    print("****************************************************************************")
    print("| This is a safe space for neurodivergent individuals to connect,          |")
    print("| share experiences, and find support. Whether you're looking for advice,  |")
    print("| resources, or just someone to talk to, we're here for you. Feel free to  |")
    print("| explore the different sections of our network, join discussions, and     |")
    print("| reach out to others who understand your journey. Remember,               |")
    print("| you're not alone, and we're stronger together!                           |")
    print("****************************************************************************")

def main_menu(profile): # Displays the main menu and handles user input to navigate through different sections
   
    while True:
        print("\n~ Main Menu ~")
        print("1. Join a Discussion")
        print("2. Access Resources")
        print("3. Connect with a Mentor")
        print("4. Profile Settings")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            join_discussion()
        elif choice == '2':
            access_resources(profile)
        elif choice == '3':
            connect_with_mentor(profile)
        elif choice == '4':
            profile_settings(profile)
        elif choice == '5':
            print("\nThank you for visiting N.E.R.D. Take care!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

def create_profile()-> dict: # Creates a new student profile by asking the user for their information
    global students

    print("\nFirst, let's create your profile!")
    first_name = input("Enter your first name: ").title()
    last_name = input("Enter your last name: ").title()

    # Check if the profile already exists based on the full name (first + last)
    full_name = f"{first_name} {last_name}"
    if full_name in students: # If the profile already exists, load it and welcome the user back
        print(f"\nWelcome back, {full_name}! Your profile has been loaded.")
        return students[full_name]
    
    # If the profile does not exist, create a new one by asking the user for their information
    age = int(input("Enter your age: "))
    condition = input("Enter your neurodivergent condition (e.g., Autism, ADHD, Dyslexia): ").strip().capitalize()
    college_year = input("Enter your college year (e.g., Freshman, Sophomore): ").capitalize()
    major = input("Enter your major: ").strip().capitalize()
    stress_level = int(input("On a scale of 1-10, how stressed do you feel about college? "))
    average_sleep_hours = float(input("On average, how many hours of sleep do you get per night? "))
    profile = {
        "Name": full_name,
        "Age": age,
        "Condition": condition,
        "College Year": college_year,
        "Major": major,
        "Stress Level": stress_level,
        "Average Sleep Hours": average_sleep_hours
    }
    print(f"\nProfile created successfully for {first_name}! Here's your information:")

    # Display the profile information back to the user in a clear format
    for key, value in profile.items():
        print(f"{key}: {value}")
    # Add the new profile to the global students dictionary and save it to the file
    students[full_name] = profile

    save_profile_to_file(profile)

    return profile

def join_discussion(): # Simulates a discussion forum
    print("\n~ Welcome to the Discussion ~")
    responses = (
    "I understand how you feel. You're not alone.",
    "That sounds really challenging. Thanks for sharing.",
    "I've had a similar experience before.",
    "It might help to talk with a mentor or support group.",
    "Remember to take breaks and take care of yourself.",
    "You're doing your best, and that matters."
    )
    while True:
        user_input = input("\nEnter your thoughts or feelings (or type 'exit' to return to the main menu): ")
        if user_input[0].lower() == 'e':
            break
        else:
            print(random.choice(responses))

def access_resources(profile): # Displays resource categories and allows the user to explore different types of resources
    while True:
        print("   \n~ Resource Categories ~")
        print("   1. Academic Support")
        print("   2. Mental Health Resources")
        print("   3. Social Connection Opportunities")
        print("   4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nAcademic support")
            academic_support(profile)
        elif choice == '2':
            print("\nMental health resources")
            mental_health_resources()
        elif choice == '3':
            print("\nSocial connection opportunities")
            social_connection()
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
    print()

def academic_support(profile): # Provides resources for academic support, including time management tools, study techniques, and accommodations eligibility
    time_management_tools = [
        "Trello: A visual project management tool to organize tasks and deadlines", 
        "Forest: A focus timer app that helps you stay on track by planting virtual trees", 
        "Google Calendar: A versatile calendar app to schedule study sessions and reminders"]
    study_techniques = [
        "Pomodoro Technique: Study for 25 minutes, then take a 5-minute break", 
        "Active Recall: Test yourself on the material instead of just rereading", 
        "Mind Mapping: Create visual diagrams to connect concepts and ideas"]
    
    while True:
        print("\t~ Academic Support Resources ~")
        print("\t1. Time Management Tools")
        print("\t2. Study Techniques")
        print("\t3. Accommodations Eligibility")
        print("\t4. Return to Resource Categories")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nTime management tools:")
            for tool in time_management_tools:
                print(f"- {tool}")
            print()
        elif choice == '2':
            print("\nStudy techniques:")
            for technique in study_techniques:
                print(f"- {technique}")
            print()
        elif choice == '3':
            print("\nAccommodations Eligibility:")
            accommodations_eligibility(profile)
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def calculate_accommodations_score(profile) -> float: # Calculates a score based on the user's stress level and average sleep hours
    score = profile.get("Stress Level", 0) * 0.5 + (10 - profile.get("Average Sleep Hours", 0)) * 0.5
    return score

def accommodations_eligibility(profile): # Determines the user's eligibility for accommodations and provides a list of potential accommodations
    score = calculate_accommodations_score(profile)
    accommodations = [
        "Extended time on exams",
        "Quiet testing environment",
        "Note-taking assistance",
        "Priority registration for classes",
        "Access to recorded lectures"
    ]
    print(f"\nAccommodations Eligibility Score: {score}")
    print("You are eligible for the following accommodations:")
    if score >= 9:
        for accommodation in accommodations:  # Show all accommodations for very high score
            print(f"- {accommodation}")
    elif score >= 7:
        for accommodation in accommodations[:3]:  # Show top 3 accommodations for high score
            print(f"- {accommodation}")
    elif score >= 4:
        for accommodation in accommodations[:2]:  # Show top 2 accommodations for moderate score
            print(f"- {accommodation}")
    else:
        print("- You are not eligible for accommodations at this time.")
    print()

def mental_health_resources(): # Provides a list of mental health resources specifically tailored for neurodivergent individuals
    mental_health = [
        "National Alliance on Mental Illness (NAMI)", 
        "Autistic Self Advocacy Network (ASAN)", 
        "The Mighty: Mental Health Support for Neurodivergent Individuals"]
    
    print("\n~ Mental Health Resources ~")
    for resource in mental_health:
        print(f"- {resource}")

def social_connection(): # Provides opportunities for social connections
    virtual_meetups = [
        "Something like Neurodivergent Virtual Meetup", 
        "Neurodivergent Social Hour", 
        "Neurodivergent Support Group"]
    local_support_groups = [
        "Everett Neurodivergent Support Group", 
        "Neurodivergent of Seattle", 
        "Tacoma Neurodivergent Social Group"]
    online_communities = [
        "Reddit: r/Neurodivergent", 
        "Facebook: Neurodivergent Support Network", 
        "Discord: Neurodivergent Hangout"]

    while True:
        print("\t~ Social connections opportunities ~")
        print("\t1. Virtual meetups")
        print("\t2. Local support groups")
        print("\t3. Online communities")
        print("\t4. Return to Resource Categories")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\nVirtual meetups:")
            for meetup in virtual_meetups:
                print(f"- {meetup}")
            print()
        elif choice == '2':
            print("\nLocal support groups:")
            for group in local_support_groups:
                print(f"- {group}")
            print()
        elif choice == '3':
            print("\nOnline communities:")
            for community in online_communities:
                print(f"- {community}")
            print()
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def connect_with_mentor(profile): # Provides a mentor based on the user's neurodivergent condition
    mentors = {
        "John Doe": "Autism", 
        "Jane Smith": "ADHD", 
        "Alex Johnson": "Dyslexia",
        "Emily Davis": "Dyspraxia",
        "Michael Brown": "Sensory Processing Disorder"}
  
    print("\n~ Connect with a Mentor ~")
    if profile["Condition"].lower() not in [condition.lower() for condition in mentors.values()]:
        print(f"- Robert Clark (Condition: {profile['Condition']})")
        print(f"  Contact: robert.clark@neurodivergentsupport.org")
    else:
        for mentor, condition in mentors.items():
            if condition.lower() == profile["Condition"].lower():
                email = mentor.lower().replace(" ", ".") + "@neurodivergentsupport.org"
                print(f"- {mentor} (Condition: {condition})")
                print(f"  Contact: {email}")

def profile_settings(profile): # Allows the user to update their profile information
    while True:
        print("\n.  ~ Profile Settings ~")
        print(".  1. Update Personal Information")
        print(".  2. Update Stress Level and Sleep Hours")
        print(".  3. Delete Profile")
        print(".  4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            update_personal_info(profile)
        elif choice == '2':
            update_stress_and_sleep(profile)
        elif choice == '3':
            delete_profile(profile)
            break
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def update_personal_info(profile): # Allows the user to update their personal information
    print("\nUpdate Personal Information")
    profile["Name"] = profile["Name"]  # Name is not editable to maintain consistency in the students dictionary
    profile["Age"] = int(input("Enter your age: "))
    profile["Condition"] = input("Enter your neurodivergent condition (e.g., Autism, ADHD, Dyslexia): ").strip().capitalize()
    profile["College Year"] = input("Enter your college year (e.g., Freshman, Sophomore): ").capitalize()
    profile["Major"] = input("Enter your major: ").strip().capitalize()
    profile["Stress Level"] = int(input("On a scale of 1-10, how stressed do you feel about college? "))
    profile["Average Sleep Hours"] = float(input("On average, how many hours of sleep do you get per night? "))
    students[profile["Name"]] = profile
    rewrite_file()
    print("\nPersonal information updated successfully!")

def update_stress_and_sleep(profile): # Allows the user to update their stress level and average sleep hours
    print("\nUpdate Stress Level and Sleep Hours")
    profile["Stress Level"] = int(input("On a scale of 1-10, how stressed do you feel about college? "))
    profile["Average Sleep Hours"] = float(input("On average, how many hours of sleep do you get per night? "))
    students[profile["Name"]] = profile
    rewrite_file()
    print("\nStress level and sleep hours updated successfully!")

def delete_profile(profile): # Allows the user to delete their profile from the system
    confirmation = input("\nAre you sure you want to delete your profile? This action cannot be undone. (yes/no): ").lower()
    if confirmation == 'yes' or confirmation == 'y':
        del students[profile["Name"]]
        rewrite_file()
        print("\nProfile deleted successfully.  Have a great day!")
        exit()
    else:
        print("\nProfile deletion canceled.")

def average_stress_level(students): # Calculates the average stress level of all students in the system
    stress_values = [
        student["Stress Level"]
        for student in students.values()
        if isinstance(student.get("Stress Level"), (int, float))
    ]
    return sum(stress_values) / len(stress_values) if stress_values else 0

def average_sleep_hours(students): # Calculates the average sleep hours of all students in the system
    sleep_values = [
        student["Average Sleep Hours"]
        for student in students.values()
        if isinstance(student.get("Average Sleep Hours"), (int, float))
    ]
    return sum(sleep_values) / len(sleep_values) if sleep_values else 0

def main():
    display_welcome_message()
    user_profile = create_profile()
    main_menu(user_profile)
    
    print(f"Average Stress Level: {average_stress_level(students):.2f}")
    print(f"Average Sleep Hours: {average_sleep_hours(students):.2f}")
    print()

if __name__ == "__main__":
    main()