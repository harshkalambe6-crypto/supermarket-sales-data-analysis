"""
Visualizations — Supermarket Sales Data Analysis.
Author: Harsh Ganesh Kalambe, B.Sc. Data Science

Reads data/supermarket_sales_cleaned.csv, adds the engineered columns
(Total_Sales, Discount_Amount, Final_Sales, Month) exactly as in the
original notebook, and saves charts to visuals/:
  sales_overview.png    - monthly Final Sales (Fig. 14 in the report)
  category_analysis.png - Final Sales by category (Fig. 4)
  product_analysis.png  - top 10 products by Final Sales (Fig. 6)
  category_share.png    - category share donut (Fig. 8)
  payment_analysis.png  - payment method distribution (Fig. 17)
  daily_trend.png       - daily sales + 7-day moving average (Fig. 13)

All figures are in Indian rupees, Final Sales = after discount.
Run:  python src/visualization.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "supermarket_sales_cleaned.csv"
VISUALS = ROOT / "visuals"
sns.set_theme(style="whitegrid")
plt.rcParams.update({"figure.dpi": 150})


def load() -> pd.DataFrame:
    df = pd.read_csv(CLEAN, parse_dates=["Date"])
    df["Total_Sales"] = df["Unit_Price"] * df["Quantity"]
    df["Discount_Amount"] = (df["Total_Sales"] * df["Discount_Percent"] / 100).round(2)
    df["Final_Sales"] = (df["Total_Sales"] - df["Discount_Amount"]).round(2)
    df["Month"] = df["Date"].dt.month_name()
    df["Month_No"] = df["Date"].dt.month
    return df


def main() -> None:
    VISUALS.mkdir(exist_ok=True)
    df = load()
    cat = df.groupby("Category")["Final_Sales"].sum().sort_values(ascending=False)

    monthly = df.groupby(["Month_No", "Month"])["Final_Sales"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5.5))
    bars = ax.bar(monthly["Month"], monthly["Final_Sales"], color=["#4c72b0", "#55a868", "#c44e52"])
    ax.bar_label(bars, fmt="%.0f")
    ax.set_title("Monthly Final Sales (Jul–Sep 2026, Sep ends 28 Sep)")
    ax.set_ylabel("Final Sales (Rs.)")
    fig.tight_layout(); fig.savefig(VISUALS / "sales_overview.png"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    sns.barplot(x=cat.index, y=cat.values, hue=cat.index, palette="viridis", legend=False, ax=ax)
    ax.set_title("Total Final Sales by Product Category")
    ax.set_ylabel("Final Sales (Rs.)")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout(); fig.savefig(VISUALS / "category_analysis.png"); plt.close(fig)

    top10 = df.groupby("Product_Name")["Final_Sales"].sum().sort_values(ascending=False).head(10).sort_values()
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.barh(top10.index, top10.values, color="teal")
    ax.set_title("Top 10 Products by Final Sales")
    ax.set_xlabel("Final Sales (Rs.)")
    fig.tight_layout(); fig.savefig(VISUALS / "product_analysis.png"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.pie(cat.values, autopct="%1.1f%%", startangle=90, pctdistance=0.78,
           wedgeprops={"width": 0.45, "edgecolor": "white"})
    ax.legend(cat.index, title="Category", loc="center left", bbox_to_anchor=(1, 0.5))
    ax.set_title("Category Share in Total Final Sales")
    fig.tight_layout(); fig.savefig(VISUALS / "category_share.png"); plt.close(fig)

    pay = df["Payment_Method"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5.5))
    bars = ax.bar(pay.index, pay.values, color="slateblue")
    ax.bar_label(bars)
    ax.set_title("Payment Method Distribution")
    ax.set_ylabel("Number of Records")
    fig.tight_layout(); fig.savefig(VISUALS / "payment_analysis.png"); plt.close(fig)

    daily = df.groupby("Date")["Final_Sales"].sum()
    rolling = daily.rolling(7).mean()
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(daily.index, daily.values, color="lightsteelblue", label="Daily Sales")
    ax.plot(rolling.index, rolling.values, color="darkred", linewidth=2, label="7-Day Moving Average")
    ax.set_title("Daily Sales Trend (July–September 2026)")
    ax.set_ylabel("Final Sales (Rs.)")
    ax.legend(); ax.tick_params(axis="x", rotation=30)
    fig.tight_layout(); fig.savefig(VISUALS / "daily_trend.png"); plt.close(fig)
    print("Saved 6 charts to visuals/")


if __name__ == "__main__":
    main()
