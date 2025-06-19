# Daveed A. Sumpter  10 November 2024  Programming Project # 8
# Objective: To clean up the program below to make it more readable.

#RockPaperScissors
#logic from Starting Out with Programming Logic and Design by Tony Gaddis
#Written in Python and modified by Veronica Noone for academic purposes

#include random mod so we can have the computer make a choice
import random

#The getNumber module gets the users choice
def getNumber():
    inputAnswer=input("\nEnter 'Rock' for rock, 'Paper' for paper, 'Scissors' for scissors: ")
    return str(inputAnswer)
#End Module

#The showWinner module display who wins -- calls whoWon function
def showWinner(computer, player):
    print('\nComputer chose', whichChoice(computer))
    print('Player chose', whichChoice(player), '\n')
    if computer == player:
        print("Player made same choice. Play again.")
    else:
        which = whoWon(computer, player)
        if which == "Rock":
            print("Computer wins.")
        else:
            if which == "Paper":
                print("Player wins.")
            else:
                print("No winner.")
            #end If
        #end If
    #end If
#End Module
                
#The whichChoice function displays choice
def whichChoice(str):
    if str == "Rock":
        return "rock"
    elif str == "Paper":
        return "paper"
    elif str == "Scissors":
        return "scissors"
    #end If
#End Function
 
#The whoWon function selects winner
def whoWon(computer, player):
# "R" = rock, "P" = paper, "S" = scissors
# rock smashes scissors
# scissors cuts paper
# paper wraps rock
# both choose same no winner
    if computer == player:
        return 0
    #end If
    
# test computer chose rock
    if computer == "R":
        if player == "P":
            return "P" #paper wraps rock
        elif player == "S":
            return "R" #rock smashes scissors
        #end If
    #end If
        
# test computer chose paper
    if computer == "P":
        if player == "R":
            return "P" #paper wraps rock
        elif player == "S":
            return "S" #scissors cuts paper
        #end If
    #end If
# test computer chose scissors
    if computer == "S":
        if player == "R":
            return "P" #rock smashes scissors
        elif player == "P":
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
