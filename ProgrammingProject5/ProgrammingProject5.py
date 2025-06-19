# Daveed A. Sumpter    7 October 2024    Programming Project 5
# Objective: Write a program with a loop that displays
# the projected semester tuition amount for the next five years.
# The tuition will increase by 3 percent each year for the next five years.

print("\n**************************************************")
print("Welcome to McDaniel College\n")
print("Tuition is $27k/year (broken down into $ " + str(27000/2 ) + " per semester.")
print()
print("NOTICE: There is a tuition increase for 2025 and the next 4 years.")
print("The rate schedule is as follows: \n")

semesterTuition = 27000 / 2
year = 2025
increase = 0
for period in range(0,10) :
    if period == 2 or period == 4 or period == 6 or period == 8:
        increase = float(semesterTuition) * 0.03
        semesterTuition = float(semesterTuition) + float(increase)
        year = year + 1
        print("The increase for year " + str(year) + " = $" + str(increase))
    print("Total cost for semester " + str(period+1) + " (year " + str(year) + "): $" + str(semesterTuition))