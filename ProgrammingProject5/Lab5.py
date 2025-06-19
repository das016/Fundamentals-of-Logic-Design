# Daveed A. Sumpter\ # 2024-10-07   Lab Code 5

# Objective: To create a 'for' statement and a 'while'
# statement that do not result in an infinite loop. 
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    if month in ["December", "January", "February"]:
        print("In " + month + ", it's freezing because it is winter!")
    elif month in ["March", "April", "May"]:
        print("In " + month + ", it's getting warmer because it is spring!")
    elif month in ["June", "July", "August"]:
        print("In " + month + ", it's blazing outside because it is summer!")
    elif month in ["September", "October", "November"]:
        print("In " + month + ", it's cooling down because it is fall!")
    
month = 1  
# While statement
while month <=12:
    if month in [12, 1, 2]:
        print("It's freezing because it is winter!")
    if month in [3, 4, 5]:
        print("It's getting warmer because it is spring!")
    if month in [6, 7, 8]:
        print("It's blazing outside because it is summer!")
    if month in [9, 10, 11]:
        print("It's cooling down because it is fall!")

    month += 1
    # End While Loop