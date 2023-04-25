import csv

f = open('step9_1.csv', 'r')
reader = csv.reader(f)

   
for row in reader:
    print(row[2])

f.close()
