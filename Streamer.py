import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import csv
import sys
import pandas as pd

class Listener(StreamListener):

    # Method to obtain tweets as well as relavent metadata
    def on_status(self, status):
        # Ensures that only tweets in English are obtained
        if status.lang == "en":
            print(status.text)
            # Checks if tweet is extended and if the condition is met, the full tweet is obtained
            if hasattr(status, "extended_tweet"):
                tweet_text = status.extended_tweet["full_text"]
            else:
                # Tweet is regular length
                tweet_text = status.text
            
            file = open('imported_tweets.csv', 'a', encoding='utf-8')
            writer = csv.writer(file)
            
            if status.in_reply_to_status_id is not None:
                if status.place is not None:
                    writer.writerow([status.user.id, status.user.id_str, status.user.name, status.user.screen_name, status.id,
                    status.id_str, tweet_text, status.created_at, status.in_reply_to_user_id, status.in_reply_to_user_id_str,
                    status.in_reply_to_screen_name, status.favorite_count, status.retweet_count, status.place])
            
                else:
                    writer.writerow([status.user.id, status.user.id_str, status.user.name, status.user.screen_name, status.id,
                    status.id_str, tweet_text, status.created_at, status.in_reply_to_user_id, status.in_reply_to_user_id_str,
                    status.in_reply_to_screen_name, status.favorite_count, status.retweet_count, 'Null'])
            
            else:
                if status.place is not None:
                    writer.writerow([status.user.id, status.user.id_str, status.user.name, status.user.screen_name, status.id,
                    status.id_str, tweet_text, status.created_at, 0, 'Null',
                    'Null', status.favorite_count, status.retweet_count, status.place])

                else:
                    writer.writerow([status.user.id, status.user.id_str, status.user.name, status.user.screen_name, status.id,
                    status.id_str, tweet_text, status.created_at, 0, 'Null',
                    'Null', status.favorite_count, status.retweet_count, 'Null'])

            file.close()

    # Method to identify and return any error messages to the user
    def on_error(self, status_code):
        # Error code presented to user
        print("Streaming error", status_code)
        
# Classes interpreted and run only when called, after data manipulation
if __name__ == "__main__":

    # Clears the imported_tweets file before writing to it
    f = open('imported_tweets.csv', 'r+')
    f.truncate(0)
    f.close()
    
    # Writes the headings of the data to be stored in the CSV file
    file = open('imported_tweets.csv', 'a', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['User ID Integer', 'User ID String', 'Name Of User', 'Display Name', 'Tweet ID Integer', 'Tweet ID String',
    'tweet', 'Date Created', 'Reply User ID Integer', 'Reply User ID String', 'Reply User Screen Name', 'Like Count', 'Retweet Count',
    'Place'])

    file.close()

    # My Twitter developer account credentials
    access_token = "1315924837211279360-ELgVi4duJG55DVVSLqzHgEXDggqeu9"
    access_token_secret = "GLQpVUkMowiePQlGnPDfTYJyWjwjbvqOLX8JO9LhBihTX"
    consumer_key = "IwlYQW5mIhCeMeSpcdwF8DUzS"
    consumer_key_secret = "InwCsZzwGKYveB8fVboY58MQXvWu3Xa9qxxp7Nt0Nieo9EoWGk"

    # Instantiates 'Listener' class
    listener = Listener()

    # Provides the consumer keys to the OAuthHandler function
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    
    # Provides access tokens
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Creates a list to store filters in from the 5th argument fed into the CMD terminal by the user input in the UI
    track_list = sys.argv[1]

    # Number of tweets the user wants to obtain
    num_of_tweets = sys.argv[2]

    # Creates stream and provides neccessary inputs
    stream = Stream(auth=api.auth, listener=listener)

    # Filters stream of tweets to match user input
    stream.filter(track=track_list)