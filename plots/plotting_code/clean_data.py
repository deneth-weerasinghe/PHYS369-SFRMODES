import os
import csv

'''
Removes any field that has at least one missing entry for any column
'''

path = os.getcwd()

def clean_data():
    with open(path + '/data/csv/group_cosmos_with_main_cosmos_matches.csv', 'r', newline='') as rdr, open(path + '/data/csv/group_cosmos_with_main_cosmos_matches_OUT1.csv', 'w') as wrt:
        reader = csv.reader(rdr)
        writer = csv.writer(wrt)
        for row in reader:
            flag = True
            i = 0
            while flag and i < len(row):  # iterates through all columns in a row
                if row[i] == '':
                    flag = False
                i += 1
            if flag:
                writer.writerow(row)



clean_data()
print('DONE!')

            
