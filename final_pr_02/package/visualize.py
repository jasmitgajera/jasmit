import matplotlib.pyplot as plt
import seaborn as sns


def bar_chart(df):
    try:
        Item_Type = input('enter column name (ex. - Item type) : ')
        Total_Profit = input('enter column name (ex. - Total Profit) : ')
        df.groupby(Item_Type)[Total_Profit].sum().plot(kind='bar')
        plt.title("Category Sales")
        plt.show()
    except Exception as e :
        print(e) 

def line_chart(df):
    try:
        Total_Profit = input('enter column name (ex. - Total Profit) : ')
        Order_Date = input('enter column name (ex. - Order Date) : ')
        df.groupby(Order_Date)[Total_Profit].sum().plot()
        plt.title("Sales Trend")
        plt.show()
    except Exception as e :
        print(e)

def heatmap(df):
    try:
        Unit_cost = input('enter column name (ex. -Unit Cost) : ')
        Unit_sold = input('enter column name (ex. -Units Sold) : ')
        sns.heatmap(df[[Unit_cost,Unit_sold]].corr(), annot=True)
        plt.title("Price vs Quantity")
        plt.show()
    except Exception as e :
        print(e) 

def pie_chart(df):
    try:
        Item_Type = input('enter column name (ex. - Item type) : ')
        Total_cost = input('enter column name (ex. -Total Cost) : ')
        df.groupby(Item_Type)[Total_cost].sum().plot(
            kind='pie', autopct='%1.1f%%'
        )
        plt.title("Category Share")
        plt.ylabel("")
        plt.show()
    except Exception as e :
        print(e) 

def histogram(df):
    try:
        Total_cost = input('enter column name (ex. -Total Cost) : ')
        plt.hist(df[Total_cost], bins=10)
        plt.title("Sales Distribution")
        plt.show()
    except Exception as e :
        print(e) 
    
    