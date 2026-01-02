import pandas as pd , matplotlib.pyplot as plt, seaborn as sns

def load_titanic_data():
    file_path = r"C:\Users\Rwn\Documents\Jasmit\final_project\titanic.csv"             
    df = pd.read_csv(file_path) 
    return df

def clean_titanic_data(df):
    print("choose an option : ")
    print("1. Fill missing Age with the median")
    print("2. Fill missing Embarked with the most common value")
    print("3. Create a 'FamilySize' feature (SibSp + Parch + 1 for themselves)")
    print("4. Drop columns that are too unique or have too many missing values (like Cabin)")
    choice2 = int(input("enter your choice :-"))
    match choice2:
        case 1:    
            df['Age'] = df['Age'].fillna(df['Age'].median())
            
        case 2:    
            df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

        case 3:   
            df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

        case 4:    
            df.drop(['Cabin', 'Ticket', 'Name', 'PassengerId'], axis=1, inplace=True)

        case _:
            print("invelid choice ! ")
    
    return df




def plot_survival_rates(df):
    print("choose an option--->")
    print("Plot 1: Survival by Gender")
    print("Plot 2: Survival by Passenger Class")
    choicee = int(input("enter your choice :-"))
    plt.figure(figsize=(12, 5))
    match choicee:
        case 1:
            plt.subplot(1, 2, 1)
            sns.barplot(x='Sex', y='Survived', data=df, palette='viridis')
            plt.title('Survival Rate by Gender')
            
        case 2:
            plt.subplot(1, 2, 2)
            sns.barplot(x='Pclass', y='Survived', data=df, palette='magma')
            plt.title('Survival Rate by Class')

        case _:
            print("invelid choice ! ")
                       
    plt.tight_layout()
    plt.show()

def plot_age_distribution(df):  
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Age', hue='Survived', kde=True, element="step")
    plt.title('Age Distribution of Survival')
    plt.show()

def plot_correlation(df):
    plt.figure(figsize=(10, 8)) 
    sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.show()

