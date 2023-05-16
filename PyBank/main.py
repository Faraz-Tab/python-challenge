# import the os and csv modules
import os  
import csv

# set the file path
file_path = os.path.join('Resources', 'budget_data.csv')

#open the file
with open(file_path) as file:
    

    # reading the file and skipping the header
    csv_file = csv.reader(file, delimiter=',')
    header = next(csv_file)

    # creating a list called 'Data' and storing the all the CSV file info in it
    Data = [row for row in csv_file]  
    
    # creating a list called 'date' to store all the months
    date = [Data[i][0] for i in range(len(Data))]

    # creating a list called 'amount' to store each months amount as an integer
    amount = [int(Data[i][1]) for i in range(len(Data))]

    # creating a list called 'changes' that stores the difference between everyt rows amount and 
    changes  = [(-(amount[i] - amount[i +1])) for i in range(len(amount) - 1)]
    
    # calculating the highest and lowest changes in 'changes' list and get their dates from 'Data' list
    highest_change = 0
    lowest_change = 0
    for i in range(len(changes)):
        if changes[i] > highest_change:
            highest_change = changes[i]
            x = i
        elif changes[i] < lowest_change:
            lowest_change = changes[i]
            y = i
    
    # printing the results
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(date)}')
    print(f'Total: ${sum(amount)}')
    print(f'Average Change: ${"%.2f" % (sum(changes)/len(changes))}')
    print(f'Greates Increase in Profits: {Data[x + 1][0]} (${highest_change})')
    print(f'Greatest Decrease in Profits: {Data[y + 1][0]} (${lowest_change})')

# creating a text file named 'results' and writing the analysis results inside
text_path = os.path.join("analysis", "results.txt")
with open(text_path, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f'Total Months: {len(date)}\n')
    text.write(f'Total: ${sum(amount)}\n')
    text.write(f'Average Change: ${"%.2f" % (sum(changes)/len(changes))}\n')
    text.write(f'Greates Increase in Profits: {Data[x + 1][0]} (${highest_change})\n')
    text.write(f'Greatest Decrease in Profits: {Data[y + 1][0]} (${lowest_change})\n')
    text.close


    



        
    

