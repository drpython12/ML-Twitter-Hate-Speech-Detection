import pyodbc
import sys
import csv
import pandas as pd
import tkinter as tk
from tkinter import ttk

def WriteServer(writeFile):

    # Creating connection and cursor to locally hosted MySQL server
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL}; User ID=root; Password=Palashg12; Server=' + server + '; Database=' + database)
    cursor = cnxn.cursor()

    # Obtaining input fields for 'User' table
    writeFile["UII"] = writeFile["User ID Integer"]
    writeFile["UIS"] = writeFile["User ID String"]
    writeFile["NOU"] = writeFile["Name Of User"]
    writeFile["DN"] = writeFile["Display Name"]

    # Obtaining input fields for 'Tweet' table
    writeFile["TII"] = writeFile["Tweet ID Integer"]
    writeFile["TIS"] = writeFile["Tweet ID String"]
    writeFile["TT"] = writeFile["tweet"]

    # Obtaining input fields for 'TweetEntities' table
    writeFile["CA"] = writeFile["Date Created"]
    writeFile["IRUI"] = writeFile["Reply User ID Integer"]
    writeFile["IRUS"] = writeFile["Reply User ID String"]
    writeFile["IRUN"] = writeFile["Reply User Screen Name"]
    writeFile["LC"] = writeFile["Like Count"]
    writeFile["RC"] = writeFile["Retweet Count"]
    writeFile["CN"] = writeFile["Place"]

    # Obtaining input fields for 'TweetAnalysis' table
    writeFile["PD"] = writeFile["Prediction"]
    writeFile["TF"] = writeFile["TF-IDF Score"].astype(str)
    writeFile["TK"] = writeFile["Tokens"]

    # Iterating through each row in every column and inserting fields into 'User' table
    for row in writeFile.itertuples():
        cursor.execute('''INSERT INTO User VALUES (?, ?, ?, ?)''', 
        row.UII,
        row.UIS,
        row.NOU,
        row.DN
        )

    # Insert query for 'Tweet' table
    for row in writeFile.itertuples():
        cursor.execute('''INSERT INTO Tweet VALUES (?, ?, ?, ?)''',
        row.TII,
        row.TIS,
        row.TT,
        row.UII
        )

    # Insert query for 'TweetEntities' table
    for row in writeFile.itertuples():       
        cursor.execute('''INSERT INTO tweetentities VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        row.TII,
        row.CA,
        row.IRUI,
        row.IRUS,
        row.IRUN,
        row.CN,
        row.LC,
        row.RC,
        )

    for row in writeFile.itertuples():
        cursor.execute('''INSERT INTO tweetanalysis VALUES (?, ?, ?, ?)''',
        row.TII,
        row.TF,
        row.TK,
        row.PD
        )

    cnxn.commit()

def ReadServer():
    
    # Initializing tkinter library
    view = tk.Tk()
    view.title("Analyzed Tweets")
    view.geometry("1000x1000")

    # Creating connection and cursor to locally hosted MySQL server
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL}; User ID=root; Password=Palashg12; Server=' + server + '; Database=' + database)
    cursor = cnxn.cursor()

    query = "SELECT * FROM User, Tweet, TweetEntities, TweetAnalysis WHERE user.user_id = tweet.user_id AND tweet.tweet_id = tweetentities.tweet_id AND tweet.tweet_id = tweetanalysis.tweet_id;"
    cursor.execute(query)

    tree = ttk.Treeview(view)
    tree["columns"] = ("User ID Integer" ,"User ID String", "Name Of User", "Display Name", "Tweet ID Integer", "Tweet ID String",
    "Tweet", "Date Created", "Reply User ID Integer", "Reply User ID String", "Reply User Screen Name", "Place", "Like Count", 
    "Retweet Count", "TF-IDF Score", "Tokens", "Prediction")
    
    tree.column("User ID Integer", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("User ID String", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("Name Of User", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("Display Name", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("Tweet ID Integer", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("Tweet ID String", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("Tweet", width=150, minwidth=50, anchor=tk.CENTER)
    tree.column("Date Created", width=80, minwidth=50, anchor=tk.CENTER)
    tree.column("Reply User ID Integer", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("Reply User ID String", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("Reply User Screen Name", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("Place", width=40, minwidth=20, anchor=tk.CENTER)
    tree.column("Like Count", width=40, minwidth=20, anchor=tk.CENTER)
    tree.column("Retweet Count", width=40, minwidth=20, anchor=tk.CENTER)
    tree.column("TF-IDF Score", width=100, anchor=tk.CENTER)
    tree.column("Tokens", width=100, anchor=tk.CENTER)
    tree.column("Prediction", width=50, anchor=tk.CENTER)

    tree.heading("User ID Integer", text="User ID", anchor=tk.CENTER)
    tree.heading("User ID String", text="User ID String", anchor=tk.CENTER)
    tree.heading("Name Of User", text="Name Of User", anchor=tk.CENTER)
    tree.heading("Display Name", text="Display Name", anchor=tk.CENTER)
    tree.heading("Tweet ID Integer", text="Tweet ID", anchor=tk.CENTER)
    tree.heading("Tweet ID String", text="Tweet ID String", anchor=tk.CENTER)
    tree.heading("Tweet", text="Tweet", anchor=tk.CENTER)
    tree.heading("Date Created", text="Date/Time Created", anchor=tk.CENTER)
    tree.heading("Reply User ID Integer", text="Reply User ID", anchor=tk.CENTER)
    tree.heading("Reply User ID String", text="Reply User ID String", anchor=tk.CENTER)
    tree.heading("Like Count", text="Like Count", anchor=tk.CENTER)
    tree.heading("Retweet Count", text="Retweet Count", anchor=tk.CENTER)
    tree.heading("Place", text="Location", anchor=tk.CENTER)
    tree.heading("Prediction", text="Prediction", anchor=tk.CENTER)
    tree.heading("Tokens", text="Tokens", anchor=tk.CENTER)

    i = 0
    for row in cursor:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))
        i = i + 1
    
    tree.pack()
    view.mainloop()

if __name__ == '__main__':

    # Declaring driver to use for connection
    driver = 'Devart ODBC Driver for MySQL'

    # Declaring server to connect to
    server = 'localhost'

    # Declaring database to query
    database = 'tweet_data'

    # sys.argv[1]
    if "w" == "w":

        # Obtaining filename from UI's input to console which is based on user's selected file in dialog
        filename = "today.csv"
        #sys.argv[2]

        # Reading input file as CSV
        df = pd.read_csv(filename)

        WriteServer(df)

    # sys.argv[1]
    elif "r" == "r":
        ReadServer()