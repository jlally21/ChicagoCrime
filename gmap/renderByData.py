import gmplot
import sqlite3
import webbrowser

#import webbrowser
#gmap=gmplot.GoogleMapPlotter(47.61028142523736,-122.34147349538826, 16)
#gmap.marker(47.61028142523736, -122.34147349538826, title="A street corner in Seattle")
#st="testmap.html"
#gmap.draw(st)

def retrieveLatLong(date):
  conn = sqlite3.connect('ChicagoMurders2015.db')
  c = conn.cursor()
  c.execute('SELECT latitude, longitude, date FROM (SELECT * FROM incident JOIN location ON incident.locationID = location.locationID) as firstselect WHERE firstselect.date LIKE ?', (('%'+ date+'%'),))
  latlongs = c.fetchall()
  return latlongs


def renderLatLong(latlongs):
  gmap = gmplot.GoogleMapPlotter(latlongs[0][0], latlongs[0][1], 10)
  for x in latlongs:
    lat = float(x[0])
    print(lat)
    lon = float(x[1])
    print(lon)
    gmap.marker(lat, lon, title=x[2])
    gmap.draw("testLatLonRender.html")
  file_name = 'file:///home/jlally/Chicago/gmap/' + 'testLatLonRender.html'
  webbrowser.open_new_tab(file_name)




def render(date):
  date2 = date + '%'
  print(date2)
  latlongs = retrieveLatLong(date2)
  renderLatLong(latlongs)

# gmap = gmplot.GoogleMapPlotter( 41.939943264, -87.651924995, 16)
# gmap.marker(41.939943264, -87.651924995, title='joe test')
#gmap.draw("mymap.html")

#import webbrowser
#file_name = 'file:///home/jlally/Chicago/schema/' + 'mymap.html'
#webbrowser.open_new_tab(file_name)
