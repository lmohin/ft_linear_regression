from pandas import read_csv
import csv
import matplotlib.pyplot as plt

def standardizeDatas(df):
    newDf = df.assign(
        km = (df['km'] - df['km'].mean()) / df['km'].std(),
        price = (df['price'] - df['price'].mean()) / df['price'].std()
    )
    return newDf


def linear_regretion():
    df = read_csv('data.csv')
    standardDf = standardizeDatas(df)
    print(standardDf)
    mu_x = df['km'].mean()
    sigma_x = df['km'].std()
    mu_y = df['price'].mean()
    sigma_y = df['price'].std() 
    plt.scatter(df['km'], df['price'])
    a = 0
    b = 0
    for i in range(10000):
        def a_min(row):
            return ((row['km'] * a + b - row['price']) * row['km'])
        def b_min(row):
            return ((row['km'] * a + b - row['price']))
        tmp_a = standardDf.apply(a_min, axis=1).sum()
        tmp_a = (tmp_a / df.shape[0]) * 0.01
        tmp_b = standardDf.apply(b_min, axis=1).sum()
        tmp_b = (tmp_b / df.shape[0]) * 0.01
        a -= tmp_a
        b -= tmp_b
    realA = a * sigma_y / sigma_x
    realB = b * sigma_y + mu_y - a * sigma_y / sigma_x * mu_x
    with open("values.csv", "w", newline='') as valuesFile:
        writer = csv.writer(valuesFile)
        writer.writerow(['a', 'b'])
        writer.writerow([realA, realB])
    plt.plot([0, 250000], [realA*0 + realB, realA*250000 + realB], 'r-', lw=2)
    plt.show()
linear_regretion()
