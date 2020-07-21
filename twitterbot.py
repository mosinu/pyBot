import tweepy
import time

auth = tweepy.OAuthHandler('key', 'secret')
auth.set_access_token('token', 'secret')

search_tweet = 'python'
numberOfTweets = 2

api = tweepy.API(auth)
user = api.me()

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)

print(user.followers_count)

def limitSpeed(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(30)


for tweet in limitSpeed(tweepy.Cursor(api.search, search_tweet).items(numberOfTweets)):
	try:
		tweet.favorite()
		print('I like this')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break