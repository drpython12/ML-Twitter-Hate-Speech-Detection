from os import write
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

    # Iterating through each row in every column and inserting fields into database
    for row in df.itertuples():
        cursor.execute('''INSERT INTO User VALUES (?, ?, ?, ?)''', 
        row.UII,
        row.UIS,
        row.NOU,
        row.DN
        )

    cnxn.commit()

def ReadServer():
    
    query2 = "SELECT * FROM User"
    cursor.execute(query2)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

if __name__ == '__main__':

    # Obtaining filename from UI's input to console which is based on user's selected file in dialog
    filename = sys.argv[1]

    # Reading input file as CSV
    df = pd.read_csv(filename)

    # Declaring driver to use for connection
    driver = 'Devart ODBC Driver for MySQL'

    # Declaring server to connect to
    server = 'localhost'

    # Declaring database to query
    database = 'TwitterMachineLearningDatabase'

    WriteServer(df)