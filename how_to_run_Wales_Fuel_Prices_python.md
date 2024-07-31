## WALES FUEL PRICES - quickrun instructions for Python script

**Download Files from Branch repository v 02:**

* Wales_Fuel_Prices_02.1.py
* requirements.txt
* run_script.py

Place these three files in the same folder/directory. Make sure that folder name - or the path to the folder does not have any spaces in the names i.e. /home/data project will not work - it would need to be /home/data_project


**Set-up virtual environment**

This step is optional - but HIGHLY recommended - as otherwise, you will be loading new python packages into the realtime python programme in your main directory. Working in a virtual environment avoids that, and can be quickly cleaned and deleted.

This presumes you have Python 3.4 installed:

At prompt:

*python3 -m venv venv*

FOR MACOS AND LINUX - at prompt:

*source venv/bin/activate*

FOR WINDOWS - either cmd.exe terminal or Powershell:

In cmd.exe

*venv\Scripts\activate.bat*

or if using PowerShell

*venv\Scripts\Activate.ps1*

The prompt should now show (venv) before the username and directory prompt.

At prompt type the following:

*python run_script.py Wales_Fuel_Prices_02.1.py*

That should execute the webscrapper - it takes 30 to 40 seconds to work through, as it is scrapping through over 4,000 json data points, filtering them, then passing 300 or so of those to an API to validate whether they are a Welsh based postcode.

When the script has run its course - it will ask for a folder/directory path input - this is where you will be saving your Excel file. Do not give it a name - just the folder/directory path - so for example /Volumes/hard_drive/data_stories or C:\data_stories

The script will return a message to say if the save has been successful.


