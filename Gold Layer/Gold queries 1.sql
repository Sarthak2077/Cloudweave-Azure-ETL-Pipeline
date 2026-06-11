SELECT *
FROM biker_r_project.gold.sales_fact
LIMIT 10;

--top product revenue
WITH product_sales AS
(
SELECT
    product_name,
    SUM(revenue) total_revenue
FROM biker_r_project.gold.sales_fact
GROUP BY product_name
)

SELECT *
FROM product_sales
ORDER BY total_revenue DESC
LIMIT 5;

--product ranking
SELECT
    product_name,
    SUM(revenue) revenue,
    DENSE_RANK() OVER
    (
        ORDER BY SUM(revenue) DESC
    ) product_rank
FROM biker_r_project.gold.sales_fact
GROUP BY product_name;

--top customer spending
SELECT
    customer_name,
    SUM(revenue) total_spent,
    RANK() OVER
    (
        ORDER BY SUM(revenue) DESC
    ) spending_rank
FROM biker_r_project.gold.sales_fact
GROUP BY customer_name;

--best customer in every store
WITH customer_store_sales AS
(
SELECT
    store_name,
    customer_name,
    SUM(revenue) total_sales
FROM biker_r_project.gold.sales_fact
GROUP BY store_name,
         customer_name
)

SELECT *
FROM
(
SELECT *,
       ROW_NUMBER() OVER
       (
           PARTITION BY store_name
           ORDER BY total_sales DESC
       ) rn
FROM customer_store_sales
)
x
WHERE rn = 1;


--monthly revenue trend
SELECT
    YEAR(order_date) yr,
    MONTH(order_date) mn,
    SUM(revenue) monthly_revenue
FROM biker_r_project.gold.sales_fact
GROUP BY YEAR(order_date),
         MONTH(order_date)
ORDER BY yr,mn;


--running revenue
WITH monthly_sales AS
(
SELECT
    YEAR(order_date) yr,
    MONTH(order_date) mn,
    SUM(revenue) revenue
FROM biker_r_project.gold.sales_fact
GROUP BY YEAR(order_date),
         MONTH(order_date)
)
SELECT *,
       SUM(revenue) OVER
       (
          ORDER BY yr,mn
       ) running_revenue
FROM monthly_sales;


--customer lifetime value
SELECT
    customer_id,
    customer_name,
    COUNT(DISTINCT order_id) total_orders,
    SUM(revenue) lifetime_value
FROM biker_r_project.gold.sales_fact
GROUP BY customer_id,
         customer_name
ORDER BY lifetime_value DESC;


--best product in every category
WITH category_sales AS
(
SELECT
    category_name,
    product_name,
    SUM(revenue) total_revenue
FROM biker_r_project.gold.sales_fact
GROUP BY category_name,
         product_name
)
SELECT *
FROM
(
SELECT *,
       DENSE_RANK() OVER
       (
           PARTITION BY category_name
           ORDER BY total_revenue DESC
       ) rnk
FROM category_sales
)
x
WHERE rnk = 1;


--store performance dashboard query
SELECT
    store_name,
    COUNT(DISTINCT order_id) total_orders,
    COUNT(DISTINCT customer_id) total_customers,
    SUM(revenue) total_revenue,
    AVG(revenue) avg_order_value
FROM biker_r_project.gold.sales_fact
GROUP BY store_name
ORDER BY total_revenue DESC;


--pareto analysis
WITH product_sales AS
(
SELECT
    product_name,
    SUM(revenue) revenue
FROM biker_r_project.gold.sales_fact
GROUP BY product_name
)

SELECT
    product_name,
    revenue,
    SUM(revenue) OVER
    (
       ORDER BY revenue DESC
    ) cumulative_revenue
FROM product_sales;
