import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')
csv_file = '/Users/KSlivins/Dev/api_yamdb/api_yamdb/static/data/review.csv'
# load the data into a Pandas DataFrame
review = pd.read_csv(csv_file)

# write the data to a sqlite table
review.to_sql('Review', conn, if_exists='replace', index=False)
