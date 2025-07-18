import csv
from prediction import getValues
from pandas import read_csv


def calculate_precision():
    a,b = getValues()
    def squared_diff(row):
        return ((row['km'] * a + b - row['price']) ** 2)
    try:
        df = read_csv('data.csv')
    except:
        print("Error: can not read data.csv")
        return
    print(df.apply(squared_diff, axis=1).sum() / 2)
    print(a,b)

if __name__ == "__main__":
    calculate_precision()
