import pyodbc
import sys
import csv
import pandas as pd

def WriteServer(writeFile):

    '''df = pd.read_csv(writeFile)
    userQuery = "INSERT INTO User VALUES (?, ?, ?, ?)"
    cursor.execute(userQuery, (df["User ID Integer"], df["User ID String"], df["Name Of User"], df["Display Name"]))
    cnxn.commit()'''

def ReadServer():
    query2 = "SELECT * FROM User"
    cursor.execute(query2)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

if __name__ == '__main__':

    driver = 'Devart ODBC Driver for MySQL'
    server = 'localhost'
    database = 'TwitterMachineLearningDatabase'

    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL}; User ID=root; Password=Palashg12; Server=' + server + '; Database=' + database)
    cursor = cnxn.cursor()

    filename = "imported_tweets.csv"
    df = pd.read_csv(filename)
    userQuery = "INSERT INTO User VALUES (?, ?, ?, ?)"
    cursor.execute(userQuery, (int(df["User ID Integer"]), str(df["User ID String"]), str(df["Name Of User"]), str(df["Display Name"])))
    cnxn.commit()