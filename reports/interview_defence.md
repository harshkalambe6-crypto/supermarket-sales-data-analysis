# Interview Defence — Supermarket Sales Data Analysis

**Author:** Harsh Ganesh Kalambe, B.Sc. Data Science
**Project:** Supermarket Sales Data Analysis (field project, Choice Super Market, Virar (East), visit 29 Sep 2026)

> Every answer below is based only on this project as built. Where the data cannot support a claim, the answer says so — do not invent a stronger claim in an interview. All figures are from the cleaned file (1,191 records) and are verified in `reports/audit-report-task1.md` and `reports/project_summary.md`. **The data are simulated** — never present them as the shop's real sales.

## The project in one minute

"I visited Choice Super Market in Virar (East) on 29 Sep 2026. The shop's real billing records were confidential, so I analysed a simulated dataset generated in Python (seed 42) for 1 Jul – 28 Sep 2026. I audited the supplied report and notebooks, re-ran the generation and cleaning code, and re-computed every headline number independently — they all matched. I cleaned 1,215 raw rows to 1,191 valid records, explored sales by category, product, brand, month, payment and customer type in a 124-cell notebook, and built a Streamlit dashboard. Final Sales were ₹3,02,764.90 across 3,160 units."

## Likely questions and answers

### 1. Is this real store data?
No. The sales file is simulated (seed 42). The field visit was real, but the shop's real billing records were confidential and are not in the project. Every record in the raw file has `Record_Source = "Simulated"`, and the README, dashboard and LinkedIn post all say so. No finding here is that shop's real sales.

### 2. Walk me through your cleaning. What did you drop, and why?
- Filled 30 missing `Discount_Percent` values with 0 and 20 missing `Payment_Method` values with `"Not Recorded"` — these are documented fill-ins, not real values.
- Dropped 15 exact duplicate rows.
- Standardised `Category` (strip + title-case): the raw file had 22 spellings/variants across 40 rows, e.g. `" Beverages "`, `BEVERAGES`, `beverages`.
- Parsed `Date` from `"%d-%m-%Y"`.
- Removed 9 invalid rows: `Quantity ≤ 0` (5) and `Unit_Price = 0` (4).
- Dropped `Record_Source`.
- Result: 1,215 rows × 14 cols → 1,191 rows × 13 cols, 0 missing values. Every decision is in `src/data_cleaning.py` and `data/data_dictionary.md`.

### 3. How did you compute Final Sales?
`Total_Sales = Unit_Price × Quantity`; `Discount_Amount = Total_Sales × Discount_Percent / 100`; `Final_Sales = Total_Sales − Discount_Amount`. Verified totals: Total Sales ₹3,17,577.00 − Discount ₹14,812.10 = Final Sales ₹3,02,764.90. Average ₹254.21 per record, median ₹168.00.

### 4. What is the headline finding?
Personal Care leads by value — ₹70,236.10 (23.2%) from only 135 records — led by Moisturising Lotion 400 ml (₹27,048.00). But it sold the fewest units (361). Beverages sold the most units (674) but the least value (₹33,116.75, 10.9%). Value and volume tell different stories, so a recommendation based on record count alone would be wrong.

### 5. Which month performed best?
August: ₹1,19,633.75 (438 records), vs July ₹97,200.30 and September ₹85,930.85. But September ends on 28 Sep, so it is a partial month — I do not compare it as a full month, and I would not call it a weak month.

### 6. What about payments and customers?
UPI leads: 581 records, ₹1,56,384.60 (48.8%). Cash 436 records, Card 154. Bulk Buyers average ₹571.24 per record (6.27 units) vs Regular ₹209.05 — a small group (134 records) with the largest baskets. Weekend days average ₹4,670.49/day (26 days) vs weekday ₹2,833.32/day (64 days); highest single day was 20 Sep 2026, ₹7,222.40.

### 7. Do discounts drive sales?
No — not in this file. Discount vs Final Sales correlation is r = −0.07, essentially zero. That is a **null result, not a causal finding**. Discounts were assigned independently of product and price when the file was generated, so the correlation reflects how the file was made, not how real customers respond to discounts. My recommendation is to test discounts product by product, not to claim discounts do not work.

### 8. Can you do RFM / cohort / repeat-purchase analysis?
No. There are no customer IDs — only a coarse `Customer_Type` label (Regular / Occasional / Bulk Buyer). Repeat-purchase, RFM and cohort analysis are impossible with this file. That is a stated limitation, and it is the first thing I would fix with a better dataset.

### 9. Can you analyse profit?
No. There are no cost prices in the dataset, so margin/profit analysis is impossible. I only analyse sales value, never profit.

### 10. Can you do basket analysis?
No. `Bill_ID` is one record per row, not one basket per transaction, so items bought together cannot be identified.

### 11. What about the 76 outliers?
Using the IQR boxplot method there are 76 records above the upper whisker. I did **not** delete them — they are high-value legitimate records in this file (e.g. Bulk Buyer records up to ₹2,388), and deleting them to make the charts look tidy would be manipulating the data. They are reported, not removed.

### 12. How did you verify your numbers?
I did not trust the supplied PDF/notebook calculations. I re-ran the generation code and the cleaning code and re-computed every headline number independently; the audit report (`reports/audit-report-task1.md`) shows the PDF, notebook and my re-computation agreeing on every checked figure. Re-running `src/data_cleaning.py` reproduces the cleaned file byte-for-byte, and `src/visualization.py` regenerates the charts from it.

### 13. What are the limitations of this project?
- Simulated data, not real sales.
- No cost prices (no profit), no customer IDs (no retention/RFM/cohort), no basket IDs.
- Three-month window only; September partial; no annual seasonality.
- `Stock_Available` is simulated and barely correlates with sales — I do not use it for stock recommendations.
- `"Not Recorded"` payment (20 records) is a fill-in, not a payment channel.
- Fixed prices per product and independently assigned discounts, so discount and price effects cannot be studied causally.

### 14. What would you do next with a better dataset?
Add customer IDs and basket/transaction IDs, cost prices, a longer time series (12 months), and real promotional calendars. Then RFM and cohort analysis, basket analysis, profit analysis, and a properly validated forecast would become possible. Until then, I would not claim any of those.

### 15. What did you actually build, technically?
Python + Pandas/NumPy for cleaning and analysis, Matplotlib/Seaborn for 6 charts, a 124-cell Jupyter notebook, and a Streamlit dashboard (Python 3.12, deployed on Streamlit Community Cloud) with date/product/category/brand/payment/customer filters and a filtered-CSV download. The project is on GitHub with the audit report, data dictionary, and this defence document.
