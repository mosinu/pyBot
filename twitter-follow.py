import tweepy
import time

auth = tweepy.OAuthHandler('key', 'secret')
auth.set_access_token('token', 'secret')

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

#generous
for follower in limitSpeed(tweepy.cursor(api.followers).items()):
	if follower.followers_count > 100:
		follower.follow()
		break
	#print(follower.name)