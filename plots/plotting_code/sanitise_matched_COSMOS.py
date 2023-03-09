import os
import csv

'''
Script to check:
    1. If stage 4 fields have secondary values, if so, rewrite them to be blank
    2. If secondary mass is greater than primary, if so swap out all secondary with primary columns,
    as the primary galaxy is by definition the more massive one
'''

path = os.getcwd()

def write_column_key():
    '''
    Functions to save a list of all column names.
    Needed because there are so many columns that it's hard to keep track of.
    '''
    with open(path + '/data/csv/group_cosmos_with_main_cosmos_matches.csv', newline='') as r, open(path + '/data/csv/column_key.csv', 'w', newline='') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)

        columns = next(reader)

        for n, i in enumerate(columns):
            writer.writerow([n, i])


def rewrite_csv():
    with open(path + '/data/csv/group_cosmos_with_main_cosmos_matches_OUT1.csv', newline='') as r, open(path + '/data/csv/group_cosmos_with_main_cosmos_matches_OUT2.csv', 'w', newline='') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)

        columns = next(reader)
        writer.writerow(columns)

        for row in reader:
            new_row = row
            if row[7] == 'true':  # check if there are secondary values for stage 4, if so rewrite them to be blank
                for i in range(28, 48):
                    new_row[i] = ''
            elif float(row[39]) > float(row[19]):  # swaps _1 (primary) and _2 (secondary) values if _1 mass found to be greater than _2 mass
                for i in range(8, 48):
                    if i <= 27:
                        new_row[i] = row[i+20]
                    elif i > 27:
                        new_row[i] = row[i-20]
            for j in range(4, 8):
                if new_row[j] == 'true':
                    new_row[j] = 1
                elif new_row[j] == 'false':
                    new_row[j] = 0
            writer.writerow(new_row)






# write_column_key()

rewrite_csv()






