import csv

f = open('step9_2.csv', 'w',newline='')
writer = csv.writer(f)
header = ['Age', 'Name']

data = [[50,'makoto'],[40,'midori'],[30,'kaoru']]
writer.writerow(header)
writer.writerows(data)

f.close()
