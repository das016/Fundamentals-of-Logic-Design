#RockPaperScissors
#logic from Starting Out with Programming Logic and Design by Tony Gaddis
#Written in Python and modified by Veronica Noone for academic purposes

#include random mod so we can have the computer make a choice
import random

#The getNumber module gets the users choice
def getNumber():
    inputAnswer=input("\nEnter 1 for rock, 2 for paper, 3 for scissors: ")
    return int(inputAnswer)
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
