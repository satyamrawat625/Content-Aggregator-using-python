#This program performs sentiment analysis on news articles using TextBlob.

from textblob import TextBlob


def identifySentiments(news_story):
    news = TextBlob(news_story)
    sentiments = []
    for sentence in news.sentences:#iterates over each sentence
        sentiment = sentence.sentiment #tells us polarity & subjectvity
        for metric in sentiment:
            sentiments.append(metric)

    polarity_data = []
    subjectivity_data = []
    for i in range(len(sentiments)):
        if i % 2 == 0: # polarity values lie on even index & subjectivity on odd
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append(sentiments[i])

    # The averages of both sentiment lists are calculated.
    polarity_average = avgCal(polarity_data)
    subjectivity_average = avgCal(subjectivity_data)

    # Displays the sentiment that relates to the averages on the console.
    print('\n')
    print("Brief Sentiment analysis on above article")
    print('.'*35)
    print("Polarity: " + obtainSentimentStr(polarity_average, "polarity"))
    print("Subjectivity: " + obtainSentimentStr(subjectivity_average, "subjectivity"))

def avgCal(list):
    return sum(list) / len(list)


def obtainSentimentStr(sentiment, type):
    sentiment_category = ""
    if type == "polarity":
        if sentiment > 0.75:
            sentiment_category = "Extremely positive."
        elif sentiment > 0.5:
            sentiment_category = "Significantly positive."
        elif sentiment > 0.3:
            sentiment_category = "Fairly positive."
        elif sentiment > 0.1:
            sentiment_category = "Slightly positive."
        elif sentiment < -0.1:
            sentiment_category = "Slightly negative."
        elif sentiment < -0.3:
            sentiment_category = "Fairly negative."
        elif sentiment < -0.5:
            sentiment_category = "Significantly negative."
        elif sentiment < -0.75:
            sentiment_category = "Extremely negative."
        else:
            sentiment_category = "Neutral."
        return sentiment_category
    elif type == "subjectivity":
        if sentiment > 0.75:
            sentiment_category = "Extremely subjective."
        elif sentiment > 0.5:
            sentiment_category = "Fairly subjective."
        elif sentiment > 0.3:
            sentiment_category = "Fairly objective."
        elif sentiment > 0.1:
            sentiment_category = "Extremely objective."
        return sentiment_category
    else:
        print("Invalid Input")
