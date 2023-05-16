#importing the neccessery modules 
import os
import csv

# defining a function called 'winner that takes 3 arguments and declares a winner and returns the result





# we set the path to our csv file 
file_path = os.path.join("Resources", "election_data.csv")

# we open oue file
with open(file_path, 'r') as file:
    #we read our file and store the info in a variavle called 'cdv_file'
    csv_file = csv.reader(file, delimiter=',')

    # declareing the header row
    header = next(csv_file)
    
    # creating a list to store all the data
    rows = [row for row in csv_file]

# counting the total number of votes and storing it in a varable called 'total_votes'
total_votes = len(rows)


# creating a list to store votes into their candidates list
voters_id = {"Charles Casper Stockham" : [], "Diana DeGette" : [], "Raymon Anthony Doane" : []}

# setting the conditions to seperate and count the votes
for id in range(len(rows)):
    if rows[id][2] == "Charles Casper Stockham":
        voters_id['Charles Casper Stockham'].append(rows[id][0])
    elif rows[id][2] == "Diana DeGette":
        voters_id['Diana DeGette'].append(rows[id][0])
    elif rows[id][2] == "Raymon Anthony Doane":
        voters_id['Raymon Anthony Doane'].append(rows[id][0])

# creating a dictionary that stores the names of candidates with their number of votes achived
# in lists
new_list = {"names": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"],
            "number_of_votes":[len(voters_id["Charles Casper Stockham"]), len(voters_id["Diana DeGette"]), len(voters_id["Raymon Anthony Doane"])]}

# creating a list to store the winner(s) and if there is only one winner, transforms the list
# into a single name 
winners = []
max_votes = max(new_list["number_of_votes"])
for name in range(len(new_list['names'])):
    if new_list["number_of_votes"][name] == max_votes:
        winners.append(new_list["names"][name])

if len(winners) == 1:
    winners = winners[0]
print(winners)





# printing the results
print("Election Results")
print("-------------------------")
print(f'Total Votes: {len(rows)}')
print("-------------------------")
print(f'Charles Casper Stockham: {"%.3f"%((len(voters_id["Charles Casper Stockham"]) / len(rows)) * 100)}% ({len(voters_id["Charles Casper Stockham"])})')
print(f'Diana DeGette: {"%.3f"%((len(voters_id["Diana DeGette"]) / len(rows)) * 100)}% ({len(voters_id["Diana DeGette"])})')
print(f'Raymon Anthony Doane: {"%.3f"%((len(voters_id["Raymon Anthony Doane"]) / len(rows)) * 100)}% ({len(voters_id["Raymon Anthony Doane"])})')
print("-------------------------")
print(f'Winner: {winners}')
print("-------------------------")

text_path = os.path.join("analysis", "results.txt")

with open(text_path, 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f'Total Votes: {len(rows)}\n')
    text.write("-------------------------\n")
    text.write(f'Charles Casper Stockham: {"%.3f"%((len(voters_id["Charles Casper Stockham"]) / len(rows)) * 100)}% ({len(voters_id["Charles Casper Stockham"])})\n')
    text.write(f'Diana DeGette: {"%.3f"%((len(voters_id["Diana DeGette"]) / len(rows)) * 100)}% ({len(voters_id["Diana DeGette"])})\n')
    text.write(f'Raymon Anthony Doane: {"%.3f"%((len(voters_id["Raymon Anthony Doane"]) / len(rows)) * 100)}% ({len(voters_id["Raymon Anthony Doane"])})\n')
    text.write("-------------------------\n")
    text.write(f'Winner: {winners}\n')
    text.write("-------------------------\n")
