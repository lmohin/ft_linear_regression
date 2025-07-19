from pandas import read_csv
from prediction import getValues
import matplotlib.pyplot as plt

def affDatas():
    """ plot datas from data.csv, and draw the linear line based on the results stored in values.csv"""
    try:
        df = read_csv('data.csv')
    except:
        print("Error: can not read data.csv")
        return
    plt.scatter(df['km'], df['price'], label='Experimental datas')
    a,b = getValues()
    plt.xlim(0, 250000)
    plt.plot([0, 250000], [a*0 + b, a*250000 + b], 'r-', lw=2, label=f'y = {a:.4f}x + {b:.4f}')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.title("Linear relationship between mileage and price of cars")
    try:
        plt.show()
    except:
        return

if __name__ == '__main__':    
    affDatas()
