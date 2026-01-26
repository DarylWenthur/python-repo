import random

expectancy = ""
message = ""
countdown = 10

name = input(("Hello, What is your name? "))
while len(name) < 2:
    print("Name must be at least 2 characters long.")
    name = input(("Hello, What is your name? "))

print("Hello, " + name + "!")
age = int(input("How old are you? "))
while age == 0:
    age = int(input("How old are you? "))

print(name + " is " + str(age) + ".")
if age <= 50:
    print("Not bad. You are still young!!!")
    expectancy = random.randint(35, 75)
    print("You have " + str(expectancy) + " years to live!!!")
elif age <= 60:
    print("Ha" * 4 + " you're old!!!")
    expectancy = random.randint(25, 50)
    print("You have " + str(expectancy) + " years to live!!!")
elif age < 70:
    print("Suprised you made it this far.")
    print("Congratulations, Senior Citizen!!!")
    expectancy = random.randint(25, 40)
    print("You have " + str(expectancy) + " years to live!!!")
elif age >= 70:
    print("You should be dead.")
    expectancy = random.randint(0, 30)
    print("You have " + str(expectancy) + " years to live!!!")
    if expectancy == 0:
        for countdown in range(10, 0, -1):
            print(str(countdown) + " seconds left to live.")
        print("I'm Sorry. Goodbye!!")
    elif expectancy <= 10:
        message = "I'm sorry."
    elif expectancy <= 20:
        message = "Ok. Not Bad"
    else:
        message = "Hurray!! You still have some years left!!"
    print(message)

    # This is a note. It's mean to laugh at someone's age.