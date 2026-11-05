# LinkedIn launch post — Supermarket Sales Data Analysis

> Do not post this until the GitHub repository link (and dashboard link, if deployed) are added below. The data are simulated academic data — the post says so, and must not be edited to imply real store results.

---

I turned my B.Sc. Data Science field project into a complete, portfolio-ready data analytics project — and I wanted to share what I built, and what I learned.

**Supermarket Sales Data Analysis**

It started with a field visit to Choice Super Market, Virar (East). The shop's real billing records were confidential, so — as my report states openly — I analysed a simulated dataset generated in Python (seed 42) for 1 July – 28 September 2026, and built the full pipeline:

- Audited the supplied report and notebooks, then re-ran the generation code and re-computed every headline number independently — all of them matched
- Cleaned 1,215 raw rows down to 1,191 valid records: 15 duplicates removed, 30 missing discounts and 20 missing payment methods handled, 9 invalid rows removed, 40 category names standardised
- Explored sales by category, product, brand, month, payment method, customer type and weekday vs weekend in a 124-cell Jupyter notebook with 19 figures
- Built an interactive Streamlit dashboard with category, brand, payment and customer filters

A few findings from the simulated data:

- Final Sales: ₹3,02,764.90 (Total Sales ₹3,17,577 − Discount ₹14,812.10), 3,160 units sold
- Personal Care led by value at ₹70,236.10 (23.2%), led by Moisturising Lotion 400 ml (₹27,048) — yet it sold the fewest units. Value and volume tell different stories
- August was the strongest month (₹1,19,633.75); September ends on 28 September, so I did not compare it as a full month
- UPI was the leading payment method — 581 records, ₹1,56,384.60
- Discounts barely correlated with Final Sales (r = −0.07) — discount alone does not explain sales value in this file

What mattered most to me was doing it honestly: every number was verified by running the code, the audit report lists the limitations, and the data are clearly labelled as simulated — not presented as the shop's real sales.

GitHub: https://github.com/harshkalambe6-crypto/supermarket-sales-data-analysis
Dashboard: https://supermarket-sales-data-analysis-4kpxcdnngr3ozsfog2waao.streamlit.app/

I would welcome feedback from data professionals — especially on the analysis and the dashboard design.

#DataScience #DataAnalytics #Python #Pandas #Streamlit #DataVisualization #PortfolioProject #BScDataScience #LearningInPublic

---

## Project description (for LinkedIn Featured / About section)

Supermarket Sales Data Analysis — a B.Sc. Data Science field project by Harsh Ganesh Kalambe, based on a visit to Choice Super Market, Virar (East). Audited and re-verified a simulated supermarket dataset (1,191 cleaned records, Jul–Sep 2026) with Python, Pandas, Matplotlib and Seaborn; built an interactive Streamlit dashboard; documented the audit, findings, limitations and recommendations in a full README and audit report. GitHub: https://github.com/harshkalambe6-crypto/supermarket-sales-data-analysis.
