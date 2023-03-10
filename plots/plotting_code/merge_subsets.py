import csv
import pandas as pd
import os

'''
Script to merge together each member's mergers that have been classified into each stage
'''
path = os.getcwd()  # obtains path of top-level directory from which all subdirectories can be accessed

subpath = path + "/data/csv/group_subsets/"


def merge_subsets():
    subset_list = ["emily_4000", "sofia_4000", "oscar_4000", "deneth_4000", "mason_4000"]
    files = []
    for i in subset_list:
        files.append(pd.read_csv(subpath + i + ".csv"))
    result = pd.concat(files)
    result.to_csv(path + "/data/csv/group_full_table.csv", index=False)


merge_subsets()
