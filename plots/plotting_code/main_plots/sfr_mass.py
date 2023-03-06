import os
import csv
import matplotlib.pyplot as plt

path = os.getcwd()

def data_gather():

    data = []

    with open(path + '/PHYS369-SFRMODES/data/csv/group_cosmos_with_main_cosmos_matches_OUT2.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)

        next(reader)
        '''
        Columns extracted:

        Index | Column Name | Notes
        2 | type | 0 = galaxy, 1 = star, 2 = X-ray source
        4 | isStageOne | indicates merger stage, 1 for true and 0 for false
        5 | isStageTwo | ^
        6 | isStageThree | ^
        7 | isStageFour | ^
        19 | mass_med_1 | stellar mass from the pdf
        20 | mass_med_min68_1 | stellar mass lower limit, 68% confidence
        21 | mass_med_max68_1 | stellar mass upper limit, 68% confidence
        22 | mass_best_1 | stellar mass from chi^2
        23 | sfr_med_1 | star formation rate from the pdf
        24 | sfr_med_min68_1 | star formation rate lower limit, 68% confidence 
        25 | sfr_med__max68_! | star formation rate upper limit, 68% confidence
        26 | sfr_best_1 | star formation rate from chi^2
        11 | z_pdf_1 | redshift
        '''
        for row in reader:
            if row[4] == 1:  # creates new field storing which stage of the merger it is
                stage = 1
            elif row[5] == 1:
                stage = 2
            elif row[6] == 1:
                stage = 3
            elif row[7] == 1:
                stage = 4
            data.append([row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], stage, row[11]])
    return data





def generate_plot(data):
    stage_ones = []  # list containing all indices corresponding to stage 1
    stage_twos = []  # likewise for stage 2
    stage_threes = []  # ^
    stage_fours = []  # ^

    for n, g in enumerate(data):  # generate the above lists
        if g[8] == 1:
            stage_ones.append(n)
        elif g[8] == 2:
            stage_twos.append(n)
        elif g[8] == 3:
            stage_threes.append(n)
        elif g[8] == 4:
            stage_fours.append(n)

    indices = [stage_ones, stage_twos, stage_threes, stage_fours]
    colours = ['red', 'blue', 'green', 'purple']

    for j in range(0, 4):
        mass_med = [data[i][0] for i in indices[j]]  # List of x-axis values
        mass_low_err = [data[i][0] - data[i][1] for i in indices[j]]
        mass_upp_err = [data[i][2] - data[i][0] for i in indices[j]]
        sfr_med = [data[i][4] for i in indices[j]]  # List of y-axis values
        sfr_low_err = [data[i][4] - data[i][5] for i in indices[j]]
        sfr_upp_err = [data[i][6] - data[i][4] for i in indices[j]]

        # Errors
        mass_err = [mass_low_err, mass_upp_err]
        sfr_err = [sfr_low_err, sfr_upp_err]
        # print(mass_med[0])

        
        # plt.errorbar(mass_med, sfr_med, xerr=mass_err, yerr=sfr_err, fmt='o', c=colours[j], markersize=1, ecolor='black', elinewidth=1, label=f'Stage {j+1}')
        plt.scatter(mass_med, sfr_med, s=5, c=colours[j], label=f'Stage {j+1}')
    
    plt.title('Star formation rates in each stage of mergers within the COSMOS survey')
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log Star Formation Rate')
    plt.text(7.5, -5.5, f'n={n}', fontsize=25)
    plt.legend()
    plt.show()

def generate_plot_z_limit(old_data, z_limit=1.5):

    data = []

    for i in old_data:
        if i[9] < z_limit:
            data.append(i)


    stage_ones = []  # list containing all indices corresponding to stage 1
    stage_twos = []  # likewise for stage 2
    stage_threes = []  # ^
    stage_fours = []  # ^

    for n, g in enumerate(data):  # generate the above lists
        if g[8] == 1:
            stage_ones.append(n)
        elif g[8] == 2:
            stage_twos.append(n)
        elif g[8] == 3:
            stage_threes.append(n)
        elif g[8] == 4:
            stage_fours.append(n)

    indices = [stage_ones, stage_twos, stage_threes, stage_fours]
    colours = ['red', 'blue', 'green', 'purple']

    symbols = ['o', '^', 's', 'D']
    for j in range(0, 4):
        mass_med = [data[i][0] for i in indices[j]]  # List of x-axis values
        mass_low_err = [data[i][0] - data[i][1] for i in indices[j]]
        mass_upp_err = [data[i][2] - data[i][0] for i in indices[j]]
        sfr_med = [data[i][4] for i in indices[j]]  # List of y-axis values
        sfr_low_err = [data[i][4] - data[i][5] for i in indices[j]]
        sfr_upp_err = [data[i][6] - data[i][4] for i in indices[j]]

        # Errors
        mass_err = [mass_low_err, mass_upp_err]
        sfr_err = [sfr_low_err, sfr_upp_err]
        # print(mass_med[0])

        plt.subplot(2, 2, j+1)
        # plt.errorbar(mass_med, sfr_med, xerr=mass_err, yerr=sfr_err, fmt='o', c=colours[j], markersize=1, ecolor='black', elinewidth=1, label=f'Stage {j+1}')
        plt.scatter(mass_med, sfr_med, s=15,marker=symbols[j] ,c=colours[j], label=f'Stage {j+1}')
        plt.legend()
    
    plt.suptitle(f'Star formation rates in each stage of \n mergers within the COSMOS survey for z<1.5, n={n}')
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log Star Formation Rate')
    plt.show()

mydata = data_gather()
# print(len(mydata))
# generate_plot(mydata)
generate_plot_z_limit(mydata)

