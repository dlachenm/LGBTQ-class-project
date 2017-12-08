from bs4 import BeautifulSoup


import requests, re, json
all_data = []
for counter in range (1,3):
    url = "https://www.huffingtonpost.com/topic/lgbt-art?page=" + str(counter)
    print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


LGBT_art = requests.get(url, verify=False, headers=headers)

if LGBT_art.status_code != 200:
	print ("There was an error with", url)

page_html = LGBT_art.text

soup = BeautifulSoup(page_html, "html.parser")
#print(page_html) #a test of the page working
#articles = []

LGBT_art_articles = soup.find_all ('div', attrs = {'class': 'card__content'})
for a_article in LGBT_art_articles:
    print("-----------")
    # print(a_article)
    #Matt: the variable "LGBT_art_articles" is all of the articles, we would want to use just a_article
    # print(LGBT_art_articles.text)

    print(a_article.text)
    #this works but it is not what you want, you want structred data, so like the posture scraper you need to find each piece

    # the first <a> is the title
    a_title = a_article.find ('a')
    print('-------------')
    print(a_title.text)
    print(a_title['href'])

    article_part = ['title']
    partof_article = {
        'title': a_title.text
    }
    #a_image = a_article.find ('div', attrs = {'class': 'card__image__cover-bg bn-clickable' })
    #print ('------------')
    #print(a_image)
    #print(a_image['style'])

    article_url = 'https://www.huffingtonpost.com'+ a_title['href']

    single_article = requests.get(article_url, verify=False, headers=headers)

    if single_article.status_code != 200:
    	print ("There was an error with", article_url)

    article_html = single_article.text

    soup = BeautifulSoup(article_html, "html.parser")

    #single_article = soup.find_all ('article', attrs ={'class':'entry js-entry component loaded entry--wide'})
    single_article = soup.find_all ('span',attrs = {'class': 'timestamp__date--published'})
    #for a_article in single_article:
        #print('---------')
        #print (a_article)
    for a_date in single_article:
        print('-----------')
        print (a_date.text)
        #a_date = a_article.find ('span')
    #    print('--------')
        #print(a_date.text)

    #single_image = soup.find_all ('div', attrs = {'class': 'entry__content js-entry-content'})
    #for a_image in single_image:


#Here i know that the img does not live within the span where the time stamp does but I am not sure how to include this in the script
#without rewritting the date portion. Is it just a matter of reorganizing the order of the code as the img is part of the larger article code
#I have tried other options for getting this to print correctly as you can see in the commented out code but I dont want to mess up my script up anymore than i have before possibly loosing something I have done correctly
        a_image = single_article.find ('img')
        print('------------')
        print (a_image['src'])

        article_url = ['date', 'image']
        article_url.extend(['title'])
        print(article_url)

        all_articles = {
            'image': a_image['src'],
            'date': a_date.text,
            'title': a_title.text
        }
        all_data.append(all_articles)

print (all_data)
with open ('all_data.json', 'w') as huffingtonpost:
    huffingtonpost.write(json.dumps(all_data, indent=4))

#what i need next is a json file and then collect the date --- to the year and then count how many articles were published per year


    #a_title = a_article.find ('a', attrs = {'class': 'card__link bn-card-headline'})
    #print('-------------')
    #print(a_title.text)
    #print(a_title['href'])


    #a_synap = a_article.find ('div', attrs = {'class': 'card__description js-card-headline'})
    #print('-------------')
    #print(a_synap.text)

#open('huffington_LGBT.json', 'w') as huffingtonpost:
# I get an invalid syntax for      ^ why I have no idea
    #huffingtonpost.write(json.dumps(articles, indent=4))

# I am trying to create a json file with the open / write and I am not sure where i am missing a set

#    title = a_article.find('a', attrs={'class':'bn-card-headline'})
#    print(title.text)
#title = a_article.find('a', attrs={'class':'bn-card-headline'})                                                                  ^
#IndentationError: unindent does not match any outer indentation level


#Now i am stuck
#I tried just doing the list of articles for LGBT art at huffington post https://www.huffingtonpost.com/topic/lgbt-art
#I looked in the source and the inspect element and it looks fine but what am i missing or not seeing that makes the website not work

#what i ultimately get in my terminal is that it spits back the LGBT_art = requests.get(url, verify=false)
#then a whole slew of things about errors in lines that I am not sure what they correspond to

#then i tried just doing the url for a single article and still got a whole bunch of errors
#to try and just get the title, image, small description, and the url, which i never get too because there are so many errors

# I am following our in class practice with the NYT main page but I am not seeing what makes a website work or doesnt



#WHAT I WANTOUT OF THIS WEB scrape
    #THE TITLE OF EACH ARTICLE ON THE SEARCH PAGE FOR LGBT ART
    #THE SYNOPSIS
    #THE IMAGE ASSOCIATED WITH THE article
    #THE URL FOR THE article
