import pandas as pd


main_data = pd.read_csv("./data/AMZN.csv")

senti_data = "Amazon main.csv"

# Add a new column called 'Volume' and initialize it with 0
# Convert the 'Mean' column to a numeric type
main_data['Mean'] = 0
main_data['Max'] = 0
main_data['Min'] = 0


with open(senti_data, 'r') as inFile:
    for line in inFile:

        data = line.split(",")
        if data == ['Ticker', 'Date', 'Mean', 'Max', 'Min\n']:
            continue

        date = str(data[1][0:10])
        mean = float(data[2])
        max = float(data[3])
        min = float(data[4][0:-1])
        # Update the 'Mean' column where the 'Date' is '2021-01-01'
        main_data.loc[main_data['Date'] == f'{date}', 'Mean'] += mean
        main_data.loc[main_data['Date'] == f'{date}', 'Max'] += max
        main_data.loc[main_data['Date'] == f'{date}', 'Min'] += min

main_data.to_csv('Amazon_updated.csv', index=False)
