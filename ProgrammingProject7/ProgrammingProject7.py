# Daveed A. Sumpter  Programming Project 7   3 November 2024

# The objective of this project is to design a program has two custom functions:
# 1. One called tbspToCups that accepts tbspsEntered as an argument and
# returns how many cups in however many tablespoons were passed to it.

# 2. One called cupsToTbsps that accepts cupsEntered as an argument and returns
# how many tablespoons in however many cups were passed to it.
# Your program should ask the user which conversion they want to perform and then accept
# their input before displaying the function's result.
# Your program should also ask the user if they want to convert again after their initial conversion---loop.

# variable names
tableSpoons=0.0 # Global Variable
cups=0.0 # Global Variable
select=""
playAgain=""

# 16 tableSpoons=1Cup Float Variable        8 tablespoons=0.5Cup
# This function converts tablespoons to cups.
def tableSpoons_To_Cups(tableSpoons):
    cups = float(tableSpoons)/ 16
    return cups

# This function converts cups to tablespoons.
def cups_To_TableSpoons(cups):
    tableSpoons = float(cups) * 16
    return(tableSpoons)

# This function defines my main module with a global cups variable and a global tableSpoons variable.
def main():
    global cups
    global tableSpoons
    
    select = "w"
    playAgain = "Y"

    # This is the menu loop. 
    while (select != "X" and playAgain == "Y"):
        print("======================================")
        print("")
        print("MENU:\n")
        print("     1) Convert tableSpoons to cups")
        print("     2) Convert cups to tableSpoons")
        print("     X) EXIT")
        select = input("Please make a selection...")
       # If an invalid selection is made by the user, instruct user to make a valid selection: 1, 2, or X.
        if (select != "1" and select != "2" and select != "X"):
                print("Invalid selection. Please make a valid selection: 1, 2, or X.")
        # If user provides "1", get number of tableSpoons from user and call the function: tableSpoons_To_Cups(tableSpoons)
        if select == "1":
            tableSpoons = input("Please enter the number of tablespoons that you would like to convert to cups: ")
            cups = tableSpoons_To_Cups(tableSpoons)
            print("There are " + str(cups) + " cups in " + str(tableSpoons) + " tablespoons")
            playAgain = input("Would you like to play again? Please enter Y or N: ")
        # If user provides "2", get number of cups from user and call the function: cups_To_TableSpoons(cups)   
        if select == "2":
            cups = input("Please enter the number of cups: ")
            tableSpoons = cups_To_TableSpoons(cups)
            print("There are " + str(tableSpoons) + " tablespoons in " + str(cups) + " cups")
        # Ask the user if they would like to play again. Only a value of "Y" will allow user to continue playing.
            playAgain = input("Would you like to play again? Please enter Y or N: ")
        # If user enters "X", the screen will show "Thank you for playing."
        if select == "X":
            print("Thank you for playing.")

main()