from bs4 import BeautifulSoup

import requests, re

url = "https://www.everycrsreport.com/reports/R44282.html"


crs_report = requests.get(url, verify=False)


if crs_report.status_code != 200:
    print ("There was an error with", url)
    
          
page_html = crs_report.text

soup = BeautifulSoup(page_html, "html.parser")

all_crs_reports = soup.find_all("div", attrs = {"id": "report-page"})
all_data = []
for a_div in all_crs_reports:
    title = a_div.find("h1")
    if title != None:
        title_text = title.text.strip()
    
    date = a_div.find("p",attrs = {"class": "report-metadata"})
    if date != None:
        date_text = date.text.strip()

    summary = a_div.find("div",attrs = {"class": "report-summary"})
    if summary != None:
        summary_text = summary.text.strip()
            
        a_report_data = {"title":title_text,"date":date_text, "summary":summary_text}
 
        all_data.append(a_report_data)
        print (all_data)
        
        