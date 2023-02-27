import os
import csv
import matplotlib.pyplot as plt

path = os.getcwd()

def data_gather(sample_size=100):

    data = []

    with open(path + '/data/csv/COSMOS_survey/COSMOS_0_OUT.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)

        next(reader)
        '''
        Columns extracted:

        Index | Column Name | Notes
        2 | type | 0 = galaxy, 1 = star, 2 = X-ray source
        3 | zpdf | redshift, mean value
        4 | zpdf_l68 | z lower limit, 68% confidence
        5 | zpdf_h68 | z upper limit, 68% confidence
        6 | zminchi2 | z value from chi^2
        7 | chi2_best | reduced chi^2 for zminchi^2
        8 | m_i | absolute magnitude in i band

        '''
        for i, row in enumerate(reader):
            if i == sample_size:
                break
            if row[2] == 0:  # checks if the source is a galaxy
                data.append([row[3], row[4], row[5], row[6], row[7], row[8]])
    return data