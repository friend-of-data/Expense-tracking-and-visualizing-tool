import sys
import csv
import pandas as pd
from datetime import datetime

def main():
    ...


def open_or_create():
    if len(sys.argv)==1:
        name=input('Please provide a name for your file: ')
        date=input('Specify the date yyyy/mm/dd ')  # can be changed as index
        categories=input('Specify category: ')
        amount=input('Please specify amount,e.g. 100, 24 ...: ')
        data=np.array([[int(i) for i in list(amount.split(','))]])
        df= pd.DataFrame(data=data, columns=list(categories.split(',')))
        df['Date']=[date]
        df.set_index('Date',inplace=True)
        print(df)
        df.to_csv('expense.csv')





    elif len(sys.argv)==2:
        try:
            with open(sys.argv[2]) as file:

    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
