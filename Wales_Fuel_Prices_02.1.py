#!/usr/bin/env python
# coding: utf-8

# ### Building an Excel File which includes all the UK Government Access Fuel Price Data
# 
# **This notebook has been built in the Anaconda enviroment, using Anaconda Navigtor 2.5.2 and Jupyter Notebook 7.02.**
# 
# **It using the dependencies already carried by Anaconda environment, such as BeautifulSoup**
# 
# Replicating this outside of Anaconda or different versions may require downloading dependent modules:
# 
# * beautifulsoup4
# * requests
# * pandas
# * openpyxl

# In[1]:


#CODE TO BUILD EXCEL FILE in a .xlsx format containing all the data listed for fuel prices provided at the
# UK government ACCESS FUEL PRICES website: https://www.gov.uk/guidance/access-fuel-price-data

#import the modules we need to build and export the DataFrame


#beautifulsoup 4 package is installed as part of Anaconda environment to parse HTML
from bs4 import BeautifulSoup 

#allows us to pull requests from webpages, urls and api sources
import requests

#loads the pandas data tools - shortened to pd to call it
import pandas as pd 

# module to read and manipulate json formated data
import json  

#module that allows us to specify data and time strings
from datetime import datetime   #module that allows us to specify data and time strings

# this will allow us to specify which path we want to save the final output excel file to
import os  


# #### Scraping the URLs we need from the UK government website: 

# In[2]:


# SCRAPE THE URLs:

# Define the URL of the webpage to scrape
url = 'https://www.gov.uk/guidance/access-fuel-price-data'

# use requests library to send GET request for the url

response = requests.get(url)

# Check if the request was successful - status should be 200 and parse with BeautifulSoup

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

# Initialize a list to store JSON URLs
json_url = []


# The URLs are all held within table markdown tags. To find all <td> elements in the table, using soup:

td_elements = soup.find_all('td')

# Iterate over each <td> element and extract the URLs ending with .json
for td in td_elements:
    url = td.text.strip()
    if url.startswith('https://') and url.endswith('.json') or url.endswith('.html'):
        json_url.append(url)


# #### Building the intitial DataFrame

# In[3]:


#building the dataframe

#headers - WITHOUT THIS - THE tesco_url ENTRY WILL REJECT THE REQUEST AND TIME OUT

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

#blank list to store the called json data

fuel_data = []

#loop to iterate through the urls in json_url and then add them using .append to fuel_data

for url in json_url:
    url_data = requests.get(url, headers=headers)  #use the requests.get method and tells requests, and make sure headers are used 
    data = url_data.json()   
    fuel_data.append(data)   

# Make DataFrame with pandas (pd) called df_fuel - and use the .json_normalize function get to record_path 'stations'

df_fuel = pd.json_normalize(fuel_data, record_path = 'stations')


# In[4]:


# returns the dataframe - for visual check - remove comment if required

# df_fuel


# #### Filtering our DataFrame for Wales only postcode locations
# 
# The initial filter relies on using the two letter codes used in Wales - though some, such as CH, LD and HR also cover some England postcodes areas. This will cut the entries down substantially - allowing us to make use of an API to further check the postcodes locations

# In[5]:


# Filter the DataFrame to include only postcodes starting with 'CF' or 'LL'
# This will cut the new dataframe from 4554 entries down to under 300

df_poss_wales = df_fuel[df_fuel['postcode'].str.startswith(('LL', 'NP', 'CF', 'SA', 'SY', 'CH', 'LD', 'HR3', 'HR5'))]



# #### Checking our filtered list against a database - using an API call to postcodes.io database
# 
# **We first need to build a function that will allow us to make the api calls**

# In[6]:


#We can now check to see which other postcodes are actually Wales postcodes - calling the 300 through the postcodes api
# We build this function first - which calls the api.postcodes url - and then checks the json file and nested entry 'country'
# if there's a match for Wales - it returns a True value - otherwise - it returns False

# Function to check if a postcode is in Wales
def is_postcode_in_wales(postcode):
    url = f"http://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']
        if result and result['country'] == 'Wales':
            return True
    return False


# #### Building an updated dataframe with a new columns 'Wales' which will list whether the postcode is in Wales (True) or not (False)

# In[7]:


# Update the 'Wales' column based on the postcode check 
# this applies the function we've just built - adds a new column 'Wales' to the dataframe df_poss_wales - which will be either True or False



df_wales = df_poss_wales

df_wales['Wales'] = df_wales['postcode'].apply(is_postcode_in_wales)


# In[8]:


df_wales


# **While a warning is thrown up - it does actually create the correct dataframe, listing a column of True and False values for Wales**

# #### We can now filter the new dataframe to remove all False entries

# In[9]:


#removes all false enteries - leaving only Wales enteries

df_wales = df_wales[df_wales.Wales != False]


# In[10]:


# THIS ALLOWS US TO SCROLL THROUGH THE ENTIRE DATA FRAME - it's only 300 rows

pd.set_option('display.max_rows', None)


# In[11]:


df_wales


# In[12]:


#show length of dataframe in rows

len(df_wales)


# #### Data Validation and cleaning

# In[13]:


#From looking at the data - it's clear duplicates exist - especially for Morrisons brands under both Morrisons and MFG
# we use the .duplicated method in Pandas - stating which column to look at - in our case 'postcode'
# The keep = False retains both sets of duplicates - so they can be checked physically to ensure they are true duplicates

duplicates_wales = df_wales[df_wales.duplicated(['postcode'], keep = False)]


# In[14]:


# displays the dupicates - notice the two bottom are not a true duplicate - rather two petrol stations almost next to each other

duplicates_wales


# In[15]:


# amended to use site_id reference - see note below

# uses the .drop method to remove multiple index items - these are the duplicate index numbers

#df_wales_cleaner = df_wales.drop(index =[1379, 1416, 1425,1437,1472, 1488,1489,1500, 1511])


# Instead of using .drop and index reference - we will adopt dropping the row by using the site_id reference, which remains the same - while the index may change, depending on how many stations overall are reported in a week.
# 
# We will used the format:
# ```
# # Define the strings to remove
# strings_to_remove = ['site_id_1', 'site_id2']
# 
# # Remove rows where 'Column_Name' contains any of the strings in the list
# df = df[~df['Column_Name'].str.contains('|'.join(strings_to_remove))]
# 
# ```

# In[16]:


# Define strings to remove - using first duplicate values in duplicate wales (but not the first one - it's not a real duplicate
# rather it is a second petrol forecourt in the same postcode area - different brands)

strings_to_remove = ['gcm8dw51gpm2', 'gcmx2dhz0g81', 'gchyvynu3ne0', 'gcjsxw3ztvtq', 'gcjvg7d7bx28', 'gcjsmt660upu', 
                     'gcjwwswdgrft', 'gcjm962ms3dr', 'gcmvg8328xz2', 'gcmyt0xj5rzf']

# Remove rows where 'site_id' contains any of the strings in the list

df_wales_cleaner = df_wales[~df_wales['site_id'].str.contains('|'.join(strings_to_remove))]


# In[17]:


df_wales_cleaner


# In[18]:


len(df_wales_cleaner)


# In[19]:


#suspicion is some Morrisons duplicates still exist - so filter on Morrisons using .str.contains

df_wales_cleaner[df_wales_cleaner['brand'].str.contains("Morrisons")]


# In[20]:


#CODE SUPERSEDED - USE THE site_id reference as above

# a number of duplicates still remain - remove again using the .drop method again

#df_wales_cleaner = df_wales_cleaner.drop(index = [1409, 1418, 1421, 1474])


# In[21]:


# manually check the above dataframe for Morrisons - see if any duplicates remain - and remove using the .str.contains method again

new_strings_to_remove = ['gcjtqv37tkgy', 'gcmwd1d3s9qj', 'gcjv9bypjmyh']

# Remove rows where 'site_id' contains any of the strings in the list

df_wales_much_cleaner = df_wales_cleaner[~df_wales_cleaner['site_id'].str.contains('|'.join(new_strings_to_remove))]


# #### We now have a clean and validated DataFrame of all Wales only fuel stations reporting to the UK Access Fuel site

# In[22]:


# returns the final number of rows of the dataframe

len(df_wales_much_cleaner)


# #### One final bit of housekeeping - in case we want to use the Latitude and Longitdue locations later
# **Rename them first - and then we want to change the figures from a string object to a real float number**

# In[23]:


#rename lat and longitude columns to single words

df_wales_lat = df_wales_much_cleaner.rename(columns={'location.latitude' : 'latitude', 'location.longitude' : 'longitude'})


# In[24]:


#convert lat and long from string object to float numbers

df_wales_lat['latitude'] = df_wales_lat.latitude.astype(float)
df_wales_lat['longitude'] = df_wales_lat.longitude.astype(float)


# #### Exporting the final DataFrame to an Excel file format - in this case stored on a hard-drive volume

# In[26]:


# export to file

# use datetime to append date to file name


current_date = datetime.now().strftime('%d-%m-%Y')

output = f'wales_fuel_prices_{current_date}.xlsx'


# In[27]:


# Specify the path to save the file 


#Requests user to add required path location:

path_to_save = input("Please type the path location to save your file, for example C:\Data or /Volumes/portable_drive/data (DO NOT ADD FILENAME")

path_to_save_expanded = os.path.expanduser(path_to_save)

# Full file path
file_path = os.path.join(path_to_save_expanded, output)


# In[28]:


#convert fuel DataFrame data to Excel format and store in directory specified above with date appended
try:
    df_wales_lat.to_excel(file_path, index=False)
    print(f"File successfully saved to {file_path}")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")


# In[ ]:




