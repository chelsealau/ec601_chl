# REFERENCES: https://www.youtube.com/watch?v=MqIw68fEq1k&t=1s
import tweepy
from main import authenticate
from textblob import TextBlob
import statistics
from typing import List

# Get tweets using twitter API that are returned from searching for keyword
def retrieve_tweets(keyword: str) -> List[str]:
    api = authenticate()
    tweet_list = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(100):
        tweet_list.append(tweet.full_text)
    return tweet_list

# Calculate sentiment for each tweet returned using textblob
def calc_sentiment(cleaned_tweets: List[str]) -> List[float]:
    score_list = []
    for tweet in cleaned_tweets:
        blob = TextBlob(tweet)
        score_list.append(blob.sentiment.polarity)
    return score_list

# Return average sentiment
def avg_sentiment(keyword: str) -> int:
    tweets = retrieve_tweets(keyword)
    sentiment_scores = calc_sentiment(tweets)
    avg_sent = statistics.mean(sentiment_scores)

    return avg_sent

if __name__ == '__main__':
    keyword = input("KEYWORD TO SEARCH: ")
    print(avg_sentiment(keyword))
