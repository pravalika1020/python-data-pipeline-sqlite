-- 1. View all sales
SELECT *
FROM sales;


-- 2. Calculate total revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM sales;


-- 3. Find total quantity sold
SELECT SUM(Quantity) AS Total_Quantity
FROM sales;


-- 4. Find revenue by product
SELECT Product,
       SUM(Revenue) AS Product_Revenue
FROM sales
GROUP BY Product
ORDER BY Product_Revenue DESC;


-- 5. Find revenue by category
SELECT Category,
       SUM(Revenue) AS Category_Revenue
FROM sales
GROUP BY Category
ORDER BY Category_Revenue DESC;


-- 6. Find the top-selling product by quantity
SELECT Product,
       SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Product
ORDER BY Total_Quantity DESC
LIMIT 1;