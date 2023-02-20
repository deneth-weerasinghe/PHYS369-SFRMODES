import csv
import os

path = os.getcwd()  # obtains path of top-level directory

def cosmos_count():
    with open(path + "/data/csv/full_table.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        count = 0
        for row in reader:
            if (148.0 < float(row[1]) < 152.0) and (1.3 < float(row[2]) < 3.5):  # checks if coords match range of COSMOS survey
                count += 1
        print(count)

cosmos_count()