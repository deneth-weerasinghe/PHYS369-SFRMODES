import os
import csv
import matplotlib.pyplot as plt

path = os.getcwd()

def data_gather():

    data = []

    with open(path + '/data/csv/group_cosmos_with_main_cosmos_matches_OUT2.csv', newline='') as csvfile:
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
        11 | mass_med | stellar mass from the pdf
        12 | mass_med_min68 | stellar mass lower limit, 68% confidence
        13 | mass_med_max68 | stellar mass upper limit, 68% confidence
        14 | mass_best | stellar mass from chi^2
        15 | sfr_med | star formation rate from the pdf
        16 | sfr_med_min68 | star formation rate lower limit, 68% confidence 
        17 | sfr_med__max68 | star formation rate upper limit, 68% confidence
        18 | sfr_best | star formation rate from chi^2
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
            data.append([row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], stage])
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
        mass_med = [data[i][0] for i in indices[j]]
        mass_low_err = [data[i][0] - data[i][1] for i in indices[j]]
        mass_upp_err = [data[i][2] - data[i][0] for i in indices[j]]
        sfr_med = [data[i][4] for i in indices[j]]
        sfr_low_err = [data[i][4] - data[i][5] for i in indices[j]]
        sfr_upp_err = [data[i][6] - data[i][4] for i in indices[j]]

        mass_err = [mass_low_err, mass_upp_err]
        sfr_err = [sfr_low_err, sfr_upp_err]

        
        # plt.errorbar(mass_med, sfr_med, xerr=mass_err, yerr=sfr_err, fmt='o', c=colours[j], markersize=1, ecolor='black', elinewidth=1, label=f'Stage {j+1}')
        plt.scatter(mass_med, sfr_med, s=5, c=colours[j], label=f'Stage {j+1}')
    
    plt.title('Star formation rates in each stage of mergers within the COSMOS survey')
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log Star Formation Rate')
    plt.legend()
    plt.show()


mydata = data_gather()
# print(len(mydata))
generate_plot(mydata)

