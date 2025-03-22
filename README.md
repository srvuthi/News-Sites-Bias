This project allows users to analyze the bias of news articles based on the sentiment of headlines and descriptions. Users input a news source (e.g., BBC, CNN, Breitbart) and a country (e.g., USA, China, Israel). The program then fetches articles from the provided news source related to the specified country, performs sentiment analysis, and categorizes the articles as positive, negative, or neutral.

Features

- Scraping/Fetching: Retrieves news articles based on the selected news source and country.

- Sentiment Analysis: Analyzes the sentiment of article titles and descriptions.

- Bias Detection: Categorizes coverage as positive, negative, or neutral based on sentiment scores.

Technologies Used

- NewsAPI: For fetching news articles.

- VADER Sentiment Analysis: For analyzing sentiment. (ranges from -1 to 1)

- Python: For developing the application.

Setup and Installation

1. Clone the repository.
2. Install the required dependencies:

   pip install requests vaderSentiment

4. Get your NewsAPI key:
   - Go to NewsAPI.
   - Sign up for an account (if you don't have one).
   - Once logged in, go to the API Key section and copy your API key.
   - Add your API key in the script where it's required.

Run the project:

python start.py

Enter a news source (e.g., bbc-news, cnn, breitbart-news) and a country name (e.g., USA, China, Israel), and the program will fetch articles and analyze the sentiment.

Example Usage:

Enter a news source: bbc-news

Enter a country name: China

How It Works

- Fetches news related to the specified country from the selected news source.
- Performs sentiment analysis on the headlines to determine the overall sentiment (positive, negative, or neutral).
- Determines bias by comparing sentiment scores across different articles.
