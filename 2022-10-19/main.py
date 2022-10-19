#IMPORT random library
import random

userChoice="";

# RULES
# Rock wins Scissor
# Paper wins Rock
# Scissor wins Paper
# In the event of same occurances, it's a tie. No winner


#Module to ASK for userInput
def get_userInput():
    
    #ASK The user to make a choice
    #DISPLAY user menu
    print("\n")
    print("---------------")
    print("Please enter 1 for rock");
    print("Please enter 2 for paper");
    print("Please enter 3 for scissor");
    print("Please enter q to end the game");
    
    #GET user choice
    #ASSUME the user inputs a valid int value
    global userChoice;
    userChoice = input("Please enter a choice: ");

    #SET random computer choice
    # Computer chooses randomly
    global computerChoice;
    computerChoice=  random.randint(1, 3);
    

    print("------------------")
    print("your choice: "+userChoice +"|\t"+"bot choice: "+str(computerChoice))
    print("------------------")

def check_winner():
    if(userChoice == str(computerChoice)):
        print("It's a tie")
    # ROCK VS PAPER
    elif(userChoice=="1" and  str(computerChoice)=="2"):
        #Display who won the game
        print("Rock vs Paper, Paper wins, Bot wins!")
    # ROCK VS SCISSOR
    elif(userChoice=="1" and str(computerChoice)=="3"):
        #Display who won the game
        print("Rock vs Scissor, Rock wins, Player wins!")
    #PAPER VS ROCK
    elif(userChoice=="2" and  str(computerChoice)=="1"):
        #Display who won the game
        print("Paper vs Rock, Paper wins, Player wins!")
    #PAPER VS SCISSOR
    elif(userChoice=="2" and str(computerChoice)=="3"):
        #Display who won the game
        print("Paper vs Scissor, Scissor wins, Bot wins!")
    #SCISSOR VS ROCK
    elif(userChoice=="3" and str(computerChoice)=="1"):
        #Display who won the game
        print("Scissor Vs Rock, Rock wins, Bot wins!")
    #SCISSOR VS PAPER
    elif(userChoice=="3"  and str(computerChoice)=="2"):
        #Display who won the game
        print("Scissor vs Paper, Scissor wins, Player wins!")





while(userChoice!="q"):

    #GET user choice
    #SET random computer choice
    get_userInput();

    if(userChoice=="q"):
        print("Ending the game...");
        
    elif(userChoice=="1"):
   
        check_winner()
    elif(userChoice=="2"):
    
        check_winner()
    elif(userChoice=="3"):
 
        check_winner()
    else:
        print("Please enter a valid value...")


# Continue playing the game ie repeat the process again unless the user wants to quit the game



