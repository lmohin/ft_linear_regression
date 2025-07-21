from pandas import read_csv
from prediction import getValues
import csv

def standardizeDatas(df):
    """Standardize datas of a dataframe

    Dataframe must have two columns : 'km' and 'price'"""
    newDf = df.assign(
        km = (df['km'] - df['km'].mean()) / df['km'].std(),
        price = (df['price'] - df['price'].mean()) / df['price'].std()
    )
    return newDf

def getRealValues(df, a, b):
    """"Converts a and b so their value matches the non standardized datas"""
    muX = df['km'].mean()
    sigmaX = df['km'].std()
    muY = df['price'].mean()
    sigmaY = df['price'].std()
    realA = a * sigmaY / sigmaX
    realB = b * sigmaY + muY - a * sigmaY / sigmaX * muX
    return (realA, realB)

def standardizeValues(df, a, b):
    """Converts a and b so their value matches the standardized datas"""
    muX = df['km'].mean()
    sigmaX = df['km'].std()
    muY = df['price'].mean()
    sigmaY = df['price'].std()
    newA = a * sigmaX / sigmaY
    newB = (b - muY) / sigmaY + newA / sigmaX * muX
    return (newA, newB)

def writeResults(a, b):
    """Stores a and b on 'values.csv'"""
    try:
        with open("values.csv", "w", newline='') as valuesFile:
            writer = csv.writer(valuesFile)
            writer.writerow(['a', 'b'])
            writer.writerow([a, b])
            print("Results stored in \"values.csv\"")
    except:
        print("Error: can not write results on \"values.csv\"")

def linear_regretion(iterations, delta):
    """Using a gradient descent algorithm, find a linear relationship between the datas stored in 'data.csv'

    iterations design the number of loop required, and delta the learning rate of the algorithm"""
    try:
        df = read_csv('data.csv')
    except:
        print("Error: can not read \"data.csv\"")
        return
    standardDf = standardizeDatas(df)
    a,b = getValues()
    a,b = standardizeValues(df, a, b)
    for i in range (iterations):
        def aDescent(row):
            return ((row['km'] * a + b - row['price']) * row['km'])
        def bDescent(row):
            return ((row['km'] * a + b - row['price']))
        nextA = standardDf.apply(aDescent, axis=1).sum()
        nextA = (nextA / df.shape[0]) * delta
        nextB = standardDf.apply(bDescent, axis=1).sum()
        nextB = (nextB / df.shape[0]) * delta
        a -= nextA
        b -= nextB
    realA, realB = getRealValues(df, a, b)
    print(f"Linear regression successfully completed!\nLinear relationship found: y = {realA}x + {realB}")
    writeResults(realA, realB)

if __name__ == '__main__':    
    linear_regretion(100, 1)
