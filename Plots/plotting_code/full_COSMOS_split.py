import pandas as pd
import os

path = os.getcwd()  # obtains path of top-level directory

def full_COSMOS_split():
    with pd.read_csv(path + '/data/csv/full_COSMOS.csv', chunksize=1182090/2) as reader:
        for i, chunk in enumerate(reader):
            chunk.to_csv(path + f'/data/csv/COSMOS_survey/COSMOS_{i}.csv', index=False, header=True)


full_COSMOS_split()