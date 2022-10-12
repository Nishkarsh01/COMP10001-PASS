# GET two numbers from the user
# ASSUME that the user inputs valid value ["0", 1", "2", "3", ......]
number1 = int(input("Please enter the first number: "))

#ASSUME that the user inputs a valid value ["0", "1", "2", "3", ...] 
#ASSUME when the choice is division user does not input 0
number2=int(input("Please enter the second number: "))

# CREATE user menu
print("-----------------------------------MENU-----------------------------------")
print("type a to add these numbers")
print("type b to subtract these numbers")
print("type c to multiply these numbers")
print("type d to divide these numbers")
print("type e to modulo divide these numbers")
print("type q to quit the program")
print("--------------------------------------------------------------------------")

#ASSUME the user inputs a valid value ['a', 'b', 'c', 'd', 'e', 'q']
userChoice=input("Enter the choice: ")

# GET input from the user
def get_input():
        global number1
        global number2
        global userChoice

        number1 = int(input("Please enter the first number: "))
        number2=int(input("Please enter the second number: "))
        userChoice=input("Enter the choice: ")
 


while(userChoice!="q"):

    # ADD numbers
    if(userChoice=="a"):
        userAnswer=number1+number2
        print("The Answer is: "+str(userAnswer))
        get_input()

    # SUBTRACT numbers
    elif(userChoice=="b"):
        userAnswer=number1-number2
        print("The Answer is: "+str(userAnswer))
        get_input()

    #MULTIPLY numbers
    elif(userChoice=="c"):
        userAnswer=number1*number2
        print("The Answer is: "+str(userAnswer))
        get_input()

    #DIVIDE numbers
    elif(userChoice=="d"):
        userAnswer=number1/number2
        print("The Answer is: "+str(userAnswer))
        get_input()

    #MODULUS Division    
    elif(userChoice=="e"):
        userAnswer=number1%number2
        print("The answer is: "+str(userAnswer))
        get_input()

    #QUIT The program
    else:
        print("invalid choice!")
        get_input()

# END the program
# Display end message
print("Ending the program")
