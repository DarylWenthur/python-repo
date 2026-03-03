

# 🧠N.E.R.D.  Neurodivergent Student Support Network

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A Python-based student support management system that stores student profiles, evaluates accommodation eligibility, and connects students with mentors based on neurodivergent conditions.

---

## 📌 Overview

This project provides a structured support system for neurodivergent college students by:

- Managing student profiles via CSV storage
- Calculating academic accommodation eligibility
- Connecting students with appropriate mentors
- Tracking stress and sleep statistics

The system is modular and easily extendable for GUI integration or database expansion.

---

## 📂 Project Structure

<img width="5589" height="1614" alt="supportgr_diagram" src="https://github.com/user-attachments/assets/f24383de-faa7-4921-a0ab-d3c18f880a41" />


The application reads from and writes to:

`support_network_gui/students.csv`

## 📊 CSV File Requirements

The `students.csv` file must include the following header:

Name, Age, Condition, College Year, Major, Stress Level, Average Sleep Hours

### Example 

`Jane Doe,20,ADHD,Sophomore,Psychology,8,6.5`

## 🛠 Features

### ✅ Profile Management

- Read student profiles from CSV: `read_from_file()`
- Create new profiles or returns existing profile: `create_profile()`
- Update existing profiles
- Delete profiles
- Persist data to file

---

### 📈 Accommodation Eligibility

**Eligibility Score Formula**


`score = (Stress Level * 0.5) + (10 - Average Sleep Hours) * 0.5 `

Score Range	Eligibility:

- ≥ 9	Full accommodations
- ≥ 7	Top 3 accommodations
- ≥ 4	Top 2 accommodations
- < 4	Not eligible

Accomodations include: 

- Extended time on exams
- Quiet testing environment
- Note-taking assistance 
- Priority registration
- Access to recorded lectures

###🤝 Mentor Matching

Students are matched with mentors based on condition.

Supported Conditions:

- Autism
- ADHD
- Dyslexia
- Dyspraxia
- Sensory Processing Disorder

If no direct match is found, a general mentor is assigned.

###📊 System Analytics

The system calculates:

- Average stress level across students: `average_stress_level(students)`
- Average sleep hours across students: `average_sleep_hours(students)`

###▶️ Installation & Running
####1️⃣ Clone the Repository

`git clone https://github.com/yourusername/support-network.git`
`cd support-network`

####2️⃣ Ensure Folder Structure

Make sure the following file exists before running:

`support_network_gui/students.csv`

####3️⃣ Run the Program

`python support_network.py`

###🔒 Error Handling

The program includes handling for:

- FileNotFoundError
- IOError
- Missing stress/sleep values
- Safe dictionary lookups

###🧩 Built With

- Python 3
- Built-in csv module
- Dictionary-based data storage
- File I/O operations

###🚀 Future Enhancements

- GUI integration (Tkinter or PyQt)
- Database backend (SQLite/PostgreSQL)
- User authentication
- Data validation layer
- Reporting dashboard
- REST API version

###🤝 Contributing

Contributions are welcome!

- Fork the repository
- Create a feature branch
   `git checkout -b feature-name`
- Commit changes
   `git commit -m "Add feature"`
- Push the branch
   `git push origin feature-name`
-Open pull request

###📄 License

This project is intended for educational and academic use.



