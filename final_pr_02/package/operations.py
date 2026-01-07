
def clean_data(df):
    try:
        df.dropna(inplace=True)
        print("enter column name which you want to clean")
        Unit_cost = input('enter column name (ex. -Unit Cost) : ')
        Unit_sold = input('enter column name (ex. -Units Sold) : ')
        df['Total Sales'] = df[Unit_cost] * df[Unit_sold]
        print("\n total sales")
        print(df['Total Sales'])
        print(" Data cleaned & Total Sales calculated ")
        return df
    except Exception as e :
        print(e) 
    
    
def calculate_metrics(df):
    try:
        Unit_sold = input('enter column name (ex. -Units Sold)')
        total_sales = df[Unit_sold].sum()
        avg_sales = df[Unit_sold].mean()
        popular_product = df.groupby('Item Type')['Units Sold'].sum().idxmax()

        print("\n SALES METRICS")
        print(f"Total Sales : ₹{total_sales:.2f}")
        print(f"Average Sale: ₹{avg_sales:.2f}")
        print(f"Top Product : {popular_product}")
        return df
    except Exception as e :
        print(e)    


def filter_data(df):
    try:
        print("1. Filter by Item Type")
        print("2. Filter by Date Range")

        choice = int(input("Choice: "))

        match choice:
            case 1:
                cat = input("Enter Item Type : ")
                print(df[df['Item Type'] == cat])

            case 2:
                start = input("Start date (YYYY-MM-DD): ")
                end = input("End date (YYYY-MM-DD): ")
                print(df[(df['Order Date'] >= start) & (df['Order Date'] <= end)])

            case _:
                print(" Invalid option")
    except Exception as e :
        print(e)            

    
def show_summary(df):
    print(" DATA SUMMARY")
    print(df.describe())
    

    
