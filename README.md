The Wales_Fuel_Prices.ipynb file is a Jupyter Notebook file (v.7.02) written in the Anaconda environment (Anaconda Navigator 2.5.2)

It is a webscrapper that downloads fuel price data submitted by a large number of the UK's petrol forecourt sector, and is then filtered, and validated for Wales only postcodes, verified using the postcodes.io api.

It makes use of a number of dependencies - including BeautifulSoup4, Pandas, OS, DateTime, json, and requests.

The data is accessed from the UK Government's Access Fuel website, https://www.gov.uk/guidance/access-fuel-price-data, which provides weekly data supplied by voluntarily by a number of forecourt outlets -
including supermarkets and major petroleum firms. It is not every petrol forecourt - it is only those partcipating.

The output files are in .xlsx format, using Pandas to_excel method.

The script will need to be amended to select the path you require to save the Excel file - in the penultimate script section: 

```
# Specify the path to save the file 
path_to_save = os.path.expanduser('/PATH_YOU_REQUIRE_HERE')
```

This is my very first attempt at a code project... so go easy on me!

Any queries - or improvements - please email me: george.herd@bbc.co.uk
