import pandas as pd
import random
import names  # pip install names

# Lists for random selection
conditions = ["Neurotypical", "ADHD", "Autism", "Dyslexia", "Anxiety"]
college_years = [2026, 2027, 2028, 2029, 2030]
majors = ["Computer Science", "Psychology", "Biology", "Engineering", "Mathematics",
          "Economics", "Art", "History", "Business", "Physics"]

data = []

for _ in range(100):
    name = names.get_full_name()
    age = random.randint(18, 25)
    condition = random.choice(conditions)
    year = random.choice(college_years)
    major = random.choice(majors)
    stress = int(round(random.uniform(1, 10), 1))          # Stress Level 1-10
    sleep = round(random.uniform(4, 10), 1)           # Average Sleep Hours 4-10
    data.append([name, age, condition, year, major, stress, sleep])

# Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Age", "Condition", "College Year", "Major",
                                 "Stress Level", "Average Sleep Hours"])

# Save to CSV
df.to_csv("support_network_gui/students.csv", index=False)

print("students.csv created with 100 entries.")