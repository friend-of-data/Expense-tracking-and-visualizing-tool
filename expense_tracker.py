import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    df=open_or_create()
    df=total_diff(df)
    plothelper(df,'Date','Total')


def open_or_create():
    if len(sys.argv)==1:
        name=input('Please provide a name for your file: ')
        date=input('Specify the date yyyy/mm/dd ')  # can be changed as index
        categories=input('Specify category: ')
        amount=input('Please specify amount,e.g. 100, 24 ...: ')
        row_1=[date]+[int(i) for i in list(amount.split(','))]
        header=['Date']+list(categories.split(','))
        data=np.array([row_1])
        df= pd.DataFrame(data=data, columns=header)
        print(df)
        df.to_csv(name,index=False)
        df=pd.read_csv(name)
        return df





    elif len(sys.argv)==2:
        try:
            df=pd.read_csv(sys.argv[1])
        except:
            sys.exit('Please give the correct csv file name')
        print(df.tail())
        new_date=input('Specify the date yyyy/mm/dd: ')
        new=input('Please provide new value for each column,e.g. 10,15,...: ')
        new=[int(i) for i in list(new.split(','))]
        new_row=[new_date]+new
        with open(sys.argv[1],'a', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(new_row)
        df=pd.read_csv(sys.argv[1])
        return df


    
            
                

    ...


def total_diff(df):
    df['Total']=df.sum(axis=1,numeric_only=True)
    df['Diff']=df['Total'].diff()
    #df.to_csv(sys.argv[2])
    return df
    
    ...


def plothelper(df,xcol,ycol):
    plt.subplot(1,2,1)
    plt.bar(df[xcol],df[ycol])
    plt.xticks(rotation=45)
    plt.title(f'{ycol}')

    plt.subplot(1,2,2)
    plt.plot(df[xcol], df[ycol].diff())
    for xi,yi in zip(df[xcol][1:],df[ycol].diff()[1:]):
        plt.text(xi,yi,str(yi),ha='right')
    plt.xticks(rotation=45)
    plt.title('Changes')
    plt.show()
    
    
    


if __name__ == "__main__":
    main()
