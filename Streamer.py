import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import csv

access_token = "1315924837211279360-ELgVi4duJG55DVVSLqzHgEXDggqeu9"
access_token_secret = "GLQpVUkMowiePQlGnPDfTYJyWjwjbvqOLX8JO9LhBihTX"
consumer_key = "IwlYQW5mIhCeMeSpcdwF8DUzS"
consumer_key_secret = "InwCsZzwGKYveB8fVboY58MQXvWu3Xa9qxxp7Nt0Nieo9EoWGk"

global n_tweets
n_tweets = int(input("Number of tweets to stream: "))


class Listener(StreamListener):

    def on_status(self, status):
        tweet_count = 0
        if n_tweets >= tweet_count:
            print(status.text)
            tweet_count = tweet_count + 1
            if status.lang == "en":
                if hasattr(status, "extended_tweet"):
                    tweet_text = status.extended_tweet["full_text"]
                else:
                    tweet_text = status.text
                if hasattr(status, "retweeted_status") == False:
                    with open("imported_tweets.csv", "a", encoding="utf-8") as file:
                        file.write("%s, %s, %s, %s, %s,\n" % ("User ID INT", "User ID STR", "Name", "Display Name", "Tweet"))
                        file.write("%d, %s, %s, %s, %s,\n" % (status.user.id, status.user.id_str, status.user.name, status.user.screen_name, tweet_text))
        else:
            stream.disconnect()

    def on_error(self, status_code):
        print("Streaming error", status_code)
        
if __name__ == "__main__":
    
    listener = Listener()

    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    stream = Stream(auth=api.auth, listener=listener, tweet_mode="extended")
    stream.filter(track=["trump"])