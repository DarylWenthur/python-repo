import csv
import random
from huggingface_hub import InferenceClient

HF_TOKEN = "ENTER TOKEN HERE" # Hugging Face API token for future use in AI features
client = InferenceClient(token=HF_TOKEN )

def read_from_file() -> dict: 
    """Reads student profiles from a CSV file and returns a dictionary of profiles"""
    students_dict = {}

    try:
        with open("support_network_gui_ai/students.csv", "r") as file:
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

def save_profile_to_file(profile): 
    """Appends a new student profile to the CSV file"""
    try:
        with open("support_network_gui_ai/students.csv", "a", newline="") as file:
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

def rewrite_file(students): 
    """Writes the entire students dictionary back to the CSV file, used for updates and deletions"""
    try:
        with open("support_network_gui_ai/students.csv", "w", newline="") as file:
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

def create_update_profile(students, profile_data)-> dict: 
    """Creates a new student profile by asking the user for their information"""
    full_name = profile_data["Name"]

    # Check if profile exists
    if full_name in students:
        students[full_name] = profile_data
        rewrite_file(students)
        return "updated"
    else:
        students[full_name] = profile_data
        save_profile_to_file(profile_data)
        return "created"

def calculate_accommodations_score(profile) -> float: 
    """Calculates a score based on the user's stress level and average sleep hours"""
    score = profile.get("Stress Level", 0) * 0.5 + (10 - profile.get("Average Sleep Hours", 0)) * 0.5
    return score

def accommodations_eligibility(profile):
    """Determines eligibility and returns a formatted string."""
    score = calculate_accommodations_score(profile)
    accommodations = [
        "Extended time on exams",
        "Quiet testing environment",
        "Note-taking assistance",
        "Priority registration for classes",
        "Access to recorded lectures"
    ]

    text = f"Accommodations Eligibility Score: {score}\n"

    if score >= 9:
        text += "You are eligible for the following accommodations:\n"
        text += "\n".join(f"- {a}" for a in accommodations)
    elif score >= 7:
        text += "You are eligible for the following accommodations:\n"
        text += "\n".join(f"- {a}" for a in accommodations[:3])
    elif score >= 4:
        text += "You are eligible for the following accommodations:\n"
        text += "\n".join(f"- {a}" for a in accommodations[:2])
    else:
        text += "You are not eligible for accommodations at this time."

    return text

def connect_with_mentor(profile): 
    """Provides a mentor based on the user's neurodivergent condition"""
    mentors = {
        "John Doe": "Autism", 
        "Jane Smith": "ADHD", 
        "Alex Johnson": "Dyslexia",
        "Emily Davis": "Dyspraxia",
        "Michael Brown": "Sensory Processing Disorder"}
  
    text = "Mentor Connections:\n"
    if profile["Condition"].lower() not in [condition.lower() for condition in mentors.values()]:
        text += f"- Robert Clark (Condition: {profile['Condition']})\n"
        text += f"  Contact: robert.clark@neurodivergentsupport.org\n"
    else:
        for mentor, condition in mentors.items():
            if condition.lower() == profile["Condition"].lower():
                email = mentor.lower().replace(" ", ".") + "@neurodivergentsupport.org"
                text += f"- {mentor} (Condition: {condition})\n"
                text += f"  Contact: {email}\n"

    return text

def average_stress_level(students): 
    """Calculates the average stress level of all students in the system"""
    stress_values = [
        student["Stress Level"]
        for student in students.values()
        if isinstance(student.get("Stress Level"), (int, float))
    ]
    return sum(stress_values) / len(stress_values) if stress_values else 0

def average_sleep_hours(students):
    """Calculates the average sleep hours of all students in the system"""
    sleep_values = [
        student["Average Sleep Hours"]
        for student in students.values()
        if isinstance(student.get("Average Sleep Hours"), (int, float))
    ]
    return sum(sleep_values) / len(sleep_values) if sleep_values else 0

def get_ai_response(message: str) -> str:
    """Sends a message to the Hugging Face Inference API and returns the AI's response"""
    response = client.chat_completion(
        model="deepseek-ai/DeepSeek-V3-0324",  # model with available inference provider
        messages=[
            {"role": "system", "content": "You are a supportive AI chatbot."},
            {"role": "user", "content": message},
        ],
        max_tokens=200
    )
    # The API returns a typical OpenAI‑like response format
    return response.choices[0].message.content

def show_graphs():
    """Displays a scatter plot of stress levels vs average sleep hours for all students, color-coded by condition"""
    import pandas as pd
    import matplotlib.pyplot as plt

    try:
        df = pd.read_csv("support_network_gui/students.csv")

        # Drop missing values to avoid errors
        stress = df["Stress Level"].dropna()
        sleep = df["Average Sleep Hours"].dropna()

        # Make sure both have the same length
        min_len = min(len(stress), len(sleep))
        stress = stress[:min_len]
        sleep = sleep[:min_len]

        group1 = df[df["Condition"] == "Neurotypical"]
        group2 = df[df["Condition"] == "ADHD"]
        group3 = df[df["Condition"] == "Autism"]
        group4 = df[df["Condition"] == "Dyslexia"]
        group5 = df[df["Condition"] == "Anxiety"]

        plt.figure(figsize=(6, 4))
        plt.scatter(group1["Stress Level"], 
                    group1["Average Sleep Hours"], 
                    label="Neurotypical",
                    marker="o",
                    alpha=0.7)
        plt.scatter(group2["Stress Level"], 
                    group2["Average Sleep Hours"], 
                    label="ADHD", 
                    marker="s",
                    alpha=0.7)
        plt.scatter(group3["Stress Level"], 
                    group3["Average Sleep Hours"], 
                    label="Autism", 
                    marker="^",
                    alpha=0.7)
        plt.scatter(group4["Stress Level"], 
                    group4["Average Sleep Hours"], 
                    label="Dyslexia", 
                    marker="D",
                    alpha=0.7)
        plt.scatter(group5["Stress Level"], 
                    group5["Average Sleep Hours"], 
                    label="Anxiety", 
                    marker="X",
                    alpha=0.7)
        plt.legend(loc="upper left")
        plt.title("Stress vs Sleep Hours")
        plt.xlabel("Stress Level")
        plt.ylabel("Average Sleep Hours")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

    except FileNotFoundError:
        print("students.csv not found!")
    except Exception as e:
        print(f"Error showing graph: {e}")
        
def main():
    students = {}
    students = read_from_file()

if __name__ == "__main__":
    main()

