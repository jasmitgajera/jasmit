import pandas as pd

def load_data():
    try:
        # file_path = input("enter your file path [only csv file]")
        file_path = r"C:\Users\Rwn\Documents\Jasmit\final_pr_02\10000 Sales Records.csv"
        df = pd.read_csv(file_path)
        print(df)
        print(" Data loaded successfully\n")
    except Exception as e:
        print(" Error loading file:", e)
        