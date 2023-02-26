import os
import csv

path = os.getcwd()

def clean_data(n):
    with open(path + f'/data/csv/COSMOS_survey/COSMOS_{n}.csv', 'r', newline='') as rdr, open(path + f'/data/csv/COSMOS_survey/COSMOS_{n}_OUT.csv', 'w') as wrt:
        reader = csv.reader(rdr)
        writer = csv.writer(wrt)
        for row in reader:
            flag = True
            i = 0
            while flag and i < len(row):  # iterates through all columns in a row
                if row[i] == '':
                    flag = False
                    # print('found')
                i += 1
            if flag:
                writer.writerow(row)


for i in range(0, 2):
    clean_data(i)

print('DONE!')

            
