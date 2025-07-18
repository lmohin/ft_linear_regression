from pandas import read_csv
import csv
import matplotlib.pyplot as plt

def standardizeDatas(df):
    newDf = df.assign(
        km = (df['km'] - df['km'].mean()) / df['km'].std(),
        price = (df['price'] - df['price'].mean()) / df['price'].std()
    )
    return newDf

def getRealValues(df, a, b):
    muX = df['km'].mean()
    sigmaX = df['km'].std()
    muY = df['price'].mean()
    sigmaY = df['price'].std()
    realA = a * sigmaY / sigmaX
    realB = b * sigmaY + muY - a * sigmaY / sigmaX * muX
    return (realA, realB)

def linear_regretion():
    df = read_csv('data.csv')
    standardDf = standardizeDatas(df)
    plt.scatter(df['km'], df['price'])
    a = 0
    b = 0
    for i in range(1000):
        def aDescent(row):
            return ((row['km'] * a + b - row['price']) * row['km'])
        def bDescent(row):
            return ((row['km'] * a + b - row['price']))
        nextA = standardDf.apply(aDescent, axis=1).sum()
        nextA = (nextA / df.shape[0]) * 0.01
        nextB = standardDf.apply(bDescent, axis=1).sum()
        nextB = (nextB / df.shape[0]) * 0.01
        a -= nextA
        b -= nextB
    realA, realB = getRealValues(df, a, b)
    with open("values.csv", "w", newline='') as valuesFile:
        writer = csv.writer(valuesFile)
        writer.writerow(['a', 'b'])
        writer.writerow([realA, realB])
    plt.plot([0, 250000], [realA*0 + realB, realA*250000 + realB], 'r-', lw=2)
    plt.show()
linear_regretion()
