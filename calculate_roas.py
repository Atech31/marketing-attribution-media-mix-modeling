import sqlite3
import pandas as pd

conn = sqlite3.connect('marketing_analytics.db')

query = """
WITH channel_spend AS (
    SELECT channel, SUM(spend) as total_spend
    FROM campaign_spend
    GROUP BY channel
),
channel_revenue AS (
    SELECT channel, SUM(conversion_value) as total_revenue, COUNT(DISTINCT user_id) as conversions
    FROM user_touchpoints
    WHERE converted = 1
    GROUP BY channel
)
SELECT 
    cs.channel,
    cs.total_spend,
    cr.total_revenue,
    ROUND(cr.total_revenue / cs.total_spend, 2) as roas,
    ROUND(cs.total_spend / cr.conversions, 2) as cpa
FROM channel_spend cs
JOIN channel_revenue cr ON cs.channel = cr.channel;
"""

df = pd.read_sql(query, conn)
print("--- Channel ROAS & CPA Analysis ---")
print(df)

conn.close()