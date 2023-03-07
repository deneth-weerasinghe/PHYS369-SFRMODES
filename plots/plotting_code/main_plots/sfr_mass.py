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





def generate_plot(data, n):

    colours = ['red', 'blue', 'green', 'purple']

    for j in range(0, 4):
        plt.errorbar(data[j][0], data[j][1], xerr=data[j][2], yerr=data[j][3], fmt='o', c=colours[j], markersize=1, ecolor='black', elinewidth=1, label=f'Stage {j+1}')
        # plt.scatter(mass_med, sfr_med, s=5, c=colours[j], label=f'Stage {j+1}')
    
    plt.title('Star formation rates in each stage of mergers within the COSMOS survey')
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log Star Formation Rate')
    plt.text(7.5, -5.5, f'n={n}', fontsize=25)
    plt.legend()
    plt.show()

def generate_plot_z_limit(data):

    plt_data = []
    for i in data:
        plt_data.append([i[0], i[1]])

    colours = ['red', 'blue', 'green', 'purple']
    symbols = ['o', '^', 's', 'D']

    ms = 5
    ax1 = plt.subplot(221)
    plt.plot(plt_data[0][0], plt_data[0][1], linestyle='', ms=ms, marker=symbols[0], alpha=0.4, fillstyle='none' ,c=colours[0], label=f'Stage {1}, n={plt_data[0][0]}')
    plt.ylabel(r'log SFR [$M_{\bigodot} yr^{-1}]$')
    plt.tick_params('x', labelbottom=False)
    plt.legend()

    ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
    plt.plot(plt_data[1][0], plt_data[1][1], ms=ms, linestyle='', marker=symbols[1], alpha=0.4, fillstyle='none' ,c=colours[1], label=f'Stage {2}, n={plt_data[1][0]}')
    plt.tick_params('y', labelleft=False)
    plt.tick_params('x', labelbottom=False)
    plt.legend()

    ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)
    plt.plot(plt_data[2][0], plt_data[2][1], ms=ms, linestyle='', marker=symbols[2], alpha=0.4, fillstyle='none' ,c=colours[2], label=f'Stage {3}, n={plt_data[2][0]}')
    plt.xlabel(r'log $M_{\bigstar}$ [$M_{\bigodot}$]')
    plt.ylabel(r'log SFR [$M_{\bigodot} yr^{-1}]$')
    plt.legend()

    ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)
    plt.plot(plt_data[3][0], plt_data[3][1], ms=ms, linestyle='', marker=symbols[3], alpha=0.4, fillstyle='none' ,c=colours[3], label=f'Stage {4}, n={plt_data[3][0]}')
    plt.xlabel(r'log $M_{\bigstar}$ [$M_{\bigodot}$]')
    plt.tick_params('y', labelleft=False)
    plt.legend()

    plt.suptitle('Star formation rates of primary galaxy against stellar mass in each stage of mergers\n within the COSMOS survey for redshift volume 0<z<1.5')
    plt.ylim(-6.5, 3.5)
    plt.show()

def generate_variables(old_data, isFiltering=False, z_lim=None):

    if isFiltering:
        data = []
        for i in old_data:  # filters out data that doesn't fall in the z volume bin
            if i[9] < z_lim:
                data.append(i)
    
    data = old_data
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

    output = []
    for j in range(0, 4):  #  generates lists of data for each of the four stages
        mass_med = [data[i][0] for i in indices[j]]  # List of x-axis values
        mass_low_err = [data[i][0] - data[i][1] for i in indices[j]]
        mass_upp_err = [data[i][2] - data[i][0] for i in indices[j]]
        sfr_med = [data[i][4] for i in indices[j]]  # List of y-axis values
        sfr_low_err = [data[i][4] - data[i][5] for i in indices[j]]
        sfr_upp_err = [data[i][6] - data[i][4] for i in indices[j]]

        mass_err = [mass_low_err, mass_upp_err]
        sfr_err = [sfr_low_err, sfr_upp_err]
        output.append([mass_med, sfr_med, mass_err, sfr_err])
    
    return output


raw_data = data_gather()

num = len(raw_data)

plot_data = generate_variables(raw_data)

# generate_plot(plot_data, num)

plot_data = generate_variables(raw_data, isFiltering = True, z_lim=1.5)  # redefines plot_data to have the filtered values
generate_plot_z_limit(plot_data)

