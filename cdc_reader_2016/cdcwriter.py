import csv

def cdcReader(csv_input):
    with open(csv_input,'r') as f:
        reader = csv.reader(f)
        headers = next(reader)

        all_data = []

        for row in reader:

            #survey_year = row[13]
            sex_code = row[6]
            race_code = row[11]
            male_orientation_code = row[625]
            female_orientation_code = row[626]

            if sex_code == '1':
                    sex_val = 'male'
            if sex_code == '2':
                    sex_val = 'female'
            if race_code == '1':
                    race_val = 'white'
            if race_code == '2':
                    race_val = 'black'
            if race_code == '3':
                    race_val = 'indian'
            if race_code == '6':
                    race_val = 'chinese'
            if race_code == '7':
                    race_val = 'filipino'
            if (male_orientation_code == '2') or (female_orientation_code == '2'):
                    orientation_val = 'straight'
            if (male_orientation_code == '3') or (female_orientation_code == '3'):
                    orientation_val = 'bisexual'
            if (male_orientation_code  == '1') or (female_orientation_code == '1'):
                    orientation_val = 'gay'
            if (male_orientation_code == '4') or (female_orientation_code == '4'):
                    orientation_val = 'something else'
            if (male_orientation_code == '5') or (female_orientation_code == '5'):
                    orientation_val = 'I do not know the answer'
            sex_and_orientation = sex_val,race_val,orientation_val
            all_data.append(sex_and_orientation)

        cdcWriter(all_data,'sex_and_orientation_NHISdata_2016.csv')

def cdcWriter(a_list,csv_output):
    with open(csv_output,'w') as f:
        writer = csv.writer(f)

        for a_row in a_list:
            writer.writerow(a_row)
                
cdcReader('AM_samadult_2016.csv')