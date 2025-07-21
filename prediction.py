import csv

def getValues():
    """Returns the values stored in 'values.csv'"""

    try:
        with open("values.csv") as file:
            fileIterator = csv.reader(file)
            next(fileIterator)
            firstLine = next(fileIterator)
            return (float(firstLine[0]), float(firstLine[1]))
    except:
        print("Can't read values, setting them to base values")
        return (0,0)

def affineFunction(a, b, x):
    """Returns the result of the affine function y = ax + b"""
    
    return (a * x + b)

def predict():
    """Prompts the user to enter a mileage, then calculates the estimated price of the car"""
    
    a,b = getValues()
    try:
        weight = float(input("Please enter the mileage of the car you want to predict the price of:\n"))
    except:
        print("Please enter a correct float value")
        return
    price = affineFunction(a, b, weight)
    print(f"The estimated price of the car is {price}")
    if (price < 0):
        print("Why would you buy this garbage car")

if __name__ == "__main__":
    predict()
