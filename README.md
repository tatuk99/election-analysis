# Election Analysis

## Overview of Project

This analysis was created to determine the winning candidate for an election in Colorado, along with analyzing the number of votes cast in respective counties, and overall. The deliverables include:
- Total number of votes cast
- A complete list of counties and candidates that received votes
- Total number of votes each county and candidate received
- Percentage of votes each county received and candidate won
- The winner of the election based on popular vote and the largest county turnout 

## Election Audit Results

- How many votes were cast in this congressional election?
  
  369,711 total votes were cast
  
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  ![County_Vote_Data](Resources/County_vote_breakdown.png)
  
- Which county had the largest number of votes?
 
  Denver County
  
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  ![Candidate_Vote_Data](Resources/Candidate_breakdown_data.png)
  
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  ![Winning_Candidate](Resources/Winning_candidate_data.png)

Here is the overall breakdown of our results for this analysis:

![Results](Resources/Analysis_results_screenshot.png)
  
	
## Election Audit Summary

The python script created for this analysis was very useful in analyzing the provided (and somewhat limited) set of election data. However, with some modifications, it can be used on larger datasets to determine similar results as what we found here. 
It is very easy to update the dataset that is analyzed - we simply reference a different csv file in the script. This make this script versatile and easy to use throughout various data analyses involving elections (maybe we can split this analysis by various regions in Colorado and look at specific regional data if that is of interest).
Additionally, in the current script, we are only examining two columns in the dataset provided. By adding just a handful of new lines, we can expand this analysis to many more columns, and compile similar data we compiled for the candidates and counties. Potentially some sort of demographic analysis by county and candidate would be interesting to look at in order to determine who voted for which candidate, (such as adding a column with ethnicity or household income, or really anything else would be interesting to compile) and referencing that to specific candidates and counties. 
Any sort of new ideas that can be included in the form of data in column formatting will make this script work, so it's really up to the people determining what they would like to analyze next.
