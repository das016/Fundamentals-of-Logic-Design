# Daveed A. Sumpter 17 November 2024
# Programming Project 9
# Objective: To design a program that has two parallel 1D arrays:
# 1. a String array named people that is initialized with the names of ten people.
# 2. a String array named birthdays is initialized with those people's birthdays.
# The program should allow the user to enter a person's name (or part of a person's name), search for that person in the people array,
#and If the person is found, it should get that person’s birthday and display it on the screen with a fun message. 
#If the person is not found, the program should display a message indicating so.

# I have created a string array named people that is initialized with the names of ten people.
people=['Jason', 'Marco', 'Libertad', 'Mila', 'Lupe', 'Daveed', 'Chris', 'Zack', 'John', 'Jake']

# I have created another string array named birthdays, which is initialized with those people's birthdays.
birthdays=['07/13/1992', '09/22/1993', '05/22/1985', '06/22/1961', '07/31/1954', '09/22/1987', '09/23/1987', '04/30/1988', '03/14/1950', '02/14/1980']

# Get input from user
personName=input("Please enter the name of the person that you would like to search for: ")

# Check if user input exists in people array.
if personName in people:
    # Get the index of the matching name in the people array to pass to birthday array.
    index = people.index(personName)
    print(f"{personName}'s birthday is {birthdays[index]}.")
else:
    print(f"{personName} does not exist in the array!")













