import numpy as np
import matplotlib.pyplot as plt
import csv
import os

path = os.path.dirname(os.path.dirname(os.getcwd()))  # obtains path of top-level directory


def plot():
    with open(path + "\data\csv\sample_data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        first_row = next(reader)  # prints the first row, as reference for column names
        print(first_row)

        mass_med = []
        sfr_med = []
        sfr_med_MIN_ERR = []
        sfr_med_MAX_ERR = []
        sfr_best = []

        for row in reader:
            mass_med.append(row[8])

            sfr_med.append(row[12])
            sfr_med_MAX_ERR.append(row[12] - row[13])
            sfr_med_MIN_ERR.append(row[14] - row[12])

            sfr_best.append(row[15])

        error1 = np.array([sfr_med_MIN_ERR, sfr_med_MAX_ERR])
        # print(error1)

        plt.rcParams['text.usetex'] = True
        plt.errorbar(mass_med, sfr_med, yerr=error1, c="blue", fmt="o", label="SFR_MED")
        plt.errorbar(mass_med, sfr_best, c="red", fmt="o", label="SFR_BEST")
        plt.title("Logarithmic Stellar Mass against SFR (median pdf) and SFR (minimum of $\chi^2$)")
        plt.xlabel("log MASS_MED")
        plt.ylabel("log SFR")
        plt.legend()
        plt.show()


def plot_coords(x, y):
    fig = plt.scatter(x, y, label="Position of sample sources")
    plt.xlabel("Right ascension")
    plt.ylabel("Declination")
    plt.ticklabel_format(useOffset=False)
    plt.gca().invert_xaxis()
    plt.show()


def plot_sfr(x, y):
    fig = plt.scatter(x, y, label="Logarithmic Median SFR and chi^2 SFR against Median Stellar Mass")
    plt.xlabel("Median Stellar Mass")
    plt.ylabel("Stellar Formation Rate")
    plt.show()


plot()
