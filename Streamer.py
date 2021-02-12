import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import csv
import APICredentials

class Authenticate():
    
    def authenticate(self):
        auth = OAuthHandler(APICredentials.consumer_key, APICredentials.consumer_key_secret)
        auth.set_access_token(APICredentials.access_token, APICredentials.access_token_secret)
        return auth

class Listener(StreamListener):

    def __init__(self, file_store):
        self.file_store = file_store

    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        if status == 420:
            print(status)
            return False

class Login():

    extracted_data = []
    #filter_list = []

    def __init__(self, api = False):
        
        self.auth = Authenticate()
        self.api = tweepy.API(self.auth.authenticate())
        print("Attempting login...")
        if self.api.verify_credentials:
            print("Logged in successfully!")
        else:
            print("Error logging in, please check API credentials!")
        
if __name__ == "__main__":
    Login()
    listener = Listener("tweets.csv")
    auth = OAuthHandler(APICredentials.consumer_key, APICredentials.consumer_key_secret)
    auth.set_access_token(APICredentials.access_token, APICredentials.access_token_secret)
    api = tweepy.API(auth)
    with open("tweets.csv", 'a+', newline='') as TweetCSV:
            writer = csv.writer(TweetCSV)
            for tweet in tweepy.Cursor(api.search, q='', lang = 'en', count=5).items():
                writer.writerow([tweet.id, tweet.created_at, tweet.text])