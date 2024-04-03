# Expense Tracker
## Imported libraries
- sys
- csv
- pandas
- matplotlib.pyplot
- numpy
## Description:
This project cretes a python script with which one can create a new or open an existing csv file containing expense items.
When creating a completely new file, one can specify the categories on his own and the index column is always date,i.e. when
the expense took place.
After new data to the file, a bar and line graph will be displayed, showing the total of all categories and its changing pattern.
It is possible to specify a certain category to be displyed instead of total.

### Creating new expense file
If you simply run the code without further argument, i.e. by typing python expense_tracker.py, you will create a new csv file by specifying
its name, e.g. expense.csv. Be sure to include the suffix .csv as the code only supports csv format.

After that, you will be prompted to provide a date, specifying when the expense took place, suppose you have provided rent, food, clothes.
The next prompt will ask you to provide the corresponding values of each category. Be sure to provide the same length. In this example,
you can type e.g. 1000,500,300.

After you clik enter, the script will display two figures for you, a bar chart on the left and a line plot on the right. By default,
the code will display the total of all categories and the evolving trend of difference along the time. Of course, the difference only mankes
sense if you have at least two rows of data in your csv file.

So the first time you create a new file, the line plot on the right is empty.

### Opening an existing file
If you have created a csv file containing your expenses last time and want to update it with new items, you can simply provide the name of
the csv file as an additional argument, i.e. run python expense_tracker.py expense.csv (Suppose the name for the existing file is expense.csv as above)
Please make sure that you have provided the correct name with .csv suffix.

The code in this case will first display the last five rows (if availabe) for your reference, since you will provide a new row of data and need to know
the corresponding categories.

Then you will be prompted to specify the date and the new data as next step. Following the example above, you can type 1000, 450, 500.

After you click enter, the bar chart on the left shows the total expenses on each date and the line plot on the right shows the difference of the
totals for two subsequent dates.

## Future impovements
As can be seen, the functionality of the code is rather simple and fixed. It is possible and also necessary to implement some new features to enhance
and improve user experiences. These could include:
- add new categories to an existing file
- support not only csv format, but maybe txt or excel, too
- support adding multiple lines of data by one run
- choose the plot types, for example, the user can choose to display the percentage of each categories using a pie chart


