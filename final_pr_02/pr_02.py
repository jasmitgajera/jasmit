from package import load , operations , visualize


print("\n========================= RETAIL SALES ANALYZER ================================")

df = None

while True:

    print("1. Load Data")
    print("2. Clean Data")
    print("3. Metrics")
    print("4. Filter")
    print("5. Bar Chart")
    print("6. Line Chart")
    print("7. Heatmap")
    print("8. Pie Chart")
    print("9. Histogram")
    print("10. Summary")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            load.load_data()

        case 2:
            operations.clean_data(df)

        case 3:
            operations.calculate_metrics(df)

        case 4:
            operations.filter_data(df)

        case 5:
            visualize.bar_chart(df)

        case 6:
            visualize.line_chart(df)

        case 7:
            visualize.heatmap(df)

        case 8:
            visualize.pie_chart(df)

        case 9:
            visualize.histogram(df)

        case 10:
            operations.show_summary(df)

        case 0:
            print(" Exiting...")
            break
        
        case _:
            print(" Invalid choice")