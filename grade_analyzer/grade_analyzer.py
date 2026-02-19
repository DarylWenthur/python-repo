def add_student(num_grades):
    grades = []
    for i in range(num_grades):
        grade = float(input(f"Enter grade {i + 1}: "))
        grades.append(grade)
    return grades

def average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def highest_grade(grades):
    if len(grades) == 0:
        return 0
    return max(grades)

def lowest_grade(grades):
    if len(grades) == 0:
        return 0
    return min(grades)

def num_passed_failed(grades, passing_grade=60) -> tuple:
    passed = sum(1 for grade in grades if grade >= passing_grade)
    failed = sum(1 for grade in grades if grade < passing_grade)
    return passed, failed

def letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def print_class_stats(avg, highest, lowest, passed, failed):
    print(f"Average Grade: {avg:.2f}\t{letter_grade(avg)}")
    print(f"Highest Grade: {highest:.2f}\t{letter_grade(highest)}")
    print(f"Lowest Grade: {lowest:.2f}\t{letter_grade(lowest)}")
    print(f"Number of Students Passed: {passed}")
    print(f"Number of Students Failed: {failed}")
    print()

def main():
    print("\n~ Welcome to the Grade Analyzer ~\n")
    num_students = int(input("Enter the number of students: "))
    all_grades = []
    
    for i in range(num_students):
        print(f"\nEntering grades for student {i + 1}:")
        num_grades = int(input("Enter the number of grades for this student: "))
        grades = add_student(num_grades)
        all_grades.extend(grades)
    avg = average(all_grades)
    highest = highest_grade(all_grades)
    lowest = lowest_grade(all_grades)
    passed, failed = num_passed_failed(all_grades)
    print("\nClass Statistics:")
    print_class_stats(avg, highest, lowest, passed, failed)

if __name__ == "__main__":
    main()