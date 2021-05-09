import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import csv
import sys

access_token = "1315924837211279360-ELgVi4duJG55DVVSLqzHgEXDggqeu9"
access_token_secret = "GLQpVUkMowiePQlGnPDfTYJyWjwjbvqOLX8JO9LhBihTX"
consumer_key = "IwlYQW5mIhCeMeSpcdwF8DUzS"
consumer_key_secret = "InwCsZzwGKYveB8fVboY58MQXvWu3Xa9qxxp7Nt0Nieo9EoWGk"

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
            # Opens CSV file to write tweet and metadata
            with open("imported_tweets.csv", "a", encoding="utf-8") as file:
                file.write("%s, %s, %s, %s, %s,\n" % ("User ID INT", "User ID STR", "Name", 
                "Display Name", "Tweet"))
                file.write("%d, %s, %s, %s, %s,\n" % (status.user.id, status.user.id_str, 
                status.user.name, status.user.screen_name, tweet_text))

    # Method to identify and return any error messages to the user
    def on_error(self, status_code):
        # Error code presented to user
        print("Streaming error", status_code)
        
# Classes interpreted and run only when called, after data manipulation
if __name__ == "__main__":
    
    # Instantiates 'Listener' class
    listener = Listener()

    # Provides the consumer keys to the OAuthHandler function
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    # Provides access tokens
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Creates a list to store filters in
    track_list = []
    # Asks the user how many filters to use
    # num_elements = int(input("How many filters would you like to enter in the list? "))
    #for i in range(0, num_elements):
        # Prompts user for filter the number of times they input
        #track_list.append(str(input("Element: ")))
    track_list = sys.argv[1]

    # Creates stream and provides neccessary inputs
    stream = Stream(auth=api.auth, listener=listener, tweet_mode="extended")
    # Filters stream of tweets to match user input
    stream.filter(track=track_list)