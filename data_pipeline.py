import pandas as pd
import sqlite3

# 1. Read CSV file
df = pd.read_csv("sales_data.csv")

# 2. Calculate Revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# 3. Connect to SQLite database
connection = sqlite3.connect("sales_database.db")

# 4. Load data into SQLite
df.to_sql("sales", connection, if_exists="replace", index=False)

print("Data loaded successfully into SQLite database!")


# 5. Verify the data
result = pd.read_sql_query("SELECT * FROM sales", connection)

print("\nData inside SQLite database:")
print(result)


# 6. Revenue by Product
query = """
SELECT Product,
       SUM(Revenue) AS Product_Revenue
FROM sales
GROUP BY Product
ORDER BY Product_Revenue DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nRevenue by Product:")
print(result)


# 7. Total Revenue
query = """
SELECT SUM(Revenue) AS Total_Revenue
FROM sales;
"""

result = pd.read_sql_query(query, connection)

print("\nTotal Revenue:")
print(result)


# 8. Total Quantity Sold
query = """
SELECT SUM(Quantity) AS Total_Quantity
FROM sales;
"""

result = pd.read_sql_query(query, connection)

print("\nTotal Quantity Sold:")
print(result)


# 9. Revenue by Category
query = """
SELECT Category,
       SUM(Revenue) AS Category_Revenue
FROM sales
GROUP BY Category
ORDER BY Category_Revenue DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nRevenue by Category:")
print(result)


# 10. Quantity Sold by Product
query = """
SELECT Product,
       SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Product
ORDER BY Total_Quantity DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nQuantity Sold by Product:")
print(result)


# 11. Top-Selling Product
query = """
SELECT Product,
       SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Product
ORDER BY Total_Quantity DESC
LIMIT 1;
"""

result = pd.read_sql_query(query, connection)

print("\nTop-Selling Product:")
print(result)


# 12. Close database connection
connection.close()

print("\nAll analysis completed successfully!")