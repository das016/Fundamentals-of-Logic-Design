# Daveed A. Sumpter  10 November 2024  Programming Project # 8
# Objective: To clean up the program below to make it more readable.

#RockPaperScissors
#logic from Starting Out with Programming Logic and Design by Tony Gaddis
#Written in Python and modified by Veronica Noone for academic purposes

#include random mod so we can have the computer make a choice
import random

#The getNumber module gets the users choice
def getNumber():
    # input validation loop starts here
    while True:
        # change input prompt message to instruct user to supply either rock, paper or scissors
        # call lower() function to automatically convert input received to lowercase to improve usability
        inputAnswer=input("\nEnter 'rock' for rock, 'paper' for paper, 'scissors' for scissors: ").lower()

        # If the input value is equal to 'rock', the program will return the integer 1 to represent rock.
        if inputAnswer == 'rock':
            return 1
        # Else if the input value is equal to 'paper', the program will return the integer 2 to represent paper.
        elif inputAnswer == 'paper':
            return 2
        # Else if the input value is equal to 'scissors', the program will return the integer 3 to represent scissors.
        elif inputAnswer == 'scissors':
            return 3
        # Else: The program will display an error message to the user, prompting the user to enter either 'rock', 'paper' or 'scissors' and terminate.
        else:
            print("Error! Exiting program due to invalid input: Input must be either 'rock', 'paper' or 'scissors!'")
            # Exit program by calling the exit() module
            exit(1)

    #End Module

#The showWinner module display who wins -- calls whoWon function
def showWinner(computer, player):
    print('\nComputer chose', whichChoice(computer))
    print('Player chose', whichChoice(player), '\n')
    if computer == player:
        print("Player made same choice. Play again.")
    else:
        which = whoWon(computer, player)
        if which == 1:
            print("Computer wins.")
        else:
            if which == 2:
                print("Player wins.")
            else:
                print("No winner.")
            #end If
        #end If
    #end If
#End Module
                
#The whichChoice function displays choice
def whichChoice(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    else:
        return "scissors"
    #end If
#End Function
 
#The whoWon function selects winner
def whoWon(computer, player):
# 1 = rock, 2 = paper, 3 = scissors
# rock smashes scissors
# scissors cuts paper
# paper wraps rock
# both choose same no winner
    if computer == player:
        return 0
    #end If
    
# test computer chose rock
    if computer == 1:
        if player == 2:
            return 2 #paper wraps rock
        elif player == 3:
            return 1 #rock smashes scissors
        #end If
    #end If
        
# test computer chose paper
    if computer == 2:
        if player == 1:
            return 1 #paper wraps rock
        elif player == 3:
            return 2 #scissors cuts paper
        #end If
    #end If
# test computer chose scissors
    if computer == 3:
        if player == 1:
            return 2 #rock smashes scissors
        elif player == 2:
            return 1 #scissors cuts paper
        #end If
    #end If
        
    return 0
#End Function



# main module
def main():
    # Get computer number
    computer = random.randint(1, 3)
    #print(computer) #uncomment for debugging
    # Get player number
    playerNum=getNumber()
    # Show winner
    showWinner(computer, playerNum)
#End Module

print("-------------------------------------------")
print("Welcome to Rock-Paper-Scissors with Python!")
print("-------------------------------------------")

again="y"
while again=="y":
    main()
    again=input('\nplay again? y or n ')
#end while

print("\n-------------------------------------------")
x=input("Thanks for playing! Click enter to exit")
