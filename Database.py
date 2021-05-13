import MySQLdb
import pandas as pd
import Classifier

database = MySQLdb.connect(host="127.0.0.1", user="root", password="Palashg12", database="TwitterMachineLearningDatabase")

print(Classifier.analyse)