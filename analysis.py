import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load data
df = pd.read_csv("train.csv")

# Data overview
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print(f"Missing Values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nSales Stats:\n{df['Sales'].describe()}")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

# 1. Sales by Category
data_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure()
bars = plt.bar(data_category.index, data_category.values, color=['#2196F3', '#4CAF50', '#FF5722'])
plt.title("Total Sales by Category", fontsize=16, fontweight='bold')
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
for bar, val in zip(bars, data_category.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
             f'${val:,.0f}', ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig("category_sales.png", dpi=150)
plt.show()

# 2. Sales by Region
data_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure()
bars = plt.bar(data_region.index, data_region.values, color=['#9C27B0', '#00BCD4', '#FF9800', '#F44336'])
plt.title("Total Sales by Region", fontsize=16, fontweight='bold')
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
for bar, val in zip(bars, data_region.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
             f'${val:,.0f}', ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig("region_sales.png", dpi=150)
plt.show()

# 3. Top 10 Products
data_product = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 7))
plt.barh(data_product.index, data_product.values, color='#2196F3')
plt.title("Top 10 Best Selling Products", fontsize=16, fontweight='bold')
plt.xlabel("Total Sales ($)", fontsize=12)
plt.ylabel("")
plt.tight_layout()
plt.savefig("product_sales.png", dpi=150)
plt.show()

# 4. Monthly Sales Trend
data_month = df.groupby("Month")["Sales"].sum()
plt.figure()
plt.plot(data_month.index, data_month.values, marker='o', color='#2196F3', linewidth=2.5)
plt.fill_between(data_month.index, data_month.values, alpha=0.1, color='#2196F3')
plt.title("Monthly Sales Trend", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun',
                           'Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig("monthly_trend.png", dpi=150)
plt.show()

# 5. Sales by Segment
data_segment = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
plt.figure()
plt.pie(data_segment.values, labels=data_segment.index, autopct='%1.1f%%',
        colors=['#2196F3', '#4CAF50', '#FF5722'], startangle=90)
plt.title("Sales Distribution by Segment", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig("segment_sales.png", dpi=150)
plt.show()

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(f"Best Region    : {data_region.index[0]} (${data_region.values[0]:,.0f})")
print(f"Best Category  : {data_category.index[0]} (${data_category.values[0]:,.0f})")
print(f"Best Month     : {data_month.idxmax()} ({['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][data_month.idxmax()-1]})")
print(f"Total Sales    : ${df['Sales'].sum():,.0f}")
