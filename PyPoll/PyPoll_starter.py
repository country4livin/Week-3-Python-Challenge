# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_name = []
vote_counts = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in candidate_name:
            candidate_name.append(name)
            vote_counts[name]=0

        # Add a vote to the candidate's count
        vote_counts[name]+=1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    output_1 =  (
        f'Election Results\n'
        f'------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'------------------------\n')
    
    print(output_1)

    # Write the total vote count to the text file
    txt_file.write(output_1)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in vote_counts:

        # Get the vote count and calculate the percentage
        vote = vote_counts[candidate]
        vote_percentage = float(vote)/float(total_votes)*100
        #{candidate_name:(vote_counts/total_votes)*100}

        # Update the winning candidate if this one has more votes
        if vote>winning_count:
            winning_count = vote
            winning_candidate = candidate


        # Print and save each candidate's vote count and percentage
        candidate_summary = f'{candidate}: {vote_percentage:.2f}% ({vote})\n'

        #print(vote_percentage[candidate_name], (candidate[candidate_name]))
        print(candidate_summary)
        txt_file.write(candidate_summary)
    # Generate and print the winning candidate summary
    output = (
    f'------------------------\n'
    f'Winning Candidate: {winning_candidate}\n'
    f'-------------------------\n')

    print(output)

    # Save the winning candidate summary to the text file

    txt_file.write(output)