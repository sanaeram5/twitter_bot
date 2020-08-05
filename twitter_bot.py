import tweepy
import time
import twitter_credentials

auth=tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()
search=input('Enter a hashtag or username:')
nrTweets=50

for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

