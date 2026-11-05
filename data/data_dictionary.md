# Data Dictionary — Supermarket Sales Data Analysis

**Author:** Harsh Ganesh Kalambe, B.Sc. Data Science
**Field visit:** Choice Super Market, Virar (East), 29 Sep 2026

> **Data are simulated.** The shop's real billing records were confidential and are not in this project. The sales file was generated in Python (seed 42) for analytical demonstration. No finding here is that shop's real sales.

## Files

| File | Rows × columns | Description |
|---|---|---|
| `data/supermarket_sales_raw.csv` | 1,215 × 14 | Raw file as generated, including intentional data-quality problems and the `Record_Source` column |
| `data/supermarket_sales_cleaned.csv` | 1,191 × 13 | Cleaned file used by the notebook, charts and dashboard; 0 missing values |

Period: **1 Jul – 28 Sep 2026** (September ends 28 Sep — it is a partial month).
Products: 42 · Categories: 6 · Sub-categories: 36 · Brands: 28 (all brand names are fictional).

## Cleaned columns (13)

| Column | Type | Description | Values / range (cleaned) |
|---|---|---|---|
| `Bill_ID` | text | One record per row; unique per record in the cleaned file | 1,191 unique values, e.g. `B1001` |
| `Product_ID` | text | Product identifier | 42 unique values, e.g. `P101` |
| `Product_Name` | text | Product name, including pack size | 42 unique values, e.g. `Moisturising Lotion 400 ml` |
| `Category` | text | Product category, standardised to title case | 6 values: Beverages, Dairy & Bakery, Home Care, Personal Care, Snacks & Confectionery, Staples & Grocery |
| `Sub_Category` | text | Product sub-category | 36 values, e.g. Hair Care, Noodles, Edible Oil |
| `Brand` | text | Fictional brand name | 28 values, e.g. QuickBite, SilkyLocks, SunDrop |
| `Unit_Price` | integer (₹) | Price of one unit, before discount | 20 – 620, mean ₹103.92, median ₹84.00 |
| `Quantity` | integer | Units in the record | 1 – 15, mean 2.65; total 3,160 units |
| `Discount_Percent` | float (%) | Discount applied to the record | 0, 5, 10 or 15 only; mean 4.75% |
| `Date` | date (`YYYY-MM-DD`) | Transaction date | 2026-07-01 – 2026-09-28 |
| `Payment_Method` | text | How the record was paid | UPI 581, Cash 436, Card 154, "Not Recorded" 20 (a fill-in, not a payment channel) |
| `Customer_Type` | text | Customer group label (no customer IDs) | Regular 652, Occasional 405, Bulk Buyer 134 |
| `Stock_Available` | integer | Simulated stock level recorded with the row | 6 – 139 |

## Raw-only column

| Column | Type | Description |
|---|---|---|
| `Record_Source` | text | Always `"Simulated"` in the raw file; dropped during cleaning |

## Engineered columns (computed, not stored in the CSVs)

These are computed identically in `src/data_cleaning.py`, the notebook and `app.py`:

| Column | Definition |
|---|---|
| `Total_Sales` | `Unit_Price × Quantity` |
| `Discount_Amount` | `Total_Sales × Discount_Percent / 100`, rounded to 2 decimals |
| `Final_Sales` | `Total_Sales − Discount_Amount`, rounded to 2 decimals |
| `Month` | Month name from `Date` |
| `Day_Name` / `Day_Type` | Weekday name; Weekend vs Weekday (notebook only) |
| `Sales_Category` / `Quantity_Category` | Value/quantity bands (notebook only) |

Verified totals (cleaned file): Total Sales **₹3,17,577.00** · Discount **₹14,812.10** · Final Sales **₹3,02,764.90** · average Final Sales ₹254.21 per record.

## Cleaning rules (applied in `src/data_cleaning.py`, exactly as in the original notebook)

1. `Discount_Percent` missing (30 rows) → fill 0.
2. `Payment_Method` missing (20 rows) → fill `"Not Recorded"`.
3. Drop 15 exact duplicate rows.
4. `Category`: strip leading/trailing whitespace and title-case. The raw file contains 22 spellings/variants across 40 rows (e.g. `" Beverages "`, `BEVERAGES`, `beverages`).
5. Parse `Date` from `"%d-%m-%Y"` to `YYYY-MM-DD`.
6. Remove 9 invalid rows: `Quantity ≤ 0` (5 rows) and `Unit_Price = 0` (4 rows).
7. Drop `Record_Source`.

Result: 1,215 → 1,191 rows, 14 → 13 columns, 0 missing values.

## Known limitations (do not overlook these in an interview)

- **Simulated data** — findings describe the generated file, not the visited shop's real sales.
- **No customer IDs** — repeat-purchase, RFM and cohort analysis are not possible.
- **No cost prices** — profit / margin analysis is not possible.
- **`Bill_ID` is per record, not per basket** — basket / market-basket analysis is not possible.
- **`Stock_Available` is simulated** and barely correlates with sales; do not treat it as real inventory.
- **Three-month window; September is partial** (ends 28 Sep) — no annual seasonality can be claimed.
- **Discounts were assigned independently of product/price in the generation code** — that is why the discount–sales correlation (r = −0.07) is essentially zero; it is a property of how the file was generated, not evidence about real discount behaviour.
- **"Not Recorded" (20 records)** is a fill-in for a missing payment method, not a payment channel.
