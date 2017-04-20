import gmplot
import sqlite3
import webbrowser

def pair_cases(CN1, CN2, description):
    conn = sqlite3.connect('ChicagoMurders2015.db')
    c = conn.cursor()
    c.execute('INSERT INTO detective_connections values (?, ?, ?)', (CN1, CN2, description))
    conn.commit()
    print("Update complete", CN1, CN2, description)
    conn.close()

def create_detective(DID, name, title, badge_no, station, caseID):
    conn = sqlite3.connect('ChicagoMurders2015.db')
    c = conn.cursor()
    c.execute('INSERT INTO detective values (?, ?, ?, ?, ?,?)', (DID, name, title, badge_no, station, caseID))
    conn.commit()
    print("Update complete", DID, name, title, badge_no, station, caseID)
    conn.close()


def delete_case(CN):
    conn = sqlite3.connect('ChicagoMurders2015.db')
    c = conn.cursor()
    c.execute('DELETE FROM incident WHERE caseID = ?', (CN,))
    conn.commit()
    print("Deletion complete")
    conn.close()
def update_case(CN, change, location):
    conn = sqlite3.connect('ChicagoMurders2015.db')
    c = conn.cursor()
    if location == 'Date':
        c.execute('UPDATE incident SET date = ?  WHERE caseID = ?', (change, CN))
    elif location == 'Domestic':
        c.execute('UPDATE offense SET domestic = ?  WHERE offense.offenseID IN ( SELECT offenseID FROM incident WHERE caseID = ?)', (change, CN))
    elif location == 'Arrest':
        c.execute('UPDATE offense SET arrest = ?  WHERE offense.offenseID IN ( SELECT offenseID FROM incident WHERE caseID = ?)', (change, CN))
    elif location == 'Latitude':
        c.execute('UPDATE location SET latitude = ?  WHERE location.locationID IN ( SELECT locationID FROM incident WHERE caseID = ?)', (float(change), CN))
    elif location == 'Longitude':
        c.execute('UPDATE location SET longitude = ?  WHERE location.locationID IN ( SELECT locationID FROM incident WHERE caseID = ?)', (float(change), CN))
    elif location == 'Block':
        c.execute('UPDATE location SET block = ?  WHERE location.locationID IN ( SELECT locationID FROM incident WHERE caseID = ?)', (change, CN))
    elif location == 'Beat':
        c.execute('UPDATE location SET beat = ?  WHERE location.locationID IN ( SELECT locationID FROM incident WHERE caseID = ?)', (int(change), CN))
    elif location == 'Ward':
        c.execute('UPDATE location SET ward = ?  WHERE location.locationID IN ( SELECT locationID FROM incident WHERE caseID = ?)', (int(change), CN))
    elif location == 'Primary Description':
        c.execute('UPDATE offense SET primary_type = ?  WHERE offense.offenseID IN ( SELECT offenseID FROM incident WHERE caseID = ?)', (change, CN))
    elif location == 'Secondary Description':
        c.execute('UPDATE offense SET primary_description = ?  WHERE offense.offenseID IN ( SELECT offenseID FROM incident WHERE caseID = ?)', (change, CN))
        print("in secondary description case")
    conn.commit()
    print("Update complete")
    conn.close()
def retrieveLatLong_d(date):
  conn = sqlite3.connect('ChicagoMurders2015.db')
  c = conn.cursor()
  c.execute('SELECT firstselect.latitude, firstselect.longitude FROM (SELECT * FROM incident JOIN location ON incident.locationID = location.locationID) as firstselect WHERE firstselect.date LIKE ?', (date,))
  latlongs = c.fetchall()
  conn.close()
  return latlongs
def retrieveLatLong_l(location):
  conn = sqlite3.connect('ChicagoMurders2015.db')
  c = conn.cursor()
  c.execute('SELECT latitude, longitude FROM location WHERE beat = ? and ward = ? and block = ?',  (int(location[0]), int(location[1]), location[2]),)
  latlongs = c.fetchall()
  conn.close()
  return latlongs


def renderLatLong(latlongs):
  try:
      gmap = gmplot.GoogleMapPlotter(latlongs[0][0], latlongs[0][1], 10)
      for x in latlongs:
        if x[0] !='' and x[1] !='' and x[0] != '\n' and x[1] != '\n':
            lat = float(x[0])
            print(lat)
            lon = float(x[1])
            print(lon)
            gmap.marker(lat, lon, title='Crime')
            gmap.draw("testLatLonRender.html")
      file_name = 'file:///home/jlally/Chicago/gmap/' + 'testLatLonRender.html'
      webbrowser.open_new_tab(file_name)
  except IndexError:
      print('NO VALUES FOUND')
def retrieveLatLong_CN(CN):
  conn = sqlite3.connect('ChicagoMurders2015.db')
  c = conn.cursor()
  print(CN)
  c.execute('SELECT latitude, longitude FROM location JOIN incident ON incident.caseID = ? and incident.locationID = location.locationID',  (int(CN),))
  latlong = c.fetchone()
  conn.close()
  return latlong
def getPairs(CN):
  output = []
  conn = sqlite3.connect('ChicagoMurders2015.db')
  c = conn.cursor()
  c.execute('SELECT caseID2 FROM detective_connections WHERE caseID1 = ?',  (int(CN),))
  pairs = c.fetchall()
  print (pairs)
  CN = (CN,)
  pairs.append(CN)
  print (pairs)
  for item in pairs:
    output.append(retrieveLatLong_CN(item[0]))
  conn.close()
  return output
def render(type, arguments):
    if type == 'Date':  
        date = arguments+'%'
        print(date)
        latlongs = retrieveLatLong_d(date)
        print(latlongs)
        renderLatLong(latlongs)
    elif type == 'DateLocation':
        date = arguments[3]
        location = arguments[:3]
        latlongs1 = retrieveLatLong_d(date)
        latlongs2 = retrieveLatLong_l(location)
        common_latlongs = []
        for pair1 in latlongs1:
            for pair2 in latlongs2:
                if pair1 == pair2 and pair1 not in common_latlongs:
                    common_latlongs.append(pair1)
        renderLatLong(common_latlongs)
    elif type == 'Location':
        latlongs = retrieveLatLong_l(arguments)
        print(latlongs)
        renderLatLong(latlongs)
    elif type == 'CN':
        latlong = retrieveLatLong_CN(arguments)
        renderLatLong(latlong)
    elif type == 'CNPair':
        latlongs = getPairs(arguments)
        print("in CNPair", arguments) 
        print( latlongs )
        renderLatLong(latlongs)
