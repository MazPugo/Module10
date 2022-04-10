
import sqlite3 # imports the SQLite library
import pandas as pd
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy import create_engine
from pandas import read_csv

# combined_data.csv from clean_stations.csv and clean_measures.csv
df = read_csv(r"combined_data.csv")
engine = create_engine('sqlite:///database.db', echo=True)
meta = MetaData()
sqlite_connection = engine.connect()


sqlite_table = "Table1"
df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
conn=sqlite_connection
conn.execute("SELECT * FROM Table1 LIMIT 5").fetchall()

