from bs4 import BeautifulSoup


import requests, re, json
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
    # Matt: This is limiting it to just to the image, we can get the whole article if we look for:
    LGBTQ_art_articles = soup.find_all ('article',attrs = {'role': 'article'})

    for a_article in LGBTQ_art_articles:
        #print ('---------')
        #print(a_article)
        #print(LGBTQ_art_articles.text)

        # a_title = a_article.find ('a', attrs = {'title': "Sexual Blasphemy: Rurru Mipanochia Embodies Pre-Hispanic Pop Culture"})
        # MATT: this is only finding the title on the first loop, because it has to have title == "Sexual Blasphemy..." So we can make it more generic
        # a_title = a_article.find ('a', attrs = {'title': "Sexual Blasphemy: Rurru Mipanochia Embodies Pre-Hispanic Pop Culture"})
        # im not sure but the problem here may be that the attribute for 'a' under 'title' is the title of the individual article but it prints all the articles when i say print

        # Matt: We can see the title lives in the <h3> tag, so we can get it by:
        a_title = a_article.find ('h3')
        # Matt: And get the text of it (which is the text of the nested <a> link in it:
        #print('-----------')
        print(a_title.text)
        #it wont print the .text its not clear why this happens, it worked in another of my scripts
        #print(a_title['href'])

        # Matt: To get the image you can do something similar to the title because it is the only <img> in the <article> block, give it a try

        # a_image = a_image.find ('img', attrs = 'src': )
        #i am not sure what to put after 'src' since it is a link and not an attribute
        # print(a_image)
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

a_article_dict = {
'a_date': 'Date'
'a_title': 'Title'
'a_image': 'Image'
}
a_article.append(a_article_dict)

with open ()
