WITH city_revenue as (
    SELECT
        city,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY city
),
total_city AS (
    SELECT 
        SUM(total_revenue) AS all_revenue_city
    FROM city_revenue
)
SELECT  
    city_revenue.city,
    city_revenue.total_revenue,
    ROUND(city_revenue.total_revenue * 100.0 / total_city.all_revenue_city,2) AS revenue_share
FROM city_revenue, total_city
ORDER BY revenue_share DESC;


WITH product_revenue AS (
    SELECT 
        product_category,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY product_category 
),
total_product AS (
    SELECT
        SUM(total_revenue) AS all_revenue_product
    FROM product_revenue
)
SELECT
    product_revenue.product_category,
    product_revenue.total_revenue,
    ROUND(product_revenue.total_revenue * 100.0 / total_product.all_revenue_product ,2) AS revenue_share
FROM product_revenue, total_product
ORDER BY revenue_share DESC;


WITH monthly AS (
    SELECT 
        month,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY month
    ORDER BY month
)
SELECT *
FROM monthly
WHERE total_revenue < 400;


WITH customer_revenue AS (
    SELECT 
        customer_name,
        city,
        COUNT(order_id) AS orders_count,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY customer_name, city
),
total_customer AS (
    SELECT 
        SUM(total_revenue) AS all_revenue
    FROM customer_REVENUE
),
finally_customer AS ( 
    SELECT 
        customer_revenue.customer_name,
        customer_revenue.city,
        customer_revenue.orders_count,
        customer_revenue.total_revenue,
        ROUND(customer_revenue.total_revenue * 100.0 / total_customer.all_revenue,2) AS revenue_share
    FROM customer_revenue, total_customer
    ORDER BY revenue_share DESC
)
SELECT
    customer_name,
    city,
    orders_count,
    total_revenue,
    revenue_share,
    CASE
        WHEN revenue_share >= 5 THEN 'VIP'
        WHEN revenue_share >= 3 AND revenue_share < 5 THEN 'Regular'
        ELSE 'Low Value'
    END AS customer_segments
FROM finally_customer;
