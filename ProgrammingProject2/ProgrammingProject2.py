#Daveed A. Sumpter Lab 2 2024-09-16

#Goal: To calculate the area of two rectangles and see which is larger.

#Initialize variables
#I need to store the user's name
#I need to store the length and width of Rectangle 1
#I need to store the length and width of Rectangle 2
#I need to store the area of Rectangle 1
#I need to store the area of Rectangle 2

studentName = ""
lengthRectangle1 = 0
widthRectangle1 = 0
lengthRectangle2 = 0
widthRectangle2 = 0
areaRectangle1 = 0
areaRectangle2 = 0

# get name
studentName = input("Please enter your name: ")

#greet student
print("Welcome " + studentName + "." + " This program compares the areas of two rectangles and determines the larger rectangle.")

#get length and width of rectangle 1 and rectangle 2
lengthRectangle1 = int(input("Please enter the length of Rectangle 1: "))

widthRectangle1 = int(input("Please enter the width of Rectangle 1: "))

lengthRectangle2 = int(input("Please enter the length of Rectangle 2: "))

widthRectangle2 = int(input("Please enter the width of Rectangle 2: "))

#Calculate area of rectangles 1 & 2
areaRectangle1 = lengthRectangle1 * widthRectangle1

areaRectangle2 = lengthRectangle2 * widthRectangle2

#Print areas of rectangles 1 & 2
print("The area of Rectangle 1 is " + str(areaRectangle1))
print("The area of Rectangle 2 is " + str(areaRectangle2))

#Compare the areas of rectangle 1 & rectangle 2 to determine which is larger.
if (areaRectangle1 > areaRectangle2):
    print(studentName + ", the area of Rectangle 1 is larger than the area of Rectangle 2.")

if (areaRectangle1 < areaRectangle2):
    print(studentName + ", the area of Rectangle 2 is larger than the area of Rectangle 1.")    

if (areaRectangle1 == areaRectangle2):
    print(studentName + ", the area of Rectangle 1 is the same as the area of Rectangle 2.")   

else: 
    print(studentName + ", we are unable to determine which rectangle is larger.")