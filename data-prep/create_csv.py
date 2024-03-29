"""Script to convert NELA-GT database to a CSV file"""

import pandas as pd
import sqlite3

conn = sqlite3.connect('NELA_GT_2020toMarch2023.db', isolation_level = None, detect_types = sqlite3.PARSE_COLNAMES)
df = pd.read_sql_query("SELECT * FROM newsdata", conn)
df.to_csv('global_newsdata.csv', index = False)