import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import csv
import sys
import pandas as pd

# Creates pandas dataframe
tweets_df = pd.DataFrame(columns=['User ID Integer' 'User ID String', 'Name', 'Display Name', 'Tweet ID Integer', 'Tweet ID String', 'Tweet', 'Date Posted', 
                                  'Reply User ID Integer', 'Reply User ID String', 'Reply User Display Name', 'Country', 'Country Code', 'City/State', 'Number Of Likes',
                                 'Number Of Retweets', 'Countries Withheld In'])

access_token = "1315924837211279360-ELgVi4duJG55DVVSLqzHgEXDggqeu9"
access_token_secret = "GLQpVUkMowiePQlGnPDfTYJyWjwjbvqOLX8JO9LhBihTX"
consumer_key = "IwlYQW5mIhCeMeSpcdwF8DUzS"
consumer_key_secret = "InwCsZzwGKYveB8fVboY58MQXvWu3Xa9qxxp7Nt0Nieo9EoWGk"

class Listener(StreamListener, tweets_df):

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
            
            tweets_df['User ID Integer'] = status.user.id
            tweets_df['User ID String'] = status.user.id_str
            tweets_df['Name'] = status.user.name
            tweets_df['Display Name'] = status.user.screen_name
            tweets_df['Tweet ID Integer'] = status.id
            tweets_df['Tweet ID String'] = status.id_str
            tweets_df['Tweet'] = tweet_text
            tweets_df['Date Posted'] = status.created_at
            tweets_df['Reply User ID Integer'] = status.in_reply_to_user_id
            tweets_df['Reply User ID String'] = status.in_reply_to_user_id_str
            tweets_df['Reply User Display Name'] = status.in_reply_to_user_name
            tweets_df['Number Of Likes'] = status.favorite_count
            tweets_df['Number Of Retweets'] = status.retweet_count
            if status.place.country is not None:
              tweets_df['Country'] = status.place.country
              tweets_df['Country Code'] = status.place.country_code
              tweets_df['City/State'] = status.place.full_name
            else:
                tweets_df['Country'] = 'Null'
                tweets_df['Country Code'] = 'Null'
                tweets_df['City/State'] = 'Null'
                      
            # Opens CSV file to write tweet and metadata
            '''with open("imported_tweets.csv", "a", encoding="utf-8") as file:
                file.write("%s, %s, %s, %s, %s,\n" % ("User ID INT", "User ID STR", "Name", 
                "Display Name", "Tweet"))
                file.write("%d, %s, %s, %s, %s,\n" % (status.user.id, status.user.id_str, 
                status.user.name, status.user.screen_name, tweet_text))'''

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
