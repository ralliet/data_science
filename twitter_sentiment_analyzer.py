#import the library to connect with twitter api and for natural language  processing
import tweepy
from textblob import TextBlob

# auth en connection keys/secrets
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = '' 

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# connect with API
api = tweepy.API(auth)

# get all public tweets about vitalik buterin
public_tweets = api.search('Vitalik Buterin')

# iterate over all public tweets about vitalik and find out the sentiment
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)
