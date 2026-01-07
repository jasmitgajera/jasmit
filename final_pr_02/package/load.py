import pandas as pd

def load_data():
    try:
        file_path = input("enter your file path [only csv file]")
        df = pd.read_csv(file_path)
        print(df)
        print(" Data loaded successfully\n")
        return df
    except Exception as e:
        print(" Error loading file:", e)


