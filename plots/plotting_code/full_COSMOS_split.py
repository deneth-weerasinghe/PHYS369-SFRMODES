import pandas as pd
import os
'''
Script to split the full COSMOS dataset into two halves for easier git handling.
Since I can't push the original file, this script won't work unless I re-download the dataset from IRSA.
'''
path = os.getcwd()  # obtains path of top-level directory

def full_COSMOS_split():
    with pd.read_csv(path + '/data/csv/full_COSMOS.csv', chunksize=1182090/2) as reader:
        for i, chunk in enumerate(reader):
            chunk.to_csv(path + f'/data/csv/COSMOS_survey/COSMOS_{i}.csv', index=False, header=True)


full_COSMOS_split()
