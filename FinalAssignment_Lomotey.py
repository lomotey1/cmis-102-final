#TODO
# - [X] Finish house cleaning service
# - [X] Implement yard cleaning service
# - [X] Implement senior discount
# - [ ] Fix bug that occurs when doing yard service and house cleaning service together

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

def CalculateDiscount(totalCost):
    SENIOR_AGE = 65
    SENIOR_DISCOUNT = 15 #in percentage

    # check if user is a senior; if so, apply discount
    userAge = eval(input("What is your age? "))

    try:
        if userAge >= SENIOR_AGE:
            print("You qualify for our senior discount!")
            #return discounted price
            return totalCost * ((100 - SENIOR_DISCOUNT) /100)
        else:
            #return unmodified price
            return totalCost
    except:
        print("Invalid input.")
        CalculateDiscount(totalCost)

def PerformChosenService(userChoice):

    HOUSE_SERVICE = 1
    YARD_SERVICE = 2

    if userChoice == HOUSE_SERVICE:
        return HouseCleaningService()
    elif userChoice == YARD_SERVICE:
        #to be implemented
        return YardCleaningService()

def GetHouseServiceCost(houseSize: int, cleanType: int):
    
    # constants for service rates
    SMALL_ROOM_RATE = 100
    MEDIUM_ROOM_RATE = 90
    LARGE_ROOM_RATE = 80

    if houseSize <= 2:
        costPerRoom = SMALL_ROOM_RATE
        print("You will be billed at the small house cleaning rate due to having 2 or less bedrooms.")
    elif 3 <= houseSize <= 4:
        costPerRoom = MEDIUM_ROOM_RATE
        print("You will be billed at the medium house cleaning rate due to having 3 or 4 bedrooms.")
    elif houseSize > 4:
        costPerRoom = LARGE_ROOM_RATE
        print("You will be billed at the large house cleaning rate due to having 5+ bedrooms.")

    
    cleaningCost = 1 if cleanType == 1 else 1.125 #calculate in-depth cleaning ratio

    #print( "Current subtotal: ${:.2f}".format(houseSize * costPerRoom * cleaningCost)) #returns a price-formatted string
    return houseSize * costPerRoom * cleaningCost #return cost for services

# The house cleaning service. Returns the cost for services performed.
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

    serviceCost = GetHouseServiceCost(houseSize, cleanType)   
    return (serviceCost)

def GetMowingCost(length, width):
    COST_PER_SQUARE_FOOT = 2 #in dollars
    
    yardArea = length * width

    mowingCost = (yardArea * COST_PER_SQUARE_FOOT)
    print("Your mowing cost is ${:.2f}".format(mowingCost))
    return mowingCost

def GetEdgingCost(length, width):
    COST_PER_FOOT = 1 #in dollars

    yardPerimeter = (length + width) * 2

    edgingCost = (yardPerimeter * COST_PER_FOOT)
    print("Your edging cost is ${:.2f}".format(edgingCost) )
    return edgingCost

def GetPruningCost(shrubs):
    COST_PER_SHRUB = 10

    pruningCost = shrubs * COST_PER_SHRUB

    print("Your pruning cost is ${:.2f}".format(pruningCost))
    return pruningCost

def YardCleaningService():
    serviceCost = 0
    yardLength = 0
    yardWidth = 0
    
    while True:
        selection = eval(input("1. Mowing\n2. Edging\n3. Shrub Pruning\n0. Finish\n"))

        try:
            if selection == 0:
                return serviceCost #finishes service with any current subtotal
            elif (selection == 1 or selection == 2) and (yardLength + yardWidth == 0):
                yardLength = eval(input("Please enter your yard's length, in feet: "))
                yardWidth = eval(input("Pleasse enter your yard's width, in feet: "))
            if selection == 1:
                serviceCost += GetMowingCost(yardLength, yardWidth)
                continue
            elif selection == 2:
                serviceCost += GetEdgingCost(yardLength, yardWidth)
                continue
            elif selection == 3:
                yardShrubs = eval(input("Please enter the number of shrubs you have: "))
                serviceCost += GetPruningCost(yardShrubs)
                continue
            else:
                print("Please enter a valid selection.")
                continue
        except:
            print("Invalid input, please try again.")
            continue


    return serviceCost
def GetContinueStatus():
    willContinue = eval(input("Do you want another service? Enter 1 for yes or 2 for no: "))
    try:
        if willContinue == 1:
            return True
        elif willContinue == 2:
            return False
        else:
            print("Invalid input. Please try again.")
            GetContinueStatus()
    except:
        print("Invalid input. Please try again.")
        GetContinueStatus()

def main(): 
    #variables
    subtotal = 0

    Welcome()    
    subtotal = ServiceLoop(subtotal)

    totalCost = CalculateDiscount(subtotal)
    Goodbye(totalCost)

def ServiceLoop(totalCost):
        userChoice = GetChosenService()
        #print (userChoice)
        totalCost += PerformChosenService(userChoice)
        print( "Current subtotal: ${:.2f}".format(totalCost)) #prints subtotal
        # Prompts user to continue and calls the ServiceLoop function recersively if chosen.
        if GetContinueStatus():
            ServiceLoop(totalCost)
        else:
            return totalCost

# Called when the program is ready to exit. Shows the user their total cost and exits the program.            
def Goodbye(totalCost):
    print("Your total price today is ${:.2f}".format(totalCost), ".", sep="")
    print("Thank you for using our services.")
    exit()
main()