import pandas as pd
import plotly.express as ply


pd.set_option('display.max_columns', None)

# GDP Dataset

gdp = pd.read_csv('./data/gdp.csv')

# Exploratory Data Analysis

# gdp in USD

gdp.head()
# discuss columns available
gdp.shape
gdp['Year']
min(gdp.Year)
max(gdp.Year)
gdp['Country'].unique()
len(gdp['Country'].unique())
gdp['Country'].value_counts()  # not full dataset for every country, why is this importnant? (biased data - not representative of the world)

# what do we expect this to look like? then plot. is the result surprising?
ply.scatter(data_frame= gdp,
           x= "Year",
           y="GDP_USD",
           color="Country", 
           hover_name="Country",
           log_y=False)


# Life Expectancy Dataset - Exploratory Data Analysis

life_exp = pd.read_csv('./data/life_expectancy.csv')

life_exp.head()
# note: there's a gdp column! 
# and there's also columns for country and year - common to both datasets

life_exp.shape

life_exp['Year']
min(life_exp.Year)
max(life_exp.Year)
life_exp['Country'].unique()
len(life_exp['Country'].unique())
life_exp['Country'].value_counts()  # full dataset!

ply.scatter(data_frame= life_exp,
           x= "Year",
           y="LifeExpectancy",
           color="Country", 
           hover_name="Country",
           log_y=False)




"""
Joining datasets
what is a join?
(image)
left/right/inner/outer
how should we join these datasets?
- what column(s)
- left/right/inner/outer? 
    -> smaller dataset on the left, because we only want the complete data

    
- create a country map to get a bigger dataset
- some countries are missing from life_expectancy, how can we get them?
    -> find another dataset with missing countries 
    -> eg: I have the raw data from WHO, but it's in a different format!
    - can transform it to be more "joinable
    - have made it more joinable for china
"""
len(gdp.Country.unique())
len(life_exp.Country.unique())
set(life_exp['Country']).intersection(gdp['Country Name'])
set(life_exp['Country']).difference(gdp['Country'])
set(gdp['Country']).difference(life_exp['Country'])

merged = pd.merge(life_exp, gdp, how='left',on=['Country'], suffixes=['_le','_gdp'])
# shape explosion! why?


merged = pd.merge(life_exp, gdp, how='left',on=['Country','Year'], suffixes=['_le','_gdp'])

life_exp.shape
merged.shape 
# these are the same -> better!

# Visualisation, Insights, and Conclusions

"""
what do we want from the merged dataset?
- check gdp, are the values similar?
- they're very different! why?
- what values do we trust?
- check on google to see what ones line up -> the gdp dataset seems to be accurate, so lets use that
-> this is making a judgement call about quality of data, which is an important skill
-> it's good to be aware of the weaknesses of data
"""

ply.scatter(
    data_frame=merged, 
    x="GDP_USD",
    y="LifeExpectancy",
    hover_name="Year",
    color="Country",
    log_x=True) # with / without log scale it looks very different!
"""
Why log scale?
Are these correlated, is there causation? which way does it go? can we put some metrics on it?

Other things to try:
-> discuss how to represent data and why is visualisation a good way to turn data into information

Students to play around with what kind of visualisation they want to make
- color to give info
- log scales
- plot different data to make inferences
- hover info to be different
- different chart styles
- the life expectancy dataset has columns for cause of death - are there any insights from this?
"""







