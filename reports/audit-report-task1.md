# TASK 1 — AUDIT REPORT
## Supermarket Sales Data Analysis — Harsh Ganesh Kalambe, B.Sc. Data Science

**Files audited (supplied by Harsh, 5 Nov 2026):**
- `Supermarket_Field_Project_DAP-1__1.pdf` — field project report, 20 sections, Choice Super Market, Virar (East), visit 29/09/2026
- `Field_Project_Supermarket_Analysis.ipynb` — 124 cells, no outputs
- `Supermarket_Field_Project_With_Outputs.ipynb` — 124 cells, with outputs

**Originals preserved in:** `docs/originals/`

## 1. What the two notebooks are

The two notebooks contain **identical code** — a diff shows they differ only in that one has outputs and the other does not. There is no conflicting version to reconcile.

## 2. Simulated vs real — the most important finding

**The sales dataset is simulated, not real.** This is stated explicitly in the PDF (Section 2) and in the notebook itself:

- "The supermarket's actual billing records are confidential and were not available for this project. Therefore, a sample sales dataset was created using Python (NumPy and pandas) for analytical demonstration."
- "The dataset used for analytical demonstration is a simulated/sample dataset and is not claimed to represent the actual sales records of the visited supermarket."
- Every raw row carries `Record_Source = "Simulated"`, and brand names are fictional.
- The field visit itself was real (Choice Super Market, Virar East, 29 Sep 2026, geotagged photographs, Lat 19.467296°, Long 72.815367°), but **no sales figure in this project is that shop's real sales**. The LinkedIn pack and README must keep saying so.

## 3. Dataset structure (verified by re-running the generation code)

The generation code (seed 42) was re-run from the notebook. It reproduced the raw file exactly:

- **Raw: 1,215 rows × 14 columns**, 1,200 generated + 15 intentional duplicates
- Columns: Bill_ID, Product_ID, Product_Name, Category, Sub_Category, Brand, Unit_Price, Quantity, Discount_Percent, Date, Payment_Method, Customer_Type, Stock_Available, Record_Source
- **42 products, 6 categories, 28 brands**
- Categories: Staples & Grocery, Beverages, Snacks & Confectionery, Personal Care, Home Care, Dairy & Bakery
- Dates: **1 Jul – 28 Sep 2026** (September ends on the 28th — it is not a full month)
- Customer types: Regular / Occasional / Bulk Buyer; Payments: UPI / Cash / Card
- Prices are fixed per product (₹20–₹620); quantities are Poisson-based, tripled for Bulk Buyers; weekend dates were given 1.5× sampling weight

## 4. Data-quality problems (all intentional, for the cleaning exercise)

| Problem | Count | Verified |
|---|---|---|
| Discount_Percent missing | 30 (2.47%) | ✓ matches notebook + PDF |
| Payment_Method missing | 20 (1.65%) | ✓ |
| Exact duplicate rows | 15 | ✓ |
| Category name variants (UPPER / lower / spaces) | 40 rows, 22 distinct spellings | ✓ |
| Quantity ≤ 0 (value −1) | 5 | ✓ |
| Unit_Price = 0 | 4 | ✓ |
| Invalid rows total (Quantity ≤ 0 or Unit_Price ≤ 0) | 9 | ✓ |

## 5. Cleaning — verified by independent re-run

The notebook's cleaning was re-run independently and reproduced its results exactly:

- Discount missing → fill 0; Payment missing → fill "Not Recorded"
- Drop 15 duplicates → 1,200 rows
- Category strip + title-case → 6 clean categories
- Date parsed "%d-%m-%Y"
- Drop 9 invalid rows → **1,191 rows**
- Drop Record_Source → **cleaned: 1,191 rows × 13 cols**, 0 missing values

## 6. Calculations — independently verified, all match

Recomputed from the regenerated raw file, after the same cleaning:

| Figure | Notebook / PDF | Independent re-run | Verdict |
|---|---|---|---|
| Total Sales (before discount) | ₹3,17,577.00 | ₹3,17,577 | ✓ |
| Total Discount Given | ₹14,812.10 | ₹14,812.10 | ✓ |
| Total Final Sales | ₹3,02,764.90 | ₹3,02,764.90 | ✓ |
| Average Final Sales / record | ₹254.21 | ₹254.21 | ✓ |
| Min / Max Final Sales | ₹18.00 / ₹2,388.00 | ₹18.00 / ₹2,388.00 | ✓ |
| Total quantity sold | 3,160 units | 3,160 | ✓ |
| Top category (value) | Personal Care ₹70,236.10 (23.2%) | ₹70,236.10 (23.2%) | ✓ |
| Lowest category (value) | Beverages ₹33,116.75 (10.9%) | ₹33,116.75 (10.9%) | ✓ |
| Top product | Moisturising Lotion 400 ml ₹27,048.00 | ₹27,048.00 | ✓ |
| Top 10 products' share | 52.0% | 52.0% | ✓ |
| Monthly: Jul / Aug / Sep | ₹97,200.30 / ₹1,19,633.75 / ₹85,930.85 | identical | ✓ |
| Highest daily sales | 20 Sep 2026, ₹7,222.40 | 20 Sep 2026, ₹7,222.40 | ✓ |
| Avg sales per weekend day | ₹4,670.49 (26 weekend days) | ₹4,670.49 | ✓ |
| Avg sales per weekday | ₹2,833.32 (64 weekdays) | ₹2,833.32 | ✓ |
| UPI share | 581 records, 48.8% | 581, 48.8% | ✓ |
| Bulk Buyer avg sale | ₹571.24, 6.27 units | ₹571.24, 6.27 | ✓ |
| Corr. Discount % vs Final Sales | −0.07 | −0.07 | ✓ |
| Corr. Quantity vs Total Sales | 0.53 | 0.53 | ✓ |
| Corr. Unit Price vs Total Sales | 0.67 | 0.67 | ✓ |
| Boxplot outliers (IQR method) | 76 records above upper whisker | 76 | ✓ |
| Median Final Sales / Unit Price | ₹168.00 / ₹84.00 | ₹168.00 / ₹84.00 | ✓ |

**No calculation errors were found.** Every headline number in the PDF and notebook outputs reproduced exactly.

## 7. Issues and limitations found (not errors, but must be stated)

1. **Simulated data** — the central limitation; results describe the sample file, not Choice Super Market.
2. **September is partial** (ends 28 Sep) — monthly comparisons must note this.
3. **"Not Recorded" payment (20 records, ₹3,695.20)** is a fill-in, not a real payment method; it should not be presented as a payment channel.
4. **No cost prices** — profit cannot be analysed (the PDF already states this).
5. **No customer IDs** — repeat-purchase / loyalty analysis is impossible.
6. **Three-month window only** — no annual seasonality can be claimed.
7. **Stock_Available is simulated per product** and shows almost no correlation with sales — it should not be used for stock recommendations.
8. **PDF placeholders** — student name, roll no., class, college and teacher are shown as `[MY NAME]` etc. in the supplied PDF. Those are for Harsh to fill in his academic submission; they are not filled in here.
9. **Dates are in the future relative to the project date in the files** (Jul–Sep 2026, visit 29 Sep 2026, academic year 2026–27) — reproduced as supplied, not altered.

## 8. Audit conclusion

The supplied project is internally consistent and its calculations are correct. The rebuild in this repository uses the same dataset, the same cleaning logic and the same verified numbers — it adds a professional GitHub structure, a Streamlit dashboard, refreshed charts, and a LinkedIn pack, without changing any result.
