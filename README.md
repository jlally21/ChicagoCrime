# README

Steps for setting up VM
- download vmware
- new virtual machine (typical)
- installer disk image file: ubuntu-14.04.5
- create user name, password, etc. (20 gb, default settings)

Install Dependencies (https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
sudo apt-get install git
sudo apt-get update
sudo apt-get -y upgrade (takes a while)
sudo apt-get install -y python3-pip
sudo apt-get install vim
// pip3 install numpy --user (takes a while, optional?)
// pip3 install pandas --user (takes a while, optional?)
pip3 install bokeh --user 
pip3 install googlemaps

Clone and Build CSV file
At filepath /home/jlally/
create a directory Chicago and cd into it
git clone https://github.com/jlally21/ChicagoCrime
cd  into data directory
make sure 2015murdersonlyoutput.csv does not exist, if it does exist delete it
make sure 2015murdersonly.csv does exist
python3 finalizeCSV.py 
make sure 2015murdersonlyoutput.csv now exists

Create and Populate Database
cd into schema directory
remove ChicagoMurders2015.db if it exists in the schema directory
python3 initial_schema.py
now ChicagoMurders2015.db should exist in the schema directory
cp ChicagoMurders2015.db ../gmaps/   (this copies the ChicagoMurders2015.db into gmap directory)

Launch the Application
cd into gmap directory
python3 main.py (this will launch the application, hope you have fun)

Create Operations 
Click “Pair Cases”, Enter Valid Case Numbers and Description (example: 21940, 21901, test), click OK
Click “Add Officer”, Enter values for all the fields, click OK

Retrieve Operations
Click “Find and Map Cases”
If you know valid Beat, Ward, Block values (example: 732, 6, 071XX S UNION AVE), click OK [wait and map will open]
If you know one of the Case Numbers from Pair Cases (like 21940 or 21901, see above), enter the case number (example: 21940), check Map Paired Cases, click OK [wait and map will open displaying lat/long for 21940 and its “paired case” 21901]
If you know a date, (example 12/25/15), enter it, check Search by Date, click OK [wait and map will open]

Update Operations
Click “Update Data”
Enter a Valid Case Number  (example: 22236)
In “Change”, enter the new Value (example: this is a test description)
Select what attribute you want to change (example: select “Secondary Description”)
Click OK

Delete Operations
Click “Delete Case”
Enter a valid CaseID (example: 23183), Click OK
The Incident with CaseID = 23183 is now deleted from the database

