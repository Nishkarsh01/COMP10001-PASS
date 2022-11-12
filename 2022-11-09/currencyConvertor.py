# CURRENCY COVERSION
# USD TO CAD
# USD TO INR
# USD TO EUR


# INITIALIZE user choice
userChoice=""


# if the user choice was number 2 we use this code
while(userChoice!="q"):
    #GET AMOUNT TO CONVERT FROM USER
    userUsdInput = int(input("Please enter amount you want to convert: "))
    
    print("Convert USD to CAD: 1")
    print("Convert USD to INR: 2")
    print("Convert USD to EUR: 3")
    print("quit the program: q")
    
    #ASSUME user inputs a valid string value
    userChoice=input("Please Enter your choice: ")

    if userChoice == "2":
        inr = 81.33
        usdToInr = userUsdInput * inr
        print("Your INR value is= " + str(usdToInr))
    elif(userChoice == "1"):
        cad= 1.26
        usdToCad= userUsdInput * cad
        print("Your CAD value is= " + str(usdToCad))
    elif(userChoice == "3"):
        eur=1
        usdToEur= userUsdInput * eur
        print("Your EUR value is= " + str(usdToEur))
    elif(userChoice=="q"):
        print("End the program...")
    