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
                    #if (male_orientation_val = '')
                    #print(sex_val,orientation_val)
                    #add other orientations
                    
                    
with open("AM_pythoned_2016.csv", "w") as curated_2016:
	curated_2016.write(sex_val,orientation_val)
	#for line in curated_2016:
	#	print(line)
                    #write out to a new .csv file
                        
cdcReader('AM_samadult_2016.csv', 'AM_python_2016.csv')			
#write it out to csv with x axis as orientation value and y axis as frequency one csv for male, one csv for female

#increment counter 7 variables?
#if all else fails just produced csv.s in excel spread sheet form
#goals: visual graph figure out the structure historiograph structure or bargraph
    # with x axis as orientation value and y axis as frequency one csv for male, one csv for female

#other dataset info to follow:

#sex code HHC.110_00.000 Location 39
#Question Number for male sexual orientation question ACISIM ASI.220_00.000 Location 1047
#Question Number for female sexual orientation question ACISIF ASI.240_00.000 Location 1048