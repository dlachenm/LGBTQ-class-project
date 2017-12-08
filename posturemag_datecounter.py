#load json
#make it a dictionary
import json
#with open ('all_data_posturemag.json', 'r') as
data = json.load (open ('all_data_posturemag.json'))
#print (data)

counter={
    '2013': 0,
    '2014': 0,
    '2015': 0,
    '2016': 0,
    '2017': 0,
}

for article in data:
    year = article['date'].split()[2]
    counter[year] = counter[year]+1
print(counter)
#for item in dictionary:
  #if "2017" in dictionary[date]:
    #2017count=2017count+1
