--top selling brand analysis
WITH brand_sales AS (
    SELECT
        brand_name,
        SUM(revenue) total_revenue
    FROM biker_r_project.gold.sales_fact
    GROUP BY brand_name
)

SELECT *,
       DENSE_RANK() OVER(
           ORDER BY total_revenue DESC
       ) brand_rank
FROM brand_sales;

--store X category performance
SELECT
    store_name,
    category_name,
    COUNT(DISTINCT order_id) orders,
    SUM(revenue) revenue
FROM biker_r_project.gold.sales_fact
GROUP BY
    store_name,
    category_name
ORDER BY revenue DESC;


--inventory risk analysis
WITH sales AS (
    SELECT
        product_id,
        SUM(quantity) units_sold
    FROM biker_r_project.gold.sales_fact
    GROUP BY product_id
)

SELECT
    p.product_name,
    COALESCE(s.units_sold,0) units_sold,
    SUM(st.quantity) stock_remaining
FROM biker_r_project.raw.products p
LEFT JOIN sales s
    ON p.product_id = s.product_id
LEFT JOIN biker_r_project.raw.stocks st
    ON p.product_id = st.product_id
GROUP BY
    p.product_name,
    s.units_sold
ORDER BY stock_remaining;


--top 5 customer per store
WITH customer_sales AS (
SELECT
    store_name,
    customer_name,
    SUM(revenue) total_spent
FROM biker_r_project.gold.sales_fact
GROUP BY
    store_name,
    customer_name
)

SELECT *
FROM (
SELECT *,
       ROW_NUMBER() OVER(
           PARTITION BY store_name
           ORDER BY total_spent DESC
       ) rn
FROM customer_sales
)
WHERE rn <= 5;


--revenue growth month-over-month
WITH monthly_sales AS (
SELECT
    YEAR(order_date) yr,
    MONTH(order_date) mn,
    SUM(revenue) revenue
FROM biker_r_project.gold.sales_fact
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
)

SELECT *,
       LAG(revenue)
       OVER(
           ORDER BY yr,mn
       ) prev_month,

       ROUND(
       (
         revenue -
         LAG(revenue)
         OVER(ORDER BY yr,mn)
       ) *100/
       LAG(revenue)
       OVER(ORDER BY yr,mn),
       2
       ) growth_pct

FROM monthly_sales;


--customer segmentation(NTILE)
WITH customer_sales AS (
SELECT
    customer_id,
    customer_name,
    SUM(revenue) lifetime_value
FROM biker_r_project.gold.sales_fact
GROUP BY
    customer_id,
    customer_name
)
SELECT *,
       NTILE(4)
       OVER(
           ORDER BY lifetime_value DESC
       ) customer_segment
FROM customer_sales;


--best employee performance 
SELECT
    stf.staff_id,
    CONCAT(
       stf.first_name,
       ' ',
       stf.last_name
    ) employee_name,

    COUNT(DISTINCT o.order_id) orders_handled

FROM biker_r_project.raw.orders o
JOIN biker_r_project.raw.staffs stf
     ON o.staff_id = stf.staff_id

GROUP BY
    stf.staff_id,
    employee_name

ORDER BY orders_handled DESC;


--store revenue leaderboard
SELECT
    store_name,
    SUM(revenue) revenue,

    DENSE_RANK() OVER(
        ORDER BY SUM(revenue) DESC
    ) revenue_rank

FROM biker_r_project.gold.sales_fact

GROUP BY store_name;

--product market basket analysis
SELECT
    oi1.product_id product_a,
    oi2.product_id product_b,
    COUNT(*) frequency
FROM biker_r_project.raw.order_items oi1
JOIN biker_r_project.raw.order_items oi2
     ON oi1.order_id = oi2.order_id
    AND oi1.product_id < oi2.product_id
GROUP BY
    product_a,
    product_b
ORDER BY frequency DESC;


--revenue contribution %
WITH sales AS (
SELECT
    product_name,
    SUM(revenue) revenue
FROM biker_r_project.gold.sales_fact
GROUP BY product_name
)

SELECT
    *,
    ROUND(
        revenue *100/
        SUM(revenue) OVER(),
        2
    ) revenue_pct
FROM sales;


--top product per brand
WITH brand_product_sales AS (
SELECT
    brand_name,
    product_name,
    SUM(revenue) revenue
FROM biker_r_project.gold.sales_fact
GROUP BY
    brand_name,
    product_name
)

SELECT *
FROM (
SELECT *,
       ROW_NUMBER() OVER(
           PARTITION BY brand_name
           ORDER BY revenue DESC
       ) rn
FROM brand_product_sales
)
WHERE rn = 1;


--executive KPI dashboard query
SELECT
    COUNT(DISTINCT order_id) total_orders,
    COUNT(DISTINCT customer_id) total_customers,
    COUNT(DISTINCT product_id) total_products,
    SUM(revenue) total_revenue,
    AVG(revenue) avg_revenue
FROM biker_r_project.gold.sales_fact;
