from bs4 import BeautifulSoup

import requests, re

url = "https://www.census.gov/newsroom/stories/2015/october/lgbt.html"


census_map = requests.get(url, verify=False)


if census_map.status_code != 200:
    print ("There was an error with", url)
    
          
page_html = census_map.text

soup = BeautifulSoup(page_html, "html.parser")

map_items = soup.find_all("div", attrs={ "class" : "image parbase section"})
 
for map_item in map_items:
 
    image = map_item.find("img")
    print(image["src"])
 
    desc = image["alt"] 
    src = "https://www.census.gov"+image["src"]
 
    print("----------")
    print(desc)
    print(src)
    r = requests.get(src, stream=True, verify=False)
    if r.status_code == 200:
        with open("test.png",'wb') as f:
            for chunk in r:
                f.write(chunk)