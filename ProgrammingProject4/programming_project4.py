## Daveed A. Sumpter 30 September 2024   Lab 4

# This program calculates the total amount of money a user has spent the last five times they've eaten at a restaurant, and then it displays the average cost per meal. This program uses a loop to accomplish this.

# Initialize Variables
mealNumber = 1
mealCost = 0
totalCost = 0
averageCost = 0

# Create a loop to calculate the mealCost for each mealNumber [mealNumber1, mealNumber2, mealNumber3, mealNumber4, mealNumber5]:
for x in (1, 2, 3, 4, 5):
    mealCost = int(input("Please enter the cost of meal " + str(x) + "..."))
    totalCost = totalCost + mealCost

# Display the average cost per meal.
averageCost = totalCost / 5

# Create at least 3 custom messages based on whether the user spends less than $10, less than $15, or more than $20 on average per meal.
if averageCost <= 10:
    print("Your average meal cost for the last five times that you ate at a restaurant was " + str(averageCost) + "." " You are economical in terms of being very mindful of your spending.")
elif averageCost > 10 and averageCost <= 15:
    print("Your average meal cost for the last five times that you ate at a restaurant was " + str(averageCost) + "." " You have a moderately expensive taste in terms of eating out.")
elif averageCost > 15:
    print("Your average meal cost for the last five times that you ate at a restaurant was " + str(averageCost) + "." " You have quite expensive taste in terms of eating out!")








