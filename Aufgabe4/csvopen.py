import csv


new_list = []

s = '''
Tintenherz#2007#Cornelia Funke
Harry Potter - Halbblutprinz#2008#J.K.Rowling
Herr der Ringe#1954#J.Tolkien
Forecasting#2019#F.R.
'''.strip()
llist = s.split("\n")

for l in llist:
    new_list.append( l.split("#") )


fieldnames = ['Titel','Erscheinungsjahr','Autor']

with open("new.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow( fieldnames )
    for line in new_list:
        writer.writerow(line)
