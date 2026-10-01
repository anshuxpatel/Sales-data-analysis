import pandas as pd

data = pd.read_csv("sales_data.csv")

print(data)
data["Total_Sales"] = data["Quantity"] * data["Price"]

print("\nTotal Sales Revenue:")
print(data["Total_Sales"].sum())
print("\nProduct-wise Sales:")

product_sales = data.groupby("Product")["Total_Sales"].sum()

print(product_sales)
print("\nHighest Selling Product:")

highest_product = product_sales.idxmax()

print(highest_product)
print("Total Sales:", product_sales.max())
print("\nCategory-wise Sales:")

category_sales = data.groupby("Category")["Total_Sales"].sum()

print(category_sales)
print("\nMonth-wise Sales:")

monthly_sales = data.groupby("Month")["Total_Sales"].sum()

print(monthly_sales)
import matplotlib.pyplot as plt

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()
print("\nHighest Sales Month:")

highest_month = monthly_sales.idxmax()

print(highest_month)
print("Total Sales:", monthly_sales.max())
category_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Category-wise Sales")
plt.ylabel("")
plt.show()
print("\n--- SALES FINAL REPORT ---")

print("Total Orders:", len(data))
print("Total Products:", data["Product"].nunique())
print("Total Revenue:", data["Total_Sales"].sum())

print("Highest Selling Product:", product_sales.idxmax())
print("Highest Sales Month:", monthly_sales.idxmax())

print("Total Categories:", data["Category"].nunique())
data.to_csv("sales_analysis_result.csv", index=False)

print("Sales analysis data saved successfully!")