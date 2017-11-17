from bs4 import BeautifulSoup


import requests, re, json
all_data = []
#for loop for the pages
for counter in range (1,9):
    url = "http://posturemag.com/online/category/art/page/" + str(counter)
    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    LGBTQ_art = requests.get(url, verify=False, headers=headers)

    if LGBTQ_art.status_code !=200:
        print ("There was an error with", url)

    page_html = LGBTQ_art.text

    soup = BeautifulSoup(page_html, "html.parser")
    #print(page_html)

    #articles = []

    #LGBTQ_art_articles = soup.find_all ('figure',attrs = {'class': 'post-gallery'})
    LGBTQ_art_articles = soup.find_all ('article',attrs = {'role': 'article'})

    for a_article in LGBTQ_art_articles:
        #print ('---------')
        #print(a_article)
        #print(LGBTQ_art_articles.text)


        a_title = a_article.find ('h3')
        #print('-----------')
        print(a_title.text)
        #it wont print the .text its not clear why this happens, it worked in another of my scripts
        #print(a_title['href'])


        a_image = a_article.find ('img')

        #print('-----------')
        print(a_image['src'])


        pub_dates = a_article.find ('aside', attrs = {'class': 'post-meta'})


        a_date = pub_dates.find ('a')

        print('-----------')
        print(a_date.text)
#THIS ALL WORKS


#make a list, then make it a dictionary for each article, add each dictionary to the list then write out to json dump
        a_article = ['title', 'image', 'date']

        an_article = {
            'date': a_date.text,
            'title': a_title.text,
            'image': a_image['src']
        }
        all_data.append(an_article)

print (all_data)
with open('all_data.json', 'w') as posturemag:
    posturemag.write(json.dumps(all_data, indent=4))
