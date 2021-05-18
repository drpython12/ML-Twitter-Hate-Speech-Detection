from os import times, write
import pyodbc
import sys
import csv
import pandas as pd

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

    for row in writeFile.itertuples():

        if row.IRUI != 'Null':

        # Insert query for 'TweetEntities' table
            cursor.execute('''INSERT INTO TweetEntities VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            row.TII,
            row.CA,
            row.IRUI,
            row.IRUS,
            row.IRUN,
            row.CN,
            row.CN,
            row.LC,
            row.RC,
            )
        
        else:

            cursor.execute('''INSERT INTO TweetEntities (tweet_id, created_at, country, city_state, favourite_count, retweet_count) VALUES (?, ?, ?, ?, ?, ?)''',
            row.TII,
            row.CA,
            row.CN,
            row.CN,
            row.LC,
            row.RC
            )

    cnxn.commit()

def ReadServer():

    # Creating connection and cursor to locally hosted MySQL server
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL}; User ID=root; Password=Palashg12; Server=' + server + '; Database=' + database)
    cursor = cnxn.cursor()

    query = "SELECT * FROM User, Tweet, TweetEntities"
    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

if __name__ == '__main__':

    # Declaring driver to use for connection
    driver = 'Devart ODBC Driver for MySQL'

    # Declaring server to connect to
    server = 'localhost'

    # Declaring database to query
    database = 'TwitterMachineLearningDatabase'

    if sys.argv[1] == "w":

        # Obtaining filename from UI's input to console which is based on user's selected file in dialog
        filename = sys.argv[2]

        # Reading input file as CSV
        df = pd.read_csv(filename)

        WriteServer(df)
    
    elif sys.argv[1] == "r":
        ReadServer()