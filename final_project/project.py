import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from packages import main


print("="*100 ) 
print("=============================  welcome to taitanic survival analysis =============================")
print("="*100 ) 

while True:
    
    print("1. Load Dataset")
    print("2. clean Dataset")
    print("3. Visualize ")
    print("="*100 ) 

    choose1 = int(input("enter your choice :-"))
    match choose1:
        case 1:
            print("============================= Load Dataset =============================")  
            df = main.load_titanic_data() 
            print(df) 

        case 2:
            print("============================= clean Dataset =============================")
            main.clean_titanic_data(df)
            print(df) 

        case 3:
            print("============================= Visualize Dataset =============================")
            print("1. Visualizes survival rates based on Class and Gender")
            print("2. Plots the age distribution of survivors vs non-survivors.")
            print("3. Shows how features relate to each other.")
            choice = int(input("enter your choice :-"))
            match choice:
                case 1:
                    main.plot_survival_rates(df)
                case 2:
                    main.plot_age_distribution(df)
                case 3:
                    main.plot_correlation(df)
                

   
      

    


