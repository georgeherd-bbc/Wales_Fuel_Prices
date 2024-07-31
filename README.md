

## DESCRIPTION:

The Wales_Fuel_Prices.ipynb file is a Jupyter Notebook file (v.7.02) written in the Anaconda environment (Anaconda Navigator 2.5.2)

It is a webscrapper that downloads fuel price data submitted by a large number of the UK's petrol forecourt sector, and is then filtered, and validated for Wales only postcodes, verified using the postcodes.io api.

It makes use of a number of dependencies - including BeautifulSoup4, Pandas, OS, DateTime, json, and requests. Outside of Anaconda - if running as a Python Script - in Python 3.4 it will require the dependencies: 

* beautifulsoup4
* requests
* pandas
* openpyxl

These are included in a requirements.txt file

**Python script: Wales_Fuel_Prices_02.1.py**


### TO RUN THE PYTHON SCRIPT (best run in a virtual environment) using Python 3.4 - download the .py script and requirements.txt file to a desired folder location

#### In a terminal or cmd window - go to the path/directory where you have placed the python script Wales_Fuel_Prices_02.1.py
#### At prompt type:

*python3 -m venv venv*

#### This tells Python to create a new directory called venv, which is where your virtual enviroment will run from

#### At prompt:
**(FOR MACOS AND LINUX)**

*source venv/bin/activate*


(FOR WINDOWS either CMD or Powershell)

**In cmd.exe**

venv\Scripts\activate.bat

**In PowerShell**

venv\Scripts\Activate.ps1

#### Prompt should now have (venv) proceeding to indicate you are working in a virtual environment

#### The following commane will install all the necessary dependancies required to run the script:

*pip install -r requirements.txt*

#### run the script - which will ask you to input the path directory to save your excel file to:

*python Wales_Fuel_Prices_02.1.py*


#### NOTE: The script will take about 30 seconds to work - it's downloading and then filtering through 4,000 odd enteries scrapped from a dozen different locations. When it is completed - it will ask for the path directory.


ALTERNATIVELY - DOWNLOAD THE ADDITIONAL SCRIPT run_script.py into the same directory as the wales_fuel_prices and requirements.txt files

After going into a virtual environment - at prompt

python run_script.py Wales_Fuel_Prices_02.1.py

NOTE - ensure there are no spaces between names in the directory path - or Python will return an error.

#### TO get out of virtual environment at the end, at prompt:

deactivate

**You can now safely delete the venv directory folder**

rm -r venv






___


The data is accessed from the UK Government's Access Fuel website, https://www.gov.uk/guidance/access-fuel-price-data, which provides weekly data supplied by voluntarily by a number of forecourt outlets -
including supermarkets and major petroleum firms. It is not every petrol forecourt - it is only those partcipating - but it represents most of the major players in the sector.


This is my very first attempt at a code project... so go easy on me!

Any queries - or improvements - please email me: george.herd@bbc.co.uk
