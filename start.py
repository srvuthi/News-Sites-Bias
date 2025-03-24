import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_news_sentiment(news_source, country):
    api_key = "your_api_key"  # Replace with your actual API key
    url = f"https://newsapi.org/v2/everything?q={country}&sources={news_source}&apiKey={api_key}"

    response = requests.get(url).json()

    if "articles" not in response or not response["articles"]:
        print("No news found for this source & country.")
        return

    sentiment_scores = []
    analyzer = SentimentIntensityAnalyzer()

    for article in response["articles"][:5]:  # Limit to 5 articles
        title = article["title"]
        print(f"\nArticle: {title}")

        sentiment_score = analyzer.polarity_scores(title)['compound']
        sentiment_scores.append(sentiment_score)

        print(f"Sentiment Score: {sentiment_score}")

    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
    print("\nOverall Sentiment Score:", avg_sentiment)

    if avg_sentiment > 0.2:
        print("Mostly positive coverage")
    elif avg_sentiment < -0.2:
        print("Mostly negative coverage")
    else:
        print("Neutral/mixed coverage")


news_source = input("Enter a news source: ")
country = input("Enter the name of country/figure: ")
get_news_sentiment(news_source, country)
