import sqlite3, csv

# this script populates the ChicagoMurders2015 database
# DROP DATABASE IF EXISTS ___ is not in sqlite so remove the file manually beforehand 

conn = sqlite3.connect('ChicagoMurders2015.db')
c = conn.cursor()


# Drop an existing location table
c.execute('''DROP TABLE location''')

# Create location table
c.execute('''CREATE TABLE location
             (locationID text, latitude text, longitude text, block text, locationdescription text, beat int, ward int)''')

# Populate the location table
with open('/home/jlally/Chicago/data/2015murdersonlyoutput.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['locationID'], i['Latitude'], i['Longitude'], i['Block'], i['Location Description'], i['Beat'], i['Ward']) for i in dr]

c.execute('DELETE FROM location')
c.executemany('INSERT INTO location (locationID, latitude, longitude, block, locationdescription, beat, ward) VALUES (?, ?, ?, ?, ?, ?, ?);', to_db)

#c.execute('SELECT * FROM location WHERE latitude > 0')
#print(c.fetchall())


# Drop an existing offense table
c.execute('''DROP TABLE offense''')

# Create offense table
c.execute('''CREATE TABLE offense
             (offenseID text, primary_type text, primary_description text, arrest text, UNIQUE(offenseID, primary_description, arrest))''')

# Populate the offense table
with open('/home/jlally/Chicago/data/2015murdersonlyoutput.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['offenseID'], i['Primary Type'], i['Description'], i['Arrest']) for i in dr]

c.execute('DELETE FROM offense')
c.executemany('INSERT OR IGNORE INTO offense (offenseID, primary_type, primary_description, arrest) VALUES (?, ?, ?, ?);', to_db)

#c.execute('SELECT * FROM offense')
#print(c.fetchall())


# Drop an existing incident table
# c.execute('''DROP TABLE incident''')

# Create incident table
c.execute('''CREATE TABLE incident
             (caseID text, date text, locationID text, offenseID text)''')

# Populate the incident table
with open('/home/jlally/Chicago/data/2015murdersonlyoutput.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ID'], i['Date'], i['locationID'], i['offenseID']) for i in dr]

c.execute('DELETE FROM incident')
c.executemany('INSERT OR IGNORE INTO incident (caseID, date, locationID, offenseID) VALUES (?, ?, ?, ?);', to_db)

c.execute('SELECT * FROM incident')
print(c.fetchall())



conn.commit()
conn.close()



