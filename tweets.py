from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import configparser

config = configparser.ConfigParser()
config.read('example.ini')
config["twitter"]["access_token"]

access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]
consumer_key = config["twitter"]["consumer_key"]
consumer_secret = config["twitter"]["consumer_secret"]


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    usa=[-125.0011,24.9493,-66.9326,49.5904]
    stream.filter(locations=usa)