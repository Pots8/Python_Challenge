import os
import csv

# Files needed
file_input = "Resources/election_data.csv"
file_output = "poll.txt"

# initialize
total_vcount = 0
candidate_list = []
candidate_votes = {}
winner = ""
win_counter = 0

# Read csv then convert list of dictionaries
with open(file_input) as election_data:
    reader = csv.DictReader(election_data)
    for row in reader:
        total_vcount += 1
        name = row["Candidate"]
        # initialize the name if not existed
        if name not in candidate_list:
            candidate_list.append(name)
            candidate_votes[name] = 0
        #  increase candidate's count
        candidate_votes[name] += 1

# Print result and export to text file
with open(file_output, "w") as txt_file:
    output = (
        f"\n\nElection Results\n"
        f"-----------\n"
        f"Total Votes: {total_vcount}\n"
        f"-----------\n")
    print(output)

    # to text file
    txt_file.write(output)

    # Find winner by votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        # calculate percentage
        percentage = float(votes) / float(total_vcount) * 100
        # compare
        if (votes > win_counter):
            win_counter = votes
            winner = candidate 
        candidate_output = f"{candidate}: {percentage:.3f}% ({votes})\n"
        print(candidate_output, end="")
        # to text file
        txt_file.write(candidate_output)

    final_winner = (
        f"-------------\n"
        f"Winner: {winner}\n"
        f"-------------\n")
    print (final_winner)
    # to text file
    txt_file.write(final_winner)
