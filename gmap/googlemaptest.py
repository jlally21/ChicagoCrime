import gmplot

gmap=gmplot.GoogleMapPlotter(47.61028142523736,-122.34147349538826, 16)
gmap.marker(47.61028142523736, -122.34147349538826, title="A street corner in Seattle")
st="testmap.html"
gmap.draw(st)


# import gmplot

# gmap = gmplot.GoogleMapPlotter( 41.939943264, -87.651924995, 16)
# gmap.marker(41.939943264, -87.651924995, title='joe test')
#gmap.draw("mymap.html")

#import webbrowser
#file_name = 'file:///home/jlally/Chicago/schema/' + 'mymap.html'
#webbrowser.open_new_tab(file_name)
