# The data we need to retrieve
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read and analyze data!
    # Read file object
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)
    print(headers)




    

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
# Write 3 counties to the file
    txt_file.write("Counties in the Election\n-----------\nArapahoe\nJefferson\nDenver\n")