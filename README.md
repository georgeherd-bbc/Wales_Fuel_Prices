*UPDATE: Version 2 - 26 07 2024*

Wales_Fuel_Prices_02.ipynb notebook is updated to use site_id codes from scrapped json data to filter for duplicate enteries made in the Morrisons/MFG data.

This should mean the Jupyter Notebook should continue to work to filter stations out, if the indexes change, due to count changes in reporting of stations.


*VERSION 1 - 25 07 2024*

The Wales_Fuel_Prices.ipynb file is a Jupyter Notebook file (v.7.02) written in the Anaconda environment (Anaconda Navigator 2.5.2)

It is a webscrapper that downloads fuel price data submitted by a large number of the UK's petrol forecourt sector, and is then filtered, and validated for Wales only postcodes, verified using the postcodes.io api.

It makes use of a number of dependencies - including BeautifulSoup4, Pandas, OS, DateTime, json, and requests. Outside of Anaconda - if running as a Python Script - in Python 3.4 it will require the dependencies: 

beautifulsoup4
requests
pandas
openpyxl

These will be included in a requirements.txt, which can be run with pip freeze in a virtual environment

___


The data is accessed from the UK Government's Access Fuel website, https://www.gov.uk/guidance/access-fuel-price-data, which provides weekly data supplied by voluntarily by a number of forecourt outlets -
including supermarkets and major petroleum firms. It is not every petrol forecourt - it is only those partcipating.


At present - the Morrisons and MFG data needs to be physically checked for duplicates - and the indexs returned deleted as necessary. This will be changed in a later version to use the IDs rather than indexes which can potentially change each week.

The output files are in .xlsx format, using Pandas to_excel method.

The script will need to be amended to select the path you require to save the Excel file - in the penultimate script section: 

```
# Specify the path to save the file 
path_to_save = os.path.expanduser('/PATH_YOU_REQUIRE_HERE')
```

This is my very first attempt at a code project... so go easy on me!

Any queries - or improvements - please email me: george.herd@bbc.co.uk
