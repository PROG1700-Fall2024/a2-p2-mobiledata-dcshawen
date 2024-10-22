"""
    Author: Dan Shaw
    Title: Mobile Data Plans
    Desc: Calculates the cost of a mobile data plan based on the amount of data used
"""

from DanMath import Validation

# Sets constants
TIER_THRESHOLDS = [200, 500, 1000]
TIER_TYPE = [0, 1, 1, 0] # 0 -> Flat Rate, 1 -> Tiered Rate
TIER_RATES = [20, 0.105, 0.110, 118]

def main():
    # Outputs greeting to user
    greeting = "| MOBILE DATA PLAN CALCULATOR |"
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))

    # Get amount of data used from user and validate that it's a proper float value
    while (dataUsed := Validation.validateInt(input("Enter the amount of data used (MB).\n> "))) == None:
        print("You have entered an invalid input. Please enter a whole number.")
    
    totalCost = getCost(dataUsed, getTier(dataUsed))
    print("Total charge is ${0:.2f}".format(totalCost))

def getCost(dataUsed, tier):
    if TIER_TYPE[tier] == 0:
        return TIER_RATES[tier]
    else:
        return dataUsed * TIER_RATES[tier]

def getTier(dataUsed):
    if dataUsed <= TIER_THRESHOLDS[0]:
        return 0
    elif dataUsed <= TIER_THRESHOLDS[1]:
        return 1
    elif dataUsed <= TIER_THRESHOLDS[2]:
        return 2
    else:
        return 3

if __name__ == "__main__":
    main()