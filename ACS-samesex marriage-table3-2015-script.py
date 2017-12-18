import csv
with open('ACS-samesexmarriage-table3-2015.csv') as ACS_file:
    table = csv.reader(ACS_file)
    for a_col in table:
        print(a_col[0], a_col[1], a_col[3])