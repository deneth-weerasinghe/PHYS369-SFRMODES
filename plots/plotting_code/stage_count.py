import csv
import os

path = os.path.dirname(
    os.path.dirname(os.getcwd()))  # obtains path of top-level directory from which all subdirectories can be accessed


def stage_count(filename):
    with open(path + "\data\csv\group_subsets\\" + filename + ".csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        first_row = next(reader)  # prints the first row, as reference for column names

        counts = [0, 0, 0, 0]
        row_count = 0

        for row in reader:
            if row[4] == "true":  # check if stage one
                counts[0] += 1
            elif row[5] == "true":  # check if stage two
                counts[1] += 1
            elif row[6] == "true":  # check if stage three
                counts[2] += 1
            elif row[7] == "true":  # check if stage four
                counts[3] += 1
            row_count += 1
        display_list = [["Stage 1", "Stage 2", "Stage 3", "Stage 4"],
                        counts,
                        [round(i / row_count, 2) for i in counts]]
        print("====================================")
        print(filename + ":")
        for i in range(0, len(display_list[0])):
            print(display_list[0][i] + ": " + str(display_list[1][i]) + " | " + str(display_list[2][i]))
        print("====================================")


subset_list = ["emily_4000", "sofia_4000", "oscar_4000", "deneth_4000", "mason_4000"]

for i in subset_list:
    stage_count(i)
