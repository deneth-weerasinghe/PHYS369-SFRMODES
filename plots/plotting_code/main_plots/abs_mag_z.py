import os
import csv
import matplotlib.pyplot as plt

path = os.getcwd()

def data_gather():

    data = []

    with open(path + '/data/csv/group_cosmos_with_main_cosmos_matches_OUT2.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)

        next(reader)  # skips headers

        '''
        Columns extracted

        Note the _1 indicates properties of the primary object in the merger
        i.e. the more massive one while _2 indicates the secondary object.

        Index | Column Name | Notes
        4 | isStageOne | indicates merger stage, 1 for true and 0 for false
        5 | isStageTwo | ^
        6 | isStageThree | ^
        7 | isStageFour | ^
        10 | type_1 | 0 = galaxy, 1 = star, 2 = X-ray source
        11 | zpdf_1 | redshift, mean value
        12 | zpdf_l68_1 | z lower limit, 68% confidence
        13 | zpdf_h68_1 | z upper limit, 68% confidence
        14 | zminchi2_1 | z value from chi^2
        15 | chi2_best_1 | reduced chi^2 for zminchi^2
        16 | m_i_1 | absolute magnitude in i band
        30 | type_2 | 0 = galaxy, 1 = star, 2 = X-ray source (secondary)
        '''

        for row in reader:
            if row[4] == 1:  # creates new field storing which stage of the merger it is
                stage = 0
            elif row[5] == 1:
                stage = 1
            elif row[6] == 1:
                stage = 2
            elif row[7] == 1:
                stage = 3

            if row[10] == 0 and row[30] == 0:  # checks if both objects in the merger are galaxies
                data.append([row[11], row[12], row[13], row[14], row[15], row[16], stage])
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

def generate_plot(data):
    '''
    Only generates pdf with no error bars
    '''

    z_pdf = [i[0] for i in data]
    abs_mag = [i[5] for i in data]

    plt.scatter(z_pdf, abs_mag, c='red', s=1, label='mainplot')
    plt.title(f'Absolute i-band magnitude of primary galaxy in selected mergers in COSMOS against redshift')
    plt.xlabel('Redshift')
    plt.ylabel('Abs i-band magnitude')
    ax = plt.gca()
    ax.invert_yaxis()

    plt.show()


mydata = data_gather()
# print(len(mydata))
# generate_subplots(mydata)
generate_plot(mydata)