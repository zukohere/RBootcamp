import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# Open and read csv
with open(cereal_csv) as csv_file:
    csv_reader=csv.reader(cereal_csv, delimiter = ",")
    #skip header row    
    csv_header = next(csv_file, None)
    print(csv_header)
    
    for row in csv_reader:
       # if float(row[7]) >= 5:
       #     print(row[0] + " has " + row(7))
#keep getting index out of range