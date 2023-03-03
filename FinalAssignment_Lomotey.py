

# Welcome function
def Welcome():
    print("CMIS 102 Final Assignment")

# Shows user the provided servies and prompts for input. Returns an int based on choice.
def GetChosenService():
    while True:
        print("1: House Cleaning Service")
        print("2: Yard Services")
        print("0: Exit")

        try:
            userChoice = eval(input("Please enter your choice: "))
        except:
            print("invalid choice\n")
            continue

        if userChoice == 1 or userChoice == 2:
            return userChoice
        elif userChoice == 0:
            print("Thank you for using this service.")
            exit()
        else:
            continue



def main(): 
    #variables
    totalCost = 0
    userChoice = 0

    Welcome()
    userChoice = GetChosenService()
    print (userChoice)

    #if else for service

main()