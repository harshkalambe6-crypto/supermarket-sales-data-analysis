"""
Streamlit dashboard — Supermarket Sales Data Analysis.
Author: Harsh Ganesh Kalambe, B.Sc. Data Science

Data: Harsh's field project. The sales file is SIMULATED (seed 42),
1 Jul – 28 Sep 2026, Choice Super Market, Virar (East) was visited
on 29 Sep 2026 but its real billing records were confidential and
are NOT in this file. This dashboard shows static cleaned simulated
data. It is not live and not real-time.

Run locally:  streamlit run app.py
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")
st.title("🛒 Supermarket Sales Dashboard")
st.caption(
    "Simulated academic dataset (1 Jul – 28 Sep 2026) — not the real "
    "billing records of Choice Super Market, Virar. Figures describe "
    "this file only."
)


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/supermarket_sales_cleaned.csv", parse_dates=["Date"])
    df["Total_Sales"] = df["Unit_Price"] * df["Quantity"]
    df["Discount_Amount"] = (df["Total_Sales"] * df["Discount_Percent"] / 100).round(2)
    df["Final_Sales"] = (df["Total_Sales"] - df["Discount_Amount"]).round(2)
    df["Month"] = df["Date"].dt.month_name()
    return df


df = load_data()

st.sidebar.header("Filters")
categories = sorted(df["Category"].unique())
sel_cat = st.sidebar.multiselect("Category", categories, default=categories)
brands = sorted(df["Brand"].unique())
sel_brand = st.sidebar.multiselect("Brand", brands, default=brands)
payments = sorted(df["Payment_Method"].unique())
sel_pay = st.sidebar.multiselect("Payment Method", payments, default=payments)
customers = sorted(df["Customer_Type"].unique())
sel_cust = st.sidebar.multiselect("Customer Type", customers, default=customers)

filtered = df[
    df["Category"].isin(sel_cat)
    & df["Brand"].isin(sel_brand)
    & df["Payment_Method"].isin(sel_pay)
    & df["Customer_Type"].isin(sel_cust)
]
if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Final Sales", f"₹{filtered['Final_Sales'].sum():,.2f}")
col2.metric("Records", f"{len(filtered):,}")
col3.metric("Quantity Sold", f"{int(filtered['Quantity'].sum()):,}")
col4.metric("Avg Final Sale", f"₹{filtered['Final_Sales'].mean():,.2f}")
st.caption(
    f"Full cleaned file: Final Sales ₹3,02,764.90 · Total Sales ₹3,17,577.00 · "
    f"Discount ₹14,812.10 · 1,191 records · 3,160 units."
)

st.subheader("Final Sales by Category")
st.bar_chart(filtered.groupby("Category")["Final_Sales"].sum().sort_values(ascending=False))

st.subheader("Monthly Final Sales")
st.bar_chart(filtered.groupby("Month")["Final_Sales"].sum())

st.subheader("Top 10 Products by Final Sales")
st.bar_chart(filtered.groupby("Product_Name")["Final_Sales"].sum().sort_values(ascending=False).head(10))

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Final Sales by Brand (Top 10)")
    st.bar_chart(filtered.groupby("Brand")["Final_Sales"].sum().sort_values(ascending=False).head(10))
with col_b:
    st.subheader("Final Sales by Payment Method")
    st.bar_chart(filtered.groupby("Payment_Method")["Final_Sales"].sum())

st.subheader("Product Comparison")
products = sorted(filtered["Product_Name"].unique())
chosen = st.multiselect("Choose products to compare", products, default=products[:3])
if chosen:
    comp = (
        filtered[filtered["Product_Name"].isin(chosen)]
        .groupby("Product_Name")["Final_Sales"]
        .agg(["count", "sum", "mean"])
        .rename(columns={"count": "Records", "sum": "Final Sales (Rs.)", "mean": "Avg Sale (Rs.)"})
    )
    st.dataframe(comp.style.format("{:,.2f}"))

st.subheader("Business Insights (simulated data only)")
st.markdown(
    """
- **Personal Care leads by value: ₹70,236.10 (23.2%)**, led by Moisturising Lotion 400 ml (₹27,048.00) — yet it sold the fewest units (361). Value and volume tell different stories here.
- **Snacks & Confectionery is the most frequent category (259 records)** but only 4th by value — low price, high frequency.
- **August was the strongest month (₹1,19,633.75)**; September (₹85,930.85) ends on 28 Sep, so do not compare it as a full month.
- **UPI is the leading payment method: 581 records, ₹1,56,384.60 (48.8%)**.
- **Bulk Buyers average ₹571.24 per record** (6.27 units) vs Regular ₹209.05 — a small group with large baskets.
- **Discounts total ₹14,812.10 (4.7%)** and barely correlate with Final Sales (r = -0.07) — discount alone does not explain sales value in this file.
- **No profit analysis is possible** — cost prices are not in the dataset.
"""
)

st.subheader("Cleaned Data")
st.dataframe(filtered.sort_values("Date", ascending=False))
st.caption(f"Showing {len(filtered)} of {len(df)} cleaned records.")
