import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plot

# Creates Pandas dataframe of labeled data csv file for use to train the model
file_data = pd.read_csv("labeled_data.csv", encoding='cp1252')

# List of stop words
stop_words = ["until", "mustn't", "him", "d", "you'd", "which", "himself", "is", "too", "myself", "for", "shan't", 
    "once", "so", "such", "re", "does", "mightn", "there", "won't", "live", "about", "haven't", "wouldn't", "whom", 
    "at", "hadn't", "weren", "m", "make", "this", "wouldn", "a", "was", "y", "theirs", "were", "again", "amp", 
    "couldn", "not", "most", "same", "just", "come", "be", "couldn't", "hasn", "doesn't", "or", "are", "stop", 
    "why", "both", "ourselves", "over", "where", "further", "through", "how", "smh", "if", "hadn", "ain", "than", 
    "see", "didn", "more", "itself", "good", "you'll", "after", "ours", "lmao", "some", "then", "will", "her", "hers", 
    "them", "that'll", "as", "she's", "before", "all", "up", "those", "under", "still", "mightn't", "should've", 
    "doing", "their", "me", "did", "isn't", "has", "to", "thats", "read", "when", "between", "o", "being", "but", 
    "down", "da", "these", "now", "who", "shan", "the", "am", "you", "don't", "hes", "having", "do", "ll", "with"
    "while", "on", "s", "needn't", "you've", "own", "wasn't", "here", "any", "dat", "in", "he", "won", "out", "our", 
    "yourself", "dont", "isn", "we", "it's", "during", "above", "ma", "haven", "don", "hasn't", "had", "needn", "i", 
    "didn't", "mustn", "she", "very", "should", "an", "wit", "have", "t", "off", "shouldn't", "only", "its", 
    "because", "below", "by", "shouldn", "yours", "his", "nor", "it", "your", "look", "been", "you're", "into", 
    "that", "aren", "oh", "herself", "other", "yourselves", "ve", "few", "against", "can", "they", "and", "my", 
    "no", "doesn", "of", "themselves", "aren't", "ya", "from", "wasn", "weren't", "each", "what", "cant", "they're",
    "amp", "need", "said", "well", "always", "never", "tell", "thats", "i'm", "tell", "day", "ill", "i'll"]

# Look through each tweet's class and label strings that are not hate speech as 0 and any string that is hate speech as 1
def Label(df):
    # Replaces original value 0 (hate speech) with 1 and replaces values 1 and 2 (non-hate speech) with 0
    df["refined class"] = df["class"].replace([0,1,2], [1,0,0])

# Pre-processing & parsing of tweet strings for TF-IDF vectorizer
def PPT(df):
    # Makes all letters in 'tweet' column lowercase
    df["tweet"] = df["tweet"].str.lower()

    # Removing stop words
    df["tweet"] = df["tweet"].apply(lambda x: " ".join([word for word in x.split() if word not in (stop_words)]))

    # Removing punctuation and 'rt'
    df["tweet"] = df["tweet"].str.replace("[{}]".format(string.punctuation), "")
    df["tweet"] = df["tweet"].str.replace("rt", "")

    # Removing numbers
    df["tweet"] = df["tweet"].str.replace("[{}]".format(string.digits), "")
    
    # Stemming each word of the tweets
    stemmer = PorterStemmer()
    df["tweet"] = df["tweet"].apply(lambda x: " ".join([stemmer.stem(word) for word in x.split()])) 
    
    # Tokenize each word
    df["parsed tweets"] = df["tweet"].apply(lambda x: nltk.WordPunctTokenizer().tokenize(x))
    print(df[["tweet", "parsed tweets"]])

# Word cloud generator based on the parsed data
def Wordcloud(df): 
    # Creating a long string of all tweets classified as hate speech
    words = " ".join([word for word in df["tweet"][df["refined class"] == 1]])
    wc = WordCloud(width=800, height=500, max_font_size=110, max_words=80).generate(words)
    plot.figure(figsize=(12,8))
    plot.axis('off')
    plot.imshow(wc)
    plot.show()

# Trains the model
def Model(df):

    X_train, X_test, Y_train, Y_test = train_test_split(df["tweet"], df["refined class"], random_state=0)
    tfidf_scores = df["parsed tweets"].apply(lambda x: x.TfidfTransformer(norm=None))
    print(tfidf_scores)
    '''X_train_vectorized = vectorizer.fit_transform(X_train)
    
    model = LogisticRegression()
    model.fit(X_train_vectorized, Y_train)

    predictions = model.predict(X_test)
    print(classification_report(Y_test, predictions))
    
    def Train(model, train_feature_vector, label, test_feature_vector):
        model.fit(test_feature_vector, label)
        predict = model.predict(test_feature_vector)
        return predict

    print(roc_auc_score(Y_test, Train(LogisticRegression(), X_train_tfidf, Y_train, X_test_tfidf)))
    print(classification_report(Y_test, Train(LogisticRegression(), X_train_tfidf, Y_train, X_test_tfidf)))'''

    '''X_train, X_test, Y_train, Y_test = train_test_split(df["tweet"], df["refined class"], random_state=0)
    vectorizer = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=2000)
    vectorizer.fit(df["tweet"])
    X_train_tfidf = vectorizer.transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    def Train(model, train_feature_vector, label, test_feature_vector):
        model.fit(test_feature_vector, label)
        predict = model.predict(test_feature_vector)
        return predict

    print(roc_auc_score(Y_test, Train(LogisticRegression(), X_train_tfidf, Y_train, X_test_tfidf)))
    print(classification_report(Y_test, Train(LogisticRegression(), X_train_tfidf, Y_train, X_test_tfidf)))'''

Label(file_data)
PPT(file_data)
Wordcloud(file_data)
Model(file_data)
