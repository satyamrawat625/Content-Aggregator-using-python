from webscrape import *
from article_scrape import *
from analyse_sentiment import *
import time

print("\nPlease wait , getting started",end='')

for i in range(10):
    time.sleep(0.2)
    print(".",end='')
time.sleep(2)
print('\n\n')

# Welcome Messages
print("* "*80)

print(" *\t\t\t\t\t\t Welcome to my project \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
print(" *           ","\t"*36,"*")
print(" *\t\t\t\t\t\t CONTENT AGGREGATOR USING PYTHON \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
print(" *           ","\t"*36,"*")
print(" *\t\t\t\t\t\t Now access the latest articles from The New York Times \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
print(" *           ","\t"*36,"*")
print(" *\t\t\t\t\t\t Also perform sentiment analysis and check the extent of the writer's bias \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
print(" *           ","\t"*36,"*")

print("* "*80)

name = input("\n\nEnter your name and get started: ")

time.sleep(0.5)

print("\n\nWelcome " + name + "! \nYou will now see the latest  related articles in the New York Times...")
print("\nExtracting article hyperlinks...")
time.sleep(2)
print("Retrieving summaries...")
print()
time.sleep(2)
print("=" * 180)
time.sleep(2)

# Gets all the latest URL's from the NY Times Technology Section
content_string = getContent(my_url)
starts, ends = find_occurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)

# calls 2 methods to get summary of article and sentiment analysis on it.
i=0
for url in url_list:
    i=i+1
    print("\nArticle ",i," URL: " + str(url))
    article_summary = summarizer(url)
    identifySentiments(article_summary)
    print("="*180)
    time.sleep(7)


print("\nThe articles have been successfully extracted !")
print("We have extracted " + str(len(url_list)) + " different articles!")
print("Thanks for using this program , " + name )
