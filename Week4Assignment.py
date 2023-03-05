# CMIS 102 Assignment 3
# Author: David Lomotey
# This program calcluates the cost for room cleaning services based on house size and cleaning type.


# Function to calculate the total cleaning cost.
# The base rate is dependent on the room size, at the following rates:
# Small - 2 or less bedrooms - $100 per room
# Medium - 2 to 4 bedrooms - $90 per room
# Large - 5+ bedrooms - $80 per room
# A 12.5% fee is added for an in-depth cleaning, otherwise a quick clean will be done.
# An input value of 1 indicates a quick clean and 2 indicates an in-depth cleaning.

SMALL_ROOM_RATE = 100
MEDIUM_ROOM_RATE = 90
LARGE_ROOM_RATE = 80

def calculateCost(size: int, cleanType: int):
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

    return "${:.2f}".format(houseSize * costPerRoom * cleaningCost) #returns a price-formatted string

# Main program

print("House Cleaning Service")

# loop for retrieving and validating first input
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

# loop for retrieving and validating second input
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

#Rate is calculated by the cost per room (based on house size), with a 12.5% additional fee for a deep clean.
totalCost = calculateCost(houseSize, cleanType)

#Prints total cost, formatted to dollar + cents
print("You will be charged", totalCost, "for the services you have chosen. Have a good day!")