import os
import csv
import matplotlib.pyplot as plt
import numpy as np

path = os.getcwd()

def abs_mag_z():

    data = []

    with open(path + '/data/csv/COSMOS_survey/COSMOS_0.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)

        next(reader)
        '''
        Columns extracted:

        Index | Column Name | Notes
        3 | zpdf | redshift, mean value
        4 | zpdf_l68 | z lower limit, 68% confidence
        5 | zpdf_h68 | z upper limit, 68% confidence
        6 | zminchi2 | z value from chi^2
        7 | chi2_best | reduced chi^2 for zminchi^2
        8 | m_i | absolute magnitude in i band

        '''
        for i, row in enumerate(reader):
            data.append([row[3], row[4], row[5], row[6], row[7], row[8]])
            if i == 4:
                break
        print(data)

abs_mag_z()