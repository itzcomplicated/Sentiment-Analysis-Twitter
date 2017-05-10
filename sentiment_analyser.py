import tweepy
from textblob import TextBlob

consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'

access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print("Trend analysis from twitter feed.")
print("=========================================================================")

topic=input("Which topic do you prefer? ")

api = tweepy.API(auth)
public_tweets = api.search(topic)

total_tweets=0
total_polarity=0.0
for tweet in public_tweets:
    #print(tweet.text)
    total_tweets=total_tweets+1
    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)

    # analysis.sentiment is a named tuple
    # polarity -1.0 to 1.0
    polarity = analysis.sentiment.polarity
    # subjectivity
    subjectivity=analysis.sentiment.subjectivity

    total_polarity += polarity

avg_polarity=total_polarity/total_tweets

if total_tweets==0:
    print("Sorry! No tweets available with given {}. Please try again.".format(topic))
    exit(0)

trend_result= "neutral"
if avg_polarity > 0.3:
    trend_result = "very positive"
elif avg_polarity > 0 :
    trend_result = "positive"
elif avg_polarity < -0.3:
    trend_result = "very negative"
elif avg_polarity < 0:
    trend_result = "negative"

# print(total_polarity)
# print(avg_polarity)

print("=========================================================================")
print("From {} tweets analysed, {} is trending as {}".format(total_tweets, topic, trend_result))
print("=========================================================================")
