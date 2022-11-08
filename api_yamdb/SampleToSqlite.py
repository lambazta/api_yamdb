import sqlite3

import pandas as pd

# database = 'db.sqlite3'
# source_list = ['/static/data/review.csv']

conn = sqlite3.connect('api_yamdb/db.sqlite3')
# csv_file = '/Users/KSlivins/Dev/api_yamdb/api_yamdb/static/data/review.csv'
csv_file = 'api_yamdb/static/data/review.csv'
# load the data into a Pandas DataFrame
data = pd.read_csv(csv_file)

# write the data to a sqlite table
data.to_sql('reviews_review', conn, if_exists='append', index=False)
