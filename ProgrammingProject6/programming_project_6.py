# Daveed A. Sumpter \ # 27 October 2024 \ # Programming Project 6
# Objective: To create a program with two Modules.  SuBMIt your own Module and it must do another function besides adding.
# Add comments to explain why I modularized my Modules the way I did.
# 25 Points Extra Credit: Create a program with 5 Modules total.

# Declare and initialize variables for:
#  Body Mass Index (BMI), which is the relationship between weight in kilograms (kg)/(height in meters squared).
#  Body Weight,
#  Height,
#  user's name.
BMI = 0
height = 0
weight = 0
userName = ""

def main():
    # Call showIntro Module to explain the purpose of the program to the user.
    showIntro()
    
    # Call getWeightInput module to get weight value from the user.
    weight = getWeightInput()

    # Call getHeightInput module to get height value from the user.
    height = getHeightInput()

    # Convert the user's body weight from pounds to kilograms by calling a module called convertWeight and passing it the user's weight in pounds.
    weight = convertWeight(weight)
    print("Your weight in kilograms is: " + str(weight))

    # Convert the user's height from feet to inches to centimeters to meters.
    height = convertHeight(height)
    print("Your height in meters is: " + str(height))

    # Calculate Body Mass Index (BMI) = kilograms/(meters)^2
    BMI = calculateBMI(height, weight)
    
    # Display BMI to the user
    print("Your Body Mass Index (BMI) is: " + str(BMI))


def showIntro():
    # Display the purpose of this module.
    print("This program converts a user's body weight in pounds to kilograms. For your reference, the formula is 1 kilogram = 2.2 pounds.")

def getWeightInput():
    # Get the user's body weight in pounds by asking the user to input their weight in pounds.
    userWeight = int(input("Welcome, please type your body weight in pounds: "))
    print("Your body weight in pounds is: " + str(userWeight))

    return userWeight

def getHeightInput():
    # Get the user's height in feet by asking the user to input their height in feet.
    userHeight = float(input("Please type your height in feet: "))
    print("Your height in feet is: " + str(userHeight))

    return userHeight
    
# Convert pounds to kilograms by calling a module named poundsToKilograms().
def convertWeight(weight: int):
    weightInKilograms = weight / 2.2

    return weightInKilograms

# This module converts the user's height in feet to inches to centimeters, and then converts height in centimeters to meters.
def convertHeight(height: float):
    heightInInches = height * 12
    heightInCentimeters = heightInInches * 2.54
    heightInMeters = heightInCentimeters / 100

    return heightInMeters

# 
def calculateBMI(height: float, weight: float):
    BMI = weight/(height**2)
    
    return BMI

# Calling the main function
if __name__ == "__main__":
    main()