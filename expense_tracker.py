import sys
import csv
import pandas as pd

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
        df.to_csv(name)
        return df





    elif len(sys.argv)==2:
        try:
            df=pd.read_csv(sys.argv[2])
            print(df.tail(3))
            new_date=input('Specify the date yyyy/mm/dd: ')
            new=input('Please provide new value for each column,e.g. 10,15,...: ')
            new=[int(i) for i in list(new.split(','))]
            new_row=[new_date]+new
            with open('expense.csv','a', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(new_row)
            df=pd.read_csv(sys.argv[2])
            return df

    
            
                

    ...


def total_diff(df):
    df['Total']=df.sum(axis=1,numeric_only=True)
    df['Diff']=df['Total'].diff()
    df.to_csv(sys.argv[2])
    return df
    
    ...


def bar_plot(col):
    


if __name__ == "__main__":
    main()
