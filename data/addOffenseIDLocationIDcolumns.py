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
            if row[8] == 'false':
              row.append('AAA111')
            elif row[8] == 'true':
              row.append('BBB222')
            else:
              row.append('CCC333')

            row.append(locationID)
            locationID += 1
            
            all.append(row)

        writer.writerows(all)
