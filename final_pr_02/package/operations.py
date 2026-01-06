
def clean_data(df):
    df.dropna(inplace=True)
    df['Total Sales'] = df['Price'] * df['Quantity Sold']
    print(" Data cleaned & Total Sales calculated")
    return df
    
    
    
def calculate_metrics(df):
    total_sales = df['Units sold'].sum()
    avg_sales = df['Units sold'].mean()
    popular_product = df.groupby('item type')['Units sold'].sum().idxmax()

    print("\n SALES METRICS")
    print(f"Total Sales : ₹{total_sales:.2f}")
    print(f"Average Sale: ₹{avg_sales:.2f}")
    print(f"Top Product : {popular_product}")
    


def filter_data(df):
    print("1. Filter by Category")
    print("2. Filter by Date Range")

    choice = input("Choice: ")

    match choice:
        case "1":
            cat = input("Enter category: ")
            print(df[df['Category'] == cat])

        case "2":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            print(df[(df['Date'] >= start) & (df['Date'] <= end)])

        case _:
            print(" Invalid option")
            

    
def show_summary(df):
    print(" DATA SUMMARY")
    print(df.describe())
    
    