# Supermarket Sales Data Analysis — Project Report

**Author:** Harsh Ganesh Kalambe, B.Sc. Data Science
**Field visit:** Choice Super Market, Virar (East), 29 Sep 2026
**Period:** 1 Jul – 28 Sep 2026 (September ends 28 Sep)
**Live dashboard:** https://supermarket-sales-data-analysis-4kpxcdnngr3ozsfog2waao.streamlit.app/
**GitHub:** https://github.com/harshkalambe6-crypto/supermarket-sales-data-analysis

> **Data are simulated.** The shop's real billing records were confidential and are not in this project. The sales file was generated in Python (seed 42) for analytical demonstration. No finding here is that shop's real sales. This report summarises the verified findings already documented in `reports/project_summary.md` and `reports/audit-report-task1.md` — it adds no new numbers.

## 1. Executive summary

This project turns a B.Sc. Data Science field project into a complete, reproducible analytics project: an independent audit of the supplied report and notebooks, documented cleaning, exploratory analysis in a 124-cell Jupyter notebook, six publication-ready charts, and an interactive Streamlit dashboard. Every headline number was re-computed independently and matched the supplied materials exactly.

Headline result (cleaned file, 1,191 records): **Final Sales ₹3,02,764.90** (Total Sales ₹3,17,577.00 − Discount ₹14,812.10), 3,160 units sold, average ₹254.21 per record. Personal Care leads by value (₹70,236.10, 23.2%); UPI is the leading payment method (581 records, 48.8%); August was the strongest month (₹1,19,633.75). Discounts barely correlate with Final Sales (r = −0.07) — a null result, not a causal finding.

## 2. Business problem

Which categories, products and brands drive sales, when sales rise and fall, how customers pay, and what discounts actually do — answered from the field-project dataset, honestly and within its limits.

## 3. Objectives

Audit the supplied materials without trusting their calculations; clean the raw file with every dropped/filled row accounted for; summarise sales by category, product, brand, month, payment, customer type and weekday/weekend; visualise the results; build an interactive dashboard; and present findings honestly, with limitations stated.

## 4. Dataset methodology

The sales file is **simulated** (seed 42, NumPy/pandas): 1,200 generated rows + 15 intentional duplicates = 1,215 raw rows × 14 columns; 42 products, 6 categories, 28 fictional brands. The field visit (29 Sep 2026, geotagged) was real; no sales figure is that shop's real sales. See `data/data_dictionary.md` for every column.

## 5. Data cleaning methodology

Implemented in `src/data_cleaning.py`, exactly as in the original notebook: fill Discount_Percent missing (30) with 0 and Payment_Method missing (20) with `"Not Recorded"`; drop 15 exact duplicates; standardise Category (strip + title-case, 40 rows with 22 spelling variants); parse Date `"%d-%m-%Y"`; remove 9 invalid rows (Quantity ≤ 0: 5; Unit_Price = 0: 4); drop `Record_Source`. Result: 1,191 rows × 13 columns, 0 missing values. Re-running the script reproduces the cleaned file exactly.

Feature engineering: `Total_Sales = Unit_Price × Quantity`; `Discount_Amount = Total_Sales × Discount_Percent / 100`; `Final_Sales = Total_Sales − Discount_Amount`.

## 6. Exploratory analysis — verified results

### Overall
Total Sales ₹3,17,577.00 · Discount ₹14,812.10 (4.7%) · Final Sales ₹3,02,764.90 · average ₹254.21, median ₹168.00, min ₹18.00, max ₹2,388.00 · 3,160 units · 42 products · 6 categories · 28 brands.

### By category (Final Sales)
| Category | Records | Units | Final Sales | Share |
|---|---|---|---|---|
| Personal Care | 135 | 361 | ₹70,236.10 | 23.2% |
| Staples & Grocery | 164 | 415 | ₹62,671.25 | 20.7% |
| Home Care | 167 | 420 | ₹60,029.00 | 19.8% |
| Snacks & Confectionery | 259 | 670 | ₹38,653.50 | 12.8% |
| Dairy & Bakery | 230 | 620 | ₹38,058.30 | 12.6% |
| Beverages | 236 | 674 | ₹33,116.75 | 10.9% |

### Top products
Moisturising Lotion 400 ml ₹27,048.00 · Tea Powder 500 g ₹21,324.00 · Wheat Flour 5 kg ₹21,203.00 · Room Freshener 250 ml ₹19,789.00 · Body Deodorant 150 ml ₹13,313.10. Top 10 products = 52.0% of Final Sales. Lowest: Iodised Salt 1 kg ₹1,197.30.

### By month, payment, customer
July ₹97,200.30 (396 records) · August ₹1,19,633.75 (438) · September ₹85,930.85 (357, to 28 Sep). UPI 581 records, ₹1,56,384.60 (48.8%) · Cash 436, ₹1,08,751.15 · Card 154, ₹33,933.95 · Not Recorded 20, ₹3,695.20. Regular 652 records (54.7%), avg ₹209.05 · Occasional 405, avg ₹222.02 · Bulk Buyer 134, avg ₹571.24, 6.27 units/record. Weekend ₹4,670.49/day (26 days) vs weekday ₹2,833.32/day (64 days); highest daily sale 20 Sep 2026, ₹7,222.40.

### Discounts and correlations
Discounts: 0% on 547 records, 5% on 326, 10% on 148, 15% on 170. Correlation Discount % vs Final Sales −0.07; Quantity vs Total Sales 0.53; Unit Price vs Total Sales 0.67. IQR boxplot outliers: 76 records above the upper whisker — reported, not deleted.

## 7. Business findings

1. Value and volume diverge: Personal Care leads value with the fewest units; Beverages lead units with the least value.
2. Sales concentrate: the top 10 products are 52.0% of Final Sales.
3. August is the strongest full month; September must not be judged as a full month.
4. UPI is nearly half of all records — checkout speed for UPI matters.
5. Bulk Buyers are few (134 records) but have the largest baskets.
6. Discounts do not explain sales value in this file (r = −0.07), and that is a property of how the file was generated (discounts assigned independently), not evidence about real discount behaviour.

## 8. Recommendations (for the simulated store only)

1. Protect Personal Care availability — 23.2% of value from 135 records.
2. Keep UPI checkout fast and visible.
3. Serve Bulk Buyers well — largest baskets.
4. Do not judge September as weak — it is a partial month.
5. Test discounts product by product; a blanket discount does not explain sales here.
6. Review slow-value items (Iodised Salt, Full Cream Milk, Cheese Slices) for display/stocking.

## 9. Limitations

Simulated data; no cost prices (no profit analysis); no customer IDs (no repeat-purchase, RFM or cohort analysis); `Bill_ID` is per record, not per basket; three-month window, September partial; `Stock_Available` is simulated and barely correlates with sales; `"Not Recorded"` payment is a fill-in, not a channel. Full list in the audit report.

## 10. Future scope

Real, permissioned transaction data; cost prices for profit analysis; customer and basket IDs for retention and basket analysis; a longer (12-month) time series for seasonality and a validated forecast.

## 11. Technical references

Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook · Streamlit (Python 3.12, Streamlit Community Cloud). Repository: https://github.com/harshkalambe6-crypto/supermarket-sales-data-analysis. Original field-project PDF and notebooks are preserved unchanged in `docs/originals/`.
