# source: https://pythontips.com/2013/09/04/increase-your-twitter-followers/
from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = 'your oauth token'
OAUTH_SECRET = 'your oauth secret'
CONSUMER_KEY = 'your consumer key'
CONSUMER_SECRET = 'your consumer secret'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

def fav_tweet(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print "Favorited: %s" % (result['text'])
        return result
    # when you have already favourited a tweet
    # this error is thrown
    except TwitterHTTPError as e:
        print "Error: ", e
        return None

def auto_fav(q, count=100):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print a
    success = 0
    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1
    print "We Favorited a total of %i out of %i tweets" % (success,
          len(result['statuses']))
