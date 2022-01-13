import csv 
file = open("E:\python\csv.csv")
reader = csv.reader(file)
header = []
header = next(reader)
header
rows = []
for rows in reader:
    rows.append(rows)
rows
print(header)
print(rows)
file.close()
