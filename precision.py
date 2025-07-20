import csv
from prediction import getValues
from pandas import read_csv

def calculate_mean_diff(df):
    mu = df['price'].mean()
    def squared_diff(row):
        return((row['price'] - mu) ** 2)
    return (df.apply(squared_diff, axis=1).sum())

def calculate_precision():
    a,b = getValues()
    def squared_diff(row):
        return ((row['km'] * a + b - row['price']) ** 2)
    try:
        df = read_csv('data.csv')
    except:
        print("Error: can not read data.csv")
        return
    d = df.apply(squared_diff, axis=1).sum()
    c = calculate_mean_diff(df)
    print(1 - d / c)

if __name__ == "__main__":
    calculate_precision()
