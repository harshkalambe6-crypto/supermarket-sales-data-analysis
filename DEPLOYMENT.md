# Deployment — Streamlit app

## Status

**Live and verified** (5 Nov 2026): https://supermarket-sales-data-analysis-4kpxcdnngr3ozsfog2waao.streamlit.app/

The live dashboard was opened in a fresh browser tab and verified: title "Supermarket Sales Dashboard", Final Sales ₹3,02,764.90, 1,191 records.

Note: the first deploy failed with "Error installing requirements" because Streamlit Cloud defaulted to Python 3.14, on which pandas==2.1.4 has no wheel. The fix was `runtime.txt` (python-3.12) plus setting the app's Python version to 3.12 in Streamlit Cloud Advanced settings — a plain reboot alone did not pick up the change.

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
