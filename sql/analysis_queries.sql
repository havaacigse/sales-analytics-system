
SELECT 
    p.category,
    SUM(o.sales) AS total_sales
FROM orders_new o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;


SELECT 
    region,
    SUM(sales) AS total_sales
FROM orders_new
GROUP BY region
ORDER BY total_sales DESC;


SELECT category, product_name, total_sales
FROM (
    SELECT 
        p.category,
        p.product_name,
        SUM(o.sales) AS total_sales,
        RANK() OVER (
            PARTITION BY p.category 
            ORDER BY SUM(o.sales) DESC
        ) AS rnk
    FROM orders_new o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category, p.product_name
)
WHERE rnk = 1;




SELECT 
    p.product_name,
    SUM(o.sales) AS total_sales
FROM orders_new o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
LIMIT 5;



SELECT 
    strftime('%Y-%m', order_date) AS month,
    SUM(sales) AS total_sales
FROM orders_new
GROUP BY month
ORDER BY month;


WITH category_sales AS (
    SELECT 
        p.category,
        SUM(o.sales) AS total_sales
    FROM orders_new o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category
)
SELECT *
FROM category_sales
ORDER BY total_sales DESC;



SELECT 
    AVG(sales) AS avg_order_value
FROM orders_new;


SELECT city, SUM(sales) AS total_sales
FROM orders_new
GROUP BY city
ORDER BY total_sales DESC
LIMIT 5;


SELECT p.category, AVG(o.sales) AS avg_sales
FROM orders_new o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category;


SELECT strftime('%Y', order_date) AS year, SUM(sales) AS total_sales
FROM orders_new
GROUP BY year
ORDER BY year;


SELECT *
FROM (
    SELECT p.category, strftime('%Y', o.order_date) AS year, SUM(o.sales) AS total_sales,
    RANK() OVER (PARTITION BY p.category ORDER BY SUM(o.sales) DESC) AS rnk
    FROM orders_new o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category, year
)
WHERE rnk = 1;

