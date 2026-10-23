import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# 1. Generate Daily Campaign Spend Data
dates = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(180)]
channels = ['Google Ads', 'Meta Ads', 'Email Marketing']

spend_data = []
for d in dates:
    for channel in channels:
        if channel == 'Google Ads':
            spend = np.random.uniform(500, 1500)
            impressions = int(spend * np.random.uniform(20, 30))
            clicks = int(impressions * np.random.uniform(0.03, 0.06))
        elif channel == 'Meta Ads':
            spend = np.random.uniform(400, 1200)
            impressions = int(spend * np.random.uniform(30, 45))
            clicks = int(impressions * np.random.uniform(0.015, 0.035))
        else: # Email Marketing
            spend = np.random.uniform(50, 200)
            impressions = int(spend * np.random.uniform(50, 80))
            clicks = int(impressions * np.random.uniform(0.08, 0.15))
            
        spend_data.append({
            'date': d.strftime('%Y-%m-%d'),
            'channel': channel,
            'spend': round(spend, 2),
            'impressions': impressions,
            'clicks': clicks
        })

df_spend = pd.DataFrame(spend_data)
df_spend.to_csv('campaign_spend.csv', index=False)

# 2. Generate User Journey & Attribution Touchpoints Data
n_users = 2500
touchpoint_data = []

for user_id in range(1001, 1001 + n_users):
    n_touchpoints = np.random.choice([1, 2, 3, 4], p=[0.4, 0.3, 0.2, 0.1])
    user_channels = np.random.choice(channels, size=n_touchpoints, p=[0.45, 0.40, 0.15])
    converted = np.random.choice([0, 1], p=[0.7, 0.3])
    conversion_value = round(np.random.uniform(50, 300), 2) if converted == 1 else 0.0
    
    start_date = datetime(2026, 1, 1) + timedelta(days=int(np.random.uniform(0, 150)))
    
    for step, ch in enumerate(user_channels, start=1):
        tp_date = start_date + timedelta(days=step * int(np.random.uniform(1, 4)))
        touchpoint_data.append({
            'user_id': f"USER_{user_id}",
            'touchpoint_order': step,
            'channel': ch,
            'touchpoint_date': tp_date.strftime('%Y-%m-%d'),
            'converted': converted if step == n_touchpoints else 0,
            'conversion_value': conversion_value if step == n_touchpoints else 0.0
        })

df_touchpoints = pd.DataFrame(touchpoint_data)
df_touchpoints.to_csv('user_touchpoints.csv', index=False)

print("Marketing Attribution Datasets Generated Successfully!")
print("Saved: campaign_spend.csv & user_touchpoints.csv")