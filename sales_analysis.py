import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/sales.csv")

# =========================
# DATA CLEANING
# =========================

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Revenue Calculation
df["Revenue"] = df["Quantity"] * df["Unit Price"]

# =========================
# KPI CALCULATIONS
# =========================

total_revenue = df["Revenue"].sum()

total_orders = df["Order ID"].nunique()

average_order_value = total_revenue / total_orders

# =========================
# TOP PRODUCTS
# =========================

top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# =========================
# TOP REGIONS
# =========================

top_regions = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# =========================
# MONTHLY SALES TREND
# =========================

df["Month"] = df["Order Date"].dt.strftime("%Y-%m")

monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
)

# =========================
# PRINT RESULTS
# =========================

print("=" * 50)
print("SALES ANALYSIS REPORT")
print("=" * 50)

print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

print(f"Total Orders: {total_orders}")

print(f"Average Order Value: ₹{average_order_value:,.2f}")

print("\nTOP PRODUCTS")
print(top_products)

print("\nTOP REGIONS")
print(top_regions)

# =========================
# CHART 1
# Monthly Sales
# =========================

plt.figure(figsize=(10,5))

monthly_sales.plot(
    kind="bar",
    color="skyblue"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("charts/monthly_sales.png")

plt.close()

# =========================
# CHART 2
# Top Products
# =========================

plt.figure(figsize=(10,5))

top_products.plot(
    kind="bar",
    color="green"
)

plt.title("Top Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("charts/top_products.png")

plt.close()

# =========================
# CHART 3
# Top Regions
# =========================

plt.figure(figsize=(10,5))

top_regions.plot(
    kind="bar",
    color="orange"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("charts/regions.png")

plt.close()

# =========================
# BUSINESS INSIGHTS
# =========================

print("\nBUSINESS INSIGHTS")

print(
    f"\n1. Highest revenue product: "
    f"{top_products.idxmax()}"
)

print(
    f"2. Best performing region: "
    f"{top_regions.idxmax()}"
)

print(
    f"3. Total business revenue generated: "
    f"₹{total_revenue:,.2f}"
)

print("\nRECOMMENDATIONS")

print("• Increase inventory of top-selling products.")
print("• Focus marketing in high-performing regions.")
print("• Improve sales strategy in low-performing regions.")
print("• Track monthly trends for seasonal demand.")

print("\nCharts saved successfully.")