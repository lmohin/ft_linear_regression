import csv

def getValues():
    try:
        with open("values.csv") as file:
            fileIterator = csv.reader(file)
            next(fileIterator)
            firstLine = next(fileIterator)
            return (float(firstLine[0]), float(firstLine[1]))
    except:
        print("Can't read values, setting them to base values")
        return (0,0)

def calculate(a, b, x):
    return (a * x + b)

def predict():
    values = getValues()
    try:
        weight = float(input("Please enter the mileage of the car you want to predict the price of:\n"))
    except:
        print("Please enter a correct float value")
        return
    price = calculate(values[0], values[1], weight)
    print(f"The estimated price of the car is {price}")

if __name__ == "__main__":
    predict()
