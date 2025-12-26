import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os
import random




print("========== Data Analysis & Visualization Program ==========")
print("This program analyzes and visualizes data from a CSV or Excel file.")

while True:
    print("="*100 )
    print("Please select an option:")
    print("="*100 )
    print("1. Load Dataset")
    print("2. Explore Dataset")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Values")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualizations")
    print("8. Exit")
    print("="*100 )
    choice = int(input("Enter your choice [1 to 8]: "))
    
    match choice:
        case 1:
            try:
                print("="*100 )
                file = input("Enter the path to the dataset (csv file): ")
                data = pd.read_csv(file)
                print("dataset loaded success fully ! ")
                print("="*100 )
            except Exception as e :
                print(e)
                
            
        case 2:
            print("="*100 )
            print("======= explore data ======")
            print("="*100 )
            
            print("1. Display first 5 rows : ")
            print("2. Display last 5 rows : ")
            print("3. Display Column Names : ")
            print("4. Display Data Types : ")
            print("5. Display Basic info : ")
            print("="*100 )
            
            choose = int(input("Enter your choice [1 to 5]: "))
            
            match choose:
                case 1:
                    print(data.head())
                case 2:
                    print(data.tail())
                case 3:
                    print(data.columns)
                case 4:
                    print(data.dtypes)
                case 5:
                    print(data.info())
                case _:
                    print("Invalid choice ! enter only 1 to 5 ")

        case 3:
            print("="*100 )
            print("=====DataFrame Operations:=====")
            print("="*100 )
            print("1. Filter Rows")
            print("2. Sort Data")
            print("="*100 )
            
            choice = int(input("Choose an operation "))
                      
            match choice :
                case 1:
                    column = input("Enter the column name to filter by: ")
                    value = input("Enter the value to filter for: ")

                    fil = data[data[column].astype(str) == value]
                    print(fil)

                case 2:
                    column = input("Enter the column name to sort by: ")
                    sor = data.sort_values(by=column)
                    print(sor)

                case _:
                    print("Invalid choice !!!")
                    

        case 4:
            print("="*100 )
            print("===Handling Missing Values:===")
            print("="*100 )
            print("1. Drop Missing Values")
            print("2. Fill Missing Values")
            print("3. drop rows with missing values")
            print("4. replace missing value with a specific value")
            print("="*100 )
            choice = input("Choose an option [1 to 4]: ")
            
            match choice:
                case 1:
                    print("="*100 )
                    print("=====Missing Values Only=====")
                    print("="*100 )
                    missing = data[data.isna().any(axis=1)]
                    print(missing)
                    print(missing)

                case 2:
                    print("="*100 )
                    print("=====Missing Filled By Mean=====")
                    print("="*100 )
                    data["Salary"] = data["Salary"].fillna(data["Salary"].mean())
                    data["Bonus"] = data["Bonus"].fillna(data["Bonus"].mean())
                    print("Missing values filled with mean successfully!")

                case 3:
                    print("=====Drop Rows By Mising Values=====")
                    data = data.dropna()
                    print("Rows with missing values dropped successfully!")
                    print(data)

                case 4:
                    print("="*100 )
                    print("======Replace Missing Values With a Specific Value=====")
                    print("="*100 )
                    data = data.fillna(value)
                    print(f"Missing values replaced with {value} successfully!")
                    print(data)
        case 5:
            print("="*100 )
            print("    Generating visualizations ---    ")
            print("="*100 )
            num = data.select_dtypes(include=['float64', 'int64']).columns
            if len(num) >= 2:
                sns.pairplot(data[num])
                plt.suptitle("Pairplot of Numeric Features", y=1.02)
                plt.show(block=False)
                plt.pause(2)
                plt.close()
            
            else:
                print("Not enough numeric columns for pairplot.")
            
            for col in num:
                plt.figure(figsize=(8, 4))
                sns.histplot(data[col], kde=True)
                plt.title(f"Distribution of {col}")
                plt.show(block=False)
                plt.pause(2)
                plt.close()
            
            
            categorical_cols = data.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                plt.figure(figsize=(8, 4))
                sns.countplot(y=data[col], order=data[col].value_counts().index)
                plt.title(f"Count Plot of {col}")
                plt.show(block=False)
                plt.pause(2)
                plt.close()
                
            print(dir(data))
                

        case 6:
            print("="*100 )
            print("\nData Visualization:")
            print("="*100 )
            print("1. Bar Plot")
            print("2. line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")  
            print("="*100 )  

            choice = int(input("Choose a visualization type: "))

            data = data.sample(min(len(data), 3000))
            match choice:
                case 1:
                    col = input("Enter the column name for Bar Plot: ")
                    data[col].value_counts().plot(kind='bar')
                    plt.title(f"Bar Plot of {col}")
                    i = input("Press Enter to display the plot")
                    plt.show(block=False)
    
                case 2:
                    col = input("Enter the column name for Line Plot: ")
                    data[column].plot(kind='line')
                    plt.title(f"Line Plot of {col}")
                    i = input("Press Enter to display the plot")
                    plt.show(block=False)
                    
                case '3':
                    x_col = input("Enter the X-axis column name for Scatter Plot: ")
                    y_col = input("Enter the Y-axis column name for Scatter Plot: ")
                    data.plot(kind='scatter', x=x_col, y=y_col)
                    plt.title(f"Scatter Plot of {y_col} vs {x_col}")
                    i = input("Press Enter to display the plot")
                    plt.show(block=False)
                    
                case 4:
                    col = input("Enter the column name for Pie Chart: ")
                    data[col].value_counts().plot(kind='pie', autopct='%1.1f%%')
                    plt.title(f"Pie Chart of {col}")
                    i = input("Press Enter to display the plot")
                    plt.show(block=False)
                    
                case 5:
                    col = input("Enter the column name for Histogram: ")
                    data[col].plot(kind='hist', bins=10)
                    plt.title(f"Histogram of {col}")
                    i = input("Press Enter to display the plot")
                    plt.show(block=False)
                   
                case 6:
                    columns = input("Enter the column names for Stack Plot: ").split(',')
                    data[columns].plot(kind='area', stacked=True)
                    plt.title(f"Stack Plot of {', '.join(columns)}")
                    i = input("Press Enter to display the plot")
                    plt.show(block=False)
                    
        case 7:
            print("="*100 )
            print("=====save visualisation=====")
            print("="*100 )
            def save(data, output='visualizations'):
                if not os.path.exists(output):
                    os.makedirs(output)

                numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
                for col in numeric_cols:
                    plt.figure(figsize=(8, 4))
                    sns.histplot(data[col], kde=True)
                    plt.title(f"Distribution of {col}")
                    plt.savefig(os.path.join(output, f"{col}_distribution.png"))
                    plt.close()

                categorical_cols = data.select_dtypes(include=['object']).columns
                for col in categorical_cols:
                    plt.figure(figsize=(8, 4))
                    sns.countplot(y=data[col], order=data[col].value_counts().index)
                    plt.title(f"Count Plot of {col}")
                    plt.savefig(os.path.join(output, f"{col}_countplot.png"))
                    plt.close()

                print(f"Visualizations saved in directory: {output}")   
           

        case 8:
            print("Exiting the program. Goodbye ;)")
            break

        case _:
           print("invelid number")
        
