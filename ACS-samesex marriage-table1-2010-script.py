import csv
with open('ACS-samesexmarriage-table1-2010.csv') as ACS_file:
    table = csv.reader(ACS_file)
    for a_col in table:
        print(a_col[0], a_col[5], a_col[7], a_col[9])