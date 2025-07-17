from pandas import read_csv
import time
import csv
import matplotlib.pyplot as plt

def linear_regretion():
    df = read_csv('data.csv')
    mu_x = df['km'].mean()
    sigma_x = df['km'].std()
    mu_y = df['price'].mean()
    sigma_y = df['price'].std() 
    plt.scatter(df['km'], df['price'])
    df['km'] = (df['km'] - df['km'].mean()) / df['km'].std()
    df['price'] = (df['price'] - df['price'].mean()) / df['price'].std()
    a = 0
    b = 0
    def to_minimize(row):
        return ((row['km'] * a + b - row['price']) ** 2)
    for i in range(10000):
        def a_min(row):
            return ((row['km'] * a + b - row['price']) * row['km'])
        def b_min(row):
            return ((row['km'] * a + b - row['price']))
        tmp_a = df.apply(a_min, axis=1).sum()
        tmp_a = (tmp_a / df.shape[0]) * 0.01
        tmp_b = df.apply(b_min, axis=1).sum()
        tmp_b = (tmp_b / df.shape[0]) * 0.01
        a -= tmp_a
        b -= tmp_b
        print(a,b)
    print(a * sigma_y / sigma_x, b * sigma_y + mu_y - a * sigma_y / sigma_x  * mu_x)
    print(df.apply(to_minimize, axis=1))
    aa = a * sigma_y / sigma_x
    bb = b * sigma_y + mu_y - a * sigma_y / sigma_x * mu_x
    aas = str(aa)
    bbs = str(bb)
    with open("values.csv", "w", newline='') as valuesFile:
        writer = csv.writer(valuesFile)
        writer.writerow(['a', 'b'])
        writer.writerow([aas, bbs])
    plt.plot([0, 250000], [aa*0 + bb, aa*250000 + bb], 'r-', lw=2)
    plt.show()
linear_regretion()
