#objective_1= isolate question in survey ASL220_00.000 male How do you think of yourself (sexual orientation) multiple choice 2016
#objective_2 = isolate question in survey ASL240_00.000 female How do you think of yourself (sexual orientation) multiple choice 2016
#overall objective, repeat for each survey from 2016, 2014 and compare results for bisexual choice in sexual orientation question for male and female
#check if question is the same for 2014 in code and placement. repeat for that dataset as well
import csv

f = open("samadult_2016.csv")
csv_f = csv.reader(f)
#determine male or female based on column_x sex question 1 for male, 2 for female #g collum equals [6] x
for all in csv_f:
    sex_code = all[6]
    question_male = all[625]
    question_female = all[626]
    
    try:
        if int(sex_code) == 1:
            print(question_male, "male")
        #add write command to write out the record of males and their responses to the sex orientation question 
        
        else:
            print(question_female, "female")
            #add write command to write out the record of females and their responses to the sex orientation question
            
    except:
        print(sex_code, "nonbinary")
            
   #having trouble under here with getting except to be accepted 
   #try:
       # if int(question_male) == 3:
        #    print("bisexual")
        
     #   else int(question_male) == 2:
      #      print("str8")
            
            
f.close()
#next step: find column that corresponds with ASL220_00.000 and ASL240_00.000 x
    #asisim male sex orientation wz 624
    #asisif female sex orientation xa 625


#import another dataset
    
#do same shit
    
#write to a json file of just those datasets from larger national survey

#compare together surveys using a visual tool