import os
import csv

'''
LEGACY FILE
Decided to use Topcat to match COSMOS objects with help from Brooke
'''
path = os.getcwd()  # obtains path of top-level directory

def match_COSMOS(i):
    myrows = []
    with open(path + '/data/csv/group_COSMOS.csv', newline='') as f1, open(path + f'/data/csv/COSMOS_survey/COSMOS_{i}_OUT.csv') as f2:
        group_data = csv.reader(f1)
        cosmos_data = csv.reader(f2)
        next(group_data)  
        next(cosmos_data)  # skips the headers

        offset = 0.00001
        tol = 0.001

        for group_row in group_data:
            for cosmos_row in cosmos_data:
                # ra_lower = float(row2[0]) - offset
                # ra_upper = float(row2[0]) + offset
                # dec_lower = float(row2[1]) - offset
                # dec_upper = float(row2[1]) + offset
                # print(ra_lower, row1[1], ra_upper, row2[0])
                # print(dec_lower, row1[2], dec_upper, row2[1])
                # if (ra_lower < float(row1[1]) < ra_upper) and (dec_lower < float(row1[2]) < dec_upper):
                    # myrows.append(row2)
                
                ra_diff = abs(float(group_row[2])-float(cosmos_row[0]))#abs(150.67986638-150.679866)
                ra_tol = tol*max(float(group_row[2]), float(cosmos_row[0]))#tol*max(150.67986638, 150.679866)
                dec_diff = abs(float(group_row[3])-float(cosmos_row[1]))#abs(2.1966146-2.196563)
                dec_tol = tol*max(float(group_row[3]), float(cosmos_row[1]))#tol*max(2.1966146, 2.196563)
                
                isRaMatching = ra_diff < ra_tol
                isDecMatching = dec_diff < dec_tol
                if isRaMatching and isDecMatching:
                    myrows.append(cosmos_row)
                    break
                    
    return myrows


total = 0
for i in range(0, 2):
    portion = len(match_COSMOS(i))
    total += portion
print(total)