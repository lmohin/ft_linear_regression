from prediction import getValues
from pandas import read_csv

def calculateMeanDiffSum(df):
    """Takes a dataframe as parameter, and calculates the sum of each values distance's to the mean value"""

    mu = df['price'].mean()
    def squaredDiff(row):
        return((row['price'] - mu) ** 2)
    return (df.apply(squaredDiff, axis=1).sum())

def calculatePrecision():
    """Calculates the determination coefficient r2 of a prediction model stored in 'values.csv'"""
    a,b = getValues()
    def squaredDiff(row):
        return ((row['km'] * a + b - row['price']) ** 2)
    try:
        df = read_csv('data.csv')
    except:
        print("Error: can not read data.csv")
        return
    residualsSum = df.apply(squaredDiff, axis=1).sum()
    meanDiffSum = calculateMeanDiffSum(df)
    r2 = 1 - residualsSum / meanDiffSum
    print(f"The dertemination coefficient r2 of this modele is {r2}")

if __name__ == "__main__":
    calculatePrecision()
