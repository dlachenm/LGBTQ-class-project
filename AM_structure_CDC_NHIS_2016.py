#objective_1= isolate question in survey ASL220_00.000 male How do you think of yourself (sexual orientation) multiple choice 2016 
#objective_2 = isolate question in survey ASL240_00.000 female How do you think of yourself (sexual orientation) multiple choice 2016
#overall objective, repeat for each survey from 2016, 2014 and compare results for bisexual choice in sexual orientation question for male and female
#check if question is the same for 2014 in code and placement. repeat for that dataset as well
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
                    print(sex_val,orientation_val)
                        
cdcReader('AM_samadult_2016.csv')			
#write it out to csv
#increment counter 8 variables
#visual graph figure out the structure 
#determine male or female based on column_x sex question 1 for male, 2 for female #g collum equals [6] x
#next step: find column that corresponds with ASL220_00.000 and ASL240_00.000 x
    #asisim male sex orientation wz 624 x
    #asisif female sex orientation xa 625 x


#translate numbers and tally male bi and female bi
#create visualization with dataset?

#import other dataset

#sex code HHC.110_00.000 Location 39
#Question Number for male sexual orientation question ACISIM ASI.220_00.000 Location 1047
#Question Number for female sexual orientation question ACISIF ASI.240_00.000 Location 1048

#do same shit
# i am too basic for seaborn. Will use matplotlib.org