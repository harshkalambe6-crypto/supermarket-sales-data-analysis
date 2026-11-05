"""
Data cleaning — Supermarket Sales Data Analysis.
Author: Harsh Ganesh Kalambe, B.Sc. Data Science

Source: Harsh's field project (Choice Super Market, Virar East, visit
29 Sep 2026). The sales file itself is SIMULATED — see README and
reports/audit-report-task1.md. The shop's real billing records were
confidential and were not available. The raw file was generated with
NumPy/pandas, seed 42, and is reproduced exactly by the generation
code in the notebook (Section 2) and in docs/originals/.

Cleaning steps — exactly as in Harsh's original notebook:
1. Discount_Percent missing (30) -> fill 0.
2. Payment_Method missing (20) -> fill "Not Recorded".
3. Drop 15 exact duplicate rows.
4. Category: strip whitespace and title-case (fixes 40 rows that
   were UPPER / lower / padded with spaces).
5. Date: parse "%d-%m-%Y".
6. Remove invalid rows: Quantity <= 0 (5) or Unit_Price <= 0 (4) -> 9 rows.
7. Drop Record_Source (it only says "Simulated") and save cleaned file.

Raw: 1,215 rows x 14 cols -> Cleaned: 1,191 rows x 13 cols.
Run:  python src/data_cleaning.py
"""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "supermarket_sales_raw.csv"
CLEAN = ROOT / "data" / "supermarket_sales_cleaned.csv"


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    print(f"Raw shape: {df.shape}")
    print("Missing before cleaning:")
    print(df.isna().sum().to_string())

    df["Discount_Percent"] = df["Discount_Percent"].fillna(0)
    df["Payment_Method"] = df["Payment_Method"].fillna("Not Recorded")

    n_dup = int(df.duplicated().sum())
    df = df.drop_duplicates()
    print(f"Duplicates removed: {n_dup}")

    df["Category"] = df["Category"].str.strip().str.title()
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

    n_invalid = int(((df["Quantity"] <= 0) | (df["Unit_Price"] <= 0)).sum())
    df = df[(df["Quantity"] > 0) & (df["Unit_Price"] > 0)]
    print(f"Invalid rows removed (Quantity<=0 or Unit_Price<=0): {n_invalid}")

    df = df.drop(columns=["Record_Source"]).reset_index(drop=True)
    print(f"Cleaned shape: {df.shape}")
    print(f"Missing after cleaning: {int(df.isna().sum().sum())}")
    return df


def main() -> None:
    raw = pd.read_csv(RAW)
    cleaned = clean(raw)
    cleaned.to_csv(CLEAN, index=False)
    print(f"Saved cleaned data to {CLEAN}")


if __name__ == "__main__":
    main()
