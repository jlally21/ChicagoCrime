import csv

with open('2015murdersonly.csv','r') as csvinput:
    with open('2015murdersonlyoutput.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('offenseID')
        row.append('locationID')
        all.append(row)

        locationID = 1000

        for row in reader:
            if row[8] == 'false' and row[9] == 'false': #no arrest, no domestic
              row.append('AAA111')
            elif row[8] == 'false' and row[9] == 'true': #no arrest, yes domestic
              row.append('BBB222')
            elif row[8] == 'true' and row[9] == 'false': #yes arrest, no domesic
              row.append('CCC333')
            elif row[8] == 'true' and row[9] == 'true': #yes arrest, yes domestic
              row.append('DDD444')
            else:
              row.append('EEE555')

            row.append(locationID)
            locationID += 1
            
            all.append(row)

        writer.writerows(all)
