**Update: 31 07 2024 - Version 02.1 includes request to input excel file location to save it in a folder/directory. There is also a standalone python script, with a requirements.txt file to install necessary python dependencies - or you can use the run_script tool to execute the code. Recommended to run in a virtual environment - see full ReadMe in branch repository for 02.1**

*UPDATE: 26 07 2024 - Version 2 of notebook with site_id filters is available in branch repository*



---

#### What is Wales_Fuel_Prices?

The Wales_Fuel_Prices.ipynb file is a Jupyter Notebook file (v.7.02) written in the Anaconda environment (Anaconda Navigator 2.5.2)

It is a webscrapper that downloads fuel price data submitted by a large number of the UK's petrol forecourt sector, and is then filtered, and validated for Wales only postcodes, verified using the postcodes.io api.

It makes use of a number of dependencies - including BeautifulSoup4, Pandas, OS, DateTime, json, and requests.

The data is accessed from the UK Government's Access Fuel website, https://www.gov.uk/guidance/access-fuel-price-data, which provides weekly data supplied by voluntarily by a number of forecourt outlets -
including supermarkets and major petroleum firms. It is not every petrol forecourt - it is only those partcipating.


In the orginal version - the Morrisons and MFG data needs to be physically checked for duplicates - and the indexs returned deleted as necessary. This has been substantially updated in v2 and current v 02.1 in branch repository, to filter on site_ids rather than postcode duplicates.

The output files are in .xlsx format, using Pandas to_excel method (which requires the openpyxl dependency to be installed if run in a native python environment rather than through Anaconda)

In the original version - the script will need to be amended to select the path you require to save the Excel file - in the penultimate script section: 

```
# Specify the path to save the file 
path_to_save = os.path.expanduser('/PATH_YOU_REQUIRE_HERE')

```

This is updated in v 02.1 - which requests user to input directory/folder path location in


This is my very first attempt at a code project... so go easy on me!

Any queries - or improvements - please email me: george.herd@bbc.co.uk
