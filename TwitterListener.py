from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import config
import sys


default_stdout = sys.stdout
sys.stdout = open('test-out', 'w')

class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')

    stream.filter(track=['art', 'marketing', 'movies', 'travel'])

sys.stdout = default_stdout
