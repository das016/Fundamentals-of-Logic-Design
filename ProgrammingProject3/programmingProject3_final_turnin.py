# Daveed A. Sumpter
# 23-09-24
# Programming Project 3

#Initialize variables
birthYear = 0
studentName = ""
### This program determines which generation a user belongs to based on his or her birth year.

#GET studentName
studentName = input("Please enter your name... ")

#greet student
print("Welcome" + " " + studentName + "." + " This program determines which generation you belong to based on your birth year.")

#GET birthYear
birthYear = int(input("Please enter your birth year..."))


# The Silent Generation: Born up to 1945
if birthYear <= 1945:
    print ("Congrats " + studentName + "," " you belong to the Silent Generation since you were born before 1946.")

# The Baby Boomers: Born 1946-1964
elif birthYear > 1945 and birthYear <= 1964:
    print ("Congrats " + studentName + "," " you belong to the Baby Boomers Generation since you were born between 1946 and 1964.")

# Generation X: Born 1965-1980
elif birthYear > 1964 and birthYear <= 1980:
    print ("Congratulations " + studentName + "," + " you belong to Generation X since you were born between 1965 and 1980.")

    # Xennials: Born 1975-1983
    if birthYear > 1974 and birthYear <= 1983:
        print ("Congratulations " + studentName + "," + " you also belong to Xennials since you were born between 1975 and 1983.")

# Millenials: Born 1981-1996
elif birthYear >= 1981 and birthYear < 1997:
    print ("Congratulations " + studentName + "," + " you belong to Millennials since you were born between 1981 and 1996.")

    # Xennials: Born 1975-1983
    if birthYear >= 1975 and birthYear < 1984:
        print ("Congratulations " + studentName + "," + " you also belong to Xennials since you were born between 1975 and 1983.")

    # Zillenials: Born 1993-1998
    if birthYear >= 1993 and birthYear < 1999:
        print ("Congratulations " + studentName + "," + " you also belong to Zillenials since you were born between 1993 and 1998.")

# Generation Z: Born 1997-2012
elif birthYear > 1996 and birthYear < 2013:
    print ("Congratulations " + studentName + "," + " you belong to Generation Z since you were born between 1997 and 2012.")

    # Zillenials: Born 1993-1998
    if birthYear >= 1993 and birthYear < 1999:
        print ("Congratulations " + studentName + "," + " you also belong to Zillenials since you were born between 1993 and 1998.")

# Generation Alpha: Born 2012-2025
elif birthYear > 2011 and birthYear < 2026:
    print ("Congratulations " + studentName + "," + " you belong to Generation Alpha since you were born between 2012 and 2025.")

