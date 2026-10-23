import pandas as pd
import sqlite3

# Load generated CSV files
df_spend = pd.read_csv('campaign_spend.csv')
df_touchpoints = pd.read_csv('user_touchpoints.csv')

# Connect to SQLite database (this will create marketing_analytics.db automatically)
conn = sqlite3.connect('marketing_analytics.db')

# Write dataframes to SQL tables
df_spend.to_sql('campaign_spend', conn, if_exists='replace', index=False)
df_touchpoints.to_sql('user_touchpoints', conn, if_exists='replace', index=False)

conn.close()

print("Marketing datasets successfully loaded into marketing_analytics.db!")