#This program extracts ALL the latest articles from the New York Times using BeautifulSoup

import requests
from bs4 import BeautifulSoup as soup
# import nltk
# nltk.download('punkt')

my_url = "https://www.nytimes.com/"

def getContent(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')

    containers = page_soup.find_all("script", {"type": "application/ld+json"})

    article_list = []
    #get all articles list
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)
    article_list[0:2] = [''.join(article_list[0:2])] #to get url & remove blank space

    content_string = article_list[0]

    article_index = content_string.index("itemListElement")
    content_string = content_string[article_index + 18:] #removes itemlistelement
    return content_string

def find_occurrences(content_string): # to get si & di of urls so that we can pick them
    start_indices = [i for i in range(len(content_string)) if
                     content_string.startswith('https://www.nytimes.com/2022', i)]#if pattern found in hyperlink, append it to si
    end_indices = [i for i in range(len(content_string)) if content_string.startswith('.html', i)]#hyperlinks end with .html so based on that we cal end indices
    end_indices = [x + 5 for x in end_indices] #for removing .html from hyperlink

    if len(start_indices) > len(end_indices):
        difference = len(start_indices) - len(end_indices)
        start_indices = start_indices[:difference]
    if len(end_indices) > len(start_indices):
        difference = len(end_indices) - (len(end_indices) - len(start_indices))
        end_indices = end_indices[:difference]
    return start_indices, end_indices


def get_all_urls(start_indices, end_indices, content_string):
    url_list = []#list to store all urls
    for i in range(min(5,len(start_indices))):#max 5 articles .
        if len(content_string[start_indices[i]:end_indices[i]])!=0 :#some articles require subscription so they are not scraped. hence to resolve it
            url_list.append(content_string[start_indices[i]:end_indices[i]])#appending substr from content strings to url_list
    return url_list
