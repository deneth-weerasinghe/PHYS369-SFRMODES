import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

path = os.getcwd() + '/PHYS369-SFRMODES'

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
    symbols = ['o', '^', 's', 'D']


    for j in range(0, 4):
        plt.errorbar(data[j][0], data[j][1], fmt=symbols[j], c=colours[j], alpha=0.4, fillstyle='none', markersize=5, ecolor='black', elinewidth=1, label=f'Stage {j+1}')
        # plt.scatter(mass_med, sfr_med, s=5, c=colours[j], label=f'Stage {j+1}')
    
    plt.title('Star formation rates in each stage of mergers within the COSMOS survey')
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log Star Formation Rate')
    plt.text(7.5, -5.5, f'n={n}', fontsize=25)
    plt.legend()
    plt.show()

def generate_plot_z_limit(data):

    colours = ['red', 'blue', 'green', 'purple']
    symbols = ['o', '^', 's', 'D']

    ms = 5
    ax1 = plt.subplot(221)
    plt.plot(data[0][0], data[0][1], linestyle='', ms=ms, marker=symbols[0], alpha=0.4, fillstyle='none' ,c=colours[0], label=f'Stage {1}\nn={len(data[0][0])}')
    plt.ylabel(r'log SFR [$M_{\bigodot} yr^{-1}]$')
    plt.tick_params('x', labelbottom=False)
    plt.legend(loc='lower left')

    ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
    plt.plot(data[1][0], data[1][1], ms=ms, linestyle='', marker=symbols[1], alpha=0.4, fillstyle='none' ,c=colours[1], label=f'Stage {2}\nn={len(data[1][0])}')
    plt.tick_params('y', labelleft=False)
    plt.tick_params('x', labelbottom=False)
    plt.legend(loc='lower left')

    ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)
    plt.plot(data[2][0], data[2][1], ms=ms, linestyle='', marker=symbols[2], alpha=0.4, fillstyle='none' ,c=colours[2], label=f'Stage {3}\nn={len(data[2][0])}')
    plt.xlabel(r'log $M_{\bigstar}$ [$M_{\bigodot}$]')
    plt.ylabel(r'log SFR [$M_{\bigodot} yr^{-1}]$')
    plt.legend(loc='lower left')

    ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)
    plt.plot(data[3][0], data[3][1], ms=ms, linestyle='', marker=symbols[3], alpha=0.4, fillstyle='none' ,c=colours[3], label=f'Stage {4}\nn={len(data[3][0])}')
    plt.xlabel(r'log $M_{\bigstar}$ [$M_{\bigodot}$]')
    plt.tick_params('y', labelleft=False)
    plt.legend(loc='lower left')

    plt.suptitle('Star formation rates of primary galaxy against stellar mass in each stage of mergers\n within the COSMOS survey for redshift volume 0<z<1.5')
    plt.ylim(-6.5, 3.5)
    plt.show()

def generate_separate(data):

    colours = ['red', 'blue', 'green', 'purple']
    symbols = ['o', '^', 's', 'D']

    ms = 5

    for n, j in enumerate(data):
        fig = plt.figure()

        # Figure settings
        fig.suptitle(f'Star formation rates of primary galaxies of stage {n+1}\nmergers in COSMOS, n={len(j[0])}')
        gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4),
                              left=0.1, right=0.9, bottom=0.1, top=0.9,
                              wspace=0.05, hspace=0.05)
        ax = fig.add_subplot(gs[1, 0])
        ax_hist_x = fig.add_subplot(gs[0, 0], sharex=ax)
        ax_hist_y = fig.add_subplot(gs[1, 1], sharey=ax)

        # Histogram axes
        ax_hist_x.tick_params(axis='x', bottom=False, labelbottom=False)
        ax_hist_y.tick_params(axis='y', left=False, labelleft=False)

        # Scatter plot
        ax.plot(j[0], j[1], ms=ms, linestyle='', marker=symbols[n], alpha=0.4, fillstyle='none' ,c=colours[n], label=f'Stage {n+1}')
        ax.set_xlabel(r'log $M_{\bigstar}$ [$M_{\bigodot}$]')
        ax.set_ylabel(r'log SFR [$M_{\bigodot} yr^{-1}]$')
        ax.set_ylim(-6.5, 3.5)
        ax.set_xlim(6.5, 12.5)

        # ax.contour(j[0], j[1])
        
        # Histogram
        binwidth = 0.25
        xymax = max(max(j[0]), max(j[1]))
        lim = (int(xymax/binwidth) + 1) * binwidth
        bins_x = np.arange(-lim, lim + binwidth, 0.15)
        bins_y = np.arange(-lim, lim + binwidth, binwidth)
        ax_hist_x.hist(j[0], bins=bins_x, color=colours[n], density=True)
        ax_hist_y.hist(j[1], bins=bins_y, color=colours[n], density=True, orientation='horizontal')

        ax_hist_x.set_ylabel('Probability density')
        ax_hist_y.set_xlabel('Probability density')
        
        plt.savefig(path+f'/plots/output/stage_{n+1}')
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

raw_data = data_gather()  # gathers the data from the csv

num = len(raw_data)

plot_data = generate_variables(raw_data)  # formats data so it's useful for the plotting function

# generate_plot(plot_data, num)  # plots with all stages on same graph

filtered_data = generate_variables(raw_data, isFiltering = True, z_lim=1.5)  # redefines plot_data to have the filtered values
# generate_plot_z_limit(filtered_data)  # generates 4 subplots, one for each stage

generate_separate(filtered_data)



