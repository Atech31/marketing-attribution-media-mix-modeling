# Marketing Attribution & Media Mix Modeling (MMM)  
A comprehensive marketing analytics project demonstrating Multi-Touch Attribution (MTA) modeling, Return on Ad Spend (ROAS) analysis, Cost Per Acquisition (CPA) calculations, and dynamic Power BI dashboard visualization using **Python, SQL (SQLite), and Power BI**.

---

##   Executive Summary
Marketing teams across digital platforms (Google Ads, Meta Ads, Email Marketing) face challenges evaluating which channels drive the highest customer conversion value. This project models user conversion pathways across multiple channels, calculates First-Touch vs. Last-Touch attribution metrics, evaluates performance efficiency via ROAS & CPA, and delivers an executive dashboard for data-driven budget allocation.

---

## 🛠️ Tech Stack & Tools
* **Programming Language:** Python 3.x
* **Data Processing & Analytics:** Pandas, NumPy
* **Database & SQL:** SQLite3 (Window Functions, CTEs, Aggregations)
* **Data Visualization:** Power BI Desktop
* **Version Control:** Git, GitHub

---

##   Project Structure
```text
├── campaign_spend.csv                  # Daily marketing ad spend by channel
├── user_touchpoints.csv                # Granular user clickstream & conversion paths
├── generate_marketing_data.py          # Synthetic data generation script
├── load_marketing_to_sqlite.py         # Ingestion script to SQLite database
├── calculate_attribution.py            # SQL queries for First-Touch & Last-Touch attribution
├── calculate_roas.py                   # SQL queries for ROAS and CPA metrics
├── marketing_analytics.db              # Relational SQLite database
└── Marketing_Attribution_Dashboard.pbix# Interactive Power BI report file
