# Daveed A. Sumpter
# 2024-09-09
# LAB 1

# initial variables
studentName = ""
studentPoints = 0
pointsNeeded = 0
A_points = 900

# get name
studentName = input("Please enter your name...")

# greet student
print("Hello " + studentName)

# get points
studentPoints = int(input("Please enter the points you have earned, so far..."))

# calculate how many points needed for an A
pointsNeeded = A_points - studentPoints

# greet the user, display points earned so far
print(studentName + ", so far, you have earned " + str(studentPoints) + " points.")

# tell the user how many more points they need for an A
print("You need " + str(pointsNeeded) + " more points to earn an A.")
      
