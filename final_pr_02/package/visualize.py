import matplotlib.pyplot as plt
import seaborn as sns


def bar_chart(df):
    df.groupby('Category')['Total Sales'].sum().plot(kind='bar')
    plt.title("Category Sales")
    plt.show()

def line_chart(df):
    df.groupby('Date')['Total Sales'].sum().plot()
    plt.title("Sales Trend")
    plt.show()

def heatmap(df):
    sns.heatmap(df[['Price','Quantity Sold']].corr(), annot=True)
    plt.title("Price vs Quantity")
    plt.show()

def pie_chart(df):
    df.groupby('Category')['Total Sales'].sum().plot(
        kind='pie', autopct='%1.1f%%'
    )
    plt.title("Category Share")
    plt.ylabel("")
    plt.show()

def histogram(df):
    plt.hist(df['Total Sales'], bins=10)
    plt.title("Sales Distribution")
    plt.show()
    
    