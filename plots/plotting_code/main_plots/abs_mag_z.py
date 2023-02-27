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

def generate_subplots(data):
    '''
    Generates 3 plots:
    * pdf with error bars
    * pdf with no error bars
    * chi^2 with no error bars
    '''

    z_pdf = [i[0] for i in data]
    z_chi2 = [i[3] for i in data]
    abs_mag = [i[5] for i in data]
    lower_err = [i[0] - i[1] for i in data]
    upper_err = [i[2] - i[0] for i in data]
    z_err = [lower_err, upper_err]

    # plot with error bars
    plt.subplot(311)
    plt.errorbar(z_pdf, abs_mag, xerr=z_err, fmt='o', c='red', ecolor='black', label='plot1')
    plt.title('Absolute i-band magnitude against pdf redshift, with errors')
    plt.xlabel('Redshift')
    plt.ylabel('Abs i-band magnitude')
    ax = plt.gca()
    ax.invert_yaxis()

    # plot with no error bars
    plt.subplot(312)
    plt.scatter(z_pdf, abs_mag, c='red', label='plot2')
    plt.title('Absolute i-band magnitude against pdf redshift')
    plt.xlabel('Redshift')
    plt.ylabel('Abs i-band magnitude')
    ax = plt.gca()
    ax.invert_yaxis()

    # plot with chi^2
    plt.subplot(313)
    plt.scatter(z_chi2, abs_mag, c='red', label='plot3')
    plt.title('Absolute i-band magnitude against chi^2 redshift')
    plt.xlabel('Redshift')
    plt.ylabel('Abs i-band magnitude')
    ax = plt.gca()
    ax.invert_yaxis()

    plt.tight_layout()
    plt.show()

def generate_plot(data, n):
    '''
    Only generates pdf with no error bars
    '''

    z_pdf = [i[0] for i in data]
    abs_mag = [i[5] for i in data]

    plt.scatter(z_pdf, abs_mag, c='red', label='mainplot')
    plt.title(f'Absolute i-band magnitude of the first {n} COSMOS objects against redshift')
    plt.xlabel('Redshift')
    plt.ylabel('Abs i-band magnitude')
    ax = plt.gca()
    ax.invert_yaxis()

    plt.show()

n = 1000
mydata = data_gather(sample_size=n)
print(len(mydata))
# generate_subplots(mydata)
# generate_plot(mydata, n)