import csv

def cdcReader(csvfile):
	with open(csvfile,'r') as f:
		reader = csv.reader(f)
		headers = next(reader)
		for row in reader:

                    sex_code = row[6]
                    male_orientation_code = row[625]
                    female_orientation_code = row[626]

                    if sex_code == '1':
                            sex_val = 'male'
                    if sex_code == '2':
                            sex_val = 'female'
                    if (male_orientation_code == '2') or (female_orientation_code == '2'):
                            orientation_val = 'straight'
                    if (male_orientation_code == '3') or (female_orientation_code == '3'):
                            orientation_val = 'bisexual'
                    if (male_orientation_code  == '1') or (female_orientation_code == '1'):
                            orientation_val = 'gay'
                    file.write (sex_val,orientation_val)
#add all other identities as well in if statements
                    
                    #write out to a new .csv file
cdcReader('AM_samadult_2014.csv')			