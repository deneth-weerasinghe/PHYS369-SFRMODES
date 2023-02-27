import os
import csv

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
    with open(path + '/data/csv/group_cosmos_with_main_cosmos_matches.csv', newline='') as r:
        reader = csv.reader(r)

        columns = next(reader)

        for row in reader:
            if row[7] == 'true':  # check if there are secondary values for stage 4, if so rewrite them to be blank
                new_row = row
                for i in range(28, 48):
                    new_row[i] = ''
                print(new_row)
                break





# write_column_key()

# rewrite_csv()






