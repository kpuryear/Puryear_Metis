## Project Benson 
### Problem to be Solved:
Our metaphorical Data Science Company was approached by a group called Women Tech Women Yes (WTWY). Their group is relativey new in New York, and will be hosting their annual gala event during the summer. They are interested in using street teams to hand out fliers in popular NYC subway stations.

Our task is to recommend a plan for their street team that will yield the highest attendence and largest donations during the Summer Gala. 

### Decoding the Problem and Planning Our Approach
My partner and I unpacked WTWY's request and determined that we were looking for locations that optimize 3 distinct factors:
* Very busy subway stations
* Wealthy populations
* Regions with an interest in tech

To utilize those distinct factors, we approached the data from 3 different angles:

1. Obtain MTA turnstile data:
* To obtain busiest subway stations


2. Obtain US census data to obtain income values:
* To obtain boroughs/sub-boroughs that have high average incomes


3. Obtain location data for Startups in NYC:
* Correlate location of NYC startups with busiest subway stations and wealthiest sub-borough


### MTA Data
We found the mta data available for free online. The data was broken down into separate documents for each week. We chose to use data for 4 weeks, from April 15, 2017 to May 12, 2017. 

The raw data comes in looking like this:

![SUBWAYS](https://github.com/kpuryear/Puryear_Metis/tree/master/Project1/images/RawMTA.png?raw=true)
  
Our objective was to determine which NYC subway stations were the busiest during this time of year. To do this, we looked at the column called "ENTRIES". Our overall plan was to isolate the top 6 busiest subway stations, then delve deeper into each station individually.

Cleaning the "ENTRIES" data was a serious undertaking, since the numbers provided under the "ENTRIES" column never get reset, and are unique to each turnstile. The count starts at 0 when any given turnstile goes online, and the counts keep increasing for the rest of the turnstile's life, or until it gets reset for maintenence. Further clouding this data, there are many turnstiles for each station, each with their own arbitrary starting count. To handle these discrepancies, we devised a series of pandas "grouby" formulas.  

INSERT CODE HERE

Once the "ENTRIES" data was more manageable, we were able to graph our data and gather meaningful results.

### Census Data:
We found 2014 US census data available online for free through the American Housing and Vacancy Survey. This census data included a 172 digit number for each response. Luckily, the data included a key for how to extract desired information. Using this data, we created a pandas dataframe that included income and place of residence. We plotted the mean and median incomes for each sub-borough. 

### Startup Data
We found a graphic from Digital NYC that showed density of startup companies in NYC. Conveniently, the vast majority of startups are located near busy subway stops in mid/lower Manhattan. 

### Results: Graphs and Tables
After analyzing the MTA data, Census Data and Startup images, it became very clear that mid/lower Manhattan was the location to yeild high subway traffic, wealthy populations, and a large tech intrest.

INSERT ALL 3 CORRELATION IMAGES

### Conclusion and Recommendation to Client
We recommend deploying a street team of 27 people in total on weekdays only, to the 6 busiest subway stations in NYC:
* 5 people to 14th St, Union Sq    
* 4 people to 47th-50th St Rockefeller Center
* 4 people to 59 St Columbus
* 4 people to Chambers St
* 5 people to World Trade Center Station
* 5 people to Times Sq, 42 St
