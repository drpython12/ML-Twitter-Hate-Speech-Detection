from sqlalchemy import create_engine
import mypysql
import pandas as pd
import Classifier

dataframe = Classifier.analyse
sqlEngine = create_engine('mysql+pymysql://root:Palashg12@127.0.0.1/TwitterMachineLearningDatabase')
dbConnection = sqlEngine.connect()

try:
    frame = dataframe.to_sql('User', dbConnection, if_exists='append');
except ValueError:
    print(ValueError)
except Exception:
    print(Exception)
else:
    print("Query successful");
finally:
    dbConnection.close()