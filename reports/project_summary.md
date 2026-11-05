# Supermarket Sales Data Analysis — Project Summary

**Author:** Harsh Ganesh Kalambe, B.Sc. Data Science
**Field visit:** Choice Super Market, Virar (East), 29 Sep 2026
**Period:** 1 Jul – 28 Sep 2026 (September ends 28 Sep)
**Dataset: SIMULATED** — generated in Python, seed 42. Not the real billing records of the visited shop (those were confidential). See `reports/audit-report-task1.md`.

## Verified results (cleaned data, 1,191 records)

- **Total Sales (before discount): ₹3,17,577.00**
- **Total Discount Given: ₹14,812.10 (4.7%)**
- **Total Final Sales: ₹3,02,764.90**
- Average Final Sales per record: ₹254.21 · Median: ₹168.00 · Min: ₹18.00 · Max: ₹2,388.00
- Total quantity sold: 3,160 units · 42 products · 6 categories · 28 brands

### By category (Final Sales)

| Category | Records | Qty | Final Sales | Share |
|---|---|---|---|---|
| Personal Care | 135 | 361 | ₹70,236.10 | 23.2% |
| Staples & Grocery | 164 | 415 | ₹62,671.25 | 20.7% |
| Home Care | 167 | 420 | ₹60,029.00 | 19.8% |
| Snacks & Confectionery | 259 | 670 | ₹38,653.50 | 12.8% |
| Dairy & Bakery | 230 | 620 | ₹38,058.30 | 12.6% |
| Beverages | 236 | 674 | ₹33,116.75 | 10.9% |

Note the value/volume split: Beverages sold the most units (674) but the least value; Personal Care sold the fewest units (361) but the most value.

### Top products (Final Sales)

Moisturising Lotion 400 ml ₹27,048.00 · Tea Powder 500 g ₹21,324.00 · Wheat Flour 5 kg ₹21,203.00 · Room Freshener 250 ml ₹19,789.00 · Body Deodorant 150 ml ₹13,313.10. Top 10 products = 52.0% of Final Sales. Lowest: Iodised Salt 1 kg ₹1,197.30.

### By month, payment, customer

- July ₹97,200.30 (396 records) · August ₹1,19,633.75 (438) · September ₹85,930.85 (357, to 28 Sep)
- UPI 581 records, ₹1,56,384.60 (48.8%) · Cash 436, ₹1,08,751.15 · Card 154, ₹33,933.95 · Not Recorded 20, ₹3,695.20
- Regular 652 records (54.7%), avg ₹209.05 · Occasional 405, avg ₹222.02 · Bulk Buyer 134, avg ₹571.24, 6.27 units/record
- Weekend: 454 records, ₹1,21,432.65, ₹4,670.49 per weekend day · Weekday: 737 records, ₹1,81,332.25, ₹2,833.32 per weekday
- Highest daily sales: 20 Sep 2026, ₹7,222.40

### Discounts and correlations

- Discounts: 0% on 547 records, 5% on 326, 10% on 148, 15% on 170
- Correlation Discount % vs Final Sales: −0.07 (almost none)
- Correlation Quantity vs Total Sales: 0.53 · Unit Price vs Total Sales: 0.67
- Most common price band: ₹0–50 (437 records); median Unit Price ₹84.00

## Business recommendations (for the simulated store only)

1. Protect Personal Care availability — it drives 23.2% of value from only 135 records.
2. Keep UPI checkout fast and visible; it is nearly half of all records.
3. Serve Bulk Buyers well — 134 records, but the largest baskets (₹571.24 average).
4. Do not judge September as a weak month — it ends on 28 Sep.
5. Discounts alone do not explain sales value here (r = −0.07); test them against specific products, not across the board.
6. Review slow value items (Iodised Salt, Full Cream Milk, Cheese Slices) for display or stocking, not just price.

## Limitations

Simulated data; no cost prices (no profit analysis); no customer IDs; three-month window; September partial; Stock_Available is simulated and barely correlates with sales. Full list in the audit report.
