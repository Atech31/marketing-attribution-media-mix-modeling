import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('marketing_analytics.db')

# 1. First-Touch Attribution Query
query_first_touch = """
WITH first_touch AS (
    SELECT user_id, channel,
           ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY touchpoint_order ASC) as rn
    FROM user_touchpoints
)
SELECT ft.channel, COUNT(DISTINCT ft.user_id) as conversions
FROM first_touch ft
JOIN user_touchpoints ut ON ft.user_id = ut.user_id
WHERE ft.rn = 1 AND ut.converted = 1
GROUP BY ft.channel;
"""

print("--- First-Touch Attribution ---")
df_ft = pd.read_sql(query_first_touch, conn)
print(df_ft)

# 2. Last-Touch Attribution Query
query_last_touch = """
WITH last_touch AS (
    SELECT user_id, channel,
           ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY touchpoint_order DESC) as rn
    FROM user_touchpoints
)
SELECT lt.channel, COUNT(DISTINCT lt.user_id) as conversions
FROM last_touch lt
JOIN user_touchpoints ut ON lt.user_id = ut.user_id
WHERE lt.rn = 1 AND ut.converted = 1
GROUP BY lt.channel;
"""

print("\n--- Last-Touch Attribution ---")
df_lt = pd.read_sql(query_last_touch, conn)
print(df_lt)

conn.close()