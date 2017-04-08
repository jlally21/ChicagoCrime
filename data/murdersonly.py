import csv
with open('2015chicagonew.csv', 'r') as inp, open('2015murdersonly.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[5] == "HOMICIDE":
            writer.writerow(row)




