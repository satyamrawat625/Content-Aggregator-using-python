# This program scrapes and summarizes news articles from the New York Times.
from newspaper import Article

def summarizer(url):
    article = Article(url)

    article.download()
    article.parse()
    # Punkt is a sentence tokenizer which is useful for extracting and detecting text.
    article.download('punkt')
    article.nlp()

    author_string = "Author(s): "
    for author in article.authors:
        author_string += author
    print(author_string)

    # Gets the publish date of the article
    date = article.publish_date

    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    #TO print url to all the images used in articles
    image_string = "All Images used in the article are : "
    for image in article.images:
        image_string += "\n\t" + image  # adds a newline and a tab before each image is printed
    print(image_string)
    print("\nImportant keywords used are: ", article.keywords)


    # prints the article summary
    print("\nSummary of the given article")
    print("."*35)
    print(article.summary)

    return article.summary
