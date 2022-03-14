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

The python script created for this analysis was very useful in analyzing the provided (and somewhat limited) set of election data. However, with some modifications, it can be used on larger datasets to determine the same kind of results as we found here. In the current script, we are only examining two columns in the dataset provided. By adding just a handful of new lines, we can expand this analysis to many more columns, and compile similar data we compiled for the candidates and counties. Potentially some sort of demographic analysis by county and candidate would be interesting to look at (mainly from the perspective of candidates, to see who voted for which candidate, and a column with ethnicity or household income, or really anything else would be interesting to compile. 

We can modify the specific dataset that is being looked at , along with adding in certain elements if other things are needed to be analyzed, such as demographic data, who was more likely to vote for which candidate from each region, etc. Really, any sort of information that can be added to the current csv file we used for this analysis would be possible. 
In the current script, we are only examining two columns in the dataset provided. We can add a couple more lines that will include more columns and expand our analysis in combination with the current data analyzed. 
