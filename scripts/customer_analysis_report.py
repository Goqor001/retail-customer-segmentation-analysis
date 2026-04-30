import pandas as pd
import sqlite3

conn = sqlite3.connect("sales.db")
query = """
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
"""

df = pd.read_sql_query(query, conn)
df.to_csv("customer_segments_report.csv", index=False)
print("Customer segments report saved")

conn.close()
