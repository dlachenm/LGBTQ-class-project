#load json
#make it a dictionary
import json
#with open ('all_data_posturemag.json', 'r') as
data = json.load (open ('all_data_huffington.json'))
#print (data)

counter={
    '2016':0,
    '2014': 0,
    '2015': 0,
}

for article in data:
    year = article['date'].split()[0]
    year= year.split('/')[2]
    counter[year] = counter[year]+1
    #p= re.compile ('([0-9]{4})')
print(counter)

#key error: 'am'
#key error: '08:37' [1]
#key error: '07/08/2015' [0]

#now all i need is the year
#for item in dictionary:
  #if "2017" in dictionary[date]:
    #2017count=2017count+1
