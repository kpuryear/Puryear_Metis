

# Metis Data Science Bootcamp
## Kaitlin Puryear
## Seattle Cohort, Winter 2018
As a Metis Student, I will be analyzing data for multile different projects over the course of the 12 week bootcamp.

-------------------

## Project Benson 
### Problem to be Solved:
Our metaphorical Data Science Company was approached by a group called Women Tech Women Yes (WTWY). Their group is relativey new in New York, and will be hosting their annual gala event during the summer. They are interested in using street teams to hand out fliers in popular NYC subway stations.

Our task is to recommend a plan for their street team that will yield the highest attendence and largest donations during the Summer Gala. 

### Decoding the Problem and Planning Our Approach
My partner and I unpacked WTWY's request and determined that we were looking for locations that optimize 3 distinct factors:
* very busy subway stations
* wealthy populations
* regions with an interest in tech

We determined that our ideal audience consisted of wealthy, tech-focused individuals, who use high-traffic subway stations.

To utilize those distinct factors, we approached the data from 3 different angles:

1. Obtain MTA turnstile data:
* To obtain busiest subway stations


2. Obtain US census data to obtain income values:
* To obtain boroughs/sub-boroughs that have high average incomes


3. Obtain location data for Startups in NYC:
* Correlate location of NYC startups with busiest subway stations and wealthiest sub-borough


### MTA Data
We found the mta data available for free online. The data was broken down into separate documents for each week. We chose to use data for 4 weeks, from April 15, 2017 to May 12, 2017. We are assuming that the gala takes place in mid/late June, so we chose the data for the month when street teams could be most effective. 

After importing the month of data, and merging all 4 weeks into one dataframe, we can start to explore the data. The raw data comes in looking like this:

INSERT PICTURE!
  
Our objective was to determine which NYC subway stations were the busiest during this time of year. To do this, we looked at the column called "ENTRIES", because that signifies how many people came into that particular station. Our overall plan was to isolate the top 8 busiest subway stations, then delve deeper into each station individually.

We used a pandas dataframe technique to narrow down the columns in our dataset until we were left with sorted, nicely parsed data that was easy to graph. Cleaning the "ENTRIES" data was a serious undertaking, since the numbers provided under the "ENTRIES" column never get reset, and are unique to each turnstile. The count start at 0 when any given turnstile goes online, and the counts keep increasing for the rest of its life, or until it gets reset for maintenence. Further clouding this data, there are many turnstiles for each station, each with their own arbitrary starting count. To handle these discrepancies, we devised a series of pandas "grouby" formulas.  

INSERT CODE HERE

Once the "ENTRIES" data was more manageable, we were able to graph our data and gather meaningful results.


### Results: Graphs and Tables
words and tables

### Conclusion and Recommendation to Client
words words words
