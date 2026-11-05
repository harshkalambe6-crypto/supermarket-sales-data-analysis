# Deployment — Streamlit app

## Status

Not deployed yet. No deployment URL exists. Do not claim one until the steps below succeed and the live URL is verified in a browser.

## Option A — Streamlit Community Cloud (recommended, free)

1. Publish the repository to GitHub first (authorisation is required — see the main reply).
2. Go to https://share.streamlit.io and sign in with the same GitHub account.
3. Click **Create app** → select repository `supermarket-sales-data-analysis`, branch `main`, main file `app.py`.
4. Click **Deploy**. Streamlit installs `requirements.txt` automatically.
5. Open the URL Streamlit gives you and check: the title loads, the KPIs show Final Sales ₹3,02,764.90 / 1,191 records, and the category filter changes the charts.
6. Add that verified URL to the README and to `linkedin/linkedin-post.md`.

## Option B — Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501

## Notes

- The app reads `data/supermarket_sales_cleaned.csv` from the repository.
- The dashboard is static: it shows the cleaned file and does not claim live or real-time data.
