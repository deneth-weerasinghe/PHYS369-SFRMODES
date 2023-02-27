import os
import csv
import matplotlib.pyplot as plt

path = os.getcwd()

def data_gather(sample_size=100):

    data = []

    for j in range(0, 2):
        with open(path + f'/data/csv/COSMOS_survey/COSMOS_{j}_OUT.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)

            next(reader)
            '''
            Columns extracted:

            Index | Column Name | Notes
            2 | type | 0 = galaxy, 1 = star, 2 = X-ray source
            11 | mass_med | stellar mass from the pdf
            12 | mass_med_min68 | stellar mass lower limit, 68% confidence
            13 | mass_med_max68 | stellar mass upper limit, 68% confidence
            14 | mass_best | stellar mass from chi^2
            15 | sfr_med | star formation rate from the pdf
            16 | sfr_med_min68 | star formation rate lower limit, 68% confidence 
            17 | sfr_med__max68 | star formation rate upper limit, 68% confidence
            18 | sfr_best | star formation rate from chi^2
            '''
            for i, row in enumerate(reader):
                if i == sample_size:
                    break
                if row[2] == 0:  # checks if the source is a galaxy
                    data.append([row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]])
    return data





def generate_plot(data):
    mass_med = [i[0] for i in data]
    mass_low_err = [i[0] - i[1] for i in data]
    mass_upp_err = [i[2] - i[0] for i in data]
    sfr_med = [i[4] for i in data]
    sfr_low_err = [i[4] - i[5] for i in data]
    sfr_upp_err = [i[6] - i[4] for i in data]

    mass_err = [mass_low_err, mass_upp_err]
    sfr_err = [sfr_low_err, sfr_upp_err]

    plt.errorbar(mass_med, sfr_med, xerr=mass_err, yerr=sfr_err, fmt='o', c='red', ecolor='black', label='plot1')
    plt.title('Star formation rates in COSMOS mergers against stellar mass')
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log Star Formation Rate')
    plt.show()


mydata = data_gather(sample_size=1000)

generate_plot(mydata)

