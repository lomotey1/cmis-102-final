#TODO
# - [ ] Finish house cleaning service
# - [ ] Implement yard cleaning service
# - [ ] Implement senior discount

HOUSE_SERVICE = 1
YARD_SERVICE = 2

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

def CalculateDiscount():
    # check if user is a senior; if so, apply 15% discount
    return 0

def PerformChosenService(userChoice):
    if userChoice == HOUSE_SERVICE:
        return HouseCleaningService()
    elif userChoice == YARD_SERVICE:
        #to be implemented
        return YardCleaningService()




def HouseCleaningService():
    serviceCost = 0
    while True: 
        houseSize = input("Please enter the number of bedrooms in your house: ")

        # validate house size (at least one room)
        try: 
            houseSize = int(houseSize)
            if houseSize <= 0:
                print("Invalid input.")
                continue
            else:       
                break    
        except:
            print("Invalid input.")
            continue
    while True: 
        print("Do you want a quick clean (sweep/vacuum, dust) or an in-depth cleaning (mopping, surface disinfecting, bathroom cleaning)?")
        cleanType = input("Press 1 for quick or 2 for in-depth: ")
        try:
            cleanType = int(cleanType)
            if cleanType < 1 or cleanType > 2:
                print("Invalid input.")
                continue
            break
        except:
            print("Invalid input.")
            continue
    return (houseSize + cleanType)


def main(): 
    #variables
    totalCost = 0
    userChoice = 0

    Welcome()

    while True:
        userChoice = GetChosenService()
        #print (userChoice)
        totalCost += PerformChosenService(userChoice)
        print(totalCost)

    #if else for service

main()