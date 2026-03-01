import tkinter as tk
from tkinter import messagebox
import support_network as logic
from tkinter import scrolledtext

current_profile = None

# ---------- FUNCTIONS ----------

def show_frame(frame):
    frame.tkraise()

def open_profile_form():
    show_frame(profile_frame)

def open_returning_form():
    show_frame(returning_frame)

def open_main_screen():
    show_frame(main_frame)

def open_academic_resources():
    show_frame(academic_frame)

def open_mental_health_resources():
    show_frame(mental_health_frame)

def open_mentor_program():
    show_frame(mentor_frame)

def open_discussion_groups():
    show_frame(discussion_frame)

def open_support_groups():
    show_frame(support_frame)

def open_statistics():
    show_frame(statistics_frame)

def submit_profile():
    global current_profile

    name = name_entry.get().strip().title()  # Capitalize first letter of each word
    age = age_entry.get().strip()
    neurodivergent_type = neurodivergent_type_entry.get().strip().upper()
    graduation_year = graduation_year_entry.get().strip()
    major = major_entry.get().strip().upper()
    stress_level = stress_entry.get().strip()
    sleep = average_sleep_entry.get().strip()

    # Check empty fields
    if not name or not age or not major or not stress_level or not sleep:
        form_status_label.config(text="Please fill out all fields.")
        print("Empty field detected") # Debugging statement to verify empty field detection
        return

    # Convert safely
    try:
        age = int(age)
        stress = int(stress_level)
        sleep = float(sleep)
    except ValueError:
        form_status_label.config(text="Age/Stress must be whole numbers. Sleep must be a number.")
        print("Conversion failed") # Debugging statement to verify conversion failure
        return

    # Create profile
    profile = {
        "Name": name,
        "Age": age,
        "Condition": neurodivergent_type,
        "College Year": graduation_year,
        "Major": major,
        "Stress Level": stress,
        "Average Sleep Hours": sleep
    }

    students[name] = profile  # Update or create profile in students dictionary
    current_profile = profile  # Set current profile for session

    welcome_text = f"Welcome, {name}! Explore the resources and connections available to you."

    # Remove old label if it exists (optional)
    for widget in main_frame.grid_slaves(row=0, column=0):
        widget.destroy()
    
    tk.Label(main_frame, 
             text=welcome_text, 
             font=("Arial", 14),
             fg="#2f2f2f",
             bg=main_frame.cget("bg")
    ).grid(row=0, column=0, pady=20)

    print("Profile created:", profile) # Debugging statement to verify profile creation

    # Save using your logic file
    result = logic.create_update_profile(students, profile)

    form_status_label.config(text="Profile saved successfully!")

    enable_menu()
    show_frame(main_frame)

def load_profile():
    global current_profile
    name = returning_name_entry.get().strip().title()  # Capitalize first letter of each word

    if name.strip() == "":
        return_form_status_label.config(text="Please fill out all fields.")
        return
    
    if name not in students:
        open_profile_form()
        return
    
    # Load existing profile
    profile = students[name]
    current_profile = profile  # Set current profile for session
    welcome_text = f"Welcome back, {name}! Explore the resources and connections."
    
    # Remove old label if it exists (optional)
    for widget in main_frame.grid_slaves(row=0, column=0):
        widget.destroy()
    
    tk.Label(main_frame, 
                text=welcome_text, 
                font=("Arial", 14),
                fg="#2f2f2f",
                bg=main_frame.cget("bg")
    ).grid(row=0, column=0, pady=20)

    enable_menu()
    show_frame(main_frame)

def enable_menu():
    """Enable the menu after profile creation."""
    window.config(menu=menu_bar)

def exit_program():
    window.quit()


# ---------- GUI SETUP ----------

def setup_frames():
    global container
    global welcome_frame, profile_frame, returning_frame, main_frame, academic_frame
    global mental_health_frame, mentor_frame, discussion_frame, support_frame, statistics_frame
    global welcome_label, name_entry, returning_name_entry, age_entry
    global neurodivergent_type_entry, graduation_year_entry, major_entry
    global stress_entry, average_sleep_entry, form_status_label, return_form_status_label

    container = tk.Frame(window, bg="#cfe8ff")
    container.pack(fill="both", expand=True)

    # Welcome Frame
    welcome_frame = tk.Frame(container, bg="#cfe8ff")

    welcome_label = tk.Label(
        welcome_frame,
         text="~ Welcome to the Neurodivergent Education Resource Database! - N.E.R.D. ~\n\n\n"
             "This is a safe space for neurodivergent individuals to connect,\n"
             "share experiences, and find support. Whether you're looking for advice,\n"
             "resources, or just someone to talk to, we're here for you. Feel free to\n"
             "explore the different sections of our network, join discussions, and\n"
             "reach out to others who understand your journey. Remember,\n"
             "you're not alone, and we're stronger together!",
        font=("Arial", 12),
        bg=welcome_frame.cget("bg"),  
        fg="#2f2f2f",
        justify="left",
        wraplength=700,   # wrap long text
        width=84,   # fixes width
        height=10,   # fixes height
        bd=1,
        relief="solid",        # solid border

        highlightthickness=2,  
        highlightbackground="#C7D5E0"
        )

    welcome_label.grid(row=0, column=0, padx=20, pady=20)

    returning_button = tk.Button(
        welcome_frame,
        text="Returning User",
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        command=load_profile
    )
    
    new_button = tk.Button(
        welcome_frame,
        text="New User",
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        command=open_profile_form
    )

    button_frame = tk.Frame(welcome_frame, bg=welcome_frame.cget("bg"))
    button_frame.grid(row=1, column=0, columnspan=2, pady=5)

    returning_button = tk.Button(button_frame, 
                                text="Returning User", 
                                font=("Arial", 12),
                                fg="#2f2f2f",
                                bg="#b7d7c8",
                                activebackground="#a3cbb7",
                                command=lambda: show_frame(returning_frame))
    returning_button.pack(side=tk.LEFT, padx=5)

    new_button = tk.Button(button_frame, 
                           text="New User", 
                           font=("Arial", 12), 
                           fg="#2f2f2f", 
                           bg="#b7d7c8", 
                           activebackground="#a3cbb7",
                           command=open_profile_form)
    new_button.pack(side=tk.LEFT, padx=5)

    # Returning Frame
    returning_frame = tk.Frame(container, bg="#cfe8ff")
    returning_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents

    tk.Label(returning_frame, 
             text="Welcome Back!", 
             font=("Arial", 16), 
             fg="#2f2f2f", 
             bg=returning_frame.cget("bg")).grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(returning_frame, 
             text="First/Last Name:",
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=returning_frame.cget("bg")).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    returning_name_entry = tk.Entry(returning_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    returning_name_entry.grid(row=1, column=1, padx=10, pady=5)

    submit_button = tk.Button(
        returning_frame,
        text="Enter",
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        activebackground="#a3cbb7",
        command=lambda: load_profile()  # calls function to process entry
    )
    submit_button.grid(row=2, column=1, sticky="w", pady=10)

    return_form_status_label = tk.Label(returning_frame, bg=returning_frame.cget("bg"),text="", fg="red")
    return_form_status_label.grid(row=3, column=0, columnspan=2, pady=5)

    # New & Update Profile Frame
    profile_frame = tk.Frame(container, bg="#cfe8ff")
    profile_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents

    tk.Label(profile_frame, 
             text="Create/Update Your Profile", 
             font=("Arial", 16),
             fg="#2f2f2f",
             bg=profile_frame.cget("bg")).grid(
        row=0, column=1, columnspan=2, pady=10)

    tk.Label(profile_frame, 
             text="First/Last Name:", 
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=1, column=0, sticky="e", padx=10)
    name_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(profile_frame, 
             text="Age:", 
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=2, column=0, sticky="e", padx=10)
    age_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    age_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(profile_frame, 
             text="Neurodivergent Type:", 
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=3, column=0, sticky="e", padx=10)
    neurodivergent_type_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    neurodivergent_type_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(profile_frame, 
             text="Graduation Year:", 
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=4, column=0, sticky="e", padx=10)
    graduation_year_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    graduation_year_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(profile_frame, 
             text="Major:", 
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=5, column=0, sticky="e", padx=10)
    major_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    major_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(profile_frame, 
             text="Stress Level (1 - 10):", 
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=6, column=0, sticky="e", padx=10)
    stress_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    stress_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(profile_frame, 
             text="Average sleep hours:",  
             font=("Arial", 12), 
             fg="#2f2f2f", 
             bg=profile_frame.cget("bg")).grid(row=7, column=0, sticky="e", padx=10)
    average_sleep_entry = tk.Entry(profile_frame, font=("Arial", 12), fg="#2f2f2f", bg="#f4f8fb")
    average_sleep_entry.grid(row=7, column=1, padx=10, pady=5)

    submit_button = tk.Button(
        profile_frame,
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        activebackground="#a3cbb7",
        text="Submit Profile",
        command=submit_profile
    )
    submit_button.grid(row=8, column=1, columnspan=2, pady=10)

    form_status_label = tk.Label(profile_frame, 
                                 text="",
                                 bg=profile_frame.cget("bg"))
    form_status_label.grid(row=9, column=0, columnspan=2, pady=5)

    # Main Frame
    main_frame = tk.Frame(container, bg="#cfe8ff")
    main_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents

    # Create a fixed-size container
    info_container = tk.Frame(
        main_frame,
        width=700,
        height=250,
        bg=main_frame.cget("bg"),
        bd=1,
        relief="solid",
        highlightthickness=2,
        highlightbackground="#C7D5E0"
    )

    info_container.grid(row=2, column=0, padx=20, pady=10)
    info_container.grid_propagate(False)  # CRITICAL: prevents resizing

    # Put the label inside and center it
    main_info_label = tk.Label(
        info_container,
        text="N.E.R.D.",
        font=("Arial", 80, "bold"),
        bg=main_frame.cget("bg"),
        fg="#2f2f2f"
    )

    main_info_label.place(relx=0.5, rely=0.5, anchor="center")

    # Academic Resources Frame
    academic_frame = tk.Frame(container, bg="#cfe8ff")
    academic_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
    tk.Label(academic_frame, 
             text="Welcome to Academic Resources", 
             font=("Arial", 16), 
             fg="#2f2f2f", 
             bg=academic_frame.cget("bg")).grid(row=0, column=0, pady=20)
    
    time_management_tools = [
        "Trello: A visual project management tool to organize tasks and deadlines", 
        "Forest: A focus timer app that helps you stay on track by planting virtual trees", 
        "Google Calendar: A versatile calendar app to schedule study sessions and reminders"]
    
    study_techniques = [
        "Pomodoro Technique: Study for 25 minutes, then take a 5-minute break", 
        "Active Recall: Test yourself on the material instead of just rereading", 
        "Mind Mapping: Create visual diagrams to connect concepts and ideas"]

    # Create a Label that can show multiple lines
    info_label = tk.Label(
        academic_frame,
        text="",         # start empty
        font=("Arial", 12),
        bg=academic_frame.cget("bg"),      # blend with background if possible
        fg="#2f2f2f",
        justify="left",
        wraplength=700,   # wrap long text
        width=84,   # fixes width
        height=10,   # fixes height
        bd=1,
        relief="solid",        # solid border
        highlightthickness=2,  
        highlightbackground="#C7D5E0"
    )
    info_label.grid(row=2, column=0, padx=20, pady=10)

    button_frame = tk.Frame(academic_frame, bg=academic_frame.cget("bg"))
    button_frame.grid(row=1, column=0, pady=10)

    time_management_button = tk.Button(
        button_frame, 
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        activebackground="#a3cbb7",
        text="Time Management Tools", 
        command=lambda: info_label.config(text="\n".join(time_management_tools)))
    time_management_button.pack(side=tk.LEFT, padx=5)

    study_techniques_button = tk.Button(
        button_frame, 
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        activebackground="#a3cbb7",
        text="Study Techniques", 
        command=lambda: info_label.config(text="\n".join(study_techniques)))
    study_techniques_button.pack(side=tk.LEFT, padx=5)

    accommodations_button = tk.Button(
        button_frame, 
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        activebackground="#a3cbb7",
        text="Accommodations", 
        command=lambda: info_label.config(text=logic.accommodations_eligibility(current_profile)))
    accommodations_button.pack(side=tk.LEFT, padx=5)

    # Mental Health Resources Frame
    mental_health_frame = tk.Frame(container, bg="#cfe8ff")
    mental_health_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
    
    tk.Label(mental_health_frame, 
             text="Mental Health Resources", 
             font=("Arial", 16), 
             fg="#2f2f2f", 
             bg=mental_health_frame.cget("bg")).grid(row=0, column=0, pady=20)

    mental_health = [
        "National Alliance on Mental Illness (NAMI)", 
        "Autistic Self Advocacy Network (ASAN)", 
        "The Mighty: Mental Health Support for Neurodivergent Individuals"]

    # Create a Label that can show multiple lines
    mh_info_label = tk.Label(
        mental_health_frame,
        text="",         # start empty
        font=("Arial", 12),
        bg=mental_health_frame.cget("bg"),      # blend with background if possible
        fg="#2f2f2f",
        justify="left",
        wraplength=700,   # wrap long text
        width=84,   # fixes width
        height=10,   # fixes height
        bd=1,
        relief="solid",        # solid border

        highlightthickness=2,  
        highlightbackground="#C7D5E0"
    )
    mh_info_label.grid(row=2, column=0, padx=20, pady=10)

    button_frame = tk.Frame(mental_health_frame, bg=mental_health_frame.cget("bg"))
    button_frame.grid(row=1, column=0, pady=10)

    mental_health_button = tk.Button(
        button_frame, 
        text="Mental Health Resources",
            font=("Arial", 12),
            fg="#2f2f2f", 
            bg="#b7d7c8",
            activebackground="#a3cbb7",
        command=lambda: mh_info_label.config(text="\n".join(mental_health)))
    mental_health_button.pack(side=tk.LEFT, padx=5)

    # Mentor Program Frame
    mentor_frame = tk.Frame(container, bg="#cfe8ff")
    mentor_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
    tk.Label(mentor_frame, 
             text="Mentor Program", 
             font=("Arial", 16), 
             fg="#2f2f2f", 
             bg=mentor_frame.cget("bg")).grid(row=0, column=0, pady=20)

    men_info_label = tk.Label(
        mentor_frame,
        text="",         # start empty
        font=("Arial", 12),
        bg=mentor_frame.cget("bg"),      # blend with background if possible
        fg="#2f2f2f",
        justify="left",
        wraplength=700,   # wrap long text
        width=84,   # fixes width
        height=10,   # fixes height
        bd=1,
        relief="solid",        # solid border

        highlightthickness=2,  
        highlightbackground="#C7D5E0"
    )
    men_info_label.grid(row=2, column=0, padx=20, pady=10)

    button_frame = tk.Frame(mentor_frame, bg=mentor_frame.cget("bg"))
    button_frame.grid(row=1, column=0, pady=10)

    mentor_button = tk.Button(
        button_frame, 
        text="Mentor Program Info",
        font=("Arial", 12),
        fg="#2f2f2f",
        bg="#b7d7c8",
        activebackground="#a3cbb7",
        command=lambda: men_info_label.config(text=logic.connect_with_mentor(current_profile)))
    mentor_button.pack(side=tk.LEFT, padx=5)

# Discussion Frame
    discussion_frame = tk.Frame(container, bg="#cfe8ff")
    discussion_frame.pack_propagate(False)
    discussion_frame.grid_columnconfigure(0, weight=1)  # Entry expands
    discussion_frame.grid_columnconfigure(1, weight=0)  # Button stays fixed

    tk.Label(
        discussion_frame,
        text="Questions? Ask AI",
        font=("Arial", 16),
        fg="#2f2f2f",
        bg=discussion_frame.cget("bg")
    ).grid(row=0, column=0, pady=20)

    # Output box (AI response goes here)
    dis_info_box = scrolledtext.ScrolledText(
        discussion_frame,
        font=("Arial", 12),
        wrap="word",              # wrap at word boundaries
        width=84,
        height=10,
        bd=1,
        bg=discussion_frame.cget("bg"),      # blend with background if possible
        relief="solid"
    )

    dis_info_box.grid(row=1, column=0, padx=20, pady=10)

    # Make it read-only initially
    dis_info_box.config(state="disabled")

    # Input container frame
    input_frame = tk.Frame(discussion_frame, bg=discussion_frame.cget("bg"))
    input_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    # Allow entry to expand inside this frame
    input_frame.grid_columnconfigure(0, weight=1)

    # Input box
    discussion_entry = tk.Entry(
        input_frame,
        font=("Arial", 12)
    )

    discussion_entry.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=(0, 10)
    )

    # Submit function
    def submit_discussion():
        user_message = discussion_entry.get().strip()

        if not user_message:
            return

        dis_info_box.config(state="normal")  # Enable editing temporarily
        dis_info_box.delete(1.0, tk.END)  # Clear previous content
        dis_info_box.insert(tk.END, "Thinking...")  # Show thinking message
        dis_info_box.config(state="disabled")  # Re-disable read-only state

        try:
            ai_reply = logic.get_ai_response(user_message)
            dis_info_box.config(state="normal")
            dis_info_box.delete(1.0, tk.END)
            dis_info_box.insert(tk.END, ai_reply)
            dis_info_box.config(state="disabled")
        except Exception as e:
            dis_info_box.config(state="normal")
            dis_info_box.delete(1.0, tk.END)
            dis_info_box.insert(tk.END, "Error connecting to AI.")
            dis_info_box.config(state="disabled")

        discussion_entry.delete(0, tk.END)

    # Submit button
    submit_button = tk.Button(
        input_frame,
        text="Submit",
        command=submit_discussion,
        font=("Arial", 12)
    )

    submit_button.grid(
        row=0,
        column=1
    )

    # Support Groups Frame
    support_frame = tk.Frame(container, bg="#cfe8ff")
    support_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
    tk.Label(support_frame, 
             text="Support Groups", 
             font=("Arial", 16), 
             fg="#2f2f2f", 
             bg=support_frame.cget("bg")).grid(row=0, column=0, pady=20)

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

    # Create a Label that can show multiple lines
    sup_info_label = tk.Label(
        support_frame,
        text="",         # start empty
        font=("Arial", 12),
        bg=support_frame.cget("bg"),      # blend with background if possible
        fg="#2f2f2f",
        justify="left",
        wraplength=700,   # wrap long text
        width=84,   # fixes width
        height=10,  # fixes height
        bd=1,
        relief="solid",        # solid border

        highlightthickness=2,  
        highlightbackground="#C7D5E0"
    )
    sup_info_label.grid(row=2, column=0, padx=20, pady=10)

    sup_button_frame = tk.Frame(support_frame, bg=support_frame.cget("bg"))
    sup_button_frame.grid(row=1, column=0, pady=10)

    virtual_meetups_button = tk.Button(
        sup_button_frame, 
        text="Virtual Meetups",
            font=("Arial", 12),
            fg="#2f2f2f",
            bg="#b7d7c8",
            activebackground="#a3cbb7",
        command=lambda: sup_info_label.config(text="\n".join(virtual_meetups)))
    virtual_meetups_button.pack(side=tk.LEFT, padx=5)

    local_support_groups_button = tk.Button(
        sup_button_frame, 
        text="Local Support Groups",
            font=("Arial", 12),
            fg="#2f2f2f",
            bg="#b7d7c8",
            activebackground="#a3cbb7", 
        command=lambda: sup_info_label.config(text="\n".join(local_support_groups)))
    local_support_groups_button.pack(side=tk.LEFT, padx=5)

    online_communities_button = tk.Button(
        sup_button_frame, 
        text="Online Communities", 
            font=("Arial", 12),
            fg="#2f2f2f",
            bg="#b7d7c8",
            activebackground="#a3cbb7",
        command=lambda: sup_info_label.config(text="\n".join(online_communities)))
    online_communities_button.pack(side=tk.LEFT, padx=5)

    # Statistics Frame
    statistics_frame = tk.Frame(container, bg="#cfe8ff")

    statistics_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
    tk.Label(statistics_frame, text="Statistics", font=("Arial", 16), bg="#cfe8ff").grid(row=0, column=0, pady=20)

    stat_info_label = tk.Label(
    statistics_frame,
        text="",         # start empty
        font=("Arial", 12),
        bg=statistics_frame.cget("bg"),      # blend with background if possible
        fg="#2f2f2f",
        justify="left",
        wraplength=700,   # wrap long text
        width=84,   # fixes width
        height=10,   # fixes height
        bd=1,
        relief="solid",        # solid border
        highlightthickness=2,  
        highlightbackground="#C7D5E0"
    )
    stat_info_label.grid(row=2, column=0, padx=20, pady=10)

    button_frame = tk.Frame(statistics_frame, bg=statistics_frame.cget("bg"))
    button_frame.grid(row=1, column=0, pady=10)

    statistics_button = tk.Button(
        button_frame, 
        text="Statistics Info", 
            font=("Arial", 12),
            fg="#2f2f2f",
            bg="#b7d7c8",
            activebackground="#a3cbb7",
        command=lambda: stat_info_label.config(text=f"Average Stress Level: {logic.average_stress_level(students):.2f}\nAverage Sleep Hours: {logic.average_sleep_hours(students):.2f}"))
    statistics_button.pack(side=tk.LEFT, padx=5)

    # STACK ALL FRAMES (ADD THIS AT END OF setup_frames)
    for frame in (
        welcome_frame,
        profile_frame,
        returning_frame,
        main_frame,
        academic_frame,
        mental_health_frame,
        mentor_frame,
        discussion_frame,
        support_frame,
        statistics_frame
    ):
        frame.grid(row=0, column=0, sticky="nsew")

def setup_menu():

    global menu_bar

    menu_bar = tk.Menu(window)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Profile", command=open_profile_form)
    file_menu.add_command(label="Exit", command=exit_program)

    resource_menu = tk.Menu(menu_bar, tearoff=0)
    resource_menu.add_command(label="Academic Resources", command=open_academic_resources)
    resource_menu.add_command(label="Mental Health Resources", command=open_mental_health_resources)

    connection_menu = tk.Menu(menu_bar, tearoff=0)
    connection_menu.add_command(label="Mentor Program", command=open_mentor_program)
    connection_menu.add_command(label="Ask AI", command=open_discussion_groups)
    connection_menu.add_command(label="Support Groups", command=open_support_groups)

    statistics_menu = tk.Menu(menu_bar, tearoff=0)
    statistics_menu.add_command(label="View Statistics", command=open_statistics)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Resources", menu=resource_menu)
    menu_bar.add_cascade(label="Connections", menu=connection_menu)
    menu_bar.add_cascade(label="Statistics", menu=statistics_menu)
    
# ---------- MAIN ----------

def main():
    global window
    global students

    students = logic.read_from_file()  # Load existing profiles

    window = tk.Tk()
    window.configure(bg="#cfe8ff")
    window.title("Neurodivergent Education Resource Database! - N.E.R.D.")
    window.geometry("800x400")

    setup_frames()
    show_frame(welcome_frame)  # Start on welcome screen
    setup_menu()

    # Start on welcome screen
    show_frame(welcome_frame)

    window.mainloop()

if __name__ == "__main__":
    main()