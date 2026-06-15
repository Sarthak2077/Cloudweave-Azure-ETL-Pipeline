{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "787adf35-82c2-4323-9b80-4316f603a9ec",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-----------+----------+---------+--------------+--------------------+--------------------+-------------+-----+--------+\n|customer_id|first_name|last_name|         phone|               email|              street|         city|state|zip_code|\n+-----------+----------+---------+--------------+--------------------+--------------------+-------------+-----+--------+\n|          1|     Debra|    Burks|          NULL|debra.burks@yahoo...|   9273 Thorne Ave. | Orchard Park|   NY|   14127|\n|          2|     Kasha|     Todd|          NULL|kasha.todd@yahoo.com|    910 Vine Street |     Campbell|   CA|   95008|\n|          3|    Tameka|   Fisher|          NULL|tameka.fisher@aol...|769C Honey Creek ...|Redondo Beach|   CA|   90278|\n|          4|     Daryl|   Spence|          NULL|daryl.spence@aol.com|     988 Pearl Lane |    Uniondale|   NY|   11553|\n|          5|Charolette|     Rice|(916) 381-6003|charolette.rice@m...|      107 River Dr. |   Sacramento|   CA|   95820|\n+-----------+----------+---------+--------------+--------------------+--------------------+-------------+-----+--------+\nonly showing top 5 rows\n"
     ]
    }
   ],
   "source": [
    "customers = spark.table(\"biker_r_project.raw.customers\")\n",
    "customers.show(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ff39c56d-2aff-475d-a5d0-c5027f7ba332",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import *\n",
    "\n",
    "customers_clean = (\n",
    "    customers\n",
    "    .dropDuplicates()\n",
    "    .filter(col(\"customer_id\").isNotNull())\n",
    "    .withColumn(\"first_name\", initcap(trim(col(\"first_name\"))))\n",
    "    .withColumn(\"last_name\", initcap(trim(col(\"last_name\"))))\n",
    ")\n",
    "\n",
    "customers_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.customers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "e9d1bda9-5083-4312-9f8f-12c3d650a8de",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "brands = spark.table(\"biker_r_project.raw.brands\")\n",
    "brands_clean = brands.dropDuplicates()\n",
    "\n",
    "brands_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.brands\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "db0e9dd3-5952-468b-be4a-2bfd8fa55af0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "categories = spark.table(\"biker_r_project.raw.categories\")\n",
    "categories_clean = categories.dropDuplicates()\n",
    "\n",
    "categories_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.categories\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c68a8886-39f1-480b-84f2-092d9af3f6e4",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "products = spark.table(\"biker_r_project.raw.products\")\n",
    "\n",
    "products_clean = (\n",
    "    products\n",
    "    .dropDuplicates()\n",
    "    .filter(col(\"product_id\").isNotNull())\n",
    "    .withColumn(\"product_name\", trim(col(\"product_name\")))\n",
    ")\n",
    "\n",
    "products_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.products\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "6f3a9a76-aaf3-4aeb-90c4-b3098214c0ff",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "orders = spark.table(\"biker_r_project.raw.orders\")\n",
    "orders_clean = (\n",
    "    orders\n",
    "    .dropDuplicates()\n",
    "    .filter(col(\"order_id\").isNotNull())\n",
    ")\n",
    "\n",
    "orders_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.orders\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "60f83e66-6baf-4143-a01e-538a0b071faa",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "order_items = spark.table(\"biker_r_project.raw.order_items\")\n",
    "order_items_clean = (\n",
    "    order_items\n",
    "    .dropDuplicates()\n",
    "    .filter(col(\"order_id\").isNotNull())\n",
    "    .filter(col(\"product_id\").isNotNull())\n",
    "    .filter(col(\"quantity\") > 0)\n",
    ")\n",
    "\n",
    "order_items_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.order_items\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c3f44919-7c1a-4282-b96f-d3fbd5de9a10",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "staffs = spark.table(\"biker_r_project.raw.staffs\")\n",
    "staffs_clean = (\n",
    "    staffs\n",
    "    .dropDuplicates()\n",
    "    .withColumn(\"first_name\", initcap(trim(col(\"first_name\"))))\n",
    "    .withColumn(\"last_name\", initcap(trim(col(\"last_name\"))))\n",
    ")\n",
    "\n",
    "staffs_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.staffs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "522f2823-f67c-4e65-87b4-69e96d49065a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "stores = spark.table(\"biker_r_project.raw.stores\")\n",
    "stores_clean = (\n",
    "    stores\n",
    "    .dropDuplicates()\n",
    "    .withColumn(\"store_name\", trim(col(\"store_name\")))\n",
    ")\n",
    "\n",
    "stores_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.stores\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "eddebfd0-bf30-439a-90d4-63a8e905e9f9",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "stocks = spark.table(\"biker_r_project.raw.stocks\")\n",
    "stocks_clean = (\n",
    "    stocks\n",
    "    .dropDuplicates()\n",
    "    .filter(col(\"quantity\") >= 0)\n",
    ")\n",
    "\n",
    "stocks_clean.write \\\n",
    ".mode(\"overwrite\") \\\n",
    ".saveAsTable(\"biker_r_project.silver.stocks\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "57e7d9df-1ddb-4427-9859-1a9b220e3cdb",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>database</th><th>tableName</th><th>isTemporary</th></tr></thead><tbody><tr><td>silver</td><td>brands</td><td>false</td></tr><tr><td>silver</td><td>categories</td><td>false</td></tr><tr><td>silver</td><td>customers</td><td>false</td></tr><tr><td>silver</td><td>order_items</td><td>false</td></tr><tr><td>silver</td><td>orders</td><td>false</td></tr><tr><td>silver</td><td>products</td><td>false</td></tr><tr><td>silver</td><td>staffs</td><td>false</td></tr><tr><td>silver</td><td>stocks</td><td>false</td></tr><tr><td>silver</td><td>stores</td><td>false</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "silver",
         "brands",
         false
        ],
        [
         "silver",
         "categories",
         false
        ],
        [
         "silver",
         "customers",
         false
        ],
        [
         "silver",
         "order_items",
         false
        ],
        [
         "silver",
         "orders",
         false
        ],
        [
         "silver",
         "products",
         false
        ],
        [
         "silver",
         "staffs",
         false
        ],
        [
         "silver",
         "stocks",
         false
        ],
        [
         "silver",
         "stores",
         false
        ]
       ],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [
           {
            "metadata": {},
            "name": "database",
            "nullable": false,
            "type": "string"
           },
           {
            "metadata": {},
            "name": "tableName",
            "nullable": false,
            "type": "string"
           },
           {
            "metadata": {},
            "name": "isTemporary",
            "nullable": false,
            "type": "boolean"
           }
          ],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 28
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "database",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "tableName",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "isTemporary",
         "type": "\"boolean\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "SHOW TABLES IN biker_r_project.silver;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3dc28230-c946-41c6-aef9-4334cabd64f0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "1445"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "customers.count()\n",
    "customers_clean.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c5709c7a-938a-4f9b-bd01-fdf0f2276dc0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----------+-----+\n|product_id|count|\n+----------+-----+\n+----------+-----+\n\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "products.groupBy(\"product_id\").count().filter(\"count > 1\").show()\n",
    "customers.filter(col(\"customer_id\").isNull()).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c3f70fcb-70b8-441b-a558-1c31a657f035",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+-----------+------------+----------+-------------+------------+--------+--------+\n|order_id|customer_id|order_status|order_date|required_date|shipped_date|store_id|staff_id|\n+--------+-----------+------------+----------+-------------+------------+--------+--------+\n+--------+-----------+------------+----------+-------------+------------+--------+--------+\n\n"
     ]
    }
   ],
   "source": [
    "invalid_orders = orders.join(\n",
    "    customers,\n",
    "    orders.customer_id == customers.customer_id,\n",
    "    \"left_anti\"\n",
    ")\n",
    "\n",
    "invalid_orders.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "cf4573cd-e5a0-4b86-afa6-c55e368c2022",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+-------+----------+--------+----------+--------+\n|order_id|item_id|product_id|quantity|list_price|discount|\n+--------+-------+----------+--------+----------+--------+\n+--------+-------+----------+--------+----------+--------+\n\n"
     ]
    }
   ],
   "source": [
    "invalid_products = order_items.join(\n",
    "    products,\n",
    "    order_items.product_id == products.product_id,\n",
    "    \"left_anti\"\n",
    ")\n",
    "\n",
    "invalid_products.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "04b39623-5952-4bb1-8170-814476f7b2c6",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "product_dim = (\n",
    "    products\n",
    "    .join(brands, \"brand_id\")\n",
    "    .join(categories, \"category_id\")\n",
    "    .select(\n",
    "        \"product_id\",\n",
    "        \"product_name\",\n",
    "        \"brand_name\",\n",
    "        \"category_name\",\n",
    "        \"model_year\",\n",
    "        \"list_price\"\n",
    "    )\n",
    ")\n",
    "\n",
    "product_dim.write.mode(\"overwrite\")\\\n",
    ".saveAsTable(\"biker_r_project.silver.dim_product\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "fc56cc13-f9bb-41b2-8859-86626225f48e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "customer_dim = customers.select(\n",
    "    \"customer_id\",\n",
    "    \"first_name\",\n",
    "    \"last_name\",\n",
    "    \"city\",\n",
    "    \"state\",\n",
    "    \"zip_code\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ecea0fb9-9016-4686-afa5-8458e4dec0f7",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.window import Window\n",
    "from pyspark.sql.functions import dense_rank, desc\n",
    "\n",
    "window_spec = Window.partitionBy(\"store_name\") \\\n",
    "                    .orderBy(desc(\"sales\"))\n",
    "\n",
    "customer_rank = customer_sales.withColumn(\n",
    "    \"rank\",\n",
    "    dense_rank().over(window_spec)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "08988c22-71a5-44e6-9c51-b9009070a204",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "window_spec = Window.partitionBy(\"store_name\") \\\n",
    "                    .orderBy(\"order_date\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ba19c5b6-f97d-4add-a445-acba9aae5229",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.window import Window\n",
    "from pyspark.sql.functions import *\n",
    "\n",
    "store_sales = (\n",
    "    sales_fact\n",
    "    .groupBy(\"store_name\",\"customer_name\")\n",
    "    .agg(sum(\"revenue\").alias(\"sales\"))\n",
    ")\n",
    "\n",
    "window_spec = Window.partitionBy(\"store_name\") \\\n",
    "                    .orderBy(desc(\"sales\"))\n",
    "\n",
    "top_customers = store_sales.withColumn(\n",
    "    \"rank\",\n",
    "    dense_rank().over(window_spec)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2d4dd10a-4871-4927-9ca5-d9a53dddee33",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/databricks/python/lib/python3.12/site-packages/pyspark/sql/connect/expressions.py:1160: UserWarning: WARN WindowExpression: No Partition Defined for Window operation! Moving all data to a single partition, this can cause serious performance degradation.\n  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "window_spec = Window.orderBy(desc(\"sales\"))\n",
    "\n",
    "segments = customer_sales.withColumn(\n",
    "    \"segment\",\n",
    "    ntile(4).over(window_spec)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "69114ca1-7ffd-46c4-8687-e3213be4f040",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import broadcast\n",
    "\n",
    "sales_fact = (\n",
    "    orders\n",
    "    .join(order_items,\"order_id\")\n",
    "    .join(\n",
    "        broadcast(products),\n",
    "        \"product_id\"\n",
    "    )\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "9774645f-3dcb-4788-93ea-c59e9b26a7f0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "== Parsed Logical Plan ==\n'Join UsingJoin(Inner, [product_id])\n:- 'Join UsingJoin(Inner, [order_id])\n:  :- 'UnresolvedRelation [biker_r_project, raw, orders], [], false\n:  +- 'UnresolvedRelation [biker_r_project, raw, order_items], [], false\n+- 'UnresolvedHint broadcast\n   +- 'UnresolvedRelation [biker_r_project, raw, products], [], false\n\n== Analyzed Logical Plan ==\nproduct_id: bigint, order_id: bigint, customer_id: bigint, order_status: bigint, order_date: date, required_date: date, shipped_date: string, store_id: bigint, staff_id: bigint, item_id: bigint, quantity: bigint, list_price: double, discount: double, product_name: string, brand_id: bigint, category_id: bigint, model_year: bigint, list_price: double\nProject [product_id#16320L, order_id#16310L, customer_id#16311L, order_status#16312L, order_date#16313, required_date#16314, shipped_date#16315, store_id#16316L, staff_id#16317L, item_id#16319L, quantity#16321L, list_price#16322, discount#16323, product_name#16325, brand_id#16326L, category_id#16327L, model_year#16328L, list_price#16329]\n+- Join Inner, (product_id#16320L = product_id#16324L)\n   :- Project [order_id#16310L, customer_id#16311L, order_status#16312L, order_date#16313, required_date#16314, shipped_date#16315, store_id#16316L, staff_id#16317L, item_id#16319L, product_id#16320L, quantity#16321L, list_price#16322, discount#16323]\n   :  +- Join Inner, (order_id#16310L = order_id#16318L)\n   :     :- SubqueryAlias biker_r_project.raw.orders\n   :     :  +- Relation biker_r_project.raw.orders[order_id#16310L,customer_id#16311L,order_status#16312L,order_date#16313,required_date#16314,shipped_date#16315,store_id#16316L,staff_id#16317L] parquet\n   :     +- SubqueryAlias biker_r_project.raw.order_items\n   :        +- Relation biker_r_project.raw.order_items[order_id#16318L,item_id#16319L,product_id#16320L,quantity#16321L,list_price#16322,discount#16323] parquet\n   +- ResolvedHint (strategy=broadcast)\n      +- SubqueryAlias biker_r_project.raw.products\n         +- Relation biker_r_project.raw.products[product_id#16324L,product_name#16325,brand_id#16326L,category_id#16327L,model_year#16328L,list_price#16329] parquet\n\n== Optimized Logical Plan ==\nProject [product_id#16320L, order_id#16310L, customer_id#16311L, order_status#16312L, order_date#16313, required_date#16314, shipped_date#16315, store_id#16316L, staff_id#16317L, item_id#16319L, quantity#16321L, list_price#16322, discount#16323, product_name#16325, brand_id#16326L, category_id#16327L, model_year#16328L, list_price#16329]\n+- Join Inner, (product_id#16320L = product_id#16324L), rightHint=(strategy=broadcast), joinId=27\n   :- Project [order_id#16310L, customer_id#16311L, order_status#16312L, order_date#16313, required_date#16314, shipped_date#16315, store_id#16316L, staff_id#16317L, item_id#16319L, product_id#16320L, quantity#16321L, list_price#16322, discount#16323]\n   :  +- Join Inner, (order_id#16310L = order_id#16318L)\n   :     :- Filter isnotnull(order_id#16310L)\n   :     :  +- Relation biker_r_project.raw.orders[order_id#16310L,customer_id#16311L,order_status#16312L,order_date#16313,required_date#16314,shipped_date#16315,store_id#16316L,staff_id#16317L] parquet\n   :     +- Filter (isnotnull(order_id#16318L) AND isnotnull(product_id#16320L))\n   :        +- Relation biker_r_project.raw.order_items[order_id#16318L,item_id#16319L,product_id#16320L,quantity#16321L,list_price#16322,discount#16323] parquet\n   +- Filter isnotnull(product_id#16324L)\n      +- Relation biker_r_project.raw.products[product_id#16324L,product_name#16325,brand_id#16326L,category_id#16327L,model_year#16328L,list_price#16329] parquet\n\n== Physical Plan ==\nAdaptiveSparkPlan isFinalPlan=false\n+- == Initial Plan ==\n   PhotonResultStage\n   +- PhotonColumnarToRow\n      +- PhotonProject [product_id#16320L, order_id#16310L, customer_id#16311L, order_status#16312L, order_date#16313, required_date#16314, shipped_date#16315, store_id#16316L, staff_id#16317L, item_id#16319L, quantity#16321L, list_price#16322, discount#16323, product_name#16325, brand_id#16326L, category_id#16327L, model_year#16328L, list_price#16329]\n         +- PhotonBroadcastHashJoin [product_id#16320L], [product_id#16324L], Inner, BuildRight, false, true\n            :- PhotonProject [order_id#16310L, customer_id#16311L, order_status#16312L, order_date#16313, required_date#16314, shipped_date#16315, store_id#16316L, staff_id#16317L, item_id#16319L, product_id#16320L, quantity#16321L, list_price#16322, discount#16323]\n            :  +- PhotonBroadcastHashJoin [order_id#16310L], [order_id#16318L], Inner, BuildLeft, false, true\n            :     :- PhotonShuffleExchangeSource\n            :     :  +- PhotonShuffleMapStage EXECUTOR_BROADCAST, [id=#9659]\n            :     :     +- PhotonShuffleExchangeSink SinglePartition\n            :     :        +- PhotonScan parquet biker_r_project.raw.orders[order_id#16310L,customer_id#16311L,order_status#16312L,order_date#16313,required_date#16314,shipped_date#16315,store_id#16316L,staff_id#16317L] DataFilters: [isnotnull(order_id#16310L)], DictionaryFilters: [], Format: parquet, Location: PreparedDeltaFileIndex(1 paths)[abfss://unitycatalog@prd5oqusghbjjlrigxkiwozf.dfs.core.windows.ne..., OptionalDataFilters: [], PartitionFilters: [], ReadSchema: struct<order_id:bigint,customer_id:bigint,order_status:bigint,order_date:date,required_date:date,..., RequiredDataFilters: [isnotnull(order_id#16310L)]\n            :     +- PhotonScan parquet biker_r_project.raw.order_items[order_id#16318L,item_id#16319L,product_id#16320L,quantity#16321L,list_price#16322,discount#16323] DataFilters: [isnotnull(order_id#16318L), isnotnull(product_id#16320L)], DictionaryFilters: [], Format: parquet, Location: PreparedDeltaFileIndex(1 paths)[abfss://unitycatalog@prd5oqusghbjjlrigxkiwozf.dfs.core.windows.ne..., OptionalDataFilters: [hashedrelationcontains(order_id#16318L), hashedrelationcontains(product_id#16320L)], PartitionFilters: [], ReadSchema: struct<order_id:bigint,item_id:bigint,product_id:bigint,quantity:bigint,list_price:double,discoun..., RequiredDataFilters: [isnotnull(order_id#16318L), isnotnull(product_id#16320L)]\n            +- PhotonShuffleExchangeSource\n               +- PhotonShuffleMapStage EXECUTOR_BROADCAST, [id=#9672]\n                  +- PhotonShuffleExchangeSink SinglePartition\n                     +- PhotonScan parquet biker_r_project.raw.products[product_id#16324L,product_name#16325,brand_id#16326L,category_id#16327L,model_year#16328L,list_price#16329] DataFilters: [isnotnull(product_id#16324L)], DictionaryFilters: [], Format: parquet, Location: PreparedDeltaFileIndex(1 paths)[abfss://unitycatalog@prd5oqusghbjjlrigxkiwozf.dfs.core.windows.ne..., OptionalDataFilters: [], PartitionFilters: [], ReadSchema: struct<product_id:bigint,product_name:string,brand_id:bigint,category_id:bigint,model_year:bigint..., RequiredDataFilters: [isnotnull(product_id#16324L)]\n\n== Photon Explanation ==\nThe query is fully supported by Photon.\n== Optimizer Statistics (table names per statistics state) ==\n  missing = \n  partial = \n  full    = order_items, orders, products\n\n"
     ]
    }
   ],
   "source": [
    "sales_fact.explain(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "9b942c9f-17a0-45cc-a622-f219eae82246",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "store_kpis = (\n",
    "    sales_fact\n",
    "    .groupBy(\"store_name\")\n",
    "    .agg(\n",
    "        countDistinct(\"order_id\")\n",
    "        .alias(\"orders\"),\n",
    "\n",
    "        countDistinct(\"customer_id\")\n",
    "        .alias(\"customers\"),\n",
    "\n",
    "        sum(\"revenue\")\n",
    "        .alias(\"revenue\")\n",
    "    )\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b24e9900-801a-4ef1-8235-6b4627747253",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>year</th><th>month</th><th>revenue</th></tr></thead><tbody><tr><td>2016</td><td>1</td><td>215146.42409999995</td></tr><tr><td>2016</td><td>2</td><td>156112.3228</td></tr><tr><td>2016</td><td>3</td><td>180600.3285</td></tr><tr><td>2016</td><td>4</td><td>167144.0512</td></tr><tr><td>2016</td><td>5</td><td>205270.00909999997</td></tr><tr><td>2016</td><td>6</td><td>210562.12449999986</td></tr><tr><td>2016</td><td>7</td><td>199556.80889999992</td></tr><tr><td>2016</td><td>8</td><td>225657.37669999996</td></tr><tr><td>2016</td><td>9</td><td>273091.60970000003</td></tr><tr><td>2016</td><td>10</td><td>212078.08050000004</td></tr><tr><td>2016</td><td>11</td><td>182329.41239999997</td></tr><tr><td>2016</td><td>12</td><td>199829.97919999994</td></tr><tr><td>2017</td><td>1</td><td>285616.48399999994</td></tr><tr><td>2017</td><td>2</td><td>312923.7470000001</td></tr><tr><td>2017</td><td>3</td><td>308911.9018000001</td></tr><tr><td>2017</td><td>4</td><td>227290.91309999992</td></tr><tr><td>2017</td><td>5</td><td>268233.23789999995</td></tr><tr><td>2017</td><td>6</td><td>378865.65350000025</td></tr><tr><td>2017</td><td>7</td><td>229995.39789999995</td></tr><tr><td>2017</td><td>8</td><td>290553.45540000015</td></tr><tr><td>2017</td><td>9</td><td>293405.25610000035</td></tr><tr><td>2017</td><td>10</td><td>310328.3090000002</td></tr><tr><td>2017</td><td>11</td><td>281577.90190000006</td></tr><tr><td>2017</td><td>12</td><td>259505.98489999995</td></tr><tr><td>2018</td><td>1</td><td>381430.0993000004</td></tr><tr><td>2018</td><td>2</td><td>200658.0615</td></tr><tr><td>2018</td><td>3</td><td>363990.9935000004</td></tr><tr><td>2018</td><td>4</td><td>817921.8604000009</td></tr><tr><td>2018</td><td>6</td><td>188.991</td></tr><tr><td>2018</td><td>7</td><td>11337.9002</td></tr><tr><td>2018</td><td>8</td><td>8377.8147</td></tr><tr><td>2018</td><td>9</td><td>8963.9647</td></tr><tr><td>2018</td><td>10</td><td>3781.1284</td></tr><tr><td>2018</td><td>11</td><td>11362.007099999999</td></tr><tr><td>2018</td><td>12</td><td>6516.9667</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         2016,
         1,
         215146.42409999995
        ],
        [
         2016,
         2,
         156112.3228
        ],
        [
         2016,
         3,
         180600.3285
        ],
        [
         2016,
         4,
         167144.0512
        ],
        [
         2016,
         5,
         205270.00909999997
        ],
        [
         2016,
         6,
         210562.12449999986
        ],
        [
         2016,
         7,
         199556.80889999992
        ],
        [
         2016,
         8,
         225657.37669999996
        ],
        [
         2016,
         9,
         273091.60970000003
        ],
        [
         2016,
         10,
         212078.08050000004
        ],
        [
         2016,
         11,
         182329.41239999997
        ],
        [
         2016,
         12,
         199829.97919999994
        ],
        [
         2017,
         1,
         285616.48399999994
        ],
        [
         2017,
         2,
         312923.7470000001
        ],
        [
         2017,
         3,
         308911.9018000001
        ],
        [
         2017,
         4,
         227290.91309999992
        ],
        [
         2017,
         5,
         268233.23789999995
        ],
        [
         2017,
         6,
         378865.65350000025
        ],
        [
         2017,
         7,
         229995.39789999995
        ],
        [
         2017,
         8,
         290553.45540000015
        ],
        [
         2017,
         9,
         293405.25610000035
        ],
        [
         2017,
         10,
         310328.3090000002
        ],
        [
         2017,
         11,
         281577.90190000006
        ],
        [
         2017,
         12,
         259505.98489999995
        ],
        [
         2018,
         1,
         381430.0993000004
        ],
        [
         2018,
         2,
         200658.0615
        ],
        [
         2018,
         3,
         363990.9935000004
        ],
        [
         2018,
         4,
         817921.8604000009
        ],
        [
         2018,
         6,
         188.991
        ],
        [
         2018,
         7,
         11337.9002
        ],
        [
         2018,
         8,
         8377.8147
        ],
        [
         2018,
         9,
         8963.9647
        ],
        [
         2018,
         10,
         3781.1284
        ],
        [
         2018,
         11,
         11362.007099999999
        ],
        [
         2018,
         12,
         6516.9667
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "year",
         "type": "\"integer\""
        },
        {
         "metadata": "{}",
         "name": "month",
         "type": "\"integer\""
        },
        {
         "metadata": "{}",
         "name": "revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from pyspark.sql.functions import *\n",
    "\n",
    "monthly_sales = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\n",
    "        year(\"order_date\").alias(\"year\"),\n",
    "        month(\"order_date\").alias(\"month\")\n",
    "    )\n",
    "    .agg(sum(\"revenue\").alias(\"revenue\"))\n",
    "    .orderBy(\"year\",\"month\")\n",
    ")\n",
    "\n",
    "display(monthly_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "40453d62-c051-4fbb-942a-403ae0279862",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>product_name</th><th>revenue</th></tr></thead><tbody><tr><td>Trek Slash 8 27.5 - 2016</td><td>555558.6111</td></tr><tr><td>Trek Conduit+ - 2016</td><td>389248.7025000002</td></tr><tr><td>Trek Fuel EX 8 29 - 2016</td><td>368472.72939999995</td></tr><tr><td>Surly Straggler 650b - 2016</td><td>226765.5509999999</td></tr><tr><td>Trek Domane SLR 6 Disc - 2017</td><td>211584.61529999998</td></tr><tr><td>Surly Straggler - 2016</td><td>203507.62000000026</td></tr><tr><td>Trek Remedy 29 Carbon Frameset - 2016</td><td>203380.87009999997</td></tr><tr><td>Trek Powerfly 8 FS Plus - 2017</td><td>188249.62349999996</td></tr><tr><td>Trek Madone 9.2 - 2017</td><td>175899.64819999994</td></tr><tr><td>Trek Silque SLR 8 Women's - 2017</td><td>174524.73150000002</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Trek Slash 8 27.5 - 2016",
         555558.6111
        ],
        [
         "Trek Conduit+ - 2016",
         389248.7025000002
        ],
        [
         "Trek Fuel EX 8 29 - 2016",
         368472.72939999995
        ],
        [
         "Surly Straggler 650b - 2016",
         226765.5509999999
        ],
        [
         "Trek Domane SLR 6 Disc - 2017",
         211584.61529999998
        ],
        [
         "Surly Straggler - 2016",
         203507.62000000026
        ],
        [
         "Trek Remedy 29 Carbon Frameset - 2016",
         203380.87009999997
        ],
        [
         "Trek Powerfly 8 FS Plus - 2017",
         188249.62349999996
        ],
        [
         "Trek Madone 9.2 - 2017",
         175899.64819999994
        ],
        [
         "Trek Silque SLR 8 Women's - 2017",
         174524.73150000002
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "product_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": [
       "Databricks visualization. Run in Databricks to view."
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1.subcommand+json": {
       "baseErrorDetails": null,
       "bindings": {},
       "collapsed": false,
       "command": "%python\n__backend_agg_display_orig = display\n__backend_agg_dfs = []\ndef __backend_agg_display_new(df):\n    __backend_agg_df_modules = [\"pandas.core.frame\", \"databricks.koalas.frame\", \"pyspark.sql.dataframe\", \"pyspark.pandas.frame\", \"pyspark.sql.connect.dataframe\", \"pyspark.sql.classic.dataframe\"]\n    if (type(df).__module__ in __backend_agg_df_modules and type(df).__name__ == 'DataFrame') or isinstance(df, list):\n        __backend_agg_dfs.append(df)\n\ndisplay = __backend_agg_display_new\n\ndef __backend_agg_user_code_fn():\n    import base64\n    exec(base64.standard_b64decode(\"dG9wX3Byb2R1Y3RzID0gKAogICAgc3BhcmsudGFibGUoImJpa2VyX3JfcHJvamVjdC5nb2xkLnNhbGVzX2ZhY3QiKQogICAgLmdyb3VwQnkoInByb2R1Y3RfbmFtZSIpCiAgICAuYWdnKHN1bSgicmV2ZW51ZSIpLmFsaWFzKCJyZXZlbnVlIikpCiAgICAub3JkZXJCeShkZXNjKCJyZXZlbnVlIikpCiAgICAubGltaXQoMTApCikKCmRpc3BsYXkodG9wX3Byb2R1Y3RzKQ==\").decode())\n\ntry:\n    # run user code\n    __backend_agg_user_code_fn()\n\n    #reset display function\n    display = __backend_agg_display_orig\n\n    if len(__backend_agg_dfs) > 0:\n        # create a temp view\n        if type(__backend_agg_dfs[0]).__module__ == \"databricks.koalas.frame\":\n            # koalas dataframe\n            __backend_agg_dfs[0].to_spark().createOrReplaceTempView(\"DatabricksView4479cee\")\n        elif type(__backend_agg_dfs[0]).__module__ == \"pandas.core.frame\" or isinstance(__backend_agg_dfs[0], list):\n            # pandas dataframe\n            spark.createDataFrame(__backend_agg_dfs[0]).createOrReplaceTempView(\"DatabricksView4479cee\")\n        else:\n            __backend_agg_dfs[0].createOrReplaceTempView(\"DatabricksView4479cee\")\n        #run backend agg\n        display(spark.sql(\"\"\"WITH q AS (select * from DatabricksView4479cee) SELECT `product_name`,SUM(`revenue`) `column_26923a16303` FROM q GROUP BY `product_name`\"\"\"))\n    else:\n        displayHTML(\"dataframe no longer exists. If you're using dataframe.display(), use display(dataframe) instead.\")\n\n\nfinally:\n    spark.sql(\"drop view if exists DatabricksView4479cee\")\n    display = __backend_agg_display_orig\n    del __backend_agg_display_new\n    del __backend_agg_display_orig\n    del __backend_agg_dfs\n    del __backend_agg_user_code_fn\n\n",
       "commandTitle": "Visualization 1",
       "commandType": "auto",
       "commandVersion": 0,
       "commentThread": [],
       "commentsVisible": false,
       "contentSha256Hex": null,
       "customPlotOptions": {
        "redashChart": [
         {
          "key": "type",
          "value": "CHART"
         },
         {
          "key": "options",
          "value": {
           "alignYAxesAtZero": true,
           "coefficient": 1,
           "columnConfigurationMap": {
            "x": {
             "column": "product_name",
             "id": "column_26923a16302"
            },
            "y": [
             {
              "column": "revenue",
              "id": "column_26923a16303",
              "transform": "SUM"
             }
            ]
           },
           "dateTimeFormat": "DD/MM/YYYY HH:mm",
           "direction": {
            "type": "counterclockwise"
           },
           "error_y": {
            "type": "data",
            "visible": true
           },
           "globalSeriesType": "column",
           "legend": {
            "traceorder": "normal"
           },
           "missingValuesAsZero": true,
           "numberFormat": "0,0.[00000]",
           "percentFormat": "0[.]00%",
           "series": {
            "error_y": {
             "type": "data",
             "visible": true
            },
            "stacking": null
           },
           "seriesOptions": {
            "column_26923a16303": {
             "name": "revenue",
             "yAxis": 0
            }
           },
           "showDataLabels": false,
           "sizemode": "diameter",
           "sortX": true,
           "sortY": true,
           "swappedAxes": true,
           "textFormat": "",
           "useAggregationsUi": true,
           "valuesOptions": {},
           "version": 2,
           "xAxis": {
            "labels": {
             "enabled": true
            },
            "type": "-"
           },
           "yAxis": [
            {
             "type": "-"
            },
            {
             "opposite": true,
             "type": "-"
            }
           ]
          }
         }
        ]
       },
       "datasetPreviewNameToCmdIdMap": {},
       "diffDeletes": [],
       "diffInserts": [],
       "displayType": "redashChart",
       "error": null,
       "errorDetails": null,
       "errorSummary": null,
       "errorTraceType": null,
       "finishTime": 0,
       "globalVars": {},
       "guid": "",
       "height": "auto",
       "hideCommandCode": false,
       "hideCommandResult": false,
       "iPythonMetadata": null,
       "inputWidgets": {},
       "isLockedInExamMode": false,
       "latestAssumeRoleInfo": null,
       "latestUser": "a user",
       "latestUserId": null,
       "listResultMetadata": null,
       "metadata": {},
       "nuid": "0f8ebf8a-a996-40cd-bb18-eae9c9256d88",
       "origId": 0,
       "parentHierarchy": [],
       "pivotAggregation": null,
       "pivotColumns": null,
       "position": 25.0,
       "resultDbfsErrorMessage": null,
       "resultDbfsStatus": "INLINED_IN_TREE",
       "results": null,
       "showCommandTitle": false,
       "startTime": 0,
       "state": "input",
       "streamStates": {},
       "subcommandOptions": {
        "queryPlan": {
         "groups": [
          {
           "column": "product_name",
           "type": "column"
          }
         ],
         "selects": [
          {
           "column": "product_name",
           "type": "column"
          },
          {
           "alias": "column_26923a16303",
           "args": [
            {
             "column": "revenue",
             "type": "column"
            }
           ],
           "function": "SUM",
           "type": "function"
          }
         ]
        }
       },
       "submitTime": 0,
       "subtype": "tableResultSubCmd.visualization",
       "tableResultIndex": 0,
       "tableResultSettingsMap": {},
       "useConsistentColors": false,
       "version": "CommandV1",
       "width": "auto",
       "workflows": [],
       "xColumns": null,
       "yColumns": null
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "top_products = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\"product_name\")\n",
    "    .agg(sum(\"revenue\").alias(\"revenue\"))\n",
    "    .orderBy(desc(\"revenue\"))\n",
    "    .limit(10)\n",
    ")\n",
    "\n",
    "display(top_products)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "999b0394-ad68-4911-8c0b-ccd526d7186b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>category_name</th><th>revenue</th></tr></thead><tbody><tr><td>Mountain Bikes</td><td>2715079.533699997</td></tr><tr><td>Road Bikes</td><td>1665098.487999998</td></tr><tr><td>Cruisers Bicycles</td><td>995032.6237000015</td></tr><tr><td>Electric Bikes</td><td>916684.7800000007</td></tr><tr><td>Cyclocross Bicycles</td><td>711011.8359000003</td></tr><tr><td>Comfort Bicycles</td><td>394020.09810000093</td></tr><tr><td>Children Bicycles</td><td>292189.1982000012</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Mountain Bikes",
         2715079.533699997
        ],
        [
         "Road Bikes",
         1665098.487999998
        ],
        [
         "Cruisers Bicycles",
         995032.6237000015
        ],
        [
         "Electric Bikes",
         916684.7800000007
        ],
        [
         "Cyclocross Bicycles",
         711011.8359000003
        ],
        [
         "Comfort Bicycles",
         394020.09810000093
        ],
        [
         "Children Bicycles",
         292189.1982000012
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "category_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": [
       "Databricks visualization. Run in Databricks to view."
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1.subcommand+json": {
       "baseErrorDetails": null,
       "bindings": {},
       "collapsed": false,
       "command": "%python\n__backend_agg_display_orig = display\n__backend_agg_dfs = []\ndef __backend_agg_display_new(df):\n    __backend_agg_df_modules = [\"pandas.core.frame\", \"databricks.koalas.frame\", \"pyspark.sql.dataframe\", \"pyspark.pandas.frame\", \"pyspark.sql.connect.dataframe\", \"pyspark.sql.classic.dataframe\"]\n    if (type(df).__module__ in __backend_agg_df_modules and type(df).__name__ == 'DataFrame') or isinstance(df, list):\n        __backend_agg_dfs.append(df)\n\ndisplay = __backend_agg_display_new\n\ndef __backend_agg_user_code_fn():\n    import base64\n    exec(base64.standard_b64decode(\"Y2F0ZWdvcnlfc2FsZXMgPSAoCiAgICBzcGFyay50YWJsZSgiYmlrZXJfcl9wcm9qZWN0LmdvbGQuc2FsZXNfZmFjdCIpCiAgICAuZ3JvdXBCeSgiY2F0ZWdvcnlfbmFtZSIpCiAgICAuYWdnKHN1bSgicmV2ZW51ZSIpLmFsaWFzKCJyZXZlbnVlIikpCiAgICAub3JkZXJCeShkZXNjKCJyZXZlbnVlIikpCikKCmRpc3BsYXkoY2F0ZWdvcnlfc2FsZXMp\").decode())\n\ntry:\n    # run user code\n    __backend_agg_user_code_fn()\n\n    #reset display function\n    display = __backend_agg_display_orig\n\n    if len(__backend_agg_dfs) > 0:\n        # create a temp view\n        if type(__backend_agg_dfs[0]).__module__ == \"databricks.koalas.frame\":\n            # koalas dataframe\n            __backend_agg_dfs[0].to_spark().createOrReplaceTempView(\"DatabricksViewe89c8e7\")\n        elif type(__backend_agg_dfs[0]).__module__ == \"pandas.core.frame\" or isinstance(__backend_agg_dfs[0], list):\n            # pandas dataframe\n            spark.createDataFrame(__backend_agg_dfs[0]).createOrReplaceTempView(\"DatabricksViewe89c8e7\")\n        else:\n            __backend_agg_dfs[0].createOrReplaceTempView(\"DatabricksViewe89c8e7\")\n        #run backend agg\n        display(spark.sql(\"\"\"WITH q AS (select * from DatabricksViewe89c8e7) SELECT `category_name`,SUM(`revenue`) `column_26923a16310` FROM q GROUP BY `category_name`\"\"\"))\n    else:\n        displayHTML(\"dataframe no longer exists. If you're using dataframe.display(), use display(dataframe) instead.\")\n\n\nfinally:\n    spark.sql(\"drop view if exists DatabricksViewe89c8e7\")\n    display = __backend_agg_display_orig\n    del __backend_agg_display_new\n    del __backend_agg_display_orig\n    del __backend_agg_dfs\n    del __backend_agg_user_code_fn\n\n",
       "commandTitle": "Visualization 1",
       "commandType": "auto",
       "commandVersion": 0,
       "commentThread": [],
       "commentsVisible": false,
       "contentSha256Hex": null,
       "customPlotOptions": {
        "redashChart": [
         {
          "key": "type",
          "value": "CHART"
         },
         {
          "key": "options",
          "value": {
           "alignYAxesAtZero": true,
           "coefficient": 1,
           "columnConfigurationMap": {
            "x": {
             "column": "category_name",
             "id": "column_26923a16309"
            },
            "y": [
             {
              "column": "revenue",
              "id": "column_26923a16310",
              "transform": "SUM"
             }
            ]
           },
           "dateTimeFormat": "DD/MM/YYYY HH:mm",
           "direction": {
            "type": "counterclockwise"
           },
           "error_y": {
            "type": "data",
            "visible": true
           },
           "globalSeriesType": "pie",
           "legend": {
            "traceorder": "normal"
           },
           "missingValuesAsZero": true,
           "numberFormat": "0,0.[00000]",
           "percentFormat": "0[.]00%",
           "series": {
            "error_y": {
             "type": "data",
             "visible": true
            },
            "stacking": null
           },
           "seriesOptions": {
            "column_26923a16310": {
             "name": "revenue",
             "type": "pie",
             "yAxis": 0
            }
           },
           "showDataLabels": true,
           "sizemode": "diameter",
           "sortX": true,
           "sortY": true,
           "swappedAxes": false,
           "textFormat": "",
           "useAggregationsUi": true,
           "valuesOptions": {},
           "version": 2,
           "xAxis": {
            "labels": {
             "enabled": true
            },
            "type": "-"
           },
           "yAxis": [
            {
             "type": "-"
            },
            {
             "opposite": true,
             "type": "-"
            }
           ]
          }
         }
        ]
       },
       "datasetPreviewNameToCmdIdMap": {},
       "diffDeletes": [],
       "diffInserts": [],
       "displayType": "redashChart",
       "error": null,
       "errorDetails": null,
       "errorSummary": null,
       "errorTraceType": null,
       "finishTime": 0,
       "globalVars": {},
       "guid": "",
       "height": "auto",
       "hideCommandCode": false,
       "hideCommandResult": false,
       "iPythonMetadata": null,
       "inputWidgets": {},
       "isLockedInExamMode": false,
       "latestAssumeRoleInfo": null,
       "latestUser": "a user",
       "latestUserId": null,
       "listResultMetadata": null,
       "metadata": {},
       "nuid": "7315b294-1a80-4b3b-a8d6-d28a4db36859",
       "origId": 0,
       "parentHierarchy": [],
       "pivotAggregation": null,
       "pivotColumns": null,
       "position": 26.0,
       "resultDbfsErrorMessage": null,
       "resultDbfsStatus": "INLINED_IN_TREE",
       "results": null,
       "showCommandTitle": false,
       "startTime": 0,
       "state": "input",
       "streamStates": {},
       "subcommandOptions": {
        "queryPlan": {
         "groups": [
          {
           "column": "category_name",
           "type": "column"
          }
         ],
         "selects": [
          {
           "column": "category_name",
           "type": "column"
          },
          {
           "alias": "column_26923a16310",
           "args": [
            {
             "column": "revenue",
             "type": "column"
            }
           ],
           "function": "SUM",
           "type": "function"
          }
         ]
        }
       },
       "submitTime": 0,
       "subtype": "tableResultSubCmd.visualization",
       "tableResultIndex": 0,
       "tableResultSettingsMap": {},
       "useConsistentColors": false,
       "version": "CommandV1",
       "width": "auto",
       "workflows": [],
       "xColumns": null,
       "yColumns": null
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "category_sales = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\"category_name\")\n",
    "    .agg(sum(\"revenue\").alias(\"revenue\"))\n",
    "    .orderBy(desc(\"revenue\"))\n",
    ")\n",
    "\n",
    "display(category_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "8716b936-66a0-4c21-9551-867a79389113",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>store_name</th><th>revenue</th></tr></thead><tbody><tr><td>Santa Cruz Bikes</td><td>1605823.0364999974</td></tr><tr><td>Baldwin Bikes</td><td>5215751.277499983</td></tr><tr><td>Rowlett Bikes</td><td>867542.2436000014</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Santa Cruz Bikes",
         1605823.0364999974
        ],
        [
         "Baldwin Bikes",
         5215751.277499983
        ],
        [
         "Rowlett Bikes",
         867542.2436000014
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "store_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": [
       "Databricks visualization. Run in Databricks to view."
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1.subcommand+json": {
       "baseErrorDetails": null,
       "bindings": {},
       "collapsed": false,
       "command": "%python\n__backend_agg_display_orig = display\n__backend_agg_dfs = []\ndef __backend_agg_display_new(df):\n    __backend_agg_df_modules = [\"pandas.core.frame\", \"databricks.koalas.frame\", \"pyspark.sql.dataframe\", \"pyspark.pandas.frame\", \"pyspark.sql.connect.dataframe\", \"pyspark.sql.classic.dataframe\"]\n    if (type(df).__module__ in __backend_agg_df_modules and type(df).__name__ == 'DataFrame') or isinstance(df, list):\n        __backend_agg_dfs.append(df)\n\ndisplay = __backend_agg_display_new\n\ndef __backend_agg_user_code_fn():\n    import base64\n    exec(base64.standard_b64decode(\"c3RvcmVfc2FsZXMgPSAoCiAgICBzcGFyay50YWJsZSgiYmlrZXJfcl9wcm9qZWN0LmdvbGQuc2FsZXNfZmFjdCIpCiAgICAuZ3JvdXBCeSgic3RvcmVfbmFtZSIpCiAgICAuYWdnKHN1bSgicmV2ZW51ZSIpLmFsaWFzKCJyZXZlbnVlIikpCikKCmRpc3BsYXkoc3RvcmVfc2FsZXMp\").decode())\n\ntry:\n    # run user code\n    __backend_agg_user_code_fn()\n\n    #reset display function\n    display = __backend_agg_display_orig\n\n    if len(__backend_agg_dfs) > 0:\n        # create a temp view\n        if type(__backend_agg_dfs[0]).__module__ == \"databricks.koalas.frame\":\n            # koalas dataframe\n            __backend_agg_dfs[0].to_spark().createOrReplaceTempView(\"DatabricksView44d242c\")\n        elif type(__backend_agg_dfs[0]).__module__ == \"pandas.core.frame\" or isinstance(__backend_agg_dfs[0], list):\n            # pandas dataframe\n            spark.createDataFrame(__backend_agg_dfs[0]).createOrReplaceTempView(\"DatabricksView44d242c\")\n        else:\n            __backend_agg_dfs[0].createOrReplaceTempView(\"DatabricksView44d242c\")\n        #run backend agg\n        display(spark.sql(\"\"\"WITH q AS (select * from DatabricksView44d242c) SELECT `store_name`,SUM(`revenue`) `column_26923a16317` FROM q GROUP BY `store_name`\"\"\"))\n    else:\n        displayHTML(\"dataframe no longer exists. If you're using dataframe.display(), use display(dataframe) instead.\")\n\n\nfinally:\n    spark.sql(\"drop view if exists DatabricksView44d242c\")\n    display = __backend_agg_display_orig\n    del __backend_agg_display_new\n    del __backend_agg_display_orig\n    del __backend_agg_dfs\n    del __backend_agg_user_code_fn\n\n",
       "commandTitle": "Visualization 1",
       "commandType": "auto",
       "commandVersion": 0,
       "commentThread": [],
       "commentsVisible": false,
       "contentSha256Hex": null,
       "customPlotOptions": {
        "redashChart": [
         {
          "key": "type",
          "value": "CHART"
         },
         {
          "key": "options",
          "value": {
           "alignYAxesAtZero": true,
           "coefficient": 1,
           "columnConfigurationMap": {
            "x": {
             "column": "store_name",
             "id": "column_26923a16316"
            },
            "y": [
             {
              "column": "revenue",
              "id": "column_26923a16317",
              "transform": "SUM"
             }
            ]
           },
           "dateTimeFormat": "DD/MM/YYYY HH:mm",
           "direction": {
            "type": "counterclockwise"
           },
           "error_y": {
            "type": "data",
            "visible": true
           },
           "globalSeriesType": "column",
           "isAggregationOn": true,
           "legend": {
            "traceorder": "normal"
           },
           "missingValuesAsZero": true,
           "numberFormat": "0,0.[00000]",
           "percentFormat": "0[.]00%",
           "series": {
            "error_y": {
             "type": "data",
             "visible": true
            },
            "stacking": null
           },
           "seriesOptions": {
            "column_26923a16317": {
             "name": "revenue",
             "yAxis": 0
            }
           },
           "showDataLabels": false,
           "sizemode": "diameter",
           "sortX": true,
           "sortY": true,
           "swappedAxes": true,
           "textFormat": "",
           "useAggregationsUi": true,
           "valuesOptions": {},
           "version": 2,
           "xAxis": {
            "labels": {
             "enabled": true
            },
            "type": "-"
           },
           "yAxis": [
            {
             "type": "-"
            },
            {
             "opposite": true,
             "type": "-"
            }
           ]
          }
         }
        ]
       },
       "datasetPreviewNameToCmdIdMap": {},
       "diffDeletes": [],
       "diffInserts": [],
       "displayType": "redashChart",
       "error": null,
       "errorDetails": null,
       "errorSummary": null,
       "errorTraceType": null,
       "finishTime": 0,
       "globalVars": {},
       "guid": "",
       "height": "auto",
       "hideCommandCode": false,
       "hideCommandResult": false,
       "iPythonMetadata": null,
       "inputWidgets": {},
       "isLockedInExamMode": false,
       "latestAssumeRoleInfo": null,
       "latestUser": "a user",
       "latestUserId": null,
       "listResultMetadata": null,
       "metadata": {},
       "nuid": "21a50315-78e4-495c-b868-678d05cd1b37",
       "origId": 0,
       "parentHierarchy": [],
       "pivotAggregation": null,
       "pivotColumns": null,
       "position": 27.0,
       "resultDbfsErrorMessage": null,
       "resultDbfsStatus": "INLINED_IN_TREE",
       "results": null,
       "showCommandTitle": false,
       "startTime": 0,
       "state": "input",
       "streamStates": {},
       "subcommandOptions": {
        "queryPlan": {
         "groups": [
          {
           "column": "store_name",
           "type": "column"
          }
         ],
         "selects": [
          {
           "column": "store_name",
           "type": "column"
          },
          {
           "alias": "column_26923a16317",
           "args": [
            {
             "column": "revenue",
             "type": "column"
            }
           ],
           "function": "SUM",
           "type": "function"
          }
         ]
        }
       },
       "submitTime": 0,
       "subtype": "tableResultSubCmd.visualization",
       "tableResultIndex": 0,
       "tableResultSettingsMap": {},
       "useConsistentColors": false,
       "version": "CommandV1",
       "width": "auto",
       "workflows": [],
       "xColumns": null,
       "yColumns": null
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "store_sales = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\"store_name\")\n",
    "    .agg(sum(\"revenue\").alias(\"revenue\"))\n",
    ")\n",
    "\n",
    "display(store_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "5ee5317b-6cf9-4baf-aa80-6e4c0ac5ee1b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>brand_name</th><th>revenue</th></tr></thead><tbody><tr><td>Trek</td><td>4602754.350899985</td></tr><tr><td>Electra</td><td>1205320.8196000017</td></tr><tr><td>Surly</td><td>949507.0633000013</td></tr><tr><td>Sun Bicycles</td><td>341994.9275000002</td></tr><tr><td>Haro</td><td>185384.5536999999</td></tr><tr><td>Heller</td><td>171459.07569999993</td></tr><tr><td>Pure Cycles</td><td>149476.34000000032</td></tr><tr><td>Ritchey</td><td>78898.94799999999</td></tr><tr><td>Strider</td><td>4320.478899999999</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Trek",
         4602754.350899985
        ],
        [
         "Electra",
         1205320.8196000017
        ],
        [
         "Surly",
         949507.0633000013
        ],
        [
         "Sun Bicycles",
         341994.9275000002
        ],
        [
         "Haro",
         185384.5536999999
        ],
        [
         "Heller",
         171459.07569999993
        ],
        [
         "Pure Cycles",
         149476.34000000032
        ],
        [
         "Ritchey",
         78898.94799999999
        ],
        [
         "Strider",
         4320.478899999999
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "brand_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": [
       "Databricks visualization. Run in Databricks to view."
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1.subcommand+json": {
       "baseErrorDetails": null,
       "bindings": {},
       "collapsed": false,
       "command": "%python\n__backend_agg_display_orig = display\n__backend_agg_dfs = []\ndef __backend_agg_display_new(df):\n    __backend_agg_df_modules = [\"pandas.core.frame\", \"databricks.koalas.frame\", \"pyspark.sql.dataframe\", \"pyspark.pandas.frame\", \"pyspark.sql.connect.dataframe\", \"pyspark.sql.classic.dataframe\"]\n    if (type(df).__module__ in __backend_agg_df_modules and type(df).__name__ == 'DataFrame') or isinstance(df, list):\n        __backend_agg_dfs.append(df)\n\ndisplay = __backend_agg_display_new\n\ndef __backend_agg_user_code_fn():\n    import base64\n    exec(base64.standard_b64decode(\"YnJhbmRfc2FsZXMgPSAoCiAgICBzcGFyay50YWJsZSgiYmlrZXJfcl9wcm9qZWN0LmdvbGQuc2FsZXNfZmFjdCIpCiAgICAuZ3JvdXBCeSgiYnJhbmRfbmFtZSIpCiAgICAuYWdnKHN1bSgicmV2ZW51ZSIpLmFsaWFzKCJyZXZlbnVlIikpCiAgICAub3JkZXJCeShkZXNjKCJyZXZlbnVlIikpCikKCmRpc3BsYXkoYnJhbmRfc2FsZXMp\").decode())\n\ntry:\n    # run user code\n    __backend_agg_user_code_fn()\n\n    #reset display function\n    display = __backend_agg_display_orig\n\n    if len(__backend_agg_dfs) > 0:\n        # create a temp view\n        if type(__backend_agg_dfs[0]).__module__ == \"databricks.koalas.frame\":\n            # koalas dataframe\n            __backend_agg_dfs[0].to_spark().createOrReplaceTempView(\"DatabricksView5fe7000\")\n        elif type(__backend_agg_dfs[0]).__module__ == \"pandas.core.frame\" or isinstance(__backend_agg_dfs[0], list):\n            # pandas dataframe\n            spark.createDataFrame(__backend_agg_dfs[0]).createOrReplaceTempView(\"DatabricksView5fe7000\")\n        else:\n            __backend_agg_dfs[0].createOrReplaceTempView(\"DatabricksView5fe7000\")\n        #run backend agg\n        display(spark.sql(\"\"\"WITH q AS (select * from DatabricksView5fe7000) SELECT `brand_name`,SUM(`revenue`) `column_26923a16324` FROM q GROUP BY `brand_name`\"\"\"))\n    else:\n        displayHTML(\"dataframe no longer exists. If you're using dataframe.display(), use display(dataframe) instead.\")\n\n\nfinally:\n    spark.sql(\"drop view if exists DatabricksView5fe7000\")\n    display = __backend_agg_display_orig\n    del __backend_agg_display_new\n    del __backend_agg_display_orig\n    del __backend_agg_dfs\n    del __backend_agg_user_code_fn\n\n",
       "commandTitle": "Visualization 1",
       "commandType": "auto",
       "commandVersion": 0,
       "commentThread": [],
       "commentsVisible": false,
       "contentSha256Hex": null,
       "customPlotOptions": {
        "redashChart": [
         {
          "key": "type",
          "value": "CHART"
         },
         {
          "key": "options",
          "value": {
           "alignYAxesAtZero": true,
           "coefficient": 1,
           "columnConfigurationMap": {
            "x": {
             "column": "brand_name",
             "id": "column_26923a16323"
            },
            "y": [
             {
              "column": "revenue",
              "id": "column_26923a16324",
              "transform": "SUM"
             }
            ]
           },
           "dateTimeFormat": "DD/MM/YYYY HH:mm",
           "direction": {
            "type": "counterclockwise"
           },
           "error_y": {
            "type": "data",
            "visible": true
           },
           "globalSeriesType": "column",
           "isAggregationOn": true,
           "legend": {
            "traceorder": "normal"
           },
           "missingValuesAsZero": true,
           "numberFormat": "0,0.[00000]",
           "percentFormat": "0[.]00%",
           "series": {
            "error_y": {
             "type": "data",
             "visible": true
            },
            "stacking": null
           },
           "seriesOptions": {
            "column_26923a16324": {
             "name": "revenue",
             "type": "column",
             "yAxis": 0
            }
           },
           "showDataLabels": false,
           "sizemode": "diameter",
           "sortX": true,
           "sortY": true,
           "swappedAxes": true,
           "textFormat": "",
           "useAggregationsUi": true,
           "valuesOptions": {},
           "version": 2,
           "xAxis": {
            "labels": {
             "enabled": true
            },
            "type": "-"
           },
           "yAxis": [
            {
             "type": "-"
            },
            {
             "opposite": true,
             "type": "-"
            }
           ]
          }
         }
        ]
       },
       "datasetPreviewNameToCmdIdMap": {},
       "diffDeletes": [],
       "diffInserts": [],
       "displayType": "redashChart",
       "error": null,
       "errorDetails": null,
       "errorSummary": null,
       "errorTraceType": null,
       "finishTime": 0,
       "globalVars": {},
       "guid": "",
       "height": "auto",
       "hideCommandCode": false,
       "hideCommandResult": false,
       "iPythonMetadata": null,
       "inputWidgets": {},
       "isLockedInExamMode": false,
       "latestAssumeRoleInfo": null,
       "latestUser": "a user",
       "latestUserId": null,
       "listResultMetadata": null,
       "metadata": {},
       "nuid": "dcb2284e-2126-45c2-bb39-ccfe992af652",
       "origId": 0,
       "parentHierarchy": [],
       "pivotAggregation": null,
       "pivotColumns": null,
       "position": 28.0,
       "resultDbfsErrorMessage": null,
       "resultDbfsStatus": "INLINED_IN_TREE",
       "results": null,
       "showCommandTitle": false,
       "startTime": 0,
       "state": "input",
       "streamStates": {},
       "subcommandOptions": {
        "queryPlan": {
         "groups": [
          {
           "column": "brand_name",
           "type": "column"
          }
         ],
         "selects": [
          {
           "column": "brand_name",
           "type": "column"
          },
          {
           "alias": "column_26923a16324",
           "args": [
            {
             "column": "revenue",
             "type": "column"
            }
           ],
           "function": "SUM",
           "type": "function"
          }
         ]
        }
       },
       "submitTime": 0,
       "subtype": "tableResultSubCmd.visualization",
       "tableResultIndex": 0,
       "tableResultSettingsMap": {},
       "useConsistentColors": false,
       "version": "CommandV1",
       "width": "auto",
       "workflows": [],
       "xColumns": null,
       "yColumns": null
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "brand_sales = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\"brand_name\")\n",
    "    .agg(sum(\"revenue\").alias(\"revenue\"))\n",
    "    .orderBy(desc(\"revenue\"))\n",
    ")\n",
    "\n",
    "display(brand_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "662dbdef-ac17-4a8e-93ba-a0b5b3766166",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>customer_name</th><th>lifetime_value</th></tr></thead><tbody><tr><td>Johnathan Velazquez</td><td>10231.0464</td></tr><tr><td>Jaqueline Cummings</td><td>1697.9717</td></tr><tr><td>Joshua Robertson</td><td>1519.981</td></tr><tr><td>Nova Hess</td><td>13023.926</td></tr><tr><td>Arla Ellis</td><td>3900.0606999999995</td></tr><tr><td>Sharyn Hopkins</td><td>34807.93919999999</td></tr><tr><td>Laureen Paul</td><td>2165.0816999999997</td></tr><tr><td>Leslie Higgins</td><td>1372.4719</td></tr><tr><td>Neil Mccall</td><td>9919.3294</td></tr><tr><td>Alane Munoz</td><td>242.991</td></tr><tr><td>Tarra Guerrero</td><td>3155.9565</td></tr><tr><td>Marvin Mullins</td><td>18856.877</td></tr><tr><td>Patience Clayton</td><td>3278.054</td></tr><tr><td>Maribel William</td><td>437.09069999999997</td></tr><tr><td>Ellsworth Michael</td><td>4030.0561</td></tr><tr><td>Lea Key</td><td>2449.7546</td></tr><tr><td>Sindy Anderson</td><td>4092.8567</td></tr><tr><td>Lanita Burton</td><td>11406.4285</td></tr><tr><td>Norine Huffman</td><td>6240.553999999999</td></tr><tr><td>Randee Pitts</td><td>5671.1307</td></tr><tr><td>Neoma Daugherty</td><td>2083.1605</td></tr><tr><td>Tangela Hurley</td><td>1104.4745</td></tr><tr><td>Drucilla Gilliam</td><td>6265.955</td></tr><tr><td>Ashton Lott</td><td>2635.122</td></tr><tr><td>Sam Lester</td><td>3633.3590000000004</td></tr><tr><td>Jackeline Colon</td><td>5342.1559</td></tr><tr><td>Pamala Henry</td><td>6981.9401</td></tr><tr><td>Eleni Gordon</td><td>8587.397</td></tr><tr><td>Laureen Barry</td><td>3859.928</td></tr><tr><td>Yvone Guerrero</td><td>11183.0335</td></tr><tr><td>Edgar Quinn</td><td>7993.865</td></tr><tr><td>Kimbery Nieves</td><td>5270.944799999999</td></tr><tr><td>Verona O'neill</td><td>4157.9724</td></tr><tr><td>Sarai Mckee</td><td>9563.338099999999</td></tr><tr><td>Neville Mcclain</td><td>3376.5951000000005</td></tr><tr><td>Shantel Gregory</td><td>5644.9152</td></tr><tr><td>Tomika Larson</td><td>1139.981</td></tr><tr><td>Lashandra Turner</td><td>11578.6544</td></tr><tr><td>Travis Whitley</td><td>3768.94</td></tr><tr><td>Darren Witt</td><td>3223.184</td></tr><tr><td>Ingeborg Ellison</td><td>2867.275</td></tr><tr><td>Corene Swanson</td><td>426.54999999999995</td></tr><tr><td>Elana Miles</td><td>1530.963</td></tr><tr><td>Olympia Figueroa</td><td>4169.9815</td></tr><tr><td>Carissa Cross</td><td>5404.055699999999</td></tr><tr><td>Eldridge Greer</td><td>386.1</td></tr><tr><td>Joshua Berg</td><td>2069.4549</td></tr><tr><td>Josephine Dale</td><td>6712.8464</td></tr><tr><td>Taisha Vang</td><td>502.1814</td></tr><tr><td>Silas Tate</td><td>2497.9559</td></tr><tr><td>Jamaal Baker</td><td>1786.4650000000001</td></tr><tr><td>Twana Arnold</td><td>464.9907</td></tr><tr><td>Margit Osborn</td><td>4781.9310000000005</td></tr><tr><td>Inge Olsen</td><td>1759.976</td></tr><tr><td>Chanel May</td><td>1904.4585000000002</td></tr><tr><td>Nathaniel Davidson</td><td>1115.9814</td></tr><tr><td>Dalia Carson</td><td>1509.4727</td></tr><tr><td>Tiana Henderson</td><td>1200.542</td></tr><tr><td>Rodney Odom</td><td>1703.6815000000001</td></tr><tr><td>Joesph Delacruz</td><td>6863.626799999999</td></tr><tr><td>Mark Garrett</td><td>3570.5560000000005</td></tr><tr><td>Denis Logan</td><td>5651.0267</td></tr><tr><td>Dann Huff</td><td>2653.073</td></tr><tr><td>Corine Stuart</td><td>2801.9320000000002</td></tr><tr><td>Serafina Clemons</td><td>494.99100000000004</td></tr><tr><td>Susannah Fields</td><td>1390.4733999999999</td></tr><tr><td>Lazaro Moran</td><td>4422.9400000000005</td></tr><tr><td>Kristen Alvarez</td><td>888.2814000000001</td></tr><tr><td>Ophelia Decker</td><td>3014.324</td></tr><tr><td>Cleotilde Booth</td><td>16179.1167</td></tr><tr><td>Cathey Lamb</td><td>1984.0729999999999</td></tr><tr><td>Cesar Wilkins</td><td>1806.4125</td></tr><tr><td>Gabriel Wagner</td><td>4196.0278</td></tr><tr><td>Mariela Huffman</td><td>1577.0717</td></tr><tr><td>Euna Lopez</td><td>8763.964399999999</td></tr><tr><td>Genoveva Baldwin</td><td>24433.8818</td></tr><tr><td>Rochelle Ward</td><td>2427.9567</td></tr><tr><td>Trinidad Chapman</td><td>2052.3520000000003</td></tr><tr><td>Ellena Clements</td><td>7568.0544</td></tr><tr><td>Jeannie Wilcox</td><td>1378.182</td></tr><tr><td>Max Charles</td><td>3998.362</td></tr><tr><td>Bronwyn Vargas</td><td>3589.5660000000003</td></tr><tr><td>Gertrude Terry</td><td>2379.973</td></tr><tr><td>Christia Wilkins</td><td>1543.7628</td></tr><tr><td>Aaron Knapp</td><td>5927.5509999999995</td></tr><tr><td>Lavette Wright</td><td>6866.9384</td></tr><tr><td>Rosa Kinney</td><td>1499.9660000000001</td></tr><tr><td>Rodolfo Buck</td><td>8280.543</td></tr><tr><td>Calandra Stanton</td><td>2100.9225</td></tr><tr><td>Romaine Haley</td><td>1337.0817</td></tr><tr><td>Catrice Hicks</td><td>3475.8442999999997</td></tr><tr><td>Kimberli Cline</td><td>1619.991</td></tr><tr><td>Cindie Franklin</td><td>4633.8544</td></tr><tr><td>Thurman Ellis</td><td>4689.4559</td></tr><tr><td>Casey Gill</td><td>6902.465</td></tr><tr><td>Keitha Black</td><td>824.9815</td></tr><tr><td>Alpha King</td><td>2813.5587</td></tr><tr><td>Leticia Snyder</td><td>1692.5370000000003</td></tr><tr><td>Rikki Morrow</td><td>9301.9304</td></tr><tr><td>Luke Kramer</td><td>12420.713</td></tr><tr><td>Katheleen Marks</td><td>879.984</td></tr><tr><td>Trisha Johnson</td><td>754.5812</td></tr><tr><td>Brigida Larson</td><td>8062.1245</td></tr><tr><td>Latasha Hays</td><td>7147.162899999999</td></tr><tr><td>Vikki Erickson</td><td>6489.5650000000005</td></tr><tr><td>Valery Saunders</td><td>872.0820000000001</td></tr><tr><td>Kiara Deleon</td><td>845.182</td></tr><tr><td>Robby Sykes</td><td>24305.1394</td></tr><tr><td>Ben Stone</td><td>923.0726999999999</td></tr><tr><td>Launa Hull</td><td>242.991</td></tr><tr><td>Zulema Browning</td><td>1265.9723999999999</td></tr><tr><td>Micki Rutledge</td><td>3511.7384</td></tr><tr><td>Theresia Barron</td><td>4803.6301</td></tr><tr><td>Mark Benton</td><td>1705.9632</td></tr><tr><td>Starr Schneider</td><td>620.0920000000001</td></tr><tr><td>Burma Summers</td><td>569.9905</td></tr><tr><td>Gwenn Melton</td><td>1644.5165</td></tr><tr><td>Danille Mcfarland</td><td>5909.614799999999</td></tr><tr><td>Bryce Monroe</td><td>474.9905</td></tr><tr><td>Sharie Alvarez</td><td>5716.5960000000005</td></tr><tr><td>Tomika Wilder</td><td>9210.7184</td></tr><tr><td>Wallace Lane</td><td>539.991</td></tr><tr><td>Lecia Hancock</td><td>989.9820000000001</td></tr><tr><td>Elouise Fry</td><td>10866.962199999998</td></tr><tr><td>Laverne Craft</td><td>386.1</td></tr><tr><td>Shenna Espinoza</td><td>5699.981</td></tr><tr><td>Chelsey Boyd</td><td>6332.9424</td></tr><tr><td>Lissa Vargas</td><td>12551.997</td></tr><tr><td>Armand Whitehead</td><td>7154.5445</td></tr><tr><td>Marcelino Mcbride</td><td>3027.0319</td></tr><tr><td>Hortencia Graham</td><td>6815.9474</td></tr><tr><td>Monika Berg</td><td>8902.506599999999</td></tr><tr><td>Jerome Bolton</td><td>728.973</td></tr><tr><td>Tuan Wolfe</td><td>3038.3214</td></tr><tr><td>Alexandria Zamora</td><td>4475.4635</td></tr><tr><td>Gena Owens</td><td>8299.965</td></tr><tr><td>Jina Cooper</td><td>521.9817</td></tr><tr><td>Katharine Herrera</td><td>1455.974</td></tr><tr><td>Ezra Silva</td><td>1765.1307</td></tr><tr><td>Devin Velazquez</td><td>2469.9585</td></tr><tr><td>Erlene Cook</td><td>359.20000000000005</td></tr><tr><td>Regine Gonzales</td><td>13801.2997</td></tr><tr><td>Merlin Foreman</td><td>375.992</td></tr><tr><td>Hubert Reilly</td><td>3419.9809999999998</td></tr><tr><td>Lavonne Anderson</td><td>6744.774</td></tr><tr><td>Keturah Massey</td><td>4765.4287</td></tr><tr><td>Diana Guerra</td><td>4183.6206999999995</td></tr><tr><td>Senaida Thompson</td><td>256.4905</td></tr><tr><td>Han Schneider</td><td>1525.1627999999998</td></tr><tr><td>Reena Higgins</td><td>5728.9344</td></tr><tr><td>Katina Mcintosh</td><td>926.091</td></tr><tr><td>Parker Prince</td><td>7168.4778</td></tr><tr><td>Edda Young</td><td>3238.9623999999994</td></tr><tr><td>Dione Pratt</td><td>494.99100000000004</td></tr><tr><td>Loni Duncan</td><td>1619.991</td></tr><tr><td>Sheri Cole</td><td>1970.5907</td></tr><tr><td>Mozelle Carter</td><td>23049.057</td></tr><tr><td>Dacia William</td><td>2371.4545</td></tr><tr><td>Araceli Golden</td><td>18037.285</td></tr><tr><td>Harris Pittman</td><td>3642.0126</td></tr><tr><td>Kasie Rodriquez</td><td>8879.452899999998</td></tr><tr><td>Williemae Holloway</td><td>19756.6432</td></tr><tr><td>Magdalena Sherman</td><td>854.191</td></tr><tr><td>Leonore Dorsey</td><td>8696.072</td></tr><tr><td>Adriene Rivera</td><td>6462.4635</td></tr><tr><td>Abbey Pugh</td><td>4132.992</td></tr><tr><td>Rico Salas</td><td>9874.6525</td></tr><tr><td>Kandace Ayers</td><td>5004.5978000000005</td></tr><tr><td>Carie Kidd</td><td>5431.8955</td></tr><tr><td>Aubrey Durham</td><td>5565.5645</td></tr><tr><td>Elvera Peck</td><td>2007.5811999999999</td></tr><tr><td>Cindi Ellis</td><td>758.9827</td></tr><tr><td>Destiny Goodman</td><td>1240.1840000000002</td></tr><tr><td>Steve Bender</td><td>3292.427</td></tr><tr><td>Melba Wilkinson</td><td>5224.5464</td></tr><tr><td>Lucy Woods</td><td>3589.122</td></tr><tr><td>Graig Roth</td><td>4318.4515</td></tr><tr><td>Shery Acosta</td><td>3372.138</td></tr><tr><td>Kristel Bullock</td><td>557.9907</td></tr><tr><td>Latosha Dalton</td><td>4877.406</td></tr><tr><td>Phylis Adkins</td><td>1972.9624</td></tr><tr><td>Adelle Larsen</td><td>16651.0484</td></tr><tr><td>Brianna Moss</td><td>3751.874</td></tr><tr><td>Corene Wall</td><td>14199.9558</td></tr><tr><td>Waldo Hart</td><td>3032.982</td></tr><tr><td>Jeniffer Ratliff</td><td>1254.9405</td></tr><tr><td>Lorrie Pollard</td><td>7439.981399999999</td></tr><tr><td>Allie Conley</td><td>959.984</td></tr><tr><td>Violet Valenzuela</td><td>2546.4665000000005</td></tr><tr><td>Ruthanne Hoover</td><td>5989.9367</td></tr><tr><td>Viva Dawson</td><td>7918.8446</td></tr><tr><td>Trena Rogers</td><td>989.9820000000001</td></tr><tr><td>Carroll Kelly</td><td>431.98400000000004</td></tr><tr><td>Kasha Sullivan</td><td>7855.2405</td></tr><tr><td>Tammie Cherry</td><td>6239.0936</td></tr><tr><td>Erlinda Nielsen</td><td>6034.965399999999</td></tr><tr><td>Allison Nolan</td><td>5809.477400000001</td></tr><tr><td>Marisa Chambers</td><td>4105.112999999999</td></tr><tr><td>Lanelle Guerra</td><td>1072.1624</td></tr><tr><td>Brenda Tate</td><td>4616.0145</td></tr><tr><td>Joi Reeves</td><td>4038.502699999999</td></tr><tr><td>Henrietta Wagner</td><td>3891.5125</td></tr><tr><td>Danilo Holmes</td><td>1646.3814</td></tr><tr><td>Myrtie James</td><td>1502.9630000000002</td></tr><tr><td>Tania Swanson</td><td>954.9825000000001</td></tr><tr><td>Marget Hodge</td><td>12461.5479</td></tr><tr><td>Leanna Manning</td><td>10620.044899999999</td></tr><tr><td>Clarita Curry</td><td>242.991</td></tr><tr><td>Lynn Mcmahon</td><td>683.0747</td></tr><tr><td>Penney Hall</td><td>2835.5514</td></tr><tr><td>Lanora Robbins</td><td>5600.0574</td></tr><tr><td>Lilliam Nolan</td><td>242.991</td></tr><tr><td>Kaci Gallegos</td><td>242.991</td></tr><tr><td>Kelsey Noble</td><td>1407.5520000000001</td></tr><tr><td>Angelina Lloyd</td><td>1625.963</td></tr><tr><td>Sebrina Hart</td><td>3591.27</td></tr><tr><td>Vernetta Banks</td><td>2123.5632</td></tr><tr><td>Inez Snider</td><td>1626.7825000000003</td></tr><tr><td>Noble Glover</td><td>3443.9377000000004</td></tr><tr><td>Donovan Cantrell</td><td>3126.6414</td></tr><tr><td>Gertrud Rhodes</td><td>7000.058000000001</td></tr><tr><td>Veronique Fulton</td><td>10216.235999999999</td></tr><tr><td>Carola Rodriquez</td><td>17861.1996</td></tr><tr><td>Fransisca Nicholson</td><td>2942.982</td></tr><tr><td>Tony Hicks</td><td>712.4905</td></tr><tr><td>Kirstie Vazquez</td><td>2853.963</td></tr><tr><td>Jamika Blanchard</td><td>4911.437899999999</td></tr><tr><td>Evelina Manning</td><td>4617.758</td></tr><tr><td>Ryan Carter</td><td>3126.6414</td></tr><tr><td>Rosamaria Meyer</td><td>5893.5494</td></tr><tr><td>Latashia Travis</td><td>7967.4144</td></tr><tr><td>Melita Dominguez</td><td>2748.7464</td></tr><tr><td>Merrie Fowler</td><td>8069.656499999999</td></tr><tr><td>Eli Contreras</td><td>8550.052699999998</td></tr><tr><td>Stephaine Riddle</td><td>8429.9454</td></tr><tr><td>Carman Hardy</td><td>2465.4572</td></tr><tr><td>Annett Rush</td><td>6089.930399999999</td></tr><tr><td>Lashawn Ortiz</td><td>14774.458299999998</td></tr><tr><td>Kanesha Vega</td><td>11151.6045</td></tr><tr><td>Divina Madden</td><td>3199.992</td></tr><tr><td>Almeta Benjamin</td><td>799.9920000000001</td></tr><tr><td>Barrett Sanders</td><td>9385.101999999999</td></tr><tr><td>Venus Hewitt</td><td>1060.553</td></tr><tr><td>Scarlet Yates</td><td>4563.091</td></tr><tr><td>Caren Stephens</td><td>5275.327</td></tr><tr><td>Joann Barber</td><td>1264.9827</td></tr><tr><td>Kimberley Reynolds</td><td>4109.065</td></tr><tr><td>Miquel Neal</td><td>8696.071999999998</td></tr><tr><td>Weldon Michael</td><td>3840.882</td></tr><tr><td>Arlena Buckner</td><td>992.965</td></tr><tr><td>Lorrie Becker</td><td>23026.2923</td></tr><tr><td>Earline Gordon</td><td>3126.6414</td></tr><tr><td>Faustino Delacruz</td><td>2346.6623999999997</td></tr><tr><td>Ophelia Rodgers</td><td>4044.848700000001</td></tr><tr><td>Theo Reese</td><td>9514.0705</td></tr><tr><td>Joeann Garrison</td><td>7045.1564</td></tr><tr><td>Cecil Hopper</td><td>6961.0917</td></tr><tr><td>Ginette Edwards</td><td>5225.9475</td></tr><tr><td>Yvette Rogers</td><td>2599.168</td></tr><tr><td>Pasquale Hogan</td><td>2155.172</td></tr><tr><td>Matilda Larson</td><td>6397.4717</td></tr><tr><td>Ai Forbes</td><td>5014.9637</td></tr><tr><td>Charolette Rice</td><td>17520.2919</td></tr><tr><td>Arnita Thomas</td><td>4799.9839999999995</td></tr><tr><td>Lurline Rivers</td><td>1708.3719</td></tr><tr><td>Randolph Chase</td><td>9163.428899999999</td></tr><tr><td>Shery Randolph</td><td>7251.965499999999</td></tr><tr><td>Terrell Mathis</td><td>3163.0425999999998</td></tr><tr><td>Ethelyn Ray</td><td>1276.9750000000001</td></tr><tr><td>Christoper Mccall</td><td>11462.5954</td></tr><tr><td>Ezra Fowler</td><td>2958.3021</td></tr><tr><td>Tona Velasquez</td><td>242.991</td></tr><tr><td>Octavia Case</td><td>9673.8444</td></tr><tr><td>Rozanne Reyes</td><td>8476.521999999999</td></tr><tr><td>Magali Dixon</td><td>7587.5154</td></tr><tr><td>Thad Castro</td><td>2197.9500000000003</td></tr><tr><td>Raven Curtis</td><td>4692.8641</td></tr><tr><td>Rosalba O'neal</td><td>464.9907</td></tr><tr><td>Tomeka Higgins</td><td>1832.0628</td></tr><tr><td>Cris Dunn</td><td>8177.0540999999985</td></tr><tr><td>Regina Burns</td><td>11013.9345</td></tr><tr><td>Olevia Pitts</td><td>8273.955899999999</td></tr><tr><td>Inger Jennings</td><td>1359.976</td></tr><tr><td>Justin Newton</td><td>2337.4625</td></tr><tr><td>Latasha Stanley</td><td>13854.6016</td></tr><tr><td>Delbert Wilkins</td><td>3810.823</td></tr><tr><td>Ouida Gregory</td><td>11314.072999999999</td></tr><tr><td>Phyllis Hill</td><td>1034.2827000000002</td></tr><tr><td>Marni Bolton</td><td>4095.0137999999997</td></tr><tr><td>Alane Kennedy</td><td>1395.1624</td></tr><tr><td>Van Peters</td><td>6448.2907</td></tr><tr><td>Rubye Mccall</td><td>1229.0919999999999</td></tr><tr><td>Lavona Austin</td><td>8975.157</td></tr><tr><td>Benny Bender</td><td>502.1814</td></tr><tr><td>Gabriela Warren</td><td>7345.7374</td></tr><tr><td>Justina Jenkins</td><td>6898.1055</td></tr><tr><td>Janna Hayden</td><td>4624.9376999999995</td></tr><tr><td>Rayna Perry</td><td>5672.281</td></tr><tr><td>Emmaline Huber</td><td>10563.648000000001</td></tr><tr><td>Carlena Salinas</td><td>2915.108</td></tr><tr><td>Bernita Mcdaniel</td><td>6079.942999999999</td></tr><tr><td>Chelsey Hardin</td><td>9211.523</td></tr><tr><td>Camille Harvey</td><td>3463.545</td></tr><tr><td>Charleen Hurst</td><td>1490.2907</td></tr><tr><td>Christoper Gould</td><td>1006.981</td></tr><tr><td>Charlyn Cantrell</td><td>4534.383</td></tr><tr><td>Gilma Dejesus</td><td>1472.481</td></tr><tr><td>Deloris Larson</td><td>11479.5394</td></tr><tr><td>Shayla Hart</td><td>2928.684</td></tr><tr><td>Jame Riggs</td><td>2687.1434</td></tr><tr><td>Dagny Owen</td><td>5578.1307</td></tr><tr><td>Janie Herrera</td><td>11950.476599999998</td></tr><tr><td>Rufina Chandler</td><td>4044.7830000000004</td></tr><tr><td>Shawnda Glover</td><td>3586.7070000000003</td></tr><tr><td>Mariam Miranda</td><td>2431.165</td></tr><tr><td>Mallie Osborn</td><td>4135.9565</td></tr><tr><td>Danyell Dickerson</td><td>3018.2852</td></tr><tr><td>Carola Johns</td><td>674.991</td></tr><tr><td>Arcelia Vinson</td><td>6479.944</td></tr><tr><td>Lea Irwin</td><td>683.0747</td></tr><tr><td>Heide Reed</td><td>1582.1634</td></tr><tr><td>Garland Weaver</td><td>3074.2065000000002</td></tr><tr><td>Ernestina Skinner</td><td>4991.9664999999995</td></tr><tr><td>Bernetta Summers</td><td>773.9817</td></tr><tr><td>Tiesha Daniel</td><td>7793.1507</td></tr><tr><td>Angele Schroeder</td><td>845.9820000000001</td></tr><tr><td>Josh Shaw</td><td>5701.1053999999995</td></tr><tr><td>Gabriel Pitts</td><td>512.981</td></tr><tr><td>Yang Roth</td><td>772.2</td></tr><tr><td>Antonetta Rocha</td><td>853.0999999999999</td></tr><tr><td>Major Merrill</td><td>5055.113</td></tr><tr><td>Hollis Rasmussen</td><td>5709.9555</td></tr><tr><td>Phebe Soto</td><td>2024.0637</td></tr><tr><td>Saran Moses</td><td>3049.983</td></tr><tr><td>Adriene Rollins</td><td>3181.5405</td></tr><tr><td>Omega Huff</td><td>8534.3743</td></tr><tr><td>Shirely Cantrell</td><td>1249.972</td></tr><tr><td>Anisha Lang</td><td>6416.5944</td></tr><tr><td>Karren Lamb</td><td>569.981</td></tr><tr><td>Reyes Merritt</td><td>4037.9646999999995</td></tr><tr><td>Iva Wilcox</td><td>5338.9555</td></tr><tr><td>Romaine Salazar</td><td>1307.6225</td></tr><tr><td>Shauna Edwards</td><td>1831.1814</td></tr><tr><td>Lynne Anderson</td><td>2090.6642</td></tr><tr><td>Jerald Blackwell</td><td>278.9907</td></tr><tr><td>Daina Sampson</td><td>3495.6623999999997</td></tr><tr><td>Jamaal Albert</td><td>10355.390800000001</td></tr><tr><td>Cinda Rocha</td><td>7482.1364</td></tr><tr><td>Emmitt Sanchez</td><td>31925.885700000003</td></tr><tr><td>Phylicia Stout</td><td>1199.9840000000002</td></tr><tr><td>Jenine Crane</td><td>642.5419999999999</td></tr><tr><td>Sebrina Gross</td><td>1042.1724</td></tr><tr><td>Sheila Goodman</td><td>3581.4619999999995</td></tr><tr><td>Garry Espinoza</td><td>15766.7006</td></tr><tr><td>Larissa Hays</td><td>5588.344399999999</td></tr><tr><td>Dorthea Walker</td><td>12965.7468</td></tr><tr><td>Clorinda Donovan</td><td>7932.9465</td></tr><tr><td>Demarcus Reese</td><td>3403.8540000000003</td></tr><tr><td>Hedwig Paul</td><td>13611.6259</td></tr><tr><td>Brain Skinner</td><td>1694.0557000000001</td></tr><tr><td>Mariette Trevino</td><td>949.981</td></tr><tr><td>Christel Cardenas</td><td>1022.9813999999999</td></tr><tr><td>Arielle Levine</td><td>3899.9656999999997</td></tr><tr><td>Afton Juarez</td><td>4279.5725</td></tr><tr><td>Amina Salazar</td><td>4447.724</td></tr><tr><td>Garth Huff</td><td>2881.14</td></tr><tr><td>Raymonde Garcia</td><td>6169.963</td></tr><tr><td>Ashlie Parrish</td><td>655.984</td></tr><tr><td>Boyd Irwin</td><td>3271.8135</td></tr><tr><td>Majorie Wyatt</td><td>5119.353999999999</td></tr><tr><td>Dante Grimes</td><td>5114.0907</td></tr><tr><td>Christiane Bradford</td><td>8376.9244</td></tr><tr><td>Kristel Byrd</td><td>1934.9634</td></tr><tr><td>Thad Gilliam</td><td>1961.0811999999999</td></tr><tr><td>Alec Peck</td><td>1139.981</td></tr><tr><td>Hassan Nash</td><td>3269.9827</td></tr><tr><td>Han Wade</td><td>3763.8714999999997</td></tr><tr><td>Vanessa West</td><td>502.1814</td></tr><tr><td>Clelia Workman</td><td>4571.0727</td></tr><tr><td>Aleta Mack</td><td>1929.514</td></tr><tr><td>Conception Slater</td><td>5478.9484999999995</td></tr><tr><td>Odette Moses</td><td>7791.0557</td></tr><tr><td>Christiana Gross</td><td>4299.957</td></tr><tr><td>Jennette Wooten</td><td>359.20000000000005</td></tr><tr><td>Mirella Duffy</td><td>3430.9631</td></tr><tr><td>Saturnina Garner</td><td>14068.2366</td></tr><tr><td>Shirely Stanley</td><td>10574.962399999999</td></tr><tr><td>Elinore Aguilar</td><td>25636.453100000002</td></tr><tr><td>Carley Reynolds</td><td>6829.7092</td></tr><tr><td>Alysha Powers</td><td>751.984</td></tr><tr><td>Tammera Fischer</td><td>1196.9665</td></tr><tr><td>Hans Price</td><td>256.4905</td></tr><tr><td>Timothy Byers</td><td>2501.764</td></tr><tr><td>Son Warner</td><td>3799.9904999999994</td></tr><tr><td>Chasidy Tran</td><td>5080.6230000000005</td></tr><tr><td>Lee Roman</td><td>3911.8624999999997</td></tr><tr><td>Alline Beasley</td><td>5022.9574</td></tr><tr><td>Sylvie Wilkerson</td><td>2718.3920000000003</td></tr><tr><td>Corina Lynch</td><td>2672.6926</td></tr><tr><td>Salena Day</td><td>8342.939</td></tr><tr><td>Laverna Hernandez</td><td>4699.9557</td></tr><tr><td>Genevieve Juarez</td><td>4890.365400000001</td></tr><tr><td>Eliz Lynch</td><td>2319.9919999999997</td></tr><tr><td>Keri Bridges</td><td>8522.9542</td></tr><tr><td>Shemeka Lyons</td><td>3370.5721</td></tr><tr><td>Luke Fuller</td><td>1709.3652000000002</td></tr><tr><td>Herminia Reyes</td><td>7139.954</td></tr><tr><td>Ferne Kline</td><td>1837.4717</td></tr><tr><td>Carmina Emerson</td><td>4497.581700000001</td></tr><tr><td>Kristofer Craig</td><td>6659.9627</td></tr><tr><td>Vernia Madden</td><td>5219.982</td></tr><tr><td>Bonita Marshall</td><td>3359.7477</td></tr><tr><td>Johana Jacobson</td><td>997.1724</td></tr><tr><td>Angie Powers</td><td>1990.1627999999998</td></tr><tr><td>Titus Bullock</td><td>9805.246399999998</td></tr><tr><td>Petronila Norris</td><td>13914.3345</td></tr><tr><td>Le Deleon</td><td>9959.0962</td></tr><tr><td>Suellen Mercado</td><td>1139.981</td></tr><tr><td>Dewayne Herring</td><td>4921.154399999999</td></tr><tr><td>Tommie Melton</td><td>1472.4724999999999</td></tr><tr><td>Tessie Farmer</td><td>1351.7224</td></tr><tr><td>Tonja Henderson</td><td>1964.0810000000001</td></tr><tr><td>Douglass Little</td><td>3092.9448</td></tr><tr><td>Bee Baker</td><td>2329.5760000000005</td></tr><tr><td>Laraine Robbins</td><td>17068.4922</td></tr><tr><td>Deja Chaney</td><td>8561.2627</td></tr><tr><td>Carlie Terrell</td><td>2133.9264000000003</td></tr><tr><td>Karla Kirk</td><td>13678.357</td></tr><tr><td>Jerri Guthrie</td><td>4477.174</td></tr><tr><td>Rochell Cantrell</td><td>7176.214899999999</td></tr><tr><td>Yun Nelson</td><td>1189.9825</td></tr><tr><td>Adam Thornton</td><td>5841.5215</td></tr><tr><td>Javier Nichols</td><td>6872.9437</td></tr><tr><td>Meredith Bryan</td><td>8474.1624</td></tr><tr><td>Hilda Harvey</td><td>6229.1214</td></tr><tr><td>Morton Barron</td><td>988.4817</td></tr><tr><td>Etsuko Garrison</td><td>2827.9494</td></tr><tr><td>Pandora Estes</td><td>1734.9325</td></tr><tr><td>Olevia Noel</td><td>3997.9747</td></tr><tr><td>Bart Hess</td><td>1331.9733999999999</td></tr><tr><td>Vallie Dixon</td><td>8083.9627</td></tr><tr><td>Nichelle Howell</td><td>1405.962</td></tr><tr><td>Justa Thompson</td><td>9927.5559</td></tr><tr><td>Laurence Christian</td><td>2222.8722</td></tr><tr><td>Charlsie Carson</td><td>512.981</td></tr><tr><td>Trinidad Mcclain</td><td>10986.904</td></tr><tr><td>Shanna Bonner</td><td>3564.9664999999995</td></tr><tr><td>Vanda Holmes</td><td>2432.9444</td></tr><tr><td>Hildegarde Christensen</td><td>2849.9905</td></tr><tr><td>Alanna Barry</td><td>1076.9307</td></tr><tr><td>Kami Rios</td><td>9278.653900000001</td></tr><tr><td>Andy O'neill</td><td>4655.040400000001</td></tr><tr><td>Mila Good</td><td>1344.7920000000001</td></tr><tr><td>Ladawn Downs</td><td>4067.6639999999998</td></tr><tr><td>Brittney Rojas</td><td>7601.154699999999</td></tr><tr><td>Lezlie Thompson</td><td>989.9820000000001</td></tr><tr><td>Brent Calderon</td><td>502.1814</td></tr><tr><td>Georgeann Waller</td><td>4036.9719999999998</td></tr><tr><td>Cheryll Snyder</td><td>1745.9640000000002</td></tr><tr><td>Ernest Rollins</td><td>10360.255</td></tr><tr><td>Marry Benjamin</td><td>4654.9529999999995</td></tr><tr><td>Adelaida Hancock</td><td>9497.172</td></tr><tr><td>Chere Mcfadden</td><td>6784.956700000001</td></tr><tr><td>Derrick Marks</td><td>3563.0245000000004</td></tr><tr><td>Alane Mccarty</td><td>728.973</td></tr><tr><td>Jeanett Herman</td><td>962.9730000000001</td></tr><tr><td>Elmo Arnold</td><td>557.9907</td></tr><tr><td>Rory Cooper</td><td>2197.892</td></tr><tr><td>Manie Sanchez</td><td>2157.916</td></tr><tr><td>Basilia Thornton</td><td>9408.7878</td></tr><tr><td>Josie Schultz</td><td>1894.541</td></tr><tr><td>Jayme Zamora</td><td>502.1814</td></tr><tr><td>Ivette Warren</td><td>6335.663699999999</td></tr><tr><td>Darcel Harmon</td><td>3816.4624</td></tr><tr><td>Jayson Rutledge</td><td>6947.9474</td></tr><tr><td>Whitney Cash</td><td>458.98300000000006</td></tr><tr><td>Diana Cobb</td><td>398.96999999999997</td></tr><tr><td>Iola Rasmussen</td><td>9838.4455</td></tr><tr><td>Birdie Kramer</td><td>1382.972</td></tr><tr><td>Vinnie Chan</td><td>3359.9717</td></tr><tr><td>George Pickett</td><td>375.992</td></tr><tr><td>Evelin Vargas</td><td>1328.6529</td></tr><tr><td>Carisa Carpenter</td><td>3239.982</td></tr><tr><td>Onita Macdonald</td><td>1525.1539</td></tr><tr><td>Ji Burt</td><td>6319.945999999999</td></tr><tr><td>Graciela Barber</td><td>2593.1289</td></tr><tr><td>Rosalie Coffey</td><td>1926.5809999999997</td></tr><tr><td>Tanesha Sawyer</td><td>269.99100000000004</td></tr><tr><td>Kecia Olsen</td><td>3065.9825</td></tr><tr><td>Ayanna Rhodes</td><td>914.9670000000001</td></tr><tr><td>Kandis Mills</td><td>929.9814</td></tr><tr><td>Divina Reeves</td><td>2195.0517</td></tr><tr><td>Rodrick Shelton</td><td>3349.6487</td></tr><tr><td>Julee Woodard</td><td>1260.973</td></tr><tr><td>Barton Cox</td><td>3328.0631</td></tr><tr><td>Shaunda Barnett</td><td>256.4905</td></tr><tr><td>Yvonne Bean</td><td>1973.7314</td></tr><tr><td>Mercedez Brooks</td><td>2414.963</td></tr><tr><td>Erlinda Osborne</td><td>479.992</td></tr><tr><td>Lory Berg</td><td>4169.981699999999</td></tr><tr><td>Enoch Rosario</td><td>4776.0444</td></tr><tr><td>Octavia Donaldson</td><td>6543.0622</td></tr><tr><td>Jeromy Elliott</td><td>5989.965</td></tr><tr><td>Ulysses Gaines</td><td>386.1</td></tr><tr><td>Klara Mosley</td><td>755.972</td></tr><tr><td>Jacquline Duncan</td><td>2201.6567</td></tr><tr><td>Lory Page</td><td>4214.9734</td></tr><tr><td>Guillermo Hart</td><td>1516.3400000000001</td></tr><tr><td>Marcel Lindsay</td><td>4544.8471</td></tr><tr><td>Shila White</td><td>6177.772499999999</td></tr><tr><td>Margene Eaton</td><td>502.1814</td></tr><tr><td>Juliane Dillard</td><td>8394.4714</td></tr><tr><td>Fran Yang</td><td>17225.4439</td></tr><tr><td>Ronald Parsons</td><td>2420.553</td></tr><tr><td>Augustus Schmidt</td><td>1272.784</td></tr><tr><td>Lois Steele</td><td>6152.6533</td></tr><tr><td>Rebbecca Espinoza</td><td>4503.7459</td></tr><tr><td>Lucas Estes</td><td>7105.7751</td></tr><tr><td>Omega Johnston</td><td>7848.2628</td></tr><tr><td>Tonda Webb</td><td>4169.3542</td></tr><tr><td>Irving Pitts</td><td>8359.215999999999</td></tr><tr><td>Gayle Wilkinson</td><td>512.981</td></tr><tr><td>Mandi Gibbs</td><td>1022.9813999999999</td></tr><tr><td>Yolando Wade</td><td>4873.9557</td></tr><tr><td>Merlene Vinson</td><td>12793.633699999998</td></tr><tr><td>Zelda Pratt</td><td>2252.915</td></tr><tr><td>Ashleigh Finch</td><td>5024.1645</td></tr><tr><td>Farrah Orr</td><td>7900.4347</td></tr><tr><td>Roseanne Maynard</td><td>1485.4635</td></tr><tr><td>Cira Downs</td><td>2214.0537</td></tr><tr><td>Agatha Daniels</td><td>3613.7245</td></tr><tr><td>Delana Scott</td><td>1199.9840000000002</td></tr><tr><td>Jewel Sparks</td><td>6187.1539</td></tr><tr><td>Lorrie Justice</td><td>2042.0634</td></tr><tr><td>Zulema Clemons</td><td>512.981</td></tr><tr><td>Melani Jarvis</td><td>4918.366</td></tr><tr><td>Alica Hunter</td><td>4122.145399999999</td></tr><tr><td>Chere Hardin</td><td>1165.0810000000001</td></tr><tr><td>Bao Wade</td><td>2793.0481</td></tr><tr><td>Loise Walker</td><td>3270.2309999999998</td></tr><tr><td>Aleta Shepard</td><td>11102.47</td></tr><tr><td>Bobbi Banks</td><td>4746.6324</td></tr><tr><td>Bobbie Foster</td><td>8778.1311</td></tr><tr><td>Alissa Craft</td><td>2754.9905</td></tr><tr><td>Beatris Joyner</td><td>4665.5492</td></tr><tr><td>Alexis Mack</td><td>2402.476</td></tr><tr><td>Liliana Kerr</td><td>1841.6217000000001</td></tr><tr><td>Katharina Bates</td><td>11776.4101</td></tr><tr><td>Buford Bridges</td><td>6155.9644</td></tr><tr><td>Bethany Herring</td><td>6794.082</td></tr><tr><td>Lezlie Lamb</td><td>10372.0934</td></tr><tr><td>Christel Barber</td><td>8816.954399999999</td></tr><tr><td>Thanh Figueroa</td><td>1649.9724999999999</td></tr><tr><td>Marjorie Logan</td><td>8956.785</td></tr><tr><td>Davis Long</td><td>1499.9719</td></tr><tr><td>Rodger Rojas</td><td>1758.5140000000001</td></tr><tr><td>Aisha Woods</td><td>2743.984</td></tr><tr><td>Nathaniel Richard</td><td>4495.272500000001</td></tr><tr><td>Jennie Middleton</td><td>9474.9404</td></tr><tr><td>Tayna Wade</td><td>3628.5126999999998</td></tr><tr><td>Lenita Bonner</td><td>2726.4905</td></tr><tr><td>Terese Briggs</td><td>1559.9725</td></tr><tr><td>Loreen Byers</td><td>5090.4175</td></tr><tr><td>Genoveva Tyler</td><td>4125.556500000001</td></tr><tr><td>Johna Powers</td><td>599.9920000000001</td></tr><tr><td>Leone Emerson</td><td>5779.8175</td></tr><tr><td>Deloris Burke</td><td>19043.9036</td></tr><tr><td>Houston Vasquez</td><td>2699.991</td></tr><tr><td>Earline Ballard</td><td>1599.9840000000002</td></tr><tr><td>Yahaira Robertson</td><td>4784.1587</td></tr><tr><td>Omer Estrada</td><td>7975.972999999999</td></tr><tr><td>Vonda Berger</td><td>7824.040099999999</td></tr><tr><td>Pearlie Cochran</td><td>3347.9813999999997</td></tr><tr><td>Edgar Horn</td><td>847.984</td></tr><tr><td>Deandrea Cox</td><td>4778.0235999999995</td></tr><tr><td>Alden Atkinson</td><td>3484.0719</td></tr><tr><td>America Swanson</td><td>3505.766</td></tr><tr><td>Grace Madden</td><td>1450.023</td></tr><tr><td>Marisol Goodman</td><td>3121.132</td></tr><tr><td>Nicki Fry</td><td>1006.981</td></tr><tr><td>Casimira Chapman</td><td>8200.726700000001</td></tr><tr><td>Brenton Whitaker</td><td>3439.944</td></tr><tr><td>Jong Guthrie</td><td>1891.1125000000002</td></tr><tr><td>Tisha Petty</td><td>1052.972</td></tr><tr><td>Sherie Ayala</td><td>7042.6723999999995</td></tr><tr><td>Aileen Marquez</td><td>4644.9130000000005</td></tr><tr><td>Shasta Combs</td><td>2360.3907</td></tr><tr><td>Ronna Butler</td><td>17240.562299999998</td></tr><tr><td>Debra Burks</td><td>27888.183399999998</td></tr><tr><td>Sharika Colon</td><td>4271.1134</td></tr><tr><td>Amparo Burks</td><td>879.984</td></tr><tr><td>Tina Bush</td><td>3464.0224</td></tr><tr><td>Vernon Knowles</td><td>3121.4817</td></tr><tr><td>Floretta Higgins</td><td>7681.124</td></tr><tr><td>Leila Barr</td><td>3144.327</td></tr><tr><td>Georgetta Hardin</td><td>14877.289</td></tr><tr><td>Anderson Martin</td><td>3900.6587000000004</td></tr><tr><td>Ardelia Cooley</td><td>12334.957</td></tr><tr><td>Stefani Gamble</td><td>6715.433999999999</td></tr><tr><td>Jovita Bishop</td><td>4436.6034</td></tr><tr><td>Leeanne Cross</td><td>1115.9814</td></tr><tr><td>Taylor Cole</td><td>1364.944</td></tr><tr><td>Charlene Norris</td><td>6764.572700000001</td></tr><tr><td>Eun Harris</td><td>660.5905</td></tr><tr><td>Tricia Daniels</td><td>3502.4932</td></tr><tr><td>Ivette Estes</td><td>1399.976</td></tr><tr><td>Le Wood</td><td>3974.6254</td></tr><tr><td>Tanesha Hampton</td><td>2335.5207</td></tr><tr><td>Terese Palmer</td><td>464.9907</td></tr><tr><td>Collen Hayes</td><td>2113.5840000000003</td></tr><tr><td>Anton Barton</td><td>797.9399999999999</td></tr><tr><td>Nevada Hood</td><td>7688.2721</td></tr><tr><td>Myron Johns</td><td>1673.9906999999998</td></tr><tr><td>Ghislaine Compton</td><td>1754.0464000000002</td></tr><tr><td>Carmela Hays</td><td>4186.5267</td></tr><tr><td>Wes Stanton</td><td>423.992</td></tr><tr><td>Tora Dunlap</td><td>5775.5446999999995</td></tr><tr><td>Kandace Hughes</td><td>953.9820000000001</td></tr><tr><td>Margaretta Clayton</td><td>4835.375999999999</td></tr><tr><td>Loyce Conway</td><td>3015.3129</td></tr><tr><td>Lean Stark</td><td>2008.7628</td></tr><tr><td>Margert Stevens</td><td>4851.1372</td></tr><tr><td>Shantae Hammond</td><td>6068.9490000000005</td></tr><tr><td>Santos Valencia</td><td>10719.098799999998</td></tr><tr><td>Andreas Herman</td><td>2754.9905</td></tr><tr><td>Mia Delgado</td><td>527.984</td></tr><tr><td>Hee Greer</td><td>3509.973</td></tr><tr><td>Verda Gilbert</td><td>6349.3634999999995</td></tr><tr><td>Felicidad Golden</td><td>10794.3537</td></tr><tr><td>Alejandrina Hodges</td><td>3447.2278</td></tr><tr><td>Adam Henderson</td><td>3695.4745000000003</td></tr><tr><td>Lizette Ellison</td><td>836.9814</td></tr><tr><td>Lonna Franks</td><td>712.4905</td></tr><tr><td>Sunshine Rosario</td><td>2789.9907</td></tr><tr><td>Consuela Collier</td><td>15455.624999999998</td></tr><tr><td>Annis Sanchez</td><td>4269.9572</td></tr><tr><td>Jaimee Day</td><td>1172.9724</td></tr><tr><td>Jenny Bell</td><td>511.49069999999995</td></tr><tr><td>Ara Vazquez</td><td>4466.6452</td></tr><tr><td>Hue Dalton</td><td>799.9920000000001</td></tr><tr><td>Toya Pratt</td><td>2082.1435</td></tr><tr><td>Milagros Weber</td><td>7130.5405</td></tr><tr><td>Barbra Dickerson</td><td>7520.0371</td></tr><tr><td>Gilberto Sanders</td><td>4497.0048</td></tr><tr><td>Kanesha Hudson</td><td>225.89100000000002</td></tr><tr><td>Venessa Frost</td><td>1279.0627</td></tr><tr><td>Mable Pratt</td><td>6912.171499999999</td></tr><tr><td>Tonisha Fowler</td><td>9399.965</td></tr><tr><td>Sheryl Chase</td><td>17086.934299999997</td></tr><tr><td>Ashlee Pena</td><td>17305.9384</td></tr><tr><td>Leigh Burke</td><td>7022.9623999999985</td></tr><tr><td>Caleb England</td><td>7339.4195</td></tr><tr><td>Herta Rollins</td><td>4464.6642</td></tr><tr><td>Reatha Perez</td><td>13130.8288</td></tr><tr><td>Syreeta Hendricks</td><td>11979.946699999999</td></tr><tr><td>Lavonda Stephenson</td><td>2208.9745</td></tr><tr><td>Klara Kim</td><td>1804.8564999999999</td></tr><tr><td>Christia Carson</td><td>3658.1809999999996</td></tr><tr><td>Carolyne Conley</td><td>1692.5720999999999</td></tr><tr><td>Virgina Berg</td><td>5154.1467</td></tr><tr><td>Elvia Cardenas</td><td>6978.715099999999</td></tr><tr><td>Delmar Wise</td><td>15439.946799999998</td></tr><tr><td>Doreatha Ford</td><td>959.984</td></tr><tr><td>Boyce Burks</td><td>1600.0929999999998</td></tr><tr><td>Petronila Gallegos</td><td>2719.4764</td></tr><tr><td>Elnora Simpson</td><td>15416.1565</td></tr><tr><td>Ivonne Yang</td><td>2371.1623999999997</td></tr><tr><td>Zina Bonner</td><td>5660.9369</td></tr><tr><td>Delila Hamilton</td><td>10869.9637</td></tr><tr><td>Lidia Ashley</td><td>9704.9449</td></tr><tr><td>Toshia Cardenas</td><td>3935.9680000000008</td></tr><tr><td>Laci Castro</td><td>1349.982</td></tr><tr><td>Quyen Houston</td><td>5537.981699999999</td></tr><tr><td>Ayanna Cherry</td><td>16950.076999999997</td></tr><tr><td>Alesia Horne</td><td>2787.9590000000003</td></tr><tr><td>Selene Austin</td><td>5382.0464</td></tr><tr><td>Jesica Fields</td><td>1800.4814999999999</td></tr><tr><td>Willian Hardin</td><td>845.9820000000001</td></tr><tr><td>Collen Dennis</td><td>4195.3079</td></tr><tr><td>Carson Macias</td><td>7747.739</td></tr><tr><td>Kasha Todd</td><td>19329.084899999998</td></tr><tr><td>Lise Hebert</td><td>5015.7377</td></tr><tr><td>Damien Dorsey</td><td>21514.461499999998</td></tr><tr><td>Sarah Kirkland</td><td>4387.966</td></tr><tr><td>Chauncey Donaldson</td><td>4762.4631</td></tr><tr><td>Alejandro Norman</td><td>2509.881</td></tr><tr><td>Jasmin Young</td><td>10336.9624</td></tr><tr><td>Ciera Koch</td><td>5557.3307</td></tr><tr><td>Daryl Spence</td><td>21150.892700000004</td></tr><tr><td>Stephanie Browning</td><td>104.4905</td></tr><tr><td>Dorothea Miranda</td><td>3243.7533999999996</td></tr><tr><td>Zoraida Patton</td><td>7004.841</td></tr><tr><td>Dottie Roberts</td><td>6654.473400000001</td></tr><tr><td>Ileana Holt</td><td>4499.991</td></tr><tr><td>Roy Chan</td><td>2717.964</td></tr><tr><td>Ashanti Parks</td><td>16025.0715</td></tr><tr><td>Shara Pope</td><td>5959.0657</td></tr><tr><td>Carmelina Sellers</td><td>7157.3531</td></tr><tr><td>Danny Kim</td><td>11055.941</td></tr><tr><td>Dale Rasmussen</td><td>4167.846</td></tr><tr><td>Marquerite Dawson</td><td>8072.331</td></tr><tr><td>Michel Blankenship</td><td>2500.4381000000003</td></tr><tr><td>Phillis Fowler</td><td>335.98400000000004</td></tr><tr><td>Elma Molina</td><td>7111.0354</td></tr><tr><td>Tereasa Bird</td><td>10617.973</td></tr><tr><td>Zelma Browning</td><td>21535.666499999996</td></tr><tr><td>Ashely Holmes</td><td>391.992</td></tr><tr><td>Collin Webster</td><td>861.0117</td></tr><tr><td>Donnetta Henson</td><td>3860.1454000000003</td></tr><tr><td>Angelika Perry</td><td>2319.7539</td></tr><tr><td>Kathyrn Bush</td><td>2011.4626</td></tr><tr><td>Lore Sykes</td><td>3390.4649999999997</td></tr><tr><td>Dwain Carlson</td><td>8309.4449</td></tr><tr><td>Jennell Solis</td><td>391.992</td></tr><tr><td>Maple Griffin</td><td>1856.6117</td></tr><tr><td>Hubert Stone</td><td>10541.963199999998</td></tr><tr><td>Bettyann Acosta</td><td>611.9820000000001</td></tr><tr><td>Moira Lester</td><td>6196.644399999999</td></tr><tr><td>Elenore William</td><td>4334.0585</td></tr><tr><td>Bernetta Marquez</td><td>10322.972099999999</td></tr><tr><td>Pamala Fowler</td><td>3146.4644999999996</td></tr><tr><td>Maximina Hutchinson</td><td>2230.5485</td></tr><tr><td>Klara Stanley</td><td>16436.065000000002</td></tr><tr><td>Lanie Dunn</td><td>3531.3039</td></tr><tr><td>Jeni Booker</td><td>6235.5381</td></tr><tr><td>Caroll Hays</td><td>1571.1760000000002</td></tr><tr><td>Kendra Harrington</td><td>4171.947899999999</td></tr><tr><td>Thalia Dillard</td><td>16764.1256</td></tr><tr><td>Holly Nieves</td><td>1601.3717</td></tr><tr><td>Shonta Mercer</td><td>723.8905</td></tr><tr><td>Lena Mills</td><td>751.984</td></tr><tr><td>Charleen Joyner</td><td>1585.156</td></tr><tr><td>Vernita Ball</td><td>269.99100000000004</td></tr><tr><td>Yan Mcgowan</td><td>13546.9484</td></tr><tr><td>Maryalice Henry</td><td>4064.8377</td></tr><tr><td>Flossie Holder</td><td>10269.8557</td></tr><tr><td>Freddie Mathis</td><td>1755.3725</td></tr><tr><td>Hilary Savage</td><td>1652.981</td></tr><tr><td>Scarlet Reed</td><td>4147.662</td></tr><tr><td>Nita Guy</td><td>9372.3701</td></tr><tr><td>Ann Heath</td><td>6468.2263</td></tr><tr><td>Kimberely Bowen</td><td>15087.2644</td></tr><tr><td>Sommer Hopkins</td><td>1256.091</td></tr><tr><td>Joe Melton</td><td>269.99100000000004</td></tr><tr><td>Kattie Stevenson</td><td>2681.1565</td></tr><tr><td>Susann Bass</td><td>1001.6116999999999</td></tr><tr><td>Khalilah Robertson</td><td>2362.1628</td></tr><tr><td>Shiloh Bates</td><td>6330.574699999999</td></tr><tr><td>Wm Pope</td><td>930.981</td></tr><tr><td>Giselle Robles</td><td>692.0817</td></tr><tr><td>Alysia Nicholson</td><td>5126.9531</td></tr><tr><td>Tuyet Rosa</td><td>5841.099200000001</td></tr><tr><td>Ramiro Byers</td><td>376.79200000000003</td></tr><tr><td>Bettie Pierce</td><td>8392.9437</td></tr><tr><td>Manie Maxwell</td><td>1546.384</td></tr><tr><td>Angella Bridges</td><td>4062.3333999999995</td></tr><tr><td>Dorthey Jackson</td><td>12026.9409</td></tr><tr><td>Jennette Baker</td><td>583.9760000000001</td></tr><tr><td>Janella Bright</td><td>513.3507</td></tr><tr><td>Kenton Hughes</td><td>2006.0629</td></tr><tr><td>Yevette Elliott</td><td>12104.786</td></tr><tr><td>Jonna Brown</td><td>1394.9906999999998</td></tr><tr><td>Yu Mcdonald</td><td>6804.958</td></tr><tr><td>Shu Mays</td><td>8056.768000000001</td></tr><tr><td>Lolita Mosley</td><td>6680.4439</td></tr><tr><td>Blanca Hooper</td><td>6602.950500000001</td></tr><tr><td>Joni Lee</td><td>422.99100000000004</td></tr><tr><td>Carita Salinas</td><td>10792.247</td></tr><tr><td>Trudy Riddle</td><td>4214.9468</td></tr><tr><td>Jama Rodriquez</td><td>1818.4544999999998</td></tr><tr><td>Kandi Mcneil</td><td>1847.0647</td></tr><tr><td>Donette Mccarthy</td><td>9274.9654</td></tr><tr><td>Magda Eaton</td><td>723.8905</td></tr><tr><td>Collene Knox</td><td>12541.763399999998</td></tr><tr><td>Nestor Haynes</td><td>1860.5825</td></tr><tr><td>Latricia Lindsey</td><td>1174.5654</td></tr><tr><td>Nichelle Rosario</td><td>6824.972399999999</td></tr><tr><td>Julius Holt</td><td>3489.9734000000003</td></tr><tr><td>Gertha Mejia</td><td>8109.950500000001</td></tr><tr><td>Florencio Davenport</td><td>3191.9524999999994</td></tr><tr><td>Shonta Preston</td><td>5801.933999999999</td></tr><tr><td>Chere Alston</td><td>1139.962</td></tr><tr><td>Jenise Preston</td><td>751.984</td></tr><tr><td>Candelaria Coffey</td><td>14735.4152</td></tr><tr><td>Ana Palmer</td><td>4100.4358999999995</td></tr><tr><td>Paul Lester</td><td>17580.7168</td></tr><tr><td>Conchita Boone</td><td>5851.9257</td></tr><tr><td>Chi Goff</td><td>3441.2631</td></tr><tr><td>Yanira Bradshaw</td><td>9157.756</td></tr><tr><td>Armando Black</td><td>2843.0734</td></tr><tr><td>Letitia Franco</td><td>12433.4557</td></tr><tr><td>Vince Schneider</td><td>8204.530200000001</td></tr><tr><td>Winfred Harris</td><td>3804.9214000000006</td></tr><tr><td>Lenore Valdez</td><td>8009.032099999999</td></tr><tr><td>Geraldine O'donnell</td><td>1441.165</td></tr><tr><td>Larraine Horn</td><td>5017.855099999999</td></tr><tr><td>Patrina Tanner</td><td>4539.974</td></tr><tr><td>Georgeann Rojas</td><td>3818.2124000000003</td></tr><tr><td>Evelina Byrd</td><td>1754.1460000000002</td></tr><tr><td>Nanette Roman</td><td>2259.3406999999997</td></tr><tr><td>Shanti Johnston</td><td>1863.966</td></tr><tr><td>Annett Garrett</td><td>4156.6929</td></tr><tr><td>Claris Santiago</td><td>5231.8529</td></tr><tr><td>Clementine Mooney</td><td>199.99200000000002</td></tr><tr><td>Carola Mcpherson</td><td>396.1405</td></tr><tr><td>Agustina Lawrence</td><td>2283.8072</td></tr><tr><td>Clementina Sargent</td><td>1208.4825</td></tr><tr><td>Gwendolyn Miller</td><td>11349.9574</td></tr><tr><td>Giovanna Jefferson</td><td>377.982</td></tr><tr><td>Pamelia Newman</td><td>33634.2604</td></tr><tr><td>Bennett Armstrong</td><td>3347.648</td></tr><tr><td>Brittni Green</td><td>8570.9665</td></tr><tr><td>Dionne Norris</td><td>6261.957399999999</td></tr><tr><td>Ira Moore</td><td>1402.7740000000001</td></tr><tr><td>Luciano Marsh</td><td>1999.3494</td></tr><tr><td>Shiloh Reeves</td><td>1950.5750000000003</td></tr><tr><td>Karl Stephens</td><td>5745.955199999999</td></tr><tr><td>Kerrie O'neill</td><td>1139.981</td></tr><tr><td>Rosanne George</td><td>3750.873199999999</td></tr><tr><td>Marina Hinton</td><td>1885.8838999999998</td></tr><tr><td>Sherita Cherry</td><td>719.984</td></tr><tr><td>Siobhan Lang</td><td>6793.9655</td></tr><tr><td>Eliseo Knight</td><td>5220.4734</td></tr><tr><td>Novella Ross</td><td>12307.9627</td></tr><tr><td>Collene Roman</td><td>6578.9654</td></tr><tr><td>Hipolito Padilla</td><td>5062.3384</td></tr><tr><td>Dung King</td><td>4115.9724</td></tr><tr><td>Season Harvey</td><td>3185.9454</td></tr><tr><td>Macie Ayers</td><td>9334.509399999999</td></tr><tr><td>Loraine Sykes</td><td>3960.4315000000006</td></tr><tr><td>Larae Carney</td><td>10187.945099999999</td></tr><tr><td>Marilyn Frank</td><td>9499.981</td></tr><tr><td>Rudolf Moran</td><td>4017.4401</td></tr><tr><td>Angelique Merrill</td><td>333.59200000000004</td></tr><tr><td>Sanora Webster</td><td>3442.8135</td></tr><tr><td>Gabriella Jones</td><td>999.4825000000001</td></tr><tr><td>Gilberte Duke</td><td>13107.441</td></tr><tr><td>Carissa Foreman</td><td>170.991</td></tr><tr><td>Kermit Hyde</td><td>908.076</td></tr><tr><td>Arminda Weber</td><td>1044.981</td></tr><tr><td>Sandee Alvarado</td><td>799.9920000000001</td></tr><tr><td>Kam Wilder</td><td>4094.8481</td></tr><tr><td>Valentin Mclaughlin</td><td>4001.9184</td></tr><tr><td>Lashawna Richardson</td><td>11596.428899999999</td></tr><tr><td>Charlesetta Soto</td><td>3302.1734</td></tr><tr><td>Jesus Burch</td><td>7063.463899999999</td></tr><tr><td>Nathanael Bradley</td><td>377.982</td></tr><tr><td>Elease Dejesus</td><td>1217.264</td></tr><tr><td>Marcell Barrett</td><td>1197.0725</td></tr><tr><td>Lurlene Finch</td><td>1829.6654999999998</td></tr><tr><td>Louanne Martin</td><td>6450.952899999999</td></tr><tr><td>Domingo Casey</td><td>1311.2907</td></tr><tr><td>Felica Munoz</td><td>10186.628499999999</td></tr><tr><td>Miranda Kennedy</td><td>3254.9906999999994</td></tr><tr><td>Kandace Giles</td><td>3247.248</td></tr><tr><td>Virgen Clemons</td><td>7184.972399999999</td></tr><tr><td>Marcy Rodriguez</td><td>845.9820000000001</td></tr><tr><td>Trena Hudson</td><td>9287.9439</td></tr><tr><td>Nelle Beck</td><td>4012.6457</td></tr><tr><td>Dane Mcdaniel</td><td>2205.7557</td></tr><tr><td>Debbra Jacobson</td><td>1194.2817</td></tr><tr><td>Moses Pope</td><td>11471.895400000001</td></tr><tr><td>Ross Pugh</td><td>3032.7401</td></tr><tr><td>Mercy Brown</td><td>6239.278700000001</td></tr><tr><td>Coleman Boyd</td><td>6412.5547</td></tr><tr><td>Edythe Valencia</td><td>10949.946799999998</td></tr><tr><td>Sheree Pena</td><td>3022.8714999999997</td></tr><tr><td>Erlinda Humphrey</td><td>11588.6474</td></tr><tr><td>Delma Bailey</td><td>5984.981</td></tr><tr><td>Chantell Bridges</td><td>11993.972</td></tr><tr><td>Garry Juarez</td><td>1805.9660000000001</td></tr><tr><td>Edmund Gaines</td><td>989.9820000000001</td></tr><tr><td>Miriam Baker</td><td>3723.8275</td></tr><tr><td>Aimee Merritt</td><td>8096.4455</td></tr><tr><td>Laure Pena</td><td>16890.1469</td></tr><tr><td>Sally Kinney</td><td>1285.9717</td></tr><tr><td>Obdulia Barber</td><td>543.984</td></tr><tr><td>Inga Koch</td><td>418.4907</td></tr><tr><td>Elanor Patrick</td><td>2136.531</td></tr><tr><td>Bridgette Guerra</td><td>16935.6408</td></tr><tr><td>Josef Greer</td><td>5925.560100000001</td></tr><tr><td>Renita Henry</td><td>5442.0740000000005</td></tr><tr><td>Samual Warner</td><td>15876.4261</td></tr><tr><td>Mi Gray</td><td>9728.9827</td></tr><tr><td>Loan Graham</td><td>2228.2451</td></tr><tr><td>Deane Sears</td><td>5887.3423999999995</td></tr><tr><td>Lorraine Marks</td><td>14141.339399999999</td></tr><tr><td>Eliana Reese</td><td>11035.847999999998</td></tr><tr><td>Janine Manning</td><td>7783.4219</td></tr><tr><td>Luz House</td><td>9425.166799999999</td></tr><tr><td>Kerrie Morton</td><td>2282.965</td></tr><tr><td>Sharla Flynn</td><td>1729.775</td></tr><tr><td>Cassondra Pruitt</td><td>269.99100000000004</td></tr><tr><td>Graig Cannon</td><td>4369.3445</td></tr><tr><td>Rudolf Gilliam</td><td>2747.2394999999997</td></tr><tr><td>Zella Fernandez</td><td>1422.963</td></tr><tr><td>Doris Kaufman</td><td>3167.9562</td></tr><tr><td>Judith Finley</td><td>4397.9639</td></tr><tr><td>Luciana Mcgee</td><td>167.99200000000002</td></tr><tr><td>Chloe Patel</td><td>1367.0907</td></tr><tr><td>Rutha Howell</td><td>7143.6644</td></tr><tr><td>Tajuana Riddle</td><td>4205.981699999999</td></tr><tr><td>Novella Patel</td><td>5107.863799999999</td></tr><tr><td>Ehtel Cobb</td><td>3105.9644</td></tr><tr><td>Romana Barnes</td><td>1094.9750000000001</td></tr><tr><td>Agatha Melton</td><td>1258.972</td></tr><tr><td>Jayne Kirkland</td><td>10802.6294</td></tr><tr><td>Conrad Mueller</td><td>5925.474700000001</td></tr><tr><td>Mariana Strong</td><td>2317.0840000000003</td></tr><tr><td>Lee Dunn</td><td>12980.938699999999</td></tr><tr><td>Stephen Vega</td><td>912.2729999999999</td></tr><tr><td>Myron Ruiz</td><td>7350.4645</td></tr><tr><td>Abram Copeland</td><td>24607.0261</td></tr><tr><td>Tressa Weiss</td><td>6749.973399999999</td></tr><tr><td>Douglas Richards</td><td>417.9905</td></tr><tr><td>Alita Salinas</td><td>2099.9637000000002</td></tr><tr><td>Corrina Sawyer</td><td>25612.7021</td></tr><tr><td>Mellisa Farley</td><td>1096.1817</td></tr><tr><td>Melanie Hayes</td><td>31913.690199999997</td></tr><tr><td>Walton Dejesus</td><td>3011.4809999999998</td></tr><tr><td>Hugh Craft</td><td>1856.0750000000003</td></tr><tr><td>Chasidy Webster</td><td>959.984</td></tr><tr><td>Genny Hensley</td><td>4507.6134</td></tr><tr><td>Carter Bentley</td><td>4318.0054</td></tr><tr><td>Daphine Willis</td><td>927.9840000000002</td></tr><tr><td>Jone Bernard</td><td>12010.4969</td></tr><tr><td>Loreta Johnston</td><td>14172.218499999999</td></tr><tr><td>Andreas Mayer</td><td>18114.9309</td></tr><tr><td>Myesha Burgess</td><td>5226.6626</td></tr><tr><td>Skye Pope</td><td>3159.926</td></tr><tr><td>Rosalva Hamilton</td><td>10529.963</td></tr><tr><td>Nicholas Vazquez</td><td>5224.9905</td></tr><tr><td>Tamela Harrell</td><td>17479.957000000002</td></tr><tr><td>Arvilla Weiss</td><td>3015.9718999999996</td></tr><tr><td>Nicki Larson</td><td>557.9814</td></tr><tr><td>Ashleigh Frank</td><td>5219.982</td></tr><tr><td>Phebe Turner</td><td>11120.3254</td></tr><tr><td>Annabelle Hebert</td><td>3287.322</td></tr><tr><td>Camila Carroll</td><td>3292.0046</td></tr><tr><td>Shona Mcmillan</td><td>6089.983</td></tr><tr><td>Rita Bailey</td><td>2701.1742</td></tr><tr><td>Genoveva Lloyd</td><td>5333.335</td></tr><tr><td>Lizzie Joyner</td><td>18995.013700000003</td></tr><tr><td>Marissa Summers</td><td>1556.7828</td></tr><tr><td>Zona Cameron</td><td>2696.9907</td></tr><tr><td>Augustus Steele</td><td>519.984</td></tr><tr><td>Jeni Farley</td><td>377.982</td></tr><tr><td>Leif Short</td><td>877.9812</td></tr><tr><td>Ebony Cotton</td><td>2333.356</td></tr><tr><td>Mila Moody</td><td>12595.073</td></tr><tr><td>Cecelia Gill</td><td>1101.683</td></tr><tr><td>Corinna Adams</td><td>9161.946</td></tr><tr><td>Londa Gould</td><td>6782.3368</td></tr><tr><td>Claudio Wise</td><td>3646.9826999999996</td></tr><tr><td>Cindi Larson</td><td>20177.7457</td></tr><tr><td>Julienne Moody</td><td>1277.9660000000001</td></tr><tr><td>Lavinia Cotton</td><td>753.5840000000001</td></tr><tr><td>Myrl Gay</td><td>2474.9727</td></tr><tr><td>Alfredo Dodson</td><td>4766.8345</td></tr><tr><td>Raphael O'neil</td><td>2509.946</td></tr><tr><td>Romeo Steele</td><td>4922.9485</td></tr><tr><td>Bettie Glover</td><td>8740.966</td></tr><tr><td>Cecilia Camacho</td><td>7971.2261</td></tr><tr><td>Dollie Cervantes</td><td>11238.6544</td></tr><tr><td>Vito Pickett</td><td>6754.9376</td></tr><tr><td>Victor Pittman</td><td>2991.759</td></tr><tr><td>Effie Jenkins</td><td>5768.214400000001</td></tr><tr><td>Vernell Goff</td><td>1902.5629</td></tr><tr><td>Jeanie Kirkland</td><td>15841.0992</td></tr><tr><td>Honey Camacho</td><td>2200.8641</td></tr><tr><td>Deandrea Vega</td><td>3172.4449</td></tr><tr><td>Lolita O'neill</td><td>2452.948</td></tr><tr><td>Hermila Mckay</td><td>5498.3679999999995</td></tr><tr><td>Vicki Wiggins</td><td>6074.048199999999</td></tr><tr><td>Harold O'connor</td><td>9725.8374</td></tr><tr><td>Krystin Marshall</td><td>1613.3947</td></tr><tr><td>Basil Ballard</td><td>1553.965</td></tr><tr><td>Beryl Bennett</td><td>1301.4715</td></tr><tr><td>Catherine Miles</td><td>1635.5468</td></tr><tr><td>Darcie Morgan</td><td>1567.173</td></tr><tr><td>Cyndi Dyer</td><td>1655.0719</td></tr><tr><td>Lewis Garner</td><td>3818.2929999999997</td></tr><tr><td>Tonda Armstrong</td><td>7179.9832</td></tr><tr><td>Penni Best</td><td>4162.8555</td></tr><tr><td>Marlo Jefferson</td><td>13242.962</td></tr><tr><td>Ulrike Chan</td><td>1499.382</td></tr><tr><td>Myung Hooper</td><td>2681.957</td></tr><tr><td>Olimpia Mays</td><td>12774.245099999998</td></tr><tr><td>Lina Meadows</td><td>3720.8885</td></tr><tr><td>Arie Hunter</td><td>1287.5737000000001</td></tr><tr><td>Patsy Russo</td><td>1060.1721</td></tr><tr><td>Travis Goodman</td><td>2446.941</td></tr><tr><td>Eric Hardin</td><td>2065.9827</td></tr><tr><td>Babara Ochoa</td><td>2963.9809999999998</td></tr><tr><td>Oliva Blackwell</td><td>6382.9455</td></tr><tr><td>India Barron</td><td>2873.9400000000005</td></tr><tr><td>Jasper Castro</td><td>557.9814</td></tr><tr><td>Nettie Mcdaniel</td><td>3801.6487</td></tr><tr><td>Barry Buckner</td><td>1467.9554</td></tr><tr><td>Edra Fitzgerald</td><td>2297.7574999999997</td></tr><tr><td>Herlinda Stone</td><td>7067.962799999998</td></tr><tr><td>Tisa Whitney</td><td>3196.2044</td></tr><tr><td>Vashti Rosario</td><td>9865.4727</td></tr><tr><td>Kellye Campbell</td><td>6829.531</td></tr><tr><td>Tama Berg</td><td>2966.6441999999997</td></tr><tr><td>Rona Rojas</td><td>7439.981399999999</td></tr><tr><td>Cherelle Key</td><td>1052.9630000000002</td></tr><tr><td>Cheree Hale</td><td>5122.348</td></tr><tr><td>Dannette Guerrero</td><td>7719.957</td></tr><tr><td>Crystle Gilliam</td><td>4296.181500000001</td></tr><tr><td>Shea Howell</td><td>2319.9680000000003</td></tr><tr><td>Emmett Casey</td><td>3194.082</td></tr><tr><td>Soledad Moses</td><td>3168.5541</td></tr><tr><td>Elaina Key</td><td>6929.1049</td></tr><tr><td>Mica Barry</td><td>279.992</td></tr><tr><td>Cassie Cline</td><td>6987.248700000001</td></tr><tr><td>Carina Lynch</td><td>2707.8278</td></tr><tr><td>Marlen Dawson</td><td>2932.4811999999997</td></tr><tr><td>Heather Perry</td><td>718.4000000000001</td></tr><tr><td>Mellisa Griffin</td><td>10050.6281</td></tr><tr><td>Tomasa Carson</td><td>16338.9384</td></tr><tr><td>Jamika Acevedo</td><td>269.99100000000004</td></tr><tr><td>Georgina Gonzales</td><td>5417.9727</td></tr><tr><td>Ciera Webb</td><td>629.9820000000001</td></tr><tr><td>Morton Lee</td><td>3290.7715</td></tr><tr><td>Sherril Alvarado</td><td>5723.7441</td></tr><tr><td>Ilda Roberson</td><td>2379.4635</td></tr><tr><td>Dorine Roberson</td><td>12320.120700000001</td></tr><tr><td>Felice Guzman</td><td>10156.896799999999</td></tr><tr><td>Jutta Everett</td><td>1127.992</td></tr><tr><td>Romelia Myers</td><td>5440.362399999999</td></tr><tr><td>Florrie Little</td><td>9919.921</td></tr><tr><td>Damian Dawson</td><td>2069.3725</td></tr><tr><td>Cleopatra Tate</td><td>12909.9214</td></tr><tr><td>Berna Moore</td><td>949.9905</td></tr><tr><td>Serina Hensley</td><td>1690.6635</td></tr><tr><td>Ricki Bullock</td><td>7183.3227</td></tr><tr><td>Lyndsey Bean</td><td>32675.072499999995</td></tr><tr><td>Jenniffer Bullock</td><td>17746.5951</td></tr><tr><td>Marylyn Browning</td><td>655.1907</td></tr><tr><td>Shawnna Frank</td><td>2705.007</td></tr><tr><td>Luis Tyler</td><td>2749.3474</td></tr><tr><td>Crysta Velez</td><td>3567.561</td></tr><tr><td>Regenia Vaughan</td><td>14529.258299999998</td></tr><tr><td>Raul Melendez</td><td>2770.9629999999997</td></tr><tr><td>Barbera Riggs</td><td>7486.3314</td></tr><tr><td>Courtney Wyatt</td><td>7823.944000000001</td></tr><tr><td>Lise Alvarado</td><td>576.7917</td></tr><tr><td>Emelda Dickerson</td><td>1422.4825</td></tr><tr><td>Delaine Estes</td><td>799.984</td></tr><tr><td>Nikita Roy</td><td>1611.0747000000001</td></tr><tr><td>Deshawn Mendoza</td><td>3690.2361</td></tr><tr><td>Sharell Ross</td><td>3594.863</td></tr><tr><td>Tangela Quinn</td><td>9205.1175</td></tr><tr><td>Dexter Roberts</td><td>2963.9809999999998</td></tr><tr><td>Chantay Maynard</td><td>7327.040100000001</td></tr><tr><td>Martha Burgess</td><td>1227.5814</td></tr><tr><td>Cori Schwartz</td><td>12400.848</td></tr><tr><td>Jerri Henry</td><td>1576.7820000000002</td></tr><tr><td>Consuela Romero</td><td>1599.9840000000002</td></tr><tr><td>Renna Williams</td><td>7021.1487</td></tr><tr><td>Hope Cotton</td><td>1238.566</td></tr><tr><td>Lucio Sherman</td><td>6672.2946999999995</td></tr><tr><td>Kermit Bowman</td><td>7253.619500000001</td></tr><tr><td>Efren Whitfield</td><td>3110.8567000000003</td></tr><tr><td>Mikel Wilkerson</td><td>351.992</td></tr><tr><td>Phuong Wolf</td><td>5686.5815</td></tr><tr><td>Shiela Calderon</td><td>2768.3634</td></tr><tr><td>Renato Morton</td><td>2716.7650000000003</td></tr><tr><td>Wynona Douglas</td><td>16491.52</td></tr><tr><td>Jeffry Church</td><td>1512.891</td></tr><tr><td>Whitley Cannon</td><td>3975.2343</td></tr><tr><td>Lloyd Miranda</td><td>170.991</td></tr><tr><td>Bea Kane</td><td>2643.2447</td></tr><tr><td>Trista Lambert</td><td>5922.4725</td></tr><tr><td>Mina Carrillo</td><td>6671.6012</td></tr><tr><td>Glady Wells</td><td>325.4907</td></tr><tr><td>Genny Fields</td><td>2615.976</td></tr><tr><td>Trinity Riddle</td><td>7211.723399999999</td></tr><tr><td>Margret Barnett</td><td>11831.3359</td></tr><tr><td>Deangelo Cooley</td><td>314.99100000000004</td></tr><tr><td>Lashunda Cole</td><td>6591.976000000001</td></tr><tr><td>Aide Franco</td><td>2605.2824</td></tr><tr><td>Kaylee English</td><td>4775.9635</td></tr><tr><td>Inocencia Key</td><td>4949.991</td></tr><tr><td>Delana Wagner</td><td>1464.2552</td></tr><tr><td>Alyse Jacobson</td><td>11062.4171</td></tr><tr><td>Aleta Stone</td><td>418.4907</td></tr><tr><td>Randee Lester</td><td>700.792</td></tr><tr><td>Penny Acevedo</td><td>18670.9288</td></tr><tr><td>Tu Ramirez</td><td>6467.6551</td></tr><tr><td>Somer Jordan</td><td>12663.956</td></tr><tr><td>Adena Blake</td><td>19329.9492</td></tr><tr><td>Oralia Farley</td><td>5893.554999999999</td></tr><tr><td>Gustavo Gamble</td><td>4204.525799999999</td></tr><tr><td>Janae Doyle</td><td>3920.663</td></tr><tr><td>Parthenia Holman</td><td>15205.928399999999</td></tr><tr><td>Benito Hendrix</td><td>9645.3834</td></tr><tr><td>Pinkie Kirkland</td><td>11476.536399999999</td></tr><tr><td>Krissy Ochoa</td><td>4814.6255</td></tr><tr><td>Yang Giles</td><td>5244.955</td></tr><tr><td>Pearl Fox</td><td>1494.9554</td></tr><tr><td>Sherilyn Wilcox</td><td>2411.4715</td></tr><tr><td>Alissa Hood</td><td>14567.157</td></tr><tr><td>Katelin Kennedy</td><td>7568.9310000000005</td></tr><tr><td>Wendie Nash</td><td>3950.3624</td></tr><tr><td>Margorie Wynn</td><td>8498.463</td></tr><tr><td>Buford Gilbert</td><td>9044.927</td></tr><tr><td>Diana Reyes</td><td>1064.682</td></tr><tr><td>Kate Barber</td><td>6495.972</td></tr><tr><td>Rozella Fitzgerald</td><td>480.591</td></tr><tr><td>Ivelisse Nixon</td><td>10951.5614</td></tr><tr><td>Cristobal Hutchinson</td><td>1716.5529999999999</td></tr><tr><td>Marjory Leonard</td><td>6723.0765</td></tr><tr><td>Tammy Austin</td><td>13765.5468</td></tr><tr><td>Sherise Mercer</td><td>1619.991</td></tr><tr><td>Hilde Nieves</td><td>4459.2184</td></tr><tr><td>Willow Gardner</td><td>2190.566</td></tr><tr><td>Sonja Walls</td><td>176.6907</td></tr><tr><td>Jenna Saunders</td><td>993.2213999999999</td></tr><tr><td>Lamar Greer</td><td>2511.4647000000004</td></tr><tr><td>Eloisa Tucker</td><td>3377.973</td></tr><tr><td>Dorine Thornton</td><td>2834.8444</td></tr><tr><td>Malisa Mitchell</td><td>7575.3454</td></tr><tr><td>Kim Clark</td><td>2664.9644</td></tr><tr><td>Majorie Glover</td><td>1899.981</td></tr><tr><td>Trang Hardin</td><td>5732.4652</td></tr><tr><td>Devin Shaffer</td><td>1389.772</td></tr><tr><td>Tad Gardner</td><td>2195.5747</td></tr><tr><td>Julia Joyner</td><td>3995.6247000000003</td></tr><tr><td>Rodrigo Durham</td><td>1037.3715</td></tr><tr><td>Lucilla Williams</td><td>949.1727000000001</td></tr><tr><td>Joy Underwood</td><td>989.9820000000001</td></tr><tr><td>Brianne Hays</td><td>3722.9829999999997</td></tr><tr><td>Kathie Freeman</td><td>3962.0287</td></tr><tr><td>Coleen Navarro</td><td>10728.4385</td></tr><tr><td>Ocie Slater</td><td>7999.962999999999</td></tr><tr><td>Lillia Gillespie</td><td>4130.3445</td></tr><tr><td>Tilda Melton</td><td>1063.8921</td></tr><tr><td>Virgil Frost</td><td>1026.7014</td></tr><tr><td>Jule Davenport</td><td>4298.4537</td></tr><tr><td>Tonja Bean</td><td>8787.1297</td></tr><tr><td>Edris Barrett</td><td>17494.9405</td></tr><tr><td>Alejandro Haney</td><td>16846.953999999998</td></tr><tr><td>Shay Stephenson</td><td>3671.7054</td></tr><tr><td>Neida King</td><td>1590.8534</td></tr><tr><td>Dori Alvarez</td><td>1949.6365</td></tr><tr><td>Gussie Harding</td><td>1595.6657</td></tr><tr><td>Monty Frost</td><td>13947.544899999999</td></tr><tr><td>Caroline Jenkins</td><td>170.991</td></tr><tr><td>Tobie Little</td><td>17123.997499999998</td></tr><tr><td>Agnes Sims</td><td>2891.7542000000003</td></tr><tr><td>Keturah Reid</td><td>7091.936699999999</td></tr><tr><td>Desiree Branch</td><td>466.84139999999996</td></tr><tr><td>Hye Mercer</td><td>440.99100000000004</td></tr><tr><td>Tempie Jacobson</td><td>7049.673</td></tr><tr><td>Wai Soto</td><td>4912.157</td></tr><tr><td>Mary Singleton</td><td>1536.1215</td></tr><tr><td>Arline Lawson</td><td>7995.8047</td></tr><tr><td>Karole Alvarez</td><td>7159.9556999999995</td></tr><tr><td>Valeri Marshall</td><td>5834.1357</td></tr><tr><td>Janelle Maldonado</td><td>1353.748</td></tr><tr><td>Ira Erickson</td><td>12392.9547</td></tr><tr><td>Brittney Woodward</td><td>11035.7581</td></tr><tr><td>Ken Charles</td><td>9833.6547</td></tr><tr><td>Douglass Blankenship</td><td>1951.3474</td></tr><tr><td>Adrien Hunter</td><td>1234.9715</td></tr><tr><td>Bong Hebert</td><td>14208.388099999998</td></tr><tr><td>Molly Langley</td><td>814.6707</td></tr><tr><td>Vance Taylor</td><td>697.4907</td></tr><tr><td>Barton Crosby</td><td>7526.036700000001</td></tr><tr><td>Shanelle Anderson</td><td>507.2905</td></tr><tr><td>Eliz Whitney</td><td>1662.0538999999999</td></tr><tr><td>Cesar Jackson</td><td>11705.851999999999</td></tr><tr><td>Candis Harding</td><td>2548.9732</td></tr><tr><td>Antony Atkinson</td><td>208.981</td></tr><tr><td>Tam Fisher</td><td>3439.1719</td></tr><tr><td>Piedad Irwin</td><td>706.7814</td></tr><tr><td>Risa Gallagher</td><td>4445.0608999999995</td></tr><tr><td>Anya Contreras</td><td>1497.4827</td></tr><tr><td>Cami Williamson</td><td>1233.6722</td></tr><tr><td>Qiana Jackson</td><td>1988.0501</td></tr><tr><td>Lekisha Pope</td><td>527.7812</td></tr><tr><td>Andria Rivers</td><td>4327.0254</td></tr><tr><td>Lizzette Stein</td><td>16739.995799999997</td></tr><tr><td>Elenore Hensley</td><td>4789.734799999999</td></tr><tr><td>Willis Randolph</td><td>2899.4846</td></tr><tr><td>Celestine Kent</td><td>10998.0295</td></tr><tr><td>Nathalie Knowles</td><td>4231.121999999999</td></tr><tr><td>Letisha May</td><td>9927.2049</td></tr><tr><td>Verdell Joyner</td><td>1567.4715</td></tr><tr><td>Philip Bryan</td><td>1368.0717</td></tr><tr><td>Gilbert Calhoun</td><td>15097.905999999999</td></tr><tr><td>Bernardina Cooper</td><td>12867.958</td></tr><tr><td>Minnie Compton</td><td>8336.4169</td></tr><tr><td>Narcisa Knapp</td><td>279.992</td></tr><tr><td>Jenell Crosby</td><td>524.3905</td></tr><tr><td>Catarina Mendez</td><td>9908.4642</td></tr><tr><td>Yvone Yates</td><td>6515.955</td></tr><tr><td>Kiana Rivera</td><td>13033.5961</td></tr><tr><td>Sharie Whitaker</td><td>6762.1399</td></tr><tr><td>Bettye Espinoza</td><td>5627.956999999999</td></tr><tr><td>Arvilla Osborn</td><td>10805.3354</td></tr><tr><td>Lynda Newman</td><td>1868.9634</td></tr><tr><td>Myrtle Gardner</td><td>1753.7717</td></tr><tr><td>Stacie Sims</td><td>7040.8464</td></tr><tr><td>Efren Oliver</td><td>11463.958</td></tr><tr><td>Priscilla Wilkins</td><td>3599.991</td></tr><tr><td>Natosha Rowland</td><td>2658.7627</td></tr><tr><td>Kaley Blanchard</td><td>6578.9291</td></tr><tr><td>Heather Chaney</td><td>5528.957</td></tr><tr><td>Nakisha Clay</td><td>2800.2975000000006</td></tr><tr><td>Maira Long</td><td>5588.5185</td></tr><tr><td>Mechelle Chan</td><td>1210.2714999999998</td></tr><tr><td>Rolanda Larsen</td><td>3136.0432</td></tr><tr><td>Jacalyn Barnett</td><td>502.1907</td></tr><tr><td>Ami Mcmahon</td><td>2840.0460999999996</td></tr><tr><td>Junita Reese</td><td>242.991</td></tr><tr><td>Sharyn Brewer</td><td>3994.4559</td></tr><tr><td>Daisy Ward</td><td>6023.9545</td></tr><tr><td>Lucile Manning</td><td>2032.4445</td></tr><tr><td>Tajuana Rollins</td><td>7782.873</td></tr><tr><td>Marcene Curtis</td><td>3668.9260000000004</td></tr><tr><td>Charmain Webster</td><td>17834.963399999997</td></tr><tr><td>Ollie Zimmerman</td><td>5371.338</td></tr><tr><td>Onita Johns</td><td>2270.5392</td></tr><tr><td>Treasa Dickerson</td><td>889.5840000000001</td></tr><tr><td>Yan Trevino</td><td>11391.43</td></tr><tr><td>Everett Vega</td><td>1304.9750000000001</td></tr><tr><td>Kallie Best</td><td>11428.653</td></tr><tr><td>Jewell Reyes</td><td>1019.963</td></tr><tr><td>Jeffrey Hill</td><td>1845.882</td></tr><tr><td>Izola Hobbs</td><td>3439.4575</td></tr><tr><td>Terra Pickett</td><td>11787.5533</td></tr><tr><td>Eleanor Mendez</td><td>4829.1825</td></tr><tr><td>Eliana Silva</td><td>4236.3466</td></tr><tr><td>Verna Solis</td><td>3799.1634</td></tr><tr><td>Kaila Walters</td><td>1367.984</td></tr><tr><td>Clare Neal</td><td>2357.9642</td></tr><tr><td>Nenita Mooney</td><td>5806.037499999999</td></tr><tr><td>Rudolph Velez</td><td>8263.867</td></tr><tr><td>Nanette Harris</td><td>2559.992</td></tr><tr><td>Alina Mcleod</td><td>13287.526199999998</td></tr><tr><td>Genevie Miles</td><td>1850.0567</td></tr><tr><td>Sung Chambers</td><td>5115.9641</td></tr><tr><td>Grisel Maynard</td><td>989.991</td></tr><tr><td>Jeromy Burch</td><td>11907.9041</td></tr><tr><td>Letty Cobb</td><td>8820.1505</td></tr><tr><td>Danielle Bond</td><td>18553.730000000003</td></tr><tr><td>Carter Booth</td><td>1416.573</td></tr><tr><td>Ling Newman</td><td>5699.981</td></tr><tr><td>Robena Hill</td><td>13783.7813</td></tr><tr><td>Tommie Cooley</td><td>8011.311999999999</td></tr><tr><td>Aron Wiggins</td><td>10047.424500000001</td></tr><tr><td>Teofila Fischer</td><td>23195.075399999998</td></tr><tr><td>Terrance Lynn</td><td>7536.1622</td></tr><tr><td>Rubin Decker</td><td>2484.4274</td></tr><tr><td>Jeannette Skinner</td><td>2889.8561</td></tr><tr><td>Justina Long</td><td>9327.738</td></tr><tr><td>Corrinne Garrison</td><td>8481.898000000001</td></tr><tr><td>Lakenya Oliver</td><td>1099.4814999999999</td></tr><tr><td>Laurette Hebert</td><td>2309.3035</td></tr><tr><td>Shanice Spears</td><td>11299.972</td></tr><tr><td>Leola Gould</td><td>613.7907</td></tr><tr><td>Willetta Murphy</td><td>2200.9444</td></tr><tr><td>Angele Castro</td><td>1082.9715</td></tr><tr><td>Melia Brady</td><td>14011.8265</td></tr><tr><td>Jenee Rasmussen</td><td>12861.8789</td></tr><tr><td>Shae Hickman</td><td>18281.4729</td></tr><tr><td>Garret Clay</td><td>3346.0319</td></tr><tr><td>Elvina Gates</td><td>2780.5470000000005</td></tr><tr><td>Veronika Rollins</td><td>10132.3624</td></tr><tr><td>Jane Henderson</td><td>3793.1580000000004</td></tr><tr><td>Merideth Preston</td><td>11832.453899999999</td></tr><tr><td>Melodie Melton</td><td>7984.939</td></tr><tr><td>Lamar Bush</td><td>2093.4134999999997</td></tr><tr><td>Earl Stanley</td><td>5315.9042</td></tr><tr><td>Jeanice Frost</td><td>19992.864800000003</td></tr><tr><td>Elmo Sweeney</td><td>2518.1494000000002</td></tr><tr><td>Ilona Spears</td><td>8712.8466</td></tr><tr><td>Cassidy Clark</td><td>633.6245</td></tr><tr><td>Caridad Compton</td><td>8945.75</td></tr><tr><td>Nicolas Carlson</td><td>5863.4454</td></tr><tr><td>Charise Burt</td><td>1250.8636999999999</td></tr><tr><td>Edith Davenport</td><td>1243.7847000000002</td></tr><tr><td>Shanita Wiley</td><td>2217.6427</td></tr><tr><td>Porter Bass</td><td>4305.9576</td></tr><tr><td>Sylvester Chan</td><td>728.9730000000001</td></tr><tr><td>Georgeanna Webster</td><td>593.991</td></tr><tr><td>Abby Gamble</td><td>32803.0062</td></tr><tr><td>Kylee Dickson</td><td>837.9827</td></tr><tr><td>Jessika Bray</td><td>1113.2655</td></tr><tr><td>Carline Collier</td><td>5073.0365</td></tr><tr><td>Janetta Aguirre</td><td>17783.487399999998</td></tr><tr><td>Queenie Vance</td><td>3056.9624</td></tr><tr><td>Mellie Puckett</td><td>5835.858</td></tr><tr><td>Sheila Travis</td><td>5579.962799999999</td></tr><tr><td>Jenine Dawson</td><td>7938.9374</td></tr><tr><td>Cher Alston</td><td>3866.0454</td></tr><tr><td>Ayana Keith</td><td>4685.0969</td></tr><tr><td>Rod Hatfield</td><td>3546.929</td></tr><tr><td>Cicely Deleon</td><td>6701.455</td></tr><tr><td>Erma Salinas</td><td>2658.1454</td></tr><tr><td>Minerva Decker</td><td>12369.6265</td></tr><tr><td>Augustina Joyner</td><td>20509.425399999996</td></tr><tr><td>Delfina Gilliam</td><td>4274.981</td></tr><tr><td>Jana Thomas</td><td>14397.1379</td></tr><tr><td>Ruth Horton</td><td>4499.991</td></tr><tr><td>Hae Ramirez</td><td>12089.981399999999</td></tr><tr><td>Mellisa Kim</td><td>2975.9906999999994</td></tr><tr><td>Raeann Duncan</td><td>4030.9569999999994</td></tr><tr><td>Todd Waters</td><td>12381.8274</td></tr><tr><td>Vivian Deleon</td><td>1681.4809999999998</td></tr><tr><td>Deanne Parsons</td><td>9942.14</td></tr><tr><td>Alishia Elliott</td><td>7951.146799999999</td></tr><tr><td>Ashanti Hammond</td><td>17758.349000000002</td></tr><tr><td>Sarita Parks</td><td>15314.013200000001</td></tr><tr><td>Muriel Juarez</td><td>10570.471899999999</td></tr><tr><td>Brigid Sharp</td><td>20648.9537</td></tr><tr><td>Bess Mcbride</td><td>18853.354399999997</td></tr><tr><td>Kara Higgins</td><td>8127.9469</td></tr><tr><td>Shenna Benton</td><td>1797.975</td></tr><tr><td>Nicola Knight</td><td>4226.230500000001</td></tr><tr><td>Malinda Baxter</td><td>2312.4447</td></tr><tr><td>Christopher Richardson</td><td>1394.9814</td></tr><tr><td>Katia Henry</td><td>9479.9557</td></tr><tr><td>Santa Larson</td><td>8445.9545</td></tr><tr><td>Yevette Todd</td><td>4863.968000000001</td></tr><tr><td>Maurice Norton</td><td>1439.9840000000002</td></tr><tr><td>Berneice Pollard</td><td>892.981</td></tr><tr><td>Takako Casey</td><td>1855.3325</td></tr><tr><td>Regine Odom</td><td>8303.3719</td></tr><tr><td>Gilberto Parsons</td><td>12935.949399999998</td></tr><tr><td>Loni Mullen</td><td>451.78200000000004</td></tr><tr><td>Shena Carter</td><td>24890.6244</td></tr><tr><td>Deirdre Ryan</td><td>6803.971899999999</td></tr><tr><td>Jamaal Morrison</td><td>9173.381699999998</td></tr><tr><td>Ja Dillard</td><td>7947.442</td></tr><tr><td>Spring Hayes</td><td>4737.2644</td></tr><tr><td>Tena Cruz</td><td>3037.1354999999994</td></tr><tr><td>Rey Lindsay</td><td>8327.9477</td></tr><tr><td>Aida Koch</td><td>3865.7654</td></tr><tr><td>Alma Peck</td><td>1209.4747</td></tr><tr><td>Latonya Dixon</td><td>3149.991</td></tr><tr><td>Karren Stevenson</td><td>5891.162399999999</td></tr><tr><td>Cameron Carroll</td><td>5419.973</td></tr><tr><td>Kiesha Bond</td><td>1228.5207</td></tr><tr><td>Jimmy Russell</td><td>18278.9436</td></tr><tr><td>Marguerite Berger</td><td>9712.9515</td></tr><tr><td>Nubia Anderson</td><td>1538.964</td></tr><tr><td>Joel Wynn</td><td>2419.7634</td></tr><tr><td>Mathilda Pennington</td><td>1987.966</td></tr><tr><td>Renay Atkins</td><td>5332.9467</td></tr><tr><td>Joaquin Hawkins</td><td>6259.265</td></tr><tr><td>Elmira Levy</td><td>6718.5542</td></tr><tr><td>Lynwood Jackson</td><td>6843.9442</td></tr><tr><td>Dung Reid</td><td>5515.9646999999995</td></tr><tr><td>Jeniffer Slater</td><td>2699.991</td></tr><tr><td>Celestine Jacobs</td><td>6971.553699999999</td></tr><tr><td>Tenisha Lyons</td><td>20086.370799999997</td></tr><tr><td>Hortencia O'neil</td><td>1793.7574</td></tr><tr><td>Kenyetta Mason</td><td>2013.9650000000001</td></tr><tr><td>Tena Huber</td><td>11183.043399999999</td></tr><tr><td>Erik Leblanc</td><td>4749.981</td></tr><tr><td>Zora Ford</td><td>7663.9490000000005</td></tr><tr><td>Lara Guy</td><td>3659.9825</td></tr><tr><td>James Robles</td><td>9314.8357</td></tr><tr><td>Desire Mcgowan</td><td>1392.2730000000001</td></tr><tr><td>Stefany Potter</td><td>6183.5624</td></tr><tr><td>Louis Powell</td><td>2738.2497000000003</td></tr><tr><td>Linnie Branch</td><td>9586.801800000001</td></tr><tr><td>Earlean Pena</td><td>14249.6462</td></tr><tr><td>Cassandra Nichols</td><td>377.982</td></tr><tr><td>Bella Perez</td><td>5444.955999999999</td></tr><tr><td>Kellie Franco</td><td>5399.982</td></tr><tr><td>Parthenia Figueroa</td><td>1257.972</td></tr><tr><td>Katherin Clark</td><td>5777.7667</td></tr><tr><td>Ruthanne Franco</td><td>17611.957000000002</td></tr><tr><td>Monica Sears</td><td>17193.9034</td></tr><tr><td>Diane Jones</td><td>7256.773799999999</td></tr><tr><td>Tiny French</td><td>6102.963</td></tr><tr><td>Carolann Russell</td><td>4521.8839</td></tr><tr><td>Cinthia Poole</td><td>4458.955</td></tr><tr><td>Rayford Simon</td><td>1023.984</td></tr><tr><td>Bev Chang</td><td>5291.965</td></tr><tr><td>Lavern Orr</td><td>3644.045</td></tr><tr><td>Erna Sloan</td><td>9849.074</td></tr><tr><td>Sheree Blanchard</td><td>531.981</td></tr><tr><td>Jonell Rivas</td><td>3535.2758999999996</td></tr><tr><td>Selene Vega</td><td>2119.259</td></tr><tr><td>Ester Acevedo</td><td>7999.984</td></tr><tr><td>Lavina Dejesus</td><td>10314.924799999999</td></tr><tr><td>Emory O'connor</td><td>2135.0624</td></tr><tr><td>Latoya Johns</td><td>6530.911899999999</td></tr><tr><td>Addie Hahn</td><td>14935.0311</td></tr><tr><td>Patria Harper</td><td>1055.9840000000002</td></tr><tr><td>Tara Maynard</td><td>601.5812</td></tr><tr><td>Mazie Fernandez</td><td>7394.964400000001</td></tr><tr><td>Gayla Sims</td><td>1519.2</td></tr><tr><td>Britteny Schroeder</td><td>232.4907</td></tr><tr><td>Frederica Rojas</td><td>13191.9384</td></tr><tr><td>Laurel Schultz</td><td>5923.9551</td></tr><tr><td>Zenia Bruce</td><td>1041.5814</td></tr><tr><td>Homer Powers</td><td>3039.9809999999998</td></tr><tr><td>Dortha Jarvis</td><td>14405.0464</td></tr><tr><td>Jerlene Rios</td><td>10266.9542</td></tr><tr><td>Julianne Shannon</td><td>7659.3381</td></tr><tr><td>Orval Hunter</td><td>2877.7652000000003</td></tr><tr><td>Emmett Hahn</td><td>4700.0626999999995</td></tr><tr><td>Damian Mills</td><td>6396.9646999999995</td></tr><tr><td>Barry Albert</td><td>3227.391</td></tr><tr><td>Reita Dickson</td><td>3766.6347</td></tr><tr><td>Sandy Mills</td><td>3229.9525000000003</td></tr><tr><td>Lurlene Cotton</td><td>4399.992</td></tr><tr><td>Whitney Estes</td><td>674.991</td></tr><tr><td>Sheba Knapp</td><td>11972.927099999999</td></tr><tr><td>Sophia Mcmillan</td><td>13773.627700000001</td></tr><tr><td>Kristy Watkins</td><td>1396.4904999999999</td></tr><tr><td>Mireille Puckett</td><td>2320.5564000000004</td></tr><tr><td>Leland Mcdowell</td><td>377.982</td></tr><tr><td>Fairy Robinson</td><td>4041.1537</td></tr><tr><td>Greta Page</td><td>1245.973</td></tr><tr><td>Hue May</td><td>6887.1357</td></tr><tr><td>Shanda Stevenson</td><td>4960.4587</td></tr><tr><td>Ping Quinn</td><td>2804.1440000000002</td></tr><tr><td>Desmond Rose</td><td>14566.4345</td></tr><tr><td>Wanita Davenport</td><td>2319.976</td></tr><tr><td>Louise Flowers</td><td>4196.9552</td></tr><tr><td>Dorothea Chang</td><td>13821.530999999999</td></tr><tr><td>Stan Saunders</td><td>8936.446</td></tr><tr><td>Cayla Johnson</td><td>1253.981</td></tr><tr><td>Fannie Jenkins</td><td>9532.3529</td></tr><tr><td>Katherina Odom</td><td>3643.5440000000003</td></tr><tr><td>Tameka Fisher</td><td>24051.527899999994</td></tr><tr><td>Alisia Albert</td><td>6150.9367</td></tr><tr><td>Wilda Petersen</td><td>6813.7535</td></tr><tr><td>Emanuel Mckee</td><td>5833.974699999999</td></tr><tr><td>Thalia Horne</td><td>727.984</td></tr><tr><td>Hayden Cross</td><td>631.6747</td></tr><tr><td>Marshall Johnson</td><td>1669.9825</td></tr><tr><td>Yuk Vega</td><td>7952.0464</td></tr><tr><td>Guillermina Noble</td><td>22061.0729</td></tr><tr><td>Karey Steele</td><td>2478.4</td></tr><tr><td>Cyndi Bush</td><td>1681.9740000000002</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Johnathan Velazquez",
         10231.0464
        ],
        [
         "Jaqueline Cummings",
         1697.9717
        ],
        [
         "Joshua Robertson",
         1519.981
        ],
        [
         "Nova Hess",
         13023.926
        ],
        [
         "Arla Ellis",
         3900.0606999999995
        ],
        [
         "Sharyn Hopkins",
         34807.93919999999
        ],
        [
         "Laureen Paul",
         2165.0816999999997
        ],
        [
         "Leslie Higgins",
         1372.4719
        ],
        [
         "Neil Mccall",
         9919.3294
        ],
        [
         "Alane Munoz",
         242.991
        ],
        [
         "Tarra Guerrero",
         3155.9565
        ],
        [
         "Marvin Mullins",
         18856.877
        ],
        [
         "Patience Clayton",
         3278.054
        ],
        [
         "Maribel William",
         437.09069999999997
        ],
        [
         "Ellsworth Michael",
         4030.0561
        ],
        [
         "Lea Key",
         2449.7546
        ],
        [
         "Sindy Anderson",
         4092.8567
        ],
        [
         "Lanita Burton",
         11406.4285
        ],
        [
         "Norine Huffman",
         6240.553999999999
        ],
        [
         "Randee Pitts",
         5671.1307
        ],
        [
         "Neoma Daugherty",
         2083.1605
        ],
        [
         "Tangela Hurley",
         1104.4745
        ],
        [
         "Drucilla Gilliam",
         6265.955
        ],
        [
         "Ashton Lott",
         2635.122
        ],
        [
         "Sam Lester",
         3633.3590000000004
        ],
        [
         "Jackeline Colon",
         5342.1559
        ],
        [
         "Pamala Henry",
         6981.9401
        ],
        [
         "Eleni Gordon",
         8587.397
        ],
        [
         "Laureen Barry",
         3859.928
        ],
        [
         "Yvone Guerrero",
         11183.0335
        ],
        [
         "Edgar Quinn",
         7993.865
        ],
        [
         "Kimbery Nieves",
         5270.944799999999
        ],
        [
         "Verona O'neill",
         4157.9724
        ],
        [
         "Sarai Mckee",
         9563.338099999999
        ],
        [
         "Neville Mcclain",
         3376.5951000000005
        ],
        [
         "Shantel Gregory",
         5644.9152
        ],
        [
         "Tomika Larson",
         1139.981
        ],
        [
         "Lashandra Turner",
         11578.6544
        ],
        [
         "Travis Whitley",
         3768.94
        ],
        [
         "Darren Witt",
         3223.184
        ],
        [
         "Ingeborg Ellison",
         2867.275
        ],
        [
         "Corene Swanson",
         426.54999999999995
        ],
        [
         "Elana Miles",
         1530.963
        ],
        [
         "Olympia Figueroa",
         4169.9815
        ],
        [
         "Carissa Cross",
         5404.055699999999
        ],
        [
         "Eldridge Greer",
         386.1
        ],
        [
         "Joshua Berg",
         2069.4549
        ],
        [
         "Josephine Dale",
         6712.8464
        ],
        [
         "Taisha Vang",
         502.1814
        ],
        [
         "Silas Tate",
         2497.9559
        ],
        [
         "Jamaal Baker",
         1786.4650000000001
        ],
        [
         "Twana Arnold",
         464.9907
        ],
        [
         "Margit Osborn",
         4781.9310000000005
        ],
        [
         "Inge Olsen",
         1759.976
        ],
        [
         "Chanel May",
         1904.4585000000002
        ],
        [
         "Nathaniel Davidson",
         1115.9814
        ],
        [
         "Dalia Carson",
         1509.4727
        ],
        [
         "Tiana Henderson",
         1200.542
        ],
        [
         "Rodney Odom",
         1703.6815000000001
        ],
        [
         "Joesph Delacruz",
         6863.626799999999
        ],
        [
         "Mark Garrett",
         3570.5560000000005
        ],
        [
         "Denis Logan",
         5651.0267
        ],
        [
         "Dann Huff",
         2653.073
        ],
        [
         "Corine Stuart",
         2801.9320000000002
        ],
        [
         "Serafina Clemons",
         494.99100000000004
        ],
        [
         "Susannah Fields",
         1390.4733999999999
        ],
        [
         "Lazaro Moran",
         4422.9400000000005
        ],
        [
         "Kristen Alvarez",
         888.2814000000001
        ],
        [
         "Ophelia Decker",
         3014.324
        ],
        [
         "Cleotilde Booth",
         16179.1167
        ],
        [
         "Cathey Lamb",
         1984.0729999999999
        ],
        [
         "Cesar Wilkins",
         1806.4125
        ],
        [
         "Gabriel Wagner",
         4196.0278
        ],
        [
         "Mariela Huffman",
         1577.0717
        ],
        [
         "Euna Lopez",
         8763.964399999999
        ],
        [
         "Genoveva Baldwin",
         24433.8818
        ],
        [
         "Rochelle Ward",
         2427.9567
        ],
        [
         "Trinidad Chapman",
         2052.3520000000003
        ],
        [
         "Ellena Clements",
         7568.0544
        ],
        [
         "Jeannie Wilcox",
         1378.182
        ],
        [
         "Max Charles",
         3998.362
        ],
        [
         "Bronwyn Vargas",
         3589.5660000000003
        ],
        [
         "Gertrude Terry",
         2379.973
        ],
        [
         "Christia Wilkins",
         1543.7628
        ],
        [
         "Aaron Knapp",
         5927.5509999999995
        ],
        [
         "Lavette Wright",
         6866.9384
        ],
        [
         "Rosa Kinney",
         1499.9660000000001
        ],
        [
         "Rodolfo Buck",
         8280.543
        ],
        [
         "Calandra Stanton",
         2100.9225
        ],
        [
         "Romaine Haley",
         1337.0817
        ],
        [
         "Catrice Hicks",
         3475.8442999999997
        ],
        [
         "Kimberli Cline",
         1619.991
        ],
        [
         "Cindie Franklin",
         4633.8544
        ],
        [
         "Thurman Ellis",
         4689.4559
        ],
        [
         "Casey Gill",
         6902.465
        ],
        [
         "Keitha Black",
         824.9815
        ],
        [
         "Alpha King",
         2813.5587
        ],
        [
         "Leticia Snyder",
         1692.5370000000003
        ],
        [
         "Rikki Morrow",
         9301.9304
        ],
        [
         "Luke Kramer",
         12420.713
        ],
        [
         "Katheleen Marks",
         879.984
        ],
        [
         "Trisha Johnson",
         754.5812
        ],
        [
         "Brigida Larson",
         8062.1245
        ],
        [
         "Latasha Hays",
         7147.162899999999
        ],
        [
         "Vikki Erickson",
         6489.5650000000005
        ],
        [
         "Valery Saunders",
         872.0820000000001
        ],
        [
         "Kiara Deleon",
         845.182
        ],
        [
         "Robby Sykes",
         24305.1394
        ],
        [
         "Ben Stone",
         923.0726999999999
        ],
        [
         "Launa Hull",
         242.991
        ],
        [
         "Zulema Browning",
         1265.9723999999999
        ],
        [
         "Micki Rutledge",
         3511.7384
        ],
        [
         "Theresia Barron",
         4803.6301
        ],
        [
         "Mark Benton",
         1705.9632
        ],
        [
         "Starr Schneider",
         620.0920000000001
        ],
        [
         "Burma Summers",
         569.9905
        ],
        [
         "Gwenn Melton",
         1644.5165
        ],
        [
         "Danille Mcfarland",
         5909.614799999999
        ],
        [
         "Bryce Monroe",
         474.9905
        ],
        [
         "Sharie Alvarez",
         5716.5960000000005
        ],
        [
         "Tomika Wilder",
         9210.7184
        ],
        [
         "Wallace Lane",
         539.991
        ],
        [
         "Lecia Hancock",
         989.9820000000001
        ],
        [
         "Elouise Fry",
         10866.962199999998
        ],
        [
         "Laverne Craft",
         386.1
        ],
        [
         "Shenna Espinoza",
         5699.981
        ],
        [
         "Chelsey Boyd",
         6332.9424
        ],
        [
         "Lissa Vargas",
         12551.997
        ],
        [
         "Armand Whitehead",
         7154.5445
        ],
        [
         "Marcelino Mcbride",
         3027.0319
        ],
        [
         "Hortencia Graham",
         6815.9474
        ],
        [
         "Monika Berg",
         8902.506599999999
        ],
        [
         "Jerome Bolton",
         728.973
        ],
        [
         "Tuan Wolfe",
         3038.3214
        ],
        [
         "Alexandria Zamora",
         4475.4635
        ],
        [
         "Gena Owens",
         8299.965
        ],
        [
         "Jina Cooper",
         521.9817
        ],
        [
         "Katharine Herrera",
         1455.974
        ],
        [
         "Ezra Silva",
         1765.1307
        ],
        [
         "Devin Velazquez",
         2469.9585
        ],
        [
         "Erlene Cook",
         359.20000000000005
        ],
        [
         "Regine Gonzales",
         13801.2997
        ],
        [
         "Merlin Foreman",
         375.992
        ],
        [
         "Hubert Reilly",
         3419.9809999999998
        ],
        [
         "Lavonne Anderson",
         6744.774
        ],
        [
         "Keturah Massey",
         4765.4287
        ],
        [
         "Diana Guerra",
         4183.6206999999995
        ],
        [
         "Senaida Thompson",
         256.4905
        ],
        [
         "Han Schneider",
         1525.1627999999998
        ],
        [
         "Reena Higgins",
         5728.9344
        ],
        [
         "Katina Mcintosh",
         926.091
        ],
        [
         "Parker Prince",
         7168.4778
        ],
        [
         "Edda Young",
         3238.9623999999994
        ],
        [
         "Dione Pratt",
         494.99100000000004
        ],
        [
         "Loni Duncan",
         1619.991
        ],
        [
         "Sheri Cole",
         1970.5907
        ],
        [
         "Mozelle Carter",
         23049.057
        ],
        [
         "Dacia William",
         2371.4545
        ],
        [
         "Araceli Golden",
         18037.285
        ],
        [
         "Harris Pittman",
         3642.0126
        ],
        [
         "Kasie Rodriquez",
         8879.452899999998
        ],
        [
         "Williemae Holloway",
         19756.6432
        ],
        [
         "Magdalena Sherman",
         854.191
        ],
        [
         "Leonore Dorsey",
         8696.072
        ],
        [
         "Adriene Rivera",
         6462.4635
        ],
        [
         "Abbey Pugh",
         4132.992
        ],
        [
         "Rico Salas",
         9874.6525
        ],
        [
         "Kandace Ayers",
         5004.5978000000005
        ],
        [
         "Carie Kidd",
         5431.8955
        ],
        [
         "Aubrey Durham",
         5565.5645
        ],
        [
         "Elvera Peck",
         2007.5811999999999
        ],
        [
         "Cindi Ellis",
         758.9827
        ],
        [
         "Destiny Goodman",
         1240.1840000000002
        ],
        [
         "Steve Bender",
         3292.427
        ],
        [
         "Melba Wilkinson",
         5224.5464
        ],
        [
         "Lucy Woods",
         3589.122
        ],
        [
         "Graig Roth",
         4318.4515
        ],
        [
         "Shery Acosta",
         3372.138
        ],
        [
         "Kristel Bullock",
         557.9907
        ],
        [
         "Latosha Dalton",
         4877.406
        ],
        [
         "Phylis Adkins",
         1972.9624
        ],
        [
         "Adelle Larsen",
         16651.0484
        ],
        [
         "Brianna Moss",
         3751.874
        ],
        [
         "Corene Wall",
         14199.9558
        ],
        [
         "Waldo Hart",
         3032.982
        ],
        [
         "Jeniffer Ratliff",
         1254.9405
        ],
        [
         "Lorrie Pollard",
         7439.981399999999
        ],
        [
         "Allie Conley",
         959.984
        ],
        [
         "Violet Valenzuela",
         2546.4665000000005
        ],
        [
         "Ruthanne Hoover",
         5989.9367
        ],
        [
         "Viva Dawson",
         7918.8446
        ],
        [
         "Trena Rogers",
         989.9820000000001
        ],
        [
         "Carroll Kelly",
         431.98400000000004
        ],
        [
         "Kasha Sullivan",
         7855.2405
        ],
        [
         "Tammie Cherry",
         6239.0936
        ],
        [
         "Erlinda Nielsen",
         6034.965399999999
        ],
        [
         "Allison Nolan",
         5809.477400000001
        ],
        [
         "Marisa Chambers",
         4105.112999999999
        ],
        [
         "Lanelle Guerra",
         1072.1624
        ],
        [
         "Brenda Tate",
         4616.0145
        ],
        [
         "Joi Reeves",
         4038.502699999999
        ],
        [
         "Henrietta Wagner",
         3891.5125
        ],
        [
         "Danilo Holmes",
         1646.3814
        ],
        [
         "Myrtie James",
         1502.9630000000002
        ],
        [
         "Tania Swanson",
         954.9825000000001
        ],
        [
         "Marget Hodge",
         12461.5479
        ],
        [
         "Leanna Manning",
         10620.044899999999
        ],
        [
         "Clarita Curry",
         242.991
        ],
        [
         "Lynn Mcmahon",
         683.0747
        ],
        [
         "Penney Hall",
         2835.5514
        ],
        [
         "Lanora Robbins",
         5600.0574
        ],
        [
         "Lilliam Nolan",
         242.991
        ],
        [
         "Kaci Gallegos",
         242.991
        ],
        [
         "Kelsey Noble",
         1407.5520000000001
        ],
        [
         "Angelina Lloyd",
         1625.963
        ],
        [
         "Sebrina Hart",
         3591.27
        ],
        [
         "Vernetta Banks",
         2123.5632
        ],
        [
         "Inez Snider",
         1626.7825000000003
        ],
        [
         "Noble Glover",
         3443.9377000000004
        ],
        [
         "Donovan Cantrell",
         3126.6414
        ],
        [
         "Gertrud Rhodes",
         7000.058000000001
        ],
        [
         "Veronique Fulton",
         10216.235999999999
        ],
        [
         "Carola Rodriquez",
         17861.1996
        ],
        [
         "Fransisca Nicholson",
         2942.982
        ],
        [
         "Tony Hicks",
         712.4905
        ],
        [
         "Kirstie Vazquez",
         2853.963
        ],
        [
         "Jamika Blanchard",
         4911.437899999999
        ],
        [
         "Evelina Manning",
         4617.758
        ],
        [
         "Ryan Carter",
         3126.6414
        ],
        [
         "Rosamaria Meyer",
         5893.5494
        ],
        [
         "Latashia Travis",
         7967.4144
        ],
        [
         "Melita Dominguez",
         2748.7464
        ],
        [
         "Merrie Fowler",
         8069.656499999999
        ],
        [
         "Eli Contreras",
         8550.052699999998
        ],
        [
         "Stephaine Riddle",
         8429.9454
        ],
        [
         "Carman Hardy",
         2465.4572
        ],
        [
         "Annett Rush",
         6089.930399999999
        ],
        [
         "Lashawn Ortiz",
         14774.458299999998
        ],
        [
         "Kanesha Vega",
         11151.6045
        ],
        [
         "Divina Madden",
         3199.992
        ],
        [
         "Almeta Benjamin",
         799.9920000000001
        ],
        [
         "Barrett Sanders",
         9385.101999999999
        ],
        [
         "Venus Hewitt",
         1060.553
        ],
        [
         "Scarlet Yates",
         4563.091
        ],
        [
         "Caren Stephens",
         5275.327
        ],
        [
         "Joann Barber",
         1264.9827
        ],
        [
         "Kimberley Reynolds",
         4109.065
        ],
        [
         "Miquel Neal",
         8696.071999999998
        ],
        [
         "Weldon Michael",
         3840.882
        ],
        [
         "Arlena Buckner",
         992.965
        ],
        [
         "Lorrie Becker",
         23026.2923
        ],
        [
         "Earline Gordon",
         3126.6414
        ],
        [
         "Faustino Delacruz",
         2346.6623999999997
        ],
        [
         "Ophelia Rodgers",
         4044.848700000001
        ],
        [
         "Theo Reese",
         9514.0705
        ],
        [
         "Joeann Garrison",
         7045.1564
        ],
        [
         "Cecil Hopper",
         6961.0917
        ],
        [
         "Ginette Edwards",
         5225.9475
        ],
        [
         "Yvette Rogers",
         2599.168
        ],
        [
         "Pasquale Hogan",
         2155.172
        ],
        [
         "Matilda Larson",
         6397.4717
        ],
        [
         "Ai Forbes",
         5014.9637
        ],
        [
         "Charolette Rice",
         17520.2919
        ],
        [
         "Arnita Thomas",
         4799.9839999999995
        ],
        [
         "Lurline Rivers",
         1708.3719
        ],
        [
         "Randolph Chase",
         9163.428899999999
        ],
        [
         "Shery Randolph",
         7251.965499999999
        ],
        [
         "Terrell Mathis",
         3163.0425999999998
        ],
        [
         "Ethelyn Ray",
         1276.9750000000001
        ],
        [
         "Christoper Mccall",
         11462.5954
        ],
        [
         "Ezra Fowler",
         2958.3021
        ],
        [
         "Tona Velasquez",
         242.991
        ],
        [
         "Octavia Case",
         9673.8444
        ],
        [
         "Rozanne Reyes",
         8476.521999999999
        ],
        [
         "Magali Dixon",
         7587.5154
        ],
        [
         "Thad Castro",
         2197.9500000000003
        ],
        [
         "Raven Curtis",
         4692.8641
        ],
        [
         "Rosalba O'neal",
         464.9907
        ],
        [
         "Tomeka Higgins",
         1832.0628
        ],
        [
         "Cris Dunn",
         8177.0540999999985
        ],
        [
         "Regina Burns",
         11013.9345
        ],
        [
         "Olevia Pitts",
         8273.955899999999
        ],
        [
         "Inger Jennings",
         1359.976
        ],
        [
         "Justin Newton",
         2337.4625
        ],
        [
         "Latasha Stanley",
         13854.6016
        ],
        [
         "Delbert Wilkins",
         3810.823
        ],
        [
         "Ouida Gregory",
         11314.072999999999
        ],
        [
         "Phyllis Hill",
         1034.2827000000002
        ],
        [
         "Marni Bolton",
         4095.0137999999997
        ],
        [
         "Alane Kennedy",
         1395.1624
        ],
        [
         "Van Peters",
         6448.2907
        ],
        [
         "Rubye Mccall",
         1229.0919999999999
        ],
        [
         "Lavona Austin",
         8975.157
        ],
        [
         "Benny Bender",
         502.1814
        ],
        [
         "Gabriela Warren",
         7345.7374
        ],
        [
         "Justina Jenkins",
         6898.1055
        ],
        [
         "Janna Hayden",
         4624.9376999999995
        ],
        [
         "Rayna Perry",
         5672.281
        ],
        [
         "Emmaline Huber",
         10563.648000000001
        ],
        [
         "Carlena Salinas",
         2915.108
        ],
        [
         "Bernita Mcdaniel",
         6079.942999999999
        ],
        [
         "Chelsey Hardin",
         9211.523
        ],
        [
         "Camille Harvey",
         3463.545
        ],
        [
         "Charleen Hurst",
         1490.2907
        ],
        [
         "Christoper Gould",
         1006.981
        ],
        [
         "Charlyn Cantrell",
         4534.383
        ],
        [
         "Gilma Dejesus",
         1472.481
        ],
        [
         "Deloris Larson",
         11479.5394
        ],
        [
         "Shayla Hart",
         2928.684
        ],
        [
         "Jame Riggs",
         2687.1434
        ],
        [
         "Dagny Owen",
         5578.1307
        ],
        [
         "Janie Herrera",
         11950.476599999998
        ],
        [
         "Rufina Chandler",
         4044.7830000000004
        ],
        [
         "Shawnda Glover",
         3586.7070000000003
        ],
        [
         "Mariam Miranda",
         2431.165
        ],
        [
         "Mallie Osborn",
         4135.9565
        ],
        [
         "Danyell Dickerson",
         3018.2852
        ],
        [
         "Carola Johns",
         674.991
        ],
        [
         "Arcelia Vinson",
         6479.944
        ],
        [
         "Lea Irwin",
         683.0747
        ],
        [
         "Heide Reed",
         1582.1634
        ],
        [
         "Garland Weaver",
         3074.2065000000002
        ],
        [
         "Ernestina Skinner",
         4991.9664999999995
        ],
        [
         "Bernetta Summers",
         773.9817
        ],
        [
         "Tiesha Daniel",
         7793.1507
        ],
        [
         "Angele Schroeder",
         845.9820000000001
        ],
        [
         "Josh Shaw",
         5701.1053999999995
        ],
        [
         "Gabriel Pitts",
         512.981
        ],
        [
         "Yang Roth",
         772.2
        ],
        [
         "Antonetta Rocha",
         853.0999999999999
        ],
        [
         "Major Merrill",
         5055.113
        ],
        [
         "Hollis Rasmussen",
         5709.9555
        ],
        [
         "Phebe Soto",
         2024.0637
        ],
        [
         "Saran Moses",
         3049.983
        ],
        [
         "Adriene Rollins",
         3181.5405
        ],
        [
         "Omega Huff",
         8534.3743
        ],
        [
         "Shirely Cantrell",
         1249.972
        ],
        [
         "Anisha Lang",
         6416.5944
        ],
        [
         "Karren Lamb",
         569.981
        ],
        [
         "Reyes Merritt",
         4037.9646999999995
        ],
        [
         "Iva Wilcox",
         5338.9555
        ],
        [
         "Romaine Salazar",
         1307.6225
        ],
        [
         "Shauna Edwards",
         1831.1814
        ],
        [
         "Lynne Anderson",
         2090.6642
        ],
        [
         "Jerald Blackwell",
         278.9907
        ],
        [
         "Daina Sampson",
         3495.6623999999997
        ],
        [
         "Jamaal Albert",
         10355.390800000001
        ],
        [
         "Cinda Rocha",
         7482.1364
        ],
        [
         "Emmitt Sanchez",
         31925.885700000003
        ],
        [
         "Phylicia Stout",
         1199.9840000000002
        ],
        [
         "Jenine Crane",
         642.5419999999999
        ],
        [
         "Sebrina Gross",
         1042.1724
        ],
        [
         "Sheila Goodman",
         3581.4619999999995
        ],
        [
         "Garry Espinoza",
         15766.7006
        ],
        [
         "Larissa Hays",
         5588.344399999999
        ],
        [
         "Dorthea Walker",
         12965.7468
        ],
        [
         "Clorinda Donovan",
         7932.9465
        ],
        [
         "Demarcus Reese",
         3403.8540000000003
        ],
        [
         "Hedwig Paul",
         13611.6259
        ],
        [
         "Brain Skinner",
         1694.0557000000001
        ],
        [
         "Mariette Trevino",
         949.981
        ],
        [
         "Christel Cardenas",
         1022.9813999999999
        ],
        [
         "Arielle Levine",
         3899.9656999999997
        ],
        [
         "Afton Juarez",
         4279.5725
        ],
        [
         "Amina Salazar",
         4447.724
        ],
        [
         "Garth Huff",
         2881.14
        ],
        [
         "Raymonde Garcia",
         6169.963
        ],
        [
         "Ashlie Parrish",
         655.984
        ],
        [
         "Boyd Irwin",
         3271.8135
        ],
        [
         "Majorie Wyatt",
         5119.353999999999
        ],
        [
         "Dante Grimes",
         5114.0907
        ],
        [
         "Christiane Bradford",
         8376.9244
        ],
        [
         "Kristel Byrd",
         1934.9634
        ],
        [
         "Thad Gilliam",
         1961.0811999999999
        ],
        [
         "Alec Peck",
         1139.981
        ],
        [
         "Hassan Nash",
         3269.9827
        ],
        [
         "Han Wade",
         3763.8714999999997
        ],
        [
         "Vanessa West",
         502.1814
        ],
        [
         "Clelia Workman",
         4571.0727
        ],
        [
         "Aleta Mack",
         1929.514
        ],
        [
         "Conception Slater",
         5478.9484999999995
        ],
        [
         "Odette Moses",
         7791.0557
        ],
        [
         "Christiana Gross",
         4299.957
        ],
        [
         "Jennette Wooten",
         359.20000000000005
        ],
        [
         "Mirella Duffy",
         3430.9631
        ],
        [
         "Saturnina Garner",
         14068.2366
        ],
        [
         "Shirely Stanley",
         10574.962399999999
        ],
        [
         "Elinore Aguilar",
         25636.453100000002
        ],
        [
         "Carley Reynolds",
         6829.7092
        ],
        [
         "Alysha Powers",
         751.984
        ],
        [
         "Tammera Fischer",
         1196.9665
        ],
        [
         "Hans Price",
         256.4905
        ],
        [
         "Timothy Byers",
         2501.764
        ],
        [
         "Son Warner",
         3799.9904999999994
        ],
        [
         "Chasidy Tran",
         5080.6230000000005
        ],
        [
         "Lee Roman",
         3911.8624999999997
        ],
        [
         "Alline Beasley",
         5022.9574
        ],
        [
         "Sylvie Wilkerson",
         2718.3920000000003
        ],
        [
         "Corina Lynch",
         2672.6926
        ],
        [
         "Salena Day",
         8342.939
        ],
        [
         "Laverna Hernandez",
         4699.9557
        ],
        [
         "Genevieve Juarez",
         4890.365400000001
        ],
        [
         "Eliz Lynch",
         2319.9919999999997
        ],
        [
         "Keri Bridges",
         8522.9542
        ],
        [
         "Shemeka Lyons",
         3370.5721
        ],
        [
         "Luke Fuller",
         1709.3652000000002
        ],
        [
         "Herminia Reyes",
         7139.954
        ],
        [
         "Ferne Kline",
         1837.4717
        ],
        [
         "Carmina Emerson",
         4497.581700000001
        ],
        [
         "Kristofer Craig",
         6659.9627
        ],
        [
         "Vernia Madden",
         5219.982
        ],
        [
         "Bonita Marshall",
         3359.7477
        ],
        [
         "Johana Jacobson",
         997.1724
        ],
        [
         "Angie Powers",
         1990.1627999999998
        ],
        [
         "Titus Bullock",
         9805.246399999998
        ],
        [
         "Petronila Norris",
         13914.3345
        ],
        [
         "Le Deleon",
         9959.0962
        ],
        [
         "Suellen Mercado",
         1139.981
        ],
        [
         "Dewayne Herring",
         4921.154399999999
        ],
        [
         "Tommie Melton",
         1472.4724999999999
        ],
        [
         "Tessie Farmer",
         1351.7224
        ],
        [
         "Tonja Henderson",
         1964.0810000000001
        ],
        [
         "Douglass Little",
         3092.9448
        ],
        [
         "Bee Baker",
         2329.5760000000005
        ],
        [
         "Laraine Robbins",
         17068.4922
        ],
        [
         "Deja Chaney",
         8561.2627
        ],
        [
         "Carlie Terrell",
         2133.9264000000003
        ],
        [
         "Karla Kirk",
         13678.357
        ],
        [
         "Jerri Guthrie",
         4477.174
        ],
        [
         "Rochell Cantrell",
         7176.214899999999
        ],
        [
         "Yun Nelson",
         1189.9825
        ],
        [
         "Adam Thornton",
         5841.5215
        ],
        [
         "Javier Nichols",
         6872.9437
        ],
        [
         "Meredith Bryan",
         8474.1624
        ],
        [
         "Hilda Harvey",
         6229.1214
        ],
        [
         "Morton Barron",
         988.4817
        ],
        [
         "Etsuko Garrison",
         2827.9494
        ],
        [
         "Pandora Estes",
         1734.9325
        ],
        [
         "Olevia Noel",
         3997.9747
        ],
        [
         "Bart Hess",
         1331.9733999999999
        ],
        [
         "Vallie Dixon",
         8083.9627
        ],
        [
         "Nichelle Howell",
         1405.962
        ],
        [
         "Justa Thompson",
         9927.5559
        ],
        [
         "Laurence Christian",
         2222.8722
        ],
        [
         "Charlsie Carson",
         512.981
        ],
        [
         "Trinidad Mcclain",
         10986.904
        ],
        [
         "Shanna Bonner",
         3564.9664999999995
        ],
        [
         "Vanda Holmes",
         2432.9444
        ],
        [
         "Hildegarde Christensen",
         2849.9905
        ],
        [
         "Alanna Barry",
         1076.9307
        ],
        [
         "Kami Rios",
         9278.653900000001
        ],
        [
         "Andy O'neill",
         4655.040400000001
        ],
        [
         "Mila Good",
         1344.7920000000001
        ],
        [
         "Ladawn Downs",
         4067.6639999999998
        ],
        [
         "Brittney Rojas",
         7601.154699999999
        ],
        [
         "Lezlie Thompson",
         989.9820000000001
        ],
        [
         "Brent Calderon",
         502.1814
        ],
        [
         "Georgeann Waller",
         4036.9719999999998
        ],
        [
         "Cheryll Snyder",
         1745.9640000000002
        ],
        [
         "Ernest Rollins",
         10360.255
        ],
        [
         "Marry Benjamin",
         4654.9529999999995
        ],
        [
         "Adelaida Hancock",
         9497.172
        ],
        [
         "Chere Mcfadden",
         6784.956700000001
        ],
        [
         "Derrick Marks",
         3563.0245000000004
        ],
        [
         "Alane Mccarty",
         728.973
        ],
        [
         "Jeanett Herman",
         962.9730000000001
        ],
        [
         "Elmo Arnold",
         557.9907
        ],
        [
         "Rory Cooper",
         2197.892
        ],
        [
         "Manie Sanchez",
         2157.916
        ],
        [
         "Basilia Thornton",
         9408.7878
        ],
        [
         "Josie Schultz",
         1894.541
        ],
        [
         "Jayme Zamora",
         502.1814
        ],
        [
         "Ivette Warren",
         6335.663699999999
        ],
        [
         "Darcel Harmon",
         3816.4624
        ],
        [
         "Jayson Rutledge",
         6947.9474
        ],
        [
         "Whitney Cash",
         458.98300000000006
        ],
        [
         "Diana Cobb",
         398.96999999999997
        ],
        [
         "Iola Rasmussen",
         9838.4455
        ],
        [
         "Birdie Kramer",
         1382.972
        ],
        [
         "Vinnie Chan",
         3359.9717
        ],
        [
         "George Pickett",
         375.992
        ],
        [
         "Evelin Vargas",
         1328.6529
        ],
        [
         "Carisa Carpenter",
         3239.982
        ],
        [
         "Onita Macdonald",
         1525.1539
        ],
        [
         "Ji Burt",
         6319.945999999999
        ],
        [
         "Graciela Barber",
         2593.1289
        ],
        [
         "Rosalie Coffey",
         1926.5809999999997
        ],
        [
         "Tanesha Sawyer",
         269.99100000000004
        ],
        [
         "Kecia Olsen",
         3065.9825
        ],
        [
         "Ayanna Rhodes",
         914.9670000000001
        ],
        [
         "Kandis Mills",
         929.9814
        ],
        [
         "Divina Reeves",
         2195.0517
        ],
        [
         "Rodrick Shelton",
         3349.6487
        ],
        [
         "Julee Woodard",
         1260.973
        ],
        [
         "Barton Cox",
         3328.0631
        ],
        [
         "Shaunda Barnett",
         256.4905
        ],
        [
         "Yvonne Bean",
         1973.7314
        ],
        [
         "Mercedez Brooks",
         2414.963
        ],
        [
         "Erlinda Osborne",
         479.992
        ],
        [
         "Lory Berg",
         4169.981699999999
        ],
        [
         "Enoch Rosario",
         4776.0444
        ],
        [
         "Octavia Donaldson",
         6543.0622
        ],
        [
         "Jeromy Elliott",
         5989.965
        ],
        [
         "Ulysses Gaines",
         386.1
        ],
        [
         "Klara Mosley",
         755.972
        ],
        [
         "Jacquline Duncan",
         2201.6567
        ],
        [
         "Lory Page",
         4214.9734
        ],
        [
         "Guillermo Hart",
         1516.3400000000001
        ],
        [
         "Marcel Lindsay",
         4544.8471
        ],
        [
         "Shila White",
         6177.772499999999
        ],
        [
         "Margene Eaton",
         502.1814
        ],
        [
         "Juliane Dillard",
         8394.4714
        ],
        [
         "Fran Yang",
         17225.4439
        ],
        [
         "Ronald Parsons",
         2420.553
        ],
        [
         "Augustus Schmidt",
         1272.784
        ],
        [
         "Lois Steele",
         6152.6533
        ],
        [
         "Rebbecca Espinoza",
         4503.7459
        ],
        [
         "Lucas Estes",
         7105.7751
        ],
        [
         "Omega Johnston",
         7848.2628
        ],
        [
         "Tonda Webb",
         4169.3542
        ],
        [
         "Irving Pitts",
         8359.215999999999
        ],
        [
         "Gayle Wilkinson",
         512.981
        ],
        [
         "Mandi Gibbs",
         1022.9813999999999
        ],
        [
         "Yolando Wade",
         4873.9557
        ],
        [
         "Merlene Vinson",
         12793.633699999998
        ],
        [
         "Zelda Pratt",
         2252.915
        ],
        [
         "Ashleigh Finch",
         5024.1645
        ],
        [
         "Farrah Orr",
         7900.4347
        ],
        [
         "Roseanne Maynard",
         1485.4635
        ],
        [
         "Cira Downs",
         2214.0537
        ],
        [
         "Agatha Daniels",
         3613.7245
        ],
        [
         "Delana Scott",
         1199.9840000000002
        ],
        [
         "Jewel Sparks",
         6187.1539
        ],
        [
         "Lorrie Justice",
         2042.0634
        ],
        [
         "Zulema Clemons",
         512.981
        ],
        [
         "Melani Jarvis",
         4918.366
        ],
        [
         "Alica Hunter",
         4122.145399999999
        ],
        [
         "Chere Hardin",
         1165.0810000000001
        ],
        [
         "Bao Wade",
         2793.0481
        ],
        [
         "Loise Walker",
         3270.2309999999998
        ],
        [
         "Aleta Shepard",
         11102.47
        ],
        [
         "Bobbi Banks",
         4746.6324
        ],
        [
         "Bobbie Foster",
         8778.1311
        ],
        [
         "Alissa Craft",
         2754.9905
        ],
        [
         "Beatris Joyner",
         4665.5492
        ],
        [
         "Alexis Mack",
         2402.476
        ],
        [
         "Liliana Kerr",
         1841.6217000000001
        ],
        [
         "Katharina Bates",
         11776.4101
        ],
        [
         "Buford Bridges",
         6155.9644
        ],
        [
         "Bethany Herring",
         6794.082
        ],
        [
         "Lezlie Lamb",
         10372.0934
        ],
        [
         "Christel Barber",
         8816.954399999999
        ],
        [
         "Thanh Figueroa",
         1649.9724999999999
        ],
        [
         "Marjorie Logan",
         8956.785
        ],
        [
         "Davis Long",
         1499.9719
        ],
        [
         "Rodger Rojas",
         1758.5140000000001
        ],
        [
         "Aisha Woods",
         2743.984
        ],
        [
         "Nathaniel Richard",
         4495.272500000001
        ],
        [
         "Jennie Middleton",
         9474.9404
        ],
        [
         "Tayna Wade",
         3628.5126999999998
        ],
        [
         "Lenita Bonner",
         2726.4905
        ],
        [
         "Terese Briggs",
         1559.9725
        ],
        [
         "Loreen Byers",
         5090.4175
        ],
        [
         "Genoveva Tyler",
         4125.556500000001
        ],
        [
         "Johna Powers",
         599.9920000000001
        ],
        [
         "Leone Emerson",
         5779.8175
        ],
        [
         "Deloris Burke",
         19043.9036
        ],
        [
         "Houston Vasquez",
         2699.991
        ],
        [
         "Earline Ballard",
         1599.9840000000002
        ],
        [
         "Yahaira Robertson",
         4784.1587
        ],
        [
         "Omer Estrada",
         7975.972999999999
        ],
        [
         "Vonda Berger",
         7824.040099999999
        ],
        [
         "Pearlie Cochran",
         3347.9813999999997
        ],
        [
         "Edgar Horn",
         847.984
        ],
        [
         "Deandrea Cox",
         4778.0235999999995
        ],
        [
         "Alden Atkinson",
         3484.0719
        ],
        [
         "America Swanson",
         3505.766
        ],
        [
         "Grace Madden",
         1450.023
        ],
        [
         "Marisol Goodman",
         3121.132
        ],
        [
         "Nicki Fry",
         1006.981
        ],
        [
         "Casimira Chapman",
         8200.726700000001
        ],
        [
         "Brenton Whitaker",
         3439.944
        ],
        [
         "Jong Guthrie",
         1891.1125000000002
        ],
        [
         "Tisha Petty",
         1052.972
        ],
        [
         "Sherie Ayala",
         7042.6723999999995
        ],
        [
         "Aileen Marquez",
         4644.9130000000005
        ],
        [
         "Shasta Combs",
         2360.3907
        ],
        [
         "Ronna Butler",
         17240.562299999998
        ],
        [
         "Debra Burks",
         27888.183399999998
        ],
        [
         "Sharika Colon",
         4271.1134
        ],
        [
         "Amparo Burks",
         879.984
        ],
        [
         "Tina Bush",
         3464.0224
        ],
        [
         "Vernon Knowles",
         3121.4817
        ],
        [
         "Floretta Higgins",
         7681.124
        ],
        [
         "Leila Barr",
         3144.327
        ],
        [
         "Georgetta Hardin",
         14877.289
        ],
        [
         "Anderson Martin",
         3900.6587000000004
        ],
        [
         "Ardelia Cooley",
         12334.957
        ],
        [
         "Stefani Gamble",
         6715.433999999999
        ],
        [
         "Jovita Bishop",
         4436.6034
        ],
        [
         "Leeanne Cross",
         1115.9814
        ],
        [
         "Taylor Cole",
         1364.944
        ],
        [
         "Charlene Norris",
         6764.572700000001
        ],
        [
         "Eun Harris",
         660.5905
        ],
        [
         "Tricia Daniels",
         3502.4932
        ],
        [
         "Ivette Estes",
         1399.976
        ],
        [
         "Le Wood",
         3974.6254
        ],
        [
         "Tanesha Hampton",
         2335.5207
        ],
        [
         "Terese Palmer",
         464.9907
        ],
        [
         "Collen Hayes",
         2113.5840000000003
        ],
        [
         "Anton Barton",
         797.9399999999999
        ],
        [
         "Nevada Hood",
         7688.2721
        ],
        [
         "Myron Johns",
         1673.9906999999998
        ],
        [
         "Ghislaine Compton",
         1754.0464000000002
        ],
        [
         "Carmela Hays",
         4186.5267
        ],
        [
         "Wes Stanton",
         423.992
        ],
        [
         "Tora Dunlap",
         5775.5446999999995
        ],
        [
         "Kandace Hughes",
         953.9820000000001
        ],
        [
         "Margaretta Clayton",
         4835.375999999999
        ],
        [
         "Loyce Conway",
         3015.3129
        ],
        [
         "Lean Stark",
         2008.7628
        ],
        [
         "Margert Stevens",
         4851.1372
        ],
        [
         "Shantae Hammond",
         6068.9490000000005
        ],
        [
         "Santos Valencia",
         10719.098799999998
        ],
        [
         "Andreas Herman",
         2754.9905
        ],
        [
         "Mia Delgado",
         527.984
        ],
        [
         "Hee Greer",
         3509.973
        ],
        [
         "Verda Gilbert",
         6349.3634999999995
        ],
        [
         "Felicidad Golden",
         10794.3537
        ],
        [
         "Alejandrina Hodges",
         3447.2278
        ],
        [
         "Adam Henderson",
         3695.4745000000003
        ],
        [
         "Lizette Ellison",
         836.9814
        ],
        [
         "Lonna Franks",
         712.4905
        ],
        [
         "Sunshine Rosario",
         2789.9907
        ],
        [
         "Consuela Collier",
         15455.624999999998
        ],
        [
         "Annis Sanchez",
         4269.9572
        ],
        [
         "Jaimee Day",
         1172.9724
        ],
        [
         "Jenny Bell",
         511.49069999999995
        ],
        [
         "Ara Vazquez",
         4466.6452
        ],
        [
         "Hue Dalton",
         799.9920000000001
        ],
        [
         "Toya Pratt",
         2082.1435
        ],
        [
         "Milagros Weber",
         7130.5405
        ],
        [
         "Barbra Dickerson",
         7520.0371
        ],
        [
         "Gilberto Sanders",
         4497.0048
        ],
        [
         "Kanesha Hudson",
         225.89100000000002
        ],
        [
         "Venessa Frost",
         1279.0627
        ],
        [
         "Mable Pratt",
         6912.171499999999
        ],
        [
         "Tonisha Fowler",
         9399.965
        ],
        [
         "Sheryl Chase",
         17086.934299999997
        ],
        [
         "Ashlee Pena",
         17305.9384
        ],
        [
         "Leigh Burke",
         7022.9623999999985
        ],
        [
         "Caleb England",
         7339.4195
        ],
        [
         "Herta Rollins",
         4464.6642
        ],
        [
         "Reatha Perez",
         13130.8288
        ],
        [
         "Syreeta Hendricks",
         11979.946699999999
        ],
        [
         "Lavonda Stephenson",
         2208.9745
        ],
        [
         "Klara Kim",
         1804.8564999999999
        ],
        [
         "Christia Carson",
         3658.1809999999996
        ],
        [
         "Carolyne Conley",
         1692.5720999999999
        ],
        [
         "Virgina Berg",
         5154.1467
        ],
        [
         "Elvia Cardenas",
         6978.715099999999
        ],
        [
         "Delmar Wise",
         15439.946799999998
        ],
        [
         "Doreatha Ford",
         959.984
        ],
        [
         "Boyce Burks",
         1600.0929999999998
        ],
        [
         "Petronila Gallegos",
         2719.4764
        ],
        [
         "Elnora Simpson",
         15416.1565
        ],
        [
         "Ivonne Yang",
         2371.1623999999997
        ],
        [
         "Zina Bonner",
         5660.9369
        ],
        [
         "Delila Hamilton",
         10869.9637
        ],
        [
         "Lidia Ashley",
         9704.9449
        ],
        [
         "Toshia Cardenas",
         3935.9680000000008
        ],
        [
         "Laci Castro",
         1349.982
        ],
        [
         "Quyen Houston",
         5537.981699999999
        ],
        [
         "Ayanna Cherry",
         16950.076999999997
        ],
        [
         "Alesia Horne",
         2787.9590000000003
        ],
        [
         "Selene Austin",
         5382.0464
        ],
        [
         "Jesica Fields",
         1800.4814999999999
        ],
        [
         "Willian Hardin",
         845.9820000000001
        ],
        [
         "Collen Dennis",
         4195.3079
        ],
        [
         "Carson Macias",
         7747.739
        ],
        [
         "Kasha Todd",
         19329.084899999998
        ],
        [
         "Lise Hebert",
         5015.7377
        ],
        [
         "Damien Dorsey",
         21514.461499999998
        ],
        [
         "Sarah Kirkland",
         4387.966
        ],
        [
         "Chauncey Donaldson",
         4762.4631
        ],
        [
         "Alejandro Norman",
         2509.881
        ],
        [
         "Jasmin Young",
         10336.9624
        ],
        [
         "Ciera Koch",
         5557.3307
        ],
        [
         "Daryl Spence",
         21150.892700000004
        ],
        [
         "Stephanie Browning",
         104.4905
        ],
        [
         "Dorothea Miranda",
         3243.7533999999996
        ],
        [
         "Zoraida Patton",
         7004.841
        ],
        [
         "Dottie Roberts",
         6654.473400000001
        ],
        [
         "Ileana Holt",
         4499.991
        ],
        [
         "Roy Chan",
         2717.964
        ],
        [
         "Ashanti Parks",
         16025.0715
        ],
        [
         "Shara Pope",
         5959.0657
        ],
        [
         "Carmelina Sellers",
         7157.3531
        ],
        [
         "Danny Kim",
         11055.941
        ],
        [
         "Dale Rasmussen",
         4167.846
        ],
        [
         "Marquerite Dawson",
         8072.331
        ],
        [
         "Michel Blankenship",
         2500.4381000000003
        ],
        [
         "Phillis Fowler",
         335.98400000000004
        ],
        [
         "Elma Molina",
         7111.0354
        ],
        [
         "Tereasa Bird",
         10617.973
        ],
        [
         "Zelma Browning",
         21535.666499999996
        ],
        [
         "Ashely Holmes",
         391.992
        ],
        [
         "Collin Webster",
         861.0117
        ],
        [
         "Donnetta Henson",
         3860.1454000000003
        ],
        [
         "Angelika Perry",
         2319.7539
        ],
        [
         "Kathyrn Bush",
         2011.4626
        ],
        [
         "Lore Sykes",
         3390.4649999999997
        ],
        [
         "Dwain Carlson",
         8309.4449
        ],
        [
         "Jennell Solis",
         391.992
        ],
        [
         "Maple Griffin",
         1856.6117
        ],
        [
         "Hubert Stone",
         10541.963199999998
        ],
        [
         "Bettyann Acosta",
         611.9820000000001
        ],
        [
         "Moira Lester",
         6196.644399999999
        ],
        [
         "Elenore William",
         4334.0585
        ],
        [
         "Bernetta Marquez",
         10322.972099999999
        ],
        [
         "Pamala Fowler",
         3146.4644999999996
        ],
        [
         "Maximina Hutchinson",
         2230.5485
        ],
        [
         "Klara Stanley",
         16436.065000000002
        ],
        [
         "Lanie Dunn",
         3531.3039
        ],
        [
         "Jeni Booker",
         6235.5381
        ],
        [
         "Caroll Hays",
         1571.1760000000002
        ],
        [
         "Kendra Harrington",
         4171.947899999999
        ],
        [
         "Thalia Dillard",
         16764.1256
        ],
        [
         "Holly Nieves",
         1601.3717
        ],
        [
         "Shonta Mercer",
         723.8905
        ],
        [
         "Lena Mills",
         751.984
        ],
        [
         "Charleen Joyner",
         1585.156
        ],
        [
         "Vernita Ball",
         269.99100000000004
        ],
        [
         "Yan Mcgowan",
         13546.9484
        ],
        [
         "Maryalice Henry",
         4064.8377
        ],
        [
         "Flossie Holder",
         10269.8557
        ],
        [
         "Freddie Mathis",
         1755.3725
        ],
        [
         "Hilary Savage",
         1652.981
        ],
        [
         "Scarlet Reed",
         4147.662
        ],
        [
         "Nita Guy",
         9372.3701
        ],
        [
         "Ann Heath",
         6468.2263
        ],
        [
         "Kimberely Bowen",
         15087.2644
        ],
        [
         "Sommer Hopkins",
         1256.091
        ],
        [
         "Joe Melton",
         269.99100000000004
        ],
        [
         "Kattie Stevenson",
         2681.1565
        ],
        [
         "Susann Bass",
         1001.6116999999999
        ],
        [
         "Khalilah Robertson",
         2362.1628
        ],
        [
         "Shiloh Bates",
         6330.574699999999
        ],
        [
         "Wm Pope",
         930.981
        ],
        [
         "Giselle Robles",
         692.0817
        ],
        [
         "Alysia Nicholson",
         5126.9531
        ],
        [
         "Tuyet Rosa",
         5841.099200000001
        ],
        [
         "Ramiro Byers",
         376.79200000000003
        ],
        [
         "Bettie Pierce",
         8392.9437
        ],
        [
         "Manie Maxwell",
         1546.384
        ],
        [
         "Angella Bridges",
         4062.3333999999995
        ],
        [
         "Dorthey Jackson",
         12026.9409
        ],
        [
         "Jennette Baker",
         583.9760000000001
        ],
        [
         "Janella Bright",
         513.3507
        ],
        [
         "Kenton Hughes",
         2006.0629
        ],
        [
         "Yevette Elliott",
         12104.786
        ],
        [
         "Jonna Brown",
         1394.9906999999998
        ],
        [
         "Yu Mcdonald",
         6804.958
        ],
        [
         "Shu Mays",
         8056.768000000001
        ],
        [
         "Lolita Mosley",
         6680.4439
        ],
        [
         "Blanca Hooper",
         6602.950500000001
        ],
        [
         "Joni Lee",
         422.99100000000004
        ],
        [
         "Carita Salinas",
         10792.247
        ],
        [
         "Trudy Riddle",
         4214.9468
        ],
        [
         "Jama Rodriquez",
         1818.4544999999998
        ],
        [
         "Kandi Mcneil",
         1847.0647
        ],
        [
         "Donette Mccarthy",
         9274.9654
        ],
        [
         "Magda Eaton",
         723.8905
        ],
        [
         "Collene Knox",
         12541.763399999998
        ],
        [
         "Nestor Haynes",
         1860.5825
        ],
        [
         "Latricia Lindsey",
         1174.5654
        ],
        [
         "Nichelle Rosario",
         6824.972399999999
        ],
        [
         "Julius Holt",
         3489.9734000000003
        ],
        [
         "Gertha Mejia",
         8109.950500000001
        ],
        [
         "Florencio Davenport",
         3191.9524999999994
        ],
        [
         "Shonta Preston",
         5801.933999999999
        ],
        [
         "Chere Alston",
         1139.962
        ],
        [
         "Jenise Preston",
         751.984
        ],
        [
         "Candelaria Coffey",
         14735.4152
        ],
        [
         "Ana Palmer",
         4100.4358999999995
        ],
        [
         "Paul Lester",
         17580.7168
        ],
        [
         "Conchita Boone",
         5851.9257
        ],
        [
         "Chi Goff",
         3441.2631
        ],
        [
         "Yanira Bradshaw",
         9157.756
        ],
        [
         "Armando Black",
         2843.0734
        ],
        [
         "Letitia Franco",
         12433.4557
        ],
        [
         "Vince Schneider",
         8204.530200000001
        ],
        [
         "Winfred Harris",
         3804.9214000000006
        ],
        [
         "Lenore Valdez",
         8009.032099999999
        ],
        [
         "Geraldine O'donnell",
         1441.165
        ],
        [
         "Larraine Horn",
         5017.855099999999
        ],
        [
         "Patrina Tanner",
         4539.974
        ],
        [
         "Georgeann Rojas",
         3818.2124000000003
        ],
        [
         "Evelina Byrd",
         1754.1460000000002
        ],
        [
         "Nanette Roman",
         2259.3406999999997
        ],
        [
         "Shanti Johnston",
         1863.966
        ],
        [
         "Annett Garrett",
         4156.6929
        ],
        [
         "Claris Santiago",
         5231.8529
        ],
        [
         "Clementine Mooney",
         199.99200000000002
        ],
        [
         "Carola Mcpherson",
         396.1405
        ],
        [
         "Agustina Lawrence",
         2283.8072
        ],
        [
         "Clementina Sargent",
         1208.4825
        ],
        [
         "Gwendolyn Miller",
         11349.9574
        ],
        [
         "Giovanna Jefferson",
         377.982
        ],
        [
         "Pamelia Newman",
         33634.2604
        ],
        [
         "Bennett Armstrong",
         3347.648
        ],
        [
         "Brittni Green",
         8570.9665
        ],
        [
         "Dionne Norris",
         6261.957399999999
        ],
        [
         "Ira Moore",
         1402.7740000000001
        ],
        [
         "Luciano Marsh",
         1999.3494
        ],
        [
         "Shiloh Reeves",
         1950.5750000000003
        ],
        [
         "Karl Stephens",
         5745.955199999999
        ],
        [
         "Kerrie O'neill",
         1139.981
        ],
        [
         "Rosanne George",
         3750.873199999999
        ],
        [
         "Marina Hinton",
         1885.8838999999998
        ],
        [
         "Sherita Cherry",
         719.984
        ],
        [
         "Siobhan Lang",
         6793.9655
        ],
        [
         "Eliseo Knight",
         5220.4734
        ],
        [
         "Novella Ross",
         12307.9627
        ],
        [
         "Collene Roman",
         6578.9654
        ],
        [
         "Hipolito Padilla",
         5062.3384
        ],
        [
         "Dung King",
         4115.9724
        ],
        [
         "Season Harvey",
         3185.9454
        ],
        [
         "Macie Ayers",
         9334.509399999999
        ],
        [
         "Loraine Sykes",
         3960.4315000000006
        ],
        [
         "Larae Carney",
         10187.945099999999
        ],
        [
         "Marilyn Frank",
         9499.981
        ],
        [
         "Rudolf Moran",
         4017.4401
        ],
        [
         "Angelique Merrill",
         333.59200000000004
        ],
        [
         "Sanora Webster",
         3442.8135
        ],
        [
         "Gabriella Jones",
         999.4825000000001
        ],
        [
         "Gilberte Duke",
         13107.441
        ],
        [
         "Carissa Foreman",
         170.991
        ],
        [
         "Kermit Hyde",
         908.076
        ],
        [
         "Arminda Weber",
         1044.981
        ],
        [
         "Sandee Alvarado",
         799.9920000000001
        ],
        [
         "Kam Wilder",
         4094.8481
        ],
        [
         "Valentin Mclaughlin",
         4001.9184
        ],
        [
         "Lashawna Richardson",
         11596.428899999999
        ],
        [
         "Charlesetta Soto",
         3302.1734
        ],
        [
         "Jesus Burch",
         7063.463899999999
        ],
        [
         "Nathanael Bradley",
         377.982
        ],
        [
         "Elease Dejesus",
         1217.264
        ],
        [
         "Marcell Barrett",
         1197.0725
        ],
        [
         "Lurlene Finch",
         1829.6654999999998
        ],
        [
         "Louanne Martin",
         6450.952899999999
        ],
        [
         "Domingo Casey",
         1311.2907
        ],
        [
         "Felica Munoz",
         10186.628499999999
        ],
        [
         "Miranda Kennedy",
         3254.9906999999994
        ],
        [
         "Kandace Giles",
         3247.248
        ],
        [
         "Virgen Clemons",
         7184.972399999999
        ],
        [
         "Marcy Rodriguez",
         845.9820000000001
        ],
        [
         "Trena Hudson",
         9287.9439
        ],
        [
         "Nelle Beck",
         4012.6457
        ],
        [
         "Dane Mcdaniel",
         2205.7557
        ],
        [
         "Debbra Jacobson",
         1194.2817
        ],
        [
         "Moses Pope",
         11471.895400000001
        ],
        [
         "Ross Pugh",
         3032.7401
        ],
        [
         "Mercy Brown",
         6239.278700000001
        ],
        [
         "Coleman Boyd",
         6412.5547
        ],
        [
         "Edythe Valencia",
         10949.946799999998
        ],
        [
         "Sheree Pena",
         3022.8714999999997
        ],
        [
         "Erlinda Humphrey",
         11588.6474
        ],
        [
         "Delma Bailey",
         5984.981
        ],
        [
         "Chantell Bridges",
         11993.972
        ],
        [
         "Garry Juarez",
         1805.9660000000001
        ],
        [
         "Edmund Gaines",
         989.9820000000001
        ],
        [
         "Miriam Baker",
         3723.8275
        ],
        [
         "Aimee Merritt",
         8096.4455
        ],
        [
         "Laure Pena",
         16890.1469
        ],
        [
         "Sally Kinney",
         1285.9717
        ],
        [
         "Obdulia Barber",
         543.984
        ],
        [
         "Inga Koch",
         418.4907
        ],
        [
         "Elanor Patrick",
         2136.531
        ],
        [
         "Bridgette Guerra",
         16935.6408
        ],
        [
         "Josef Greer",
         5925.560100000001
        ],
        [
         "Renita Henry",
         5442.0740000000005
        ],
        [
         "Samual Warner",
         15876.4261
        ],
        [
         "Mi Gray",
         9728.9827
        ],
        [
         "Loan Graham",
         2228.2451
        ],
        [
         "Deane Sears",
         5887.3423999999995
        ],
        [
         "Lorraine Marks",
         14141.339399999999
        ],
        [
         "Eliana Reese",
         11035.847999999998
        ],
        [
         "Janine Manning",
         7783.4219
        ],
        [
         "Luz House",
         9425.166799999999
        ],
        [
         "Kerrie Morton",
         2282.965
        ],
        [
         "Sharla Flynn",
         1729.775
        ],
        [
         "Cassondra Pruitt",
         269.99100000000004
        ],
        [
         "Graig Cannon",
         4369.3445
        ],
        [
         "Rudolf Gilliam",
         2747.2394999999997
        ],
        [
         "Zella Fernandez",
         1422.963
        ],
        [
         "Doris Kaufman",
         3167.9562
        ],
        [
         "Judith Finley",
         4397.9639
        ],
        [
         "Luciana Mcgee",
         167.99200000000002
        ],
        [
         "Chloe Patel",
         1367.0907
        ],
        [
         "Rutha Howell",
         7143.6644
        ],
        [
         "Tajuana Riddle",
         4205.981699999999
        ],
        [
         "Novella Patel",
         5107.863799999999
        ],
        [
         "Ehtel Cobb",
         3105.9644
        ],
        [
         "Romana Barnes",
         1094.9750000000001
        ],
        [
         "Agatha Melton",
         1258.972
        ],
        [
         "Jayne Kirkland",
         10802.6294
        ],
        [
         "Conrad Mueller",
         5925.474700000001
        ],
        [
         "Mariana Strong",
         2317.0840000000003
        ],
        [
         "Lee Dunn",
         12980.938699999999
        ],
        [
         "Stephen Vega",
         912.2729999999999
        ],
        [
         "Myron Ruiz",
         7350.4645
        ],
        [
         "Abram Copeland",
         24607.0261
        ],
        [
         "Tressa Weiss",
         6749.973399999999
        ],
        [
         "Douglas Richards",
         417.9905
        ],
        [
         "Alita Salinas",
         2099.9637000000002
        ],
        [
         "Corrina Sawyer",
         25612.7021
        ],
        [
         "Mellisa Farley",
         1096.1817
        ],
        [
         "Melanie Hayes",
         31913.690199999997
        ],
        [
         "Walton Dejesus",
         3011.4809999999998
        ],
        [
         "Hugh Craft",
         1856.0750000000003
        ],
        [
         "Chasidy Webster",
         959.984
        ],
        [
         "Genny Hensley",
         4507.6134
        ],
        [
         "Carter Bentley",
         4318.0054
        ],
        [
         "Daphine Willis",
         927.9840000000002
        ],
        [
         "Jone Bernard",
         12010.4969
        ],
        [
         "Loreta Johnston",
         14172.218499999999
        ],
        [
         "Andreas Mayer",
         18114.9309
        ],
        [
         "Myesha Burgess",
         5226.6626
        ],
        [
         "Skye Pope",
         3159.926
        ],
        [
         "Rosalva Hamilton",
         10529.963
        ],
        [
         "Nicholas Vazquez",
         5224.9905
        ],
        [
         "Tamela Harrell",
         17479.957000000002
        ],
        [
         "Arvilla Weiss",
         3015.9718999999996
        ],
        [
         "Nicki Larson",
         557.9814
        ],
        [
         "Ashleigh Frank",
         5219.982
        ],
        [
         "Phebe Turner",
         11120.3254
        ],
        [
         "Annabelle Hebert",
         3287.322
        ],
        [
         "Camila Carroll",
         3292.0046
        ],
        [
         "Shona Mcmillan",
         6089.983
        ],
        [
         "Rita Bailey",
         2701.1742
        ],
        [
         "Genoveva Lloyd",
         5333.335
        ],
        [
         "Lizzie Joyner",
         18995.013700000003
        ],
        [
         "Marissa Summers",
         1556.7828
        ],
        [
         "Zona Cameron",
         2696.9907
        ],
        [
         "Augustus Steele",
         519.984
        ],
        [
         "Jeni Farley",
         377.982
        ],
        [
         "Leif Short",
         877.9812
        ],
        [
         "Ebony Cotton",
         2333.356
        ],
        [
         "Mila Moody",
         12595.073
        ],
        [
         "Cecelia Gill",
         1101.683
        ],
        [
         "Corinna Adams",
         9161.946
        ],
        [
         "Londa Gould",
         6782.3368
        ],
        [
         "Claudio Wise",
         3646.9826999999996
        ],
        [
         "Cindi Larson",
         20177.7457
        ],
        [
         "Julienne Moody",
         1277.9660000000001
        ],
        [
         "Lavinia Cotton",
         753.5840000000001
        ],
        [
         "Myrl Gay",
         2474.9727
        ],
        [
         "Alfredo Dodson",
         4766.8345
        ],
        [
         "Raphael O'neil",
         2509.946
        ],
        [
         "Romeo Steele",
         4922.9485
        ],
        [
         "Bettie Glover",
         8740.966
        ],
        [
         "Cecilia Camacho",
         7971.2261
        ],
        [
         "Dollie Cervantes",
         11238.6544
        ],
        [
         "Vito Pickett",
         6754.9376
        ],
        [
         "Victor Pittman",
         2991.759
        ],
        [
         "Effie Jenkins",
         5768.214400000001
        ],
        [
         "Vernell Goff",
         1902.5629
        ],
        [
         "Jeanie Kirkland",
         15841.0992
        ],
        [
         "Honey Camacho",
         2200.8641
        ],
        [
         "Deandrea Vega",
         3172.4449
        ],
        [
         "Lolita O'neill",
         2452.948
        ],
        [
         "Hermila Mckay",
         5498.3679999999995
        ],
        [
         "Vicki Wiggins",
         6074.048199999999
        ],
        [
         "Harold O'connor",
         9725.8374
        ],
        [
         "Krystin Marshall",
         1613.3947
        ],
        [
         "Basil Ballard",
         1553.965
        ],
        [
         "Beryl Bennett",
         1301.4715
        ],
        [
         "Catherine Miles",
         1635.5468
        ],
        [
         "Darcie Morgan",
         1567.173
        ],
        [
         "Cyndi Dyer",
         1655.0719
        ],
        [
         "Lewis Garner",
         3818.2929999999997
        ],
        [
         "Tonda Armstrong",
         7179.9832
        ],
        [
         "Penni Best",
         4162.8555
        ],
        [
         "Marlo Jefferson",
         13242.962
        ],
        [
         "Ulrike Chan",
         1499.382
        ],
        [
         "Myung Hooper",
         2681.957
        ],
        [
         "Olimpia Mays",
         12774.245099999998
        ],
        [
         "Lina Meadows",
         3720.8885
        ],
        [
         "Arie Hunter",
         1287.5737000000001
        ],
        [
         "Patsy Russo",
         1060.1721
        ],
        [
         "Travis Goodman",
         2446.941
        ],
        [
         "Eric Hardin",
         2065.9827
        ],
        [
         "Babara Ochoa",
         2963.9809999999998
        ],
        [
         "Oliva Blackwell",
         6382.9455
        ],
        [
         "India Barron",
         2873.9400000000005
        ],
        [
         "Jasper Castro",
         557.9814
        ],
        [
         "Nettie Mcdaniel",
         3801.6487
        ],
        [
         "Barry Buckner",
         1467.9554
        ],
        [
         "Edra Fitzgerald",
         2297.7574999999997
        ],
        [
         "Herlinda Stone",
         7067.962799999998
        ],
        [
         "Tisa Whitney",
         3196.2044
        ],
        [
         "Vashti Rosario",
         9865.4727
        ],
        [
         "Kellye Campbell",
         6829.531
        ],
        [
         "Tama Berg",
         2966.6441999999997
        ],
        [
         "Rona Rojas",
         7439.981399999999
        ],
        [
         "Cherelle Key",
         1052.9630000000002
        ],
        [
         "Cheree Hale",
         5122.348
        ],
        [
         "Dannette Guerrero",
         7719.957
        ],
        [
         "Crystle Gilliam",
         4296.181500000001
        ],
        [
         "Shea Howell",
         2319.9680000000003
        ],
        [
         "Emmett Casey",
         3194.082
        ],
        [
         "Soledad Moses",
         3168.5541
        ],
        [
         "Elaina Key",
         6929.1049
        ],
        [
         "Mica Barry",
         279.992
        ],
        [
         "Cassie Cline",
         6987.248700000001
        ],
        [
         "Carina Lynch",
         2707.8278
        ],
        [
         "Marlen Dawson",
         2932.4811999999997
        ],
        [
         "Heather Perry",
         718.4000000000001
        ],
        [
         "Mellisa Griffin",
         10050.6281
        ],
        [
         "Tomasa Carson",
         16338.9384
        ],
        [
         "Jamika Acevedo",
         269.99100000000004
        ],
        [
         "Georgina Gonzales",
         5417.9727
        ],
        [
         "Ciera Webb",
         629.9820000000001
        ],
        [
         "Morton Lee",
         3290.7715
        ],
        [
         "Sherril Alvarado",
         5723.7441
        ],
        [
         "Ilda Roberson",
         2379.4635
        ],
        [
         "Dorine Roberson",
         12320.120700000001
        ],
        [
         "Felice Guzman",
         10156.896799999999
        ],
        [
         "Jutta Everett",
         1127.992
        ],
        [
         "Romelia Myers",
         5440.362399999999
        ],
        [
         "Florrie Little",
         9919.921
        ],
        [
         "Damian Dawson",
         2069.3725
        ],
        [
         "Cleopatra Tate",
         12909.9214
        ],
        [
         "Berna Moore",
         949.9905
        ],
        [
         "Serina Hensley",
         1690.6635
        ],
        [
         "Ricki Bullock",
         7183.3227
        ],
        [
         "Lyndsey Bean",
         32675.072499999995
        ],
        [
         "Jenniffer Bullock",
         17746.5951
        ],
        [
         "Marylyn Browning",
         655.1907
        ],
        [
         "Shawnna Frank",
         2705.007
        ],
        [
         "Luis Tyler",
         2749.3474
        ],
        [
         "Crysta Velez",
         3567.561
        ],
        [
         "Regenia Vaughan",
         14529.258299999998
        ],
        [
         "Raul Melendez",
         2770.9629999999997
        ],
        [
         "Barbera Riggs",
         7486.3314
        ],
        [
         "Courtney Wyatt",
         7823.944000000001
        ],
        [
         "Lise Alvarado",
         576.7917
        ],
        [
         "Emelda Dickerson",
         1422.4825
        ],
        [
         "Delaine Estes",
         799.984
        ],
        [
         "Nikita Roy",
         1611.0747000000001
        ],
        [
         "Deshawn Mendoza",
         3690.2361
        ],
        [
         "Sharell Ross",
         3594.863
        ],
        [
         "Tangela Quinn",
         9205.1175
        ],
        [
         "Dexter Roberts",
         2963.9809999999998
        ],
        [
         "Chantay Maynard",
         7327.040100000001
        ],
        [
         "Martha Burgess",
         1227.5814
        ],
        [
         "Cori Schwartz",
         12400.848
        ],
        [
         "Jerri Henry",
         1576.7820000000002
        ],
        [
         "Consuela Romero",
         1599.9840000000002
        ],
        [
         "Renna Williams",
         7021.1487
        ],
        [
         "Hope Cotton",
         1238.566
        ],
        [
         "Lucio Sherman",
         6672.2946999999995
        ],
        [
         "Kermit Bowman",
         7253.619500000001
        ],
        [
         "Efren Whitfield",
         3110.8567000000003
        ],
        [
         "Mikel Wilkerson",
         351.992
        ],
        [
         "Phuong Wolf",
         5686.5815
        ],
        [
         "Shiela Calderon",
         2768.3634
        ],
        [
         "Renato Morton",
         2716.7650000000003
        ],
        [
         "Wynona Douglas",
         16491.52
        ],
        [
         "Jeffry Church",
         1512.891
        ],
        [
         "Whitley Cannon",
         3975.2343
        ],
        [
         "Lloyd Miranda",
         170.991
        ],
        [
         "Bea Kane",
         2643.2447
        ],
        [
         "Trista Lambert",
         5922.4725
        ],
        [
         "Mina Carrillo",
         6671.6012
        ],
        [
         "Glady Wells",
         325.4907
        ],
        [
         "Genny Fields",
         2615.976
        ],
        [
         "Trinity Riddle",
         7211.723399999999
        ],
        [
         "Margret Barnett",
         11831.3359
        ],
        [
         "Deangelo Cooley",
         314.99100000000004
        ],
        [
         "Lashunda Cole",
         6591.976000000001
        ],
        [
         "Aide Franco",
         2605.2824
        ],
        [
         "Kaylee English",
         4775.9635
        ],
        [
         "Inocencia Key",
         4949.991
        ],
        [
         "Delana Wagner",
         1464.2552
        ],
        [
         "Alyse Jacobson",
         11062.4171
        ],
        [
         "Aleta Stone",
         418.4907
        ],
        [
         "Randee Lester",
         700.792
        ],
        [
         "Penny Acevedo",
         18670.9288
        ],
        [
         "Tu Ramirez",
         6467.6551
        ],
        [
         "Somer Jordan",
         12663.956
        ],
        [
         "Adena Blake",
         19329.9492
        ],
        [
         "Oralia Farley",
         5893.554999999999
        ],
        [
         "Gustavo Gamble",
         4204.525799999999
        ],
        [
         "Janae Doyle",
         3920.663
        ],
        [
         "Parthenia Holman",
         15205.928399999999
        ],
        [
         "Benito Hendrix",
         9645.3834
        ],
        [
         "Pinkie Kirkland",
         11476.536399999999
        ],
        [
         "Krissy Ochoa",
         4814.6255
        ],
        [
         "Yang Giles",
         5244.955
        ],
        [
         "Pearl Fox",
         1494.9554
        ],
        [
         "Sherilyn Wilcox",
         2411.4715
        ],
        [
         "Alissa Hood",
         14567.157
        ],
        [
         "Katelin Kennedy",
         7568.9310000000005
        ],
        [
         "Wendie Nash",
         3950.3624
        ],
        [
         "Margorie Wynn",
         8498.463
        ],
        [
         "Buford Gilbert",
         9044.927
        ],
        [
         "Diana Reyes",
         1064.682
        ],
        [
         "Kate Barber",
         6495.972
        ],
        [
         "Rozella Fitzgerald",
         480.591
        ],
        [
         "Ivelisse Nixon",
         10951.5614
        ],
        [
         "Cristobal Hutchinson",
         1716.5529999999999
        ],
        [
         "Marjory Leonard",
         6723.0765
        ],
        [
         "Tammy Austin",
         13765.5468
        ],
        [
         "Sherise Mercer",
         1619.991
        ],
        [
         "Hilde Nieves",
         4459.2184
        ],
        [
         "Willow Gardner",
         2190.566
        ],
        [
         "Sonja Walls",
         176.6907
        ],
        [
         "Jenna Saunders",
         993.2213999999999
        ],
        [
         "Lamar Greer",
         2511.4647000000004
        ],
        [
         "Eloisa Tucker",
         3377.973
        ],
        [
         "Dorine Thornton",
         2834.8444
        ],
        [
         "Malisa Mitchell",
         7575.3454
        ],
        [
         "Kim Clark",
         2664.9644
        ],
        [
         "Majorie Glover",
         1899.981
        ],
        [
         "Trang Hardin",
         5732.4652
        ],
        [
         "Devin Shaffer",
         1389.772
        ],
        [
         "Tad Gardner",
         2195.5747
        ],
        [
         "Julia Joyner",
         3995.6247000000003
        ],
        [
         "Rodrigo Durham",
         1037.3715
        ],
        [
         "Lucilla Williams",
         949.1727000000001
        ],
        [
         "Joy Underwood",
         989.9820000000001
        ],
        [
         "Brianne Hays",
         3722.9829999999997
        ],
        [
         "Kathie Freeman",
         3962.0287
        ],
        [
         "Coleen Navarro",
         10728.4385
        ],
        [
         "Ocie Slater",
         7999.962999999999
        ],
        [
         "Lillia Gillespie",
         4130.3445
        ],
        [
         "Tilda Melton",
         1063.8921
        ],
        [
         "Virgil Frost",
         1026.7014
        ],
        [
         "Jule Davenport",
         4298.4537
        ],
        [
         "Tonja Bean",
         8787.1297
        ],
        [
         "Edris Barrett",
         17494.9405
        ],
        [
         "Alejandro Haney",
         16846.953999999998
        ],
        [
         "Shay Stephenson",
         3671.7054
        ],
        [
         "Neida King",
         1590.8534
        ],
        [
         "Dori Alvarez",
         1949.6365
        ],
        [
         "Gussie Harding",
         1595.6657
        ],
        [
         "Monty Frost",
         13947.544899999999
        ],
        [
         "Caroline Jenkins",
         170.991
        ],
        [
         "Tobie Little",
         17123.997499999998
        ],
        [
         "Agnes Sims",
         2891.7542000000003
        ],
        [
         "Keturah Reid",
         7091.936699999999
        ],
        [
         "Desiree Branch",
         466.84139999999996
        ],
        [
         "Hye Mercer",
         440.99100000000004
        ],
        [
         "Tempie Jacobson",
         7049.673
        ],
        [
         "Wai Soto",
         4912.157
        ],
        [
         "Mary Singleton",
         1536.1215
        ],
        [
         "Arline Lawson",
         7995.8047
        ],
        [
         "Karole Alvarez",
         7159.9556999999995
        ],
        [
         "Valeri Marshall",
         5834.1357
        ],
        [
         "Janelle Maldonado",
         1353.748
        ],
        [
         "Ira Erickson",
         12392.9547
        ],
        [
         "Brittney Woodward",
         11035.7581
        ],
        [
         "Ken Charles",
         9833.6547
        ],
        [
         "Douglass Blankenship",
         1951.3474
        ],
        [
         "Adrien Hunter",
         1234.9715
        ],
        [
         "Bong Hebert",
         14208.388099999998
        ],
        [
         "Molly Langley",
         814.6707
        ],
        [
         "Vance Taylor",
         697.4907
        ],
        [
         "Barton Crosby",
         7526.036700000001
        ],
        [
         "Shanelle Anderson",
         507.2905
        ],
        [
         "Eliz Whitney",
         1662.0538999999999
        ],
        [
         "Cesar Jackson",
         11705.851999999999
        ],
        [
         "Candis Harding",
         2548.9732
        ],
        [
         "Antony Atkinson",
         208.981
        ],
        [
         "Tam Fisher",
         3439.1719
        ],
        [
         "Piedad Irwin",
         706.7814
        ],
        [
         "Risa Gallagher",
         4445.0608999999995
        ],
        [
         "Anya Contreras",
         1497.4827
        ],
        [
         "Cami Williamson",
         1233.6722
        ],
        [
         "Qiana Jackson",
         1988.0501
        ],
        [
         "Lekisha Pope",
         527.7812
        ],
        [
         "Andria Rivers",
         4327.0254
        ],
        [
         "Lizzette Stein",
         16739.995799999997
        ],
        [
         "Elenore Hensley",
         4789.734799999999
        ],
        [
         "Willis Randolph",
         2899.4846
        ],
        [
         "Celestine Kent",
         10998.0295
        ],
        [
         "Nathalie Knowles",
         4231.121999999999
        ],
        [
         "Letisha May",
         9927.2049
        ],
        [
         "Verdell Joyner",
         1567.4715
        ],
        [
         "Philip Bryan",
         1368.0717
        ],
        [
         "Gilbert Calhoun",
         15097.905999999999
        ],
        [
         "Bernardina Cooper",
         12867.958
        ],
        [
         "Minnie Compton",
         8336.4169
        ],
        [
         "Narcisa Knapp",
         279.992
        ],
        [
         "Jenell Crosby",
         524.3905
        ],
        [
         "Catarina Mendez",
         9908.4642
        ],
        [
         "Yvone Yates",
         6515.955
        ],
        [
         "Kiana Rivera",
         13033.5961
        ],
        [
         "Sharie Whitaker",
         6762.1399
        ],
        [
         "Bettye Espinoza",
         5627.956999999999
        ],
        [
         "Arvilla Osborn",
         10805.3354
        ],
        [
         "Lynda Newman",
         1868.9634
        ],
        [
         "Myrtle Gardner",
         1753.7717
        ],
        [
         "Stacie Sims",
         7040.8464
        ],
        [
         "Efren Oliver",
         11463.958
        ],
        [
         "Priscilla Wilkins",
         3599.991
        ],
        [
         "Natosha Rowland",
         2658.7627
        ],
        [
         "Kaley Blanchard",
         6578.9291
        ],
        [
         "Heather Chaney",
         5528.957
        ],
        [
         "Nakisha Clay",
         2800.2975000000006
        ],
        [
         "Maira Long",
         5588.5185
        ],
        [
         "Mechelle Chan",
         1210.2714999999998
        ],
        [
         "Rolanda Larsen",
         3136.0432
        ],
        [
         "Jacalyn Barnett",
         502.1907
        ],
        [
         "Ami Mcmahon",
         2840.0460999999996
        ],
        [
         "Junita Reese",
         242.991
        ],
        [
         "Sharyn Brewer",
         3994.4559
        ],
        [
         "Daisy Ward",
         6023.9545
        ],
        [
         "Lucile Manning",
         2032.4445
        ],
        [
         "Tajuana Rollins",
         7782.873
        ],
        [
         "Marcene Curtis",
         3668.9260000000004
        ],
        [
         "Charmain Webster",
         17834.963399999997
        ],
        [
         "Ollie Zimmerman",
         5371.338
        ],
        [
         "Onita Johns",
         2270.5392
        ],
        [
         "Treasa Dickerson",
         889.5840000000001
        ],
        [
         "Yan Trevino",
         11391.43
        ],
        [
         "Everett Vega",
         1304.9750000000001
        ],
        [
         "Kallie Best",
         11428.653
        ],
        [
         "Jewell Reyes",
         1019.963
        ],
        [
         "Jeffrey Hill",
         1845.882
        ],
        [
         "Izola Hobbs",
         3439.4575
        ],
        [
         "Terra Pickett",
         11787.5533
        ],
        [
         "Eleanor Mendez",
         4829.1825
        ],
        [
         "Eliana Silva",
         4236.3466
        ],
        [
         "Verna Solis",
         3799.1634
        ],
        [
         "Kaila Walters",
         1367.984
        ],
        [
         "Clare Neal",
         2357.9642
        ],
        [
         "Nenita Mooney",
         5806.037499999999
        ],
        [
         "Rudolph Velez",
         8263.867
        ],
        [
         "Nanette Harris",
         2559.992
        ],
        [
         "Alina Mcleod",
         13287.526199999998
        ],
        [
         "Genevie Miles",
         1850.0567
        ],
        [
         "Sung Chambers",
         5115.9641
        ],
        [
         "Grisel Maynard",
         989.991
        ],
        [
         "Jeromy Burch",
         11907.9041
        ],
        [
         "Letty Cobb",
         8820.1505
        ],
        [
         "Danielle Bond",
         18553.730000000003
        ],
        [
         "Carter Booth",
         1416.573
        ],
        [
         "Ling Newman",
         5699.981
        ],
        [
         "Robena Hill",
         13783.7813
        ],
        [
         "Tommie Cooley",
         8011.311999999999
        ],
        [
         "Aron Wiggins",
         10047.424500000001
        ],
        [
         "Teofila Fischer",
         23195.075399999998
        ],
        [
         "Terrance Lynn",
         7536.1622
        ],
        [
         "Rubin Decker",
         2484.4274
        ],
        [
         "Jeannette Skinner",
         2889.8561
        ],
        [
         "Justina Long",
         9327.738
        ],
        [
         "Corrinne Garrison",
         8481.898000000001
        ],
        [
         "Lakenya Oliver",
         1099.4814999999999
        ],
        [
         "Laurette Hebert",
         2309.3035
        ],
        [
         "Shanice Spears",
         11299.972
        ],
        [
         "Leola Gould",
         613.7907
        ],
        [
         "Willetta Murphy",
         2200.9444
        ],
        [
         "Angele Castro",
         1082.9715
        ],
        [
         "Melia Brady",
         14011.8265
        ],
        [
         "Jenee Rasmussen",
         12861.8789
        ],
        [
         "Shae Hickman",
         18281.4729
        ],
        [
         "Garret Clay",
         3346.0319
        ],
        [
         "Elvina Gates",
         2780.5470000000005
        ],
        [
         "Veronika Rollins",
         10132.3624
        ],
        [
         "Jane Henderson",
         3793.1580000000004
        ],
        [
         "Merideth Preston",
         11832.453899999999
        ],
        [
         "Melodie Melton",
         7984.939
        ],
        [
         "Lamar Bush",
         2093.4134999999997
        ],
        [
         "Earl Stanley",
         5315.9042
        ],
        [
         "Jeanice Frost",
         19992.864800000003
        ],
        [
         "Elmo Sweeney",
         2518.1494000000002
        ],
        [
         "Ilona Spears",
         8712.8466
        ],
        [
         "Cassidy Clark",
         633.6245
        ],
        [
         "Caridad Compton",
         8945.75
        ],
        [
         "Nicolas Carlson",
         5863.4454
        ],
        [
         "Charise Burt",
         1250.8636999999999
        ],
        [
         "Edith Davenport",
         1243.7847000000002
        ],
        [
         "Shanita Wiley",
         2217.6427
        ],
        [
         "Porter Bass",
         4305.9576
        ],
        [
         "Sylvester Chan",
         728.9730000000001
        ],
        [
         "Georgeanna Webster",
         593.991
        ],
        [
         "Abby Gamble",
         32803.0062
        ],
        [
         "Kylee Dickson",
         837.9827
        ],
        [
         "Jessika Bray",
         1113.2655
        ],
        [
         "Carline Collier",
         5073.0365
        ],
        [
         "Janetta Aguirre",
         17783.487399999998
        ],
        [
         "Queenie Vance",
         3056.9624
        ],
        [
         "Mellie Puckett",
         5835.858
        ],
        [
         "Sheila Travis",
         5579.962799999999
        ],
        [
         "Jenine Dawson",
         7938.9374
        ],
        [
         "Cher Alston",
         3866.0454
        ],
        [
         "Ayana Keith",
         4685.0969
        ],
        [
         "Rod Hatfield",
         3546.929
        ],
        [
         "Cicely Deleon",
         6701.455
        ],
        [
         "Erma Salinas",
         2658.1454
        ],
        [
         "Minerva Decker",
         12369.6265
        ],
        [
         "Augustina Joyner",
         20509.425399999996
        ],
        [
         "Delfina Gilliam",
         4274.981
        ],
        [
         "Jana Thomas",
         14397.1379
        ],
        [
         "Ruth Horton",
         4499.991
        ],
        [
         "Hae Ramirez",
         12089.981399999999
        ],
        [
         "Mellisa Kim",
         2975.9906999999994
        ],
        [
         "Raeann Duncan",
         4030.9569999999994
        ],
        [
         "Todd Waters",
         12381.8274
        ],
        [
         "Vivian Deleon",
         1681.4809999999998
        ],
        [
         "Deanne Parsons",
         9942.14
        ],
        [
         "Alishia Elliott",
         7951.146799999999
        ],
        [
         "Ashanti Hammond",
         17758.349000000002
        ],
        [
         "Sarita Parks",
         15314.013200000001
        ],
        [
         "Muriel Juarez",
         10570.471899999999
        ],
        [
         "Brigid Sharp",
         20648.9537
        ],
        [
         "Bess Mcbride",
         18853.354399999997
        ],
        [
         "Kara Higgins",
         8127.9469
        ],
        [
         "Shenna Benton",
         1797.975
        ],
        [
         "Nicola Knight",
         4226.230500000001
        ],
        [
         "Malinda Baxter",
         2312.4447
        ],
        [
         "Christopher Richardson",
         1394.9814
        ],
        [
         "Katia Henry",
         9479.9557
        ],
        [
         "Santa Larson",
         8445.9545
        ],
        [
         "Yevette Todd",
         4863.968000000001
        ],
        [
         "Maurice Norton",
         1439.9840000000002
        ],
        [
         "Berneice Pollard",
         892.981
        ],
        [
         "Takako Casey",
         1855.3325
        ],
        [
         "Regine Odom",
         8303.3719
        ],
        [
         "Gilberto Parsons",
         12935.949399999998
        ],
        [
         "Loni Mullen",
         451.78200000000004
        ],
        [
         "Shena Carter",
         24890.6244
        ],
        [
         "Deirdre Ryan",
         6803.971899999999
        ],
        [
         "Jamaal Morrison",
         9173.381699999998
        ],
        [
         "Ja Dillard",
         7947.442
        ],
        [
         "Spring Hayes",
         4737.2644
        ],
        [
         "Tena Cruz",
         3037.1354999999994
        ],
        [
         "Rey Lindsay",
         8327.9477
        ],
        [
         "Aida Koch",
         3865.7654
        ],
        [
         "Alma Peck",
         1209.4747
        ],
        [
         "Latonya Dixon",
         3149.991
        ],
        [
         "Karren Stevenson",
         5891.162399999999
        ],
        [
         "Cameron Carroll",
         5419.973
        ],
        [
         "Kiesha Bond",
         1228.5207
        ],
        [
         "Jimmy Russell",
         18278.9436
        ],
        [
         "Marguerite Berger",
         9712.9515
        ],
        [
         "Nubia Anderson",
         1538.964
        ],
        [
         "Joel Wynn",
         2419.7634
        ],
        [
         "Mathilda Pennington",
         1987.966
        ],
        [
         "Renay Atkins",
         5332.9467
        ],
        [
         "Joaquin Hawkins",
         6259.265
        ],
        [
         "Elmira Levy",
         6718.5542
        ],
        [
         "Lynwood Jackson",
         6843.9442
        ],
        [
         "Dung Reid",
         5515.9646999999995
        ],
        [
         "Jeniffer Slater",
         2699.991
        ],
        [
         "Celestine Jacobs",
         6971.553699999999
        ],
        [
         "Tenisha Lyons",
         20086.370799999997
        ],
        [
         "Hortencia O'neil",
         1793.7574
        ],
        [
         "Kenyetta Mason",
         2013.9650000000001
        ],
        [
         "Tena Huber",
         11183.043399999999
        ],
        [
         "Erik Leblanc",
         4749.981
        ],
        [
         "Zora Ford",
         7663.9490000000005
        ],
        [
         "Lara Guy",
         3659.9825
        ],
        [
         "James Robles",
         9314.8357
        ],
        [
         "Desire Mcgowan",
         1392.2730000000001
        ],
        [
         "Stefany Potter",
         6183.5624
        ],
        [
         "Louis Powell",
         2738.2497000000003
        ],
        [
         "Linnie Branch",
         9586.801800000001
        ],
        [
         "Earlean Pena",
         14249.6462
        ],
        [
         "Cassandra Nichols",
         377.982
        ],
        [
         "Bella Perez",
         5444.955999999999
        ],
        [
         "Kellie Franco",
         5399.982
        ],
        [
         "Parthenia Figueroa",
         1257.972
        ],
        [
         "Katherin Clark",
         5777.7667
        ],
        [
         "Ruthanne Franco",
         17611.957000000002
        ],
        [
         "Monica Sears",
         17193.9034
        ],
        [
         "Diane Jones",
         7256.773799999999
        ],
        [
         "Tiny French",
         6102.963
        ],
        [
         "Carolann Russell",
         4521.8839
        ],
        [
         "Cinthia Poole",
         4458.955
        ],
        [
         "Rayford Simon",
         1023.984
        ],
        [
         "Bev Chang",
         5291.965
        ],
        [
         "Lavern Orr",
         3644.045
        ],
        [
         "Erna Sloan",
         9849.074
        ],
        [
         "Sheree Blanchard",
         531.981
        ],
        [
         "Jonell Rivas",
         3535.2758999999996
        ],
        [
         "Selene Vega",
         2119.259
        ],
        [
         "Ester Acevedo",
         7999.984
        ],
        [
         "Lavina Dejesus",
         10314.924799999999
        ],
        [
         "Emory O'connor",
         2135.0624
        ],
        [
         "Latoya Johns",
         6530.911899999999
        ],
        [
         "Addie Hahn",
         14935.0311
        ],
        [
         "Patria Harper",
         1055.9840000000002
        ],
        [
         "Tara Maynard",
         601.5812
        ],
        [
         "Mazie Fernandez",
         7394.964400000001
        ],
        [
         "Gayla Sims",
         1519.2
        ],
        [
         "Britteny Schroeder",
         232.4907
        ],
        [
         "Frederica Rojas",
         13191.9384
        ],
        [
         "Laurel Schultz",
         5923.9551
        ],
        [
         "Zenia Bruce",
         1041.5814
        ],
        [
         "Homer Powers",
         3039.9809999999998
        ],
        [
         "Dortha Jarvis",
         14405.0464
        ],
        [
         "Jerlene Rios",
         10266.9542
        ],
        [
         "Julianne Shannon",
         7659.3381
        ],
        [
         "Orval Hunter",
         2877.7652000000003
        ],
        [
         "Emmett Hahn",
         4700.0626999999995
        ],
        [
         "Damian Mills",
         6396.9646999999995
        ],
        [
         "Barry Albert",
         3227.391
        ],
        [
         "Reita Dickson",
         3766.6347
        ],
        [
         "Sandy Mills",
         3229.9525000000003
        ],
        [
         "Lurlene Cotton",
         4399.992
        ],
        [
         "Whitney Estes",
         674.991
        ],
        [
         "Sheba Knapp",
         11972.927099999999
        ],
        [
         "Sophia Mcmillan",
         13773.627700000001
        ],
        [
         "Kristy Watkins",
         1396.4904999999999
        ],
        [
         "Mireille Puckett",
         2320.5564000000004
        ],
        [
         "Leland Mcdowell",
         377.982
        ],
        [
         "Fairy Robinson",
         4041.1537
        ],
        [
         "Greta Page",
         1245.973
        ],
        [
         "Hue May",
         6887.1357
        ],
        [
         "Shanda Stevenson",
         4960.4587
        ],
        [
         "Ping Quinn",
         2804.1440000000002
        ],
        [
         "Desmond Rose",
         14566.4345
        ],
        [
         "Wanita Davenport",
         2319.976
        ],
        [
         "Louise Flowers",
         4196.9552
        ],
        [
         "Dorothea Chang",
         13821.530999999999
        ],
        [
         "Stan Saunders",
         8936.446
        ],
        [
         "Cayla Johnson",
         1253.981
        ],
        [
         "Fannie Jenkins",
         9532.3529
        ],
        [
         "Katherina Odom",
         3643.5440000000003
        ],
        [
         "Tameka Fisher",
         24051.527899999994
        ],
        [
         "Alisia Albert",
         6150.9367
        ],
        [
         "Wilda Petersen",
         6813.7535
        ],
        [
         "Emanuel Mckee",
         5833.974699999999
        ],
        [
         "Thalia Horne",
         727.984
        ],
        [
         "Hayden Cross",
         631.6747
        ],
        [
         "Marshall Johnson",
         1669.9825
        ],
        [
         "Yuk Vega",
         7952.0464
        ],
        [
         "Guillermina Noble",
         22061.0729
        ],
        [
         "Karey Steele",
         2478.4
        ],
        [
         "Cyndi Bush",
         1681.9740000000002
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "customer_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "lifetime_value",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": [
       "Databricks visualization. Run in Databricks to view."
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1.subcommand+json": {
       "baseErrorDetails": null,
       "bindings": {},
       "collapsed": false,
       "command": "%python\n__backend_agg_display_orig = display\n__backend_agg_dfs = []\ndef __backend_agg_display_new(df):\n    __backend_agg_df_modules = [\"pandas.core.frame\", \"databricks.koalas.frame\", \"pyspark.sql.dataframe\", \"pyspark.pandas.frame\", \"pyspark.sql.connect.dataframe\", \"pyspark.sql.classic.dataframe\"]\n    if (type(df).__module__ in __backend_agg_df_modules and type(df).__name__ == 'DataFrame') or isinstance(df, list):\n        __backend_agg_dfs.append(df)\n\ndisplay = __backend_agg_display_new\n\ndef __backend_agg_user_code_fn():\n    import base64\n    exec(base64.standard_b64decode(\"ZnJvbSBweXNwYXJrLnNxbC53aW5kb3cgaW1wb3J0IFdpbmRvdwoKY3VzdG9tZXJfc2FsZXMgPSAoCiAgICBzcGFyay50YWJsZSgiYmlrZXJfcl9wcm9qZWN0LmdvbGQuc2FsZXNfZmFjdCIpCiAgICAuZ3JvdXBCeSgiY3VzdG9tZXJfbmFtZSIpCiAgICAuYWdnKHN1bSgicmV2ZW51ZSIpLmFsaWFzKCJsaWZldGltZV92YWx1ZSIpKQopCgpkaXNwbGF5KGN1c3RvbWVyX3NhbGVzKQ==\").decode())\n\ntry:\n    # run user code\n    __backend_agg_user_code_fn()\n\n    #reset display function\n    display = __backend_agg_display_orig\n\n    if len(__backend_agg_dfs) > 0:\n        # create a temp view\n        if type(__backend_agg_dfs[0]).__module__ == \"databricks.koalas.frame\":\n            # koalas dataframe\n            __backend_agg_dfs[0].to_spark().createOrReplaceTempView(\"DatabricksView13de587\")\n        elif type(__backend_agg_dfs[0]).__module__ == \"pandas.core.frame\" or isinstance(__backend_agg_dfs[0], list):\n            # pandas dataframe\n            spark.createDataFrame(__backend_agg_dfs[0]).createOrReplaceTempView(\"DatabricksView13de587\")\n        else:\n            __backend_agg_dfs[0].createOrReplaceTempView(\"DatabricksView13de587\")\n        #run backend agg\n        display(spark.sql(\"\"\"WITH q AS (select * from DatabricksView13de587) ,min_max AS (SELECT `lifetime_value`,(SELECT MAX(`lifetime_value`) FROM q) `target_column_max`,(SELECT MIN(`lifetime_value`) FROM q) `target_column_min` FROM q) ,histogram_meta AS (SELECT `lifetime_value`,`target_column_min` `min_value`,IF(`target_column_max` = `target_column_min`,`target_column_max` + 1,`target_column_max`) `max_value`,(`target_column_max` - `target_column_min`) / 10 `step` FROM min_max) SELECT IF(ISNULL(`lifetime_value`),NULL,LEAST(WIDTH_BUCKET(`lifetime_value`,`min_value`,`max_value`,10),10)) `lifetime_value_BIN`,FIRST(`min_value` + ((IF(ISNULL(`lifetime_value`),NULL,LEAST(WIDTH_BUCKET(`lifetime_value`,`min_value`,`max_value`,10),10)) - 1) * `step`)) `lifetime_value_BIN_LOWER_BOUND`,FIRST(`step`) `lifetime_value_BIN_STEP`,COUNT(`lifetime_value`) `COUNT` FROM histogram_meta GROUP BY `lifetime_value_BIN`\"\"\"))\n    else:\n        displayHTML(\"dataframe no longer exists. If you're using dataframe.display(), use display(dataframe) instead.\")\n\n\nfinally:\n    spark.sql(\"drop view if exists DatabricksView13de587\")\n    display = __backend_agg_display_orig\n    del __backend_agg_display_new\n    del __backend_agg_display_orig\n    del __backend_agg_dfs\n    del __backend_agg_user_code_fn\n\n",
       "commandTitle": "Visualization 1",
       "commandType": "auto",
       "commandVersion": 0,
       "commentThread": [],
       "commentsVisible": false,
       "contentSha256Hex": null,
       "customPlotOptions": {
        "redashChart": [
         {
          "key": "type",
          "value": "CHART"
         },
         {
          "key": "options",
          "value": {
           "alignYAxesAtZero": true,
           "coefficient": 1,
           "columnConfigurationMap": {
            "x": {
             "column": "lifetime_value",
             "id": "column_26923a16333"
            }
           },
           "dateTimeFormat": "DD/MM/YYYY HH:mm",
           "direction": {
            "type": "counterclockwise"
           },
           "error_y": {
            "type": "data",
            "visible": true
           },
           "globalSeriesType": "histogram",
           "isAggregationOn": true,
           "legend": {
            "traceorder": "normal"
           },
           "missingValuesAsZero": true,
           "numBins": 10,
           "numberFormat": "0,0.[00000]",
           "percentFormat": "0[.]00%",
           "series": {
            "error_y": {
             "type": "data",
             "visible": true
            },
            "stacking": null
           },
           "seriesOptions": {},
           "showDataLabels": false,
           "sizemode": "diameter",
           "sortX": true,
           "sortY": true,
           "swappedAxes": false,
           "textFormat": "",
           "useAggregationsUi": true,
           "valuesOptions": {},
           "version": 2,
           "xAxis": {
            "labels": {
             "enabled": true
            },
            "type": "-"
           },
           "yAxis": [
            {
             "type": "-"
            },
            {
             "opposite": true,
             "type": "-"
            }
           ]
          }
         }
        ]
       },
       "datasetPreviewNameToCmdIdMap": {},
       "diffDeletes": [],
       "diffInserts": [],
       "displayType": "redashChart",
       "error": null,
       "errorDetails": null,
       "errorSummary": null,
       "errorTraceType": null,
       "finishTime": 0,
       "globalVars": {},
       "guid": "",
       "height": "auto",
       "hideCommandCode": false,
       "hideCommandResult": false,
       "iPythonMetadata": null,
       "inputWidgets": {},
       "isLockedInExamMode": false,
       "latestAssumeRoleInfo": null,
       "latestUser": "a user",
       "latestUserId": null,
       "listResultMetadata": null,
       "metadata": {},
       "nuid": "7c8eb841-776a-4a54-9338-a3c2a88d4d03",
       "origId": 0,
       "parentHierarchy": [],
       "pivotAggregation": null,
       "pivotColumns": null,
       "position": 29.0,
       "resultDbfsErrorMessage": null,
       "resultDbfsStatus": "INLINED_IN_TREE",
       "results": null,
       "showCommandTitle": false,
       "startTime": 0,
       "state": "input",
       "streamStates": {},
       "subcommandOptions": {
        "queryPlan": {
         "groups": [
          {
           "column": "lifetime_value_BIN",
           "type": "column"
          }
         ],
         "selects": [
          {
           "alias": "lifetime_value_BIN",
           "args": [
            {
             "column": "lifetime_value",
             "type": "column"
            },
            {
             "number": 10,
             "type": "number"
            }
           ],
           "function": "BIN",
           "type": "function"
          },
          {
           "alias": "lifetime_value_BIN_LOWER_BOUND",
           "args": [
            {
             "column": "lifetime_value",
             "type": "column"
            },
            {
             "number": 10,
             "type": "number"
            }
           ],
           "function": "BIN_LOWER_BOUND",
           "type": "function"
          },
          {
           "alias": "lifetime_value_BIN_STEP",
           "args": [
            {
             "column": "lifetime_value",
             "type": "column"
            },
            {
             "number": 10,
             "type": "number"
            }
           ],
           "function": "BIN_STEP",
           "type": "function"
          },
          {
           "alias": "COUNT",
           "args": [
            {
             "column": "lifetime_value",
             "type": "column"
            }
           ],
           "function": "COUNT",
           "type": "function"
          }
         ]
        }
       },
       "submitTime": 0,
       "subtype": "tableResultSubCmd.visualization",
       "tableResultIndex": 0,
       "tableResultSettingsMap": {},
       "useConsistentColors": false,
       "version": "CommandV1",
       "width": "auto",
       "workflows": [],
       "xColumns": null,
       "yColumns": null
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from pyspark.sql.window import Window\n",
    "\n",
    "customer_sales = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\"customer_name\")\n",
    "    .agg(sum(\"revenue\").alias(\"lifetime_value\"))\n",
    ")\n",
    "\n",
    "display(customer_sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "f3874259-31f4-4361-99c3-c2766ef53777",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>year</th><th>month</th><th>orders</th></tr></thead><tbody><tr><td>2016</td><td>1</td><td>50</td></tr><tr><td>2016</td><td>2</td><td>49</td></tr><tr><td>2016</td><td>3</td><td>55</td></tr><tr><td>2016</td><td>4</td><td>43</td></tr><tr><td>2016</td><td>5</td><td>51</td></tr><tr><td>2016</td><td>6</td><td>45</td></tr><tr><td>2016</td><td>7</td><td>50</td></tr><tr><td>2016</td><td>8</td><td>63</td></tr><tr><td>2016</td><td>9</td><td>67</td></tr><tr><td>2016</td><td>10</td><td>64</td></tr><tr><td>2016</td><td>11</td><td>43</td></tr><tr><td>2016</td><td>12</td><td>55</td></tr><tr><td>2017</td><td>1</td><td>50</td></tr><tr><td>2017</td><td>2</td><td>57</td></tr><tr><td>2017</td><td>3</td><td>67</td></tr><tr><td>2017</td><td>4</td><td>57</td></tr><tr><td>2017</td><td>5</td><td>57</td></tr><tr><td>2017</td><td>6</td><td>63</td></tr><tr><td>2017</td><td>7</td><td>52</td></tr><tr><td>2017</td><td>8</td><td>65</td></tr><tr><td>2017</td><td>9</td><td>53</td></tr><tr><td>2017</td><td>10</td><td>65</td></tr><tr><td>2017</td><td>11</td><td>55</td></tr><tr><td>2017</td><td>12</td><td>47</td></tr><tr><td>2018</td><td>1</td><td>52</td></tr><tr><td>2018</td><td>2</td><td>35</td></tr><tr><td>2018</td><td>3</td><td>68</td></tr><tr><td>2018</td><td>4</td><td>125</td></tr><tr><td>2018</td><td>6</td><td>1</td></tr><tr><td>2018</td><td>7</td><td>4</td></tr><tr><td>2018</td><td>8</td><td>2</td></tr><tr><td>2018</td><td>9</td><td>1</td></tr><tr><td>2018</td><td>10</td><td>1</td></tr><tr><td>2018</td><td>11</td><td>2</td></tr><tr><td>2018</td><td>12</td><td>1</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         2016,
         1,
         50
        ],
        [
         2016,
         2,
         49
        ],
        [
         2016,
         3,
         55
        ],
        [
         2016,
         4,
         43
        ],
        [
         2016,
         5,
         51
        ],
        [
         2016,
         6,
         45
        ],
        [
         2016,
         7,
         50
        ],
        [
         2016,
         8,
         63
        ],
        [
         2016,
         9,
         67
        ],
        [
         2016,
         10,
         64
        ],
        [
         2016,
         11,
         43
        ],
        [
         2016,
         12,
         55
        ],
        [
         2017,
         1,
         50
        ],
        [
         2017,
         2,
         57
        ],
        [
         2017,
         3,
         67
        ],
        [
         2017,
         4,
         57
        ],
        [
         2017,
         5,
         57
        ],
        [
         2017,
         6,
         63
        ],
        [
         2017,
         7,
         52
        ],
        [
         2017,
         8,
         65
        ],
        [
         2017,
         9,
         53
        ],
        [
         2017,
         10,
         65
        ],
        [
         2017,
         11,
         55
        ],
        [
         2017,
         12,
         47
        ],
        [
         2018,
         1,
         52
        ],
        [
         2018,
         2,
         35
        ],
        [
         2018,
         3,
         68
        ],
        [
         2018,
         4,
         125
        ],
        [
         2018,
         6,
         1
        ],
        [
         2018,
         7,
         4
        ],
        [
         2018,
         8,
         2
        ],
        [
         2018,
         9,
         1
        ],
        [
         2018,
         10,
         1
        ],
        [
         2018,
         11,
         2
        ],
        [
         2018,
         12,
         1
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "year",
         "type": "\"integer\""
        },
        {
         "metadata": "{}",
         "name": "month",
         "type": "\"integer\""
        },
        {
         "metadata": "{}",
         "name": "orders",
         "type": "\"long\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "orders_per_month = (\n",
    "    spark.table(\"biker_r_project.gold.sales_fact\")\n",
    "    .groupBy(\n",
    "        year(\"order_date\").alias(\"year\"),\n",
    "        month(\"order_date\").alias(\"month\")\n",
    "    )\n",
    "    .agg(countDistinct(\"order_id\").alias(\"orders\"))\n",
    ")\n",
    "\n",
    "display(orders_per_month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "82f0d454-1f21-4486-9d58-555889e0b2a2",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>product_name</th><th>stock_remaining</th></tr></thead><tbody><tr><td>Trek Fuel EX 8 29 XT - 2018</td><td>75</td></tr><tr><td>Sun Bicycles Lil Kitt'n - 2017</td><td>48</td></tr><tr><td>Trek Ticket S Frame - 2018</td><td>56</td></tr><tr><td>Electra Cyclosaurus 1 (16-inch) - Boy's - 2018</td><td>32</td></tr><tr><td>Electra Morningstar 3i Ladies' - 2018</td><td>28</td></tr><tr><td>Trek Precaliber 16 Girl's - 2018</td><td>55</td></tr><tr><td>Electra Straight 8 1 (20-inch) - Boy's - 2018</td><td>24</td></tr><tr><td>Trek Remedy 9.8 - 2017</td><td>35</td></tr><tr><td>Trek XM700+ Lowstep - 2018</td><td>86</td></tr><tr><td>Electra Amsterdam Original 3i - 2015/2017</td><td>11</td></tr><tr><td>Trek Precaliber 24 (7-Speed) - Boys - 2018</td><td>30</td></tr><tr><td>Trek Dual Sport+ - 2018</td><td>59</td></tr><tr><td>Electra White Water 3i - 2018</td><td>43</td></tr><tr><td>Electra Super Moto 8i - 2018</td><td>35</td></tr><tr><td>Trek X-Caliber Frameset - 2018</td><td>60</td></tr><tr><td>Surly Straggler 650b - 2016</td><td>59</td></tr><tr><td>Electra Amsterdam Fashion 7i Ladies' - 2017</td><td>62</td></tr><tr><td>Trek Superfly 20 - 2018</td><td>37</td></tr><tr><td>Surly Ogre Frameset - 2017</td><td>42</td></tr><tr><td>Sun Bicycles Cruz 7 - 2017</td><td>115</td></tr><tr><td>Trek Emonda S 5 - 2017</td><td>37</td></tr><tr><td>Trek Domane ALR 5 Disc - 2018</td><td>39</td></tr><tr><td>Electra Cruiser 7D Ladies' - 2016/2018</td><td>44</td></tr><tr><td>Electra Cruiser 1 Tall - 2016/2018</td><td>54</td></tr><tr><td>Trek Precaliber 20 6-speed Boy's - 2018</td><td>27</td></tr><tr><td>Electra Tiger Shark 3i - 2018</td><td>41</td></tr><tr><td>Haro Shredder Pro 20 - 2017</td><td>23</td></tr><tr><td>Trek Marlin 6 - 2018</td><td>27</td></tr><tr><td>Strider Strider 20 Sport - 2018</td><td>54</td></tr><tr><td>Trek Fuel EX 7 29 - 2018</td><td>64</td></tr><tr><td>Electra Townie Original 1 - 2018</td><td>12</td></tr><tr><td>Surly ECR 27.5 - 2018</td><td>59</td></tr><tr><td>Trek Domane SLR 6 Disc Women's - 2018</td><td>44</td></tr><tr><td>Trek Domane SLR 8 Disc - 2018</td><td>24</td></tr><tr><td>Pure Cycles Vine 8-Speed - 2016</td><td>27</td></tr><tr><td>Electra Sweet Ride 1 (20-inch) - Girl's - 2018</td><td>41</td></tr><tr><td>Trek X-Caliber 8 - 2018</td><td>46</td></tr><tr><td>Trek Precaliber 20 Boy's - 2018</td><td>41</td></tr><tr><td>Trek Domane AL 3 - 2018</td><td>52</td></tr><tr><td>Electra Townie Commute 8D - 2018</td><td>119</td></tr><tr><td>Surly Troll Frameset - 2018</td><td>41</td></tr><tr><td>Electra Townie 3i EQ (20-inch) - Boys' - 2017</td><td>55</td></tr><tr><td>Trek Kids' Neko - 2018</td><td>69</td></tr><tr><td>Electra Glam Punk 3i Ladies' - 2017</td><td>64</td></tr><tr><td>Trek X-Caliber 7 - 2018</td><td>52</td></tr><tr><td>Surly Ice Cream Truck Frameset - 2016</td><td>38</td></tr><tr><td>Trek Emonda SL 6 Disc - 2018</td><td>43</td></tr><tr><td>Trek Domane SL 5 - 2018</td><td>56</td></tr><tr><td>Trek Fuel EX 9.8 27.5 Plus - 2017</td><td>30</td></tr><tr><td>Trek Domane SLR 6 Disc - 2017</td><td>54</td></tr><tr><td>Trek Precaliber 24 21-speed Boy's - 2018</td><td>43</td></tr><tr><td>Trek Domane ALR 5 Gravel - 2018</td><td>24</td></tr><tr><td>Electra Sugar Skulls 1 (20-inch) - Girl's - 2017</td><td>71</td></tr><tr><td>Trek Domane ALR Disc Frameset - 2018</td><td>41</td></tr><tr><td>Trek Crockett 5 Disc - 2018</td><td>37</td></tr><tr><td>Trek Remedy 29 Carbon Frameset - 2016</td><td>13</td></tr><tr><td>Trek Domane SLR 9 Disc - 2018</td><td>54</td></tr><tr><td>Sun Bicycles Revolutions 24 - Girl's - 2017</td><td>33</td></tr><tr><td>Electra Soft Serve 1 (16-inch) - Girl's - 2018</td><td>44</td></tr><tr><td>Electra Townie Original 21D - 2018</td><td>109</td></tr><tr><td>Trek Session DH 27.5 Carbon Frameset - 2017</td><td>32</td></tr><tr><td>Haro Shredder 20 - 2017</td><td>50</td></tr><tr><td>Trek Verve+ - 2018</td><td>79</td></tr><tr><td>Electra Amsterdam Original 3i Ladies' - 2017</td><td>12</td></tr><tr><td>Electra Treasure 1 20\" - 2018</td><td>48</td></tr><tr><td>Trek Girl's Kickster - 2017</td><td>70</td></tr><tr><td>Electra Townie Original 7D EQ - 2018</td><td>34</td></tr><tr><td>Sun Bicycles Biscayne Tandem 7 - 2017</td><td>16</td></tr><tr><td>Electra Townie Balloon 3i EQ - 2017/2018</td><td>90</td></tr><tr><td>Sun Bicycles Spider 3i - 2017</td><td>46</td></tr><tr><td>Trek Farley Carbon Frameset - 2018</td><td>41</td></tr><tr><td>Trek Emonda SL 7 - 2018</td><td>50</td></tr><tr><td>Electra Cruiser 7D (24-Inch) Ladies' - 2016/2018</td><td>69</td></tr><tr><td>Surly Karate Monkey 27.5+ Frameset - 2017</td><td>65</td></tr><tr><td>Trek Kids' Dual Sport - 2018</td><td>34</td></tr><tr><td>Trek Fuel EX 5 27.5 Plus - 2017</td><td>25</td></tr><tr><td>Electra Townie Balloon 7i EQ Ladies' - 2017/2018</td><td>87</td></tr><tr><td>Haro SR 1.3 - 2017</td><td>53</td></tr><tr><td>Electra Starship 1 16\" - 2018</td><td>38</td></tr><tr><td>Trek Domane SL 8 Disc - 2018</td><td>39</td></tr><tr><td>Electra Superbolt 1 20\" - 2018</td><td>9</td></tr><tr><td>Surly Krampus - 2018</td><td>38</td></tr><tr><td>Trek Precaliber 16 Boy's - 2018</td><td>37</td></tr><tr><td>Trek CrossRip 2 - 2018</td><td>29</td></tr><tr><td>Trek Precaliber 20 6-speed Girl's - 2018</td><td>67</td></tr><tr><td>Trek X-Caliber 8 - 2017</td><td>53</td></tr><tr><td>Electra Girl's Hawaii 1 (16-inch) - 2015/2016</td><td>79</td></tr><tr><td>Trek Crockett 7 Disc - 2018</td><td>34</td></tr><tr><td>Electra Townie Balloon 8D EQ - 2016/2017/2018</td><td>90</td></tr><tr><td>Electra Townie Original 1 Ladies' - 2018</td><td>38</td></tr><tr><td>Heller Shagamaw GX1 - 2018</td><td>30</td></tr><tr><td>Trek Domane SL 6 Disc - 2018</td><td>25</td></tr><tr><td>Electra Queen of Hearts 3i - 2018</td><td>24</td></tr><tr><td>Electra Delivery 3i - 2016/2017/2018</td><td>47</td></tr><tr><td>Electra Cruiser 7D - 2016/2017/2018</td><td>74</td></tr><tr><td>Electra Cruiser Lux 3i Ladies' - 2018</td><td>39</td></tr><tr><td>Trek Superfly 24 - 2017/2018</td><td>35</td></tr><tr><td>Surly ECR Frameset - 2018</td><td>37</td></tr><tr><td>Trek Precaliber 12 Boys - 2017</td><td>57</td></tr><tr><td>Electra Townie Commute 27D - 2018</td><td>75</td></tr><tr><td>Trek Powerfly 5 FS - 2018</td><td>70</td></tr><tr><td>Trek Emonda SLR 8 - 2018</td><td>29</td></tr><tr><td>Electra Townie Original 3i EQ Ladies' - 2018</td><td>17</td></tr><tr><td>Trek Silque SLR 8 Women's - 2017</td><td>12</td></tr><tr><td>Pure Cycles William 3-Speed - 2016</td><td>43</td></tr><tr><td>Sun Bicycles Cruz 3 - Women's - 2017</td><td>67</td></tr><tr><td>Trek Precaliber 12 Girls - 2017</td><td>43</td></tr><tr><td>Trek Domane S 5 Disc - 2017</td><td>39</td></tr><tr><td>Electra Amsterdam Royal 8i - 2017/2018</td><td>45</td></tr><tr><td>Electra Townie Go! 8i - 2017/2018</td><td>120</td></tr><tr><td>Trek XM700+ - 2018</td><td>59</td></tr><tr><td>Trek Verve+ Lowstep - 2018</td><td>40</td></tr><tr><td>Electra Townie Balloon 7i EQ - 2018</td><td>96</td></tr><tr><td>Electra Sweet Ride 3i (20-inch) - Girls' - 2018</td><td>68</td></tr><tr><td>Haro SR 1.1 - 2017</td><td>51</td></tr><tr><td>Trek Farley Alloy Frameset - 2017</td><td>27</td></tr><tr><td>Electra Cruiser 7D Tall - 2016/2018</td><td>58</td></tr><tr><td>Trek Domane ALR Frameset - 2018</td><td>34</td></tr><tr><td>Trek Domane SL 5 Disc - 2018</td><td>77</td></tr><tr><td>Electra Straight 8 3i (20-inch) - Boy's - 2017</td><td>47</td></tr><tr><td>Trek CrossRip 1 - 2018</td><td>28</td></tr><tr><td>Surly Straggler 650b - 2018</td><td>62</td></tr><tr><td>Electra Amsterdam Royal 8i Ladies - 2018</td><td>26</td></tr><tr><td>Electra Moto 3i - 2018</td><td>75</td></tr><tr><td>Electra Straight 8 3i - 2018</td><td>37</td></tr><tr><td>Trek Remedy 27.5 C Frameset - 2018</td><td>56</td></tr><tr><td>Trek Precaliber 24 (21-Speed) - Girls - 2017</td><td>16</td></tr><tr><td>Electra Girl's Hawaii 1 16\" - 2017</td><td>107</td></tr><tr><td>Electra Townie Commute Go! - 2018</td><td>40</td></tr><tr><td>Electra Townie Original 7D EQ - Women's - 2016</td><td>65</td></tr><tr><td>Electra Loft Go! 8i - 2018</td><td>59</td></tr><tr><td>Electra Townie Commute Go! Ladies' - 2018</td><td>95</td></tr><tr><td>Surly Krampus Frameset - 2018</td><td>26</td></tr><tr><td>Electra Townie Commute 27D Ladies - 2018</td><td>93</td></tr><tr><td>Surly Straggler - 2016</td><td>49</td></tr><tr><td>Electra Townie Original 7D - 2017</td><td>125</td></tr><tr><td>Surly Big Dummy Frameset - 2017</td><td>52</td></tr><tr><td>Electra Cruiser Lux 7D - 2018</td><td>43</td></tr><tr><td>Trek Domane SL Frameset Women's - 2018</td><td>65</td></tr><tr><td>Trek Precaliber 12 Girl's - 2018</td><td>60</td></tr><tr><td>Electra Cruiser 1 Ladies' - 2018</td><td>10</td></tr><tr><td>Trek Powerfly 8 FS Plus - 2017</td><td>78</td></tr><tr><td>Surly Pack Rat Frameset - 2018</td><td>28</td></tr><tr><td>Electra Townie Balloon 3i EQ Ladies' - 2018</td><td>68</td></tr><tr><td>Sun Bicycles Drifter 7 - 2017</td><td>19</td></tr><tr><td>Electra Straight 8 1 (16-inch) - Boy's - 2018</td><td>43</td></tr><tr><td>Electra Townie Commute 8D Ladies' - 2018</td><td>60</td></tr><tr><td>Trek Domane ALR 4 Disc - 2018</td><td>20</td></tr><tr><td>Trek Domane S 6 - 2017</td><td>21</td></tr><tr><td>Trek Domane SLR 6 - 2018</td><td>18</td></tr><tr><td>Surly ECR - 2018</td><td>37</td></tr><tr><td>Trek 1120 - 2018</td><td>41</td></tr><tr><td>Electra Cruiser 1 - 2016/2017/2018</td><td>34</td></tr><tr><td>Sun Bicycles Biscayne Tandem CB - 2017</td><td>36</td></tr><tr><td>Sun Bicycles Atlas X-Type - 2017</td><td>68</td></tr><tr><td>Haro Downtown 16 - 2017</td><td>44</td></tr><tr><td>Sun Bicycles ElectroLite - 2017</td><td>27</td></tr><tr><td>Trek Powerfly 5 Women's - 2018</td><td>17</td></tr><tr><td>Trek MT 201 - 2018</td><td>43</td></tr><tr><td>Trek Domane AL 2 Women's - 2018</td><td>77</td></tr><tr><td>Trek Conduit+ - 2018</td><td>22</td></tr><tr><td>Strider Classic 12 Balance Bike - 2018</td><td>46</td></tr><tr><td>Electra Under-The-Sea 1 16\" - 2018</td><td>51</td></tr><tr><td>Trek Precaliber 24 21-speed Girl's - 2018</td><td>40</td></tr><tr><td>Electra Cruiser Lux Fat Tire 7D - 2018</td><td>39</td></tr><tr><td>Trek Silque SLR 7 Women's - 2017</td><td>61</td></tr><tr><td>Trek Precaliber 16 Girls - 2017</td><td>39</td></tr><tr><td>Pure Cycles Western 3-Speed - Women's - 2015/2016</td><td>34</td></tr><tr><td>Surly Straggler - 2018</td><td>109</td></tr><tr><td>Haro SR 1.2 - 2017</td><td>29</td></tr><tr><td>Trek Marlin 7 - 2017/2018</td><td>71</td></tr><tr><td>Electra Townie Original 3i EQ - 2017/2018</td><td>31</td></tr><tr><td>Trek Super Commuter+ 8S - 2018</td><td>25</td></tr><tr><td>Surly Wednesday - 2017</td><td>22</td></tr><tr><td>Trek Fuel EX 5 Plus - 2018</td><td>39</td></tr><tr><td>Trek Remedy 9.8 27.5 - 2018</td><td>19</td></tr><tr><td>Electra Cruiser 1 (24-Inch) - 2016</td><td>81</td></tr><tr><td>Electra Townie Original 7D EQ - 2016</td><td>88</td></tr><tr><td>Trek Domane ALR 3 - 2018</td><td>40</td></tr><tr><td>Trek Powerfly 5 - 2018</td><td>67</td></tr><tr><td>Trek Emonda S 4 - 2017</td><td>27</td></tr><tr><td>Trek Madone 9.2 - 2017</td><td>43</td></tr><tr><td>Electra Cruiser Lux 7D Ladies' - 2018</td><td>32</td></tr><tr><td>Sun Bicycles Streamway - 2017</td><td>73</td></tr><tr><td>Trek 820 - 2018</td><td>42</td></tr><tr><td>Electra Superbolt 3i 20\" - 2018</td><td>43</td></tr><tr><td>Heller Bloodhound Trail - 2018</td><td>52</td></tr><tr><td>Trek Fuel EX 9.8 29 - 2017</td><td>41</td></tr><tr><td>Sun Bicycles Lil Bolt Type-R - 2017</td><td>27</td></tr><tr><td>Strider Sport 16 - 2018</td><td>36</td></tr><tr><td>Trek Precaliber 20 Girl's - 2018</td><td>54</td></tr><tr><td>Trek Boone 7 Disc - 2018</td><td>64</td></tr><tr><td>Electra Townie Original 7D - 2015/2016</td><td>43</td></tr><tr><td>Trek Boone Race Shop Limited - 2017</td><td>17</td></tr><tr><td>Trek Procal AL Frameset - 2018</td><td>23</td></tr><tr><td>Electra Townie Go! 8i Ladies' - 2018</td><td>100</td></tr><tr><td>Haro Shredder 20 Girls - 2017</td><td>62</td></tr><tr><td>Electra Savannah 3i (20-inch) - Girl's - 2017</td><td>63</td></tr><tr><td>Trek Domane SL 5 Women's - 2018</td><td>63</td></tr><tr><td>Electra Cruiser Lux 1 Ladies' - 2018</td><td>61</td></tr><tr><td>Trek Powerfly 7 FS - 2018</td><td>17</td></tr><tr><td>Sun Bicycles Streamway 3 - 2017</td><td>24</td></tr><tr><td>Trek Emonda SLR 6 - 2018</td><td>31</td></tr><tr><td>Electra Tiger Shark 3i (20-inch) - Boys' - 2018</td><td>23</td></tr><tr><td>Electra Townie Original 7D EQ Ladies' - 2017/2018</td><td>51</td></tr><tr><td>Trek Precaliber 12 Boy's - 2018</td><td>52</td></tr><tr><td>Trek Domane SL Disc Frameset - 2017</td><td>30</td></tr><tr><td>Trek Boone 5 Disc - 2018</td><td>48</td></tr><tr><td>Trek Stache 5 - 2018</td><td>53</td></tr><tr><td>Trek Neko+ - 2018</td><td>28</td></tr><tr><td>Surly Troll Frameset - 2017</td><td>69</td></tr><tr><td>Trek Lift+ - 2018</td><td>56</td></tr><tr><td>Sun Bicycles Revolutions 24 - 2017</td><td>37</td></tr><tr><td>Trek Madone 9 Frameset - 2018</td><td>43</td></tr><tr><td>Electra Cruiser Lux 1 - 2016/2018</td><td>63</td></tr><tr><td>Trek Fuel EX 8 29 - 2016</td><td>36</td></tr><tr><td>Trek Remedy 7 27.5 - 2018</td><td>62</td></tr><tr><td>Electra Cruiser Lux 3i - 2018</td><td>39</td></tr><tr><td>Trek Boone 7 - 2017</td><td>29</td></tr><tr><td>Electra Townie Original 21D Ladies' - 2018</td><td>16</td></tr><tr><td>Sun Bicycles Cruz 7 - Women's - 2017</td><td>79</td></tr><tr><td>Trek Domane SLR Disc Frameset - 2018</td><td>35</td></tr><tr><td>Trek Domane SL 6 - 2017</td><td>16</td></tr><tr><td>Trek Domane SLR Frameset - 2018</td><td>5</td></tr><tr><td>Trek Domane AL 3 Women's - 2018</td><td>14</td></tr><tr><td>Trek Precaliber 24 7-speed Girl's - 2018</td><td>50</td></tr><tr><td>Electra Savannah 1 (20-inch) - Girl's - 2018</td><td>59</td></tr><tr><td>Trek Conduit+ - 2016</td><td>51</td></tr><tr><td>Trek Fuel EX 8 29 - 2018</td><td>54</td></tr><tr><td>Trek Domane ALR 4 Disc Women's - 2018</td><td>27</td></tr><tr><td>Electra Heartchya 1 (20-inch) - Girl's - 2018</td><td>39</td></tr><tr><td>Trek 820 - 2016</td><td>55</td></tr><tr><td>Trek Kickster - 2018</td><td>43</td></tr><tr><td>Ritchey Timberwolf Frameset - 2016</td><td>45</td></tr><tr><td>Haro Flightline Two 26 Plus - 2017</td><td>54</td></tr><tr><td>Surly Ice Cream Truck Frameset - 2017</td><td>70</td></tr><tr><td>Surly Wednesday Frameset - 2016</td><td>34</td></tr><tr><td>Trek Super Commuter+ 7 - 2018</td><td>64</td></tr><tr><td>Sun Bicycles Cruz 3 - 2017</td><td>109</td></tr><tr><td>Electra Cruiser Lux 1 - 2017</td><td>49</td></tr><tr><td>Electra Moto 1 - 2016</td><td>31</td></tr><tr><td>Sun Bicycles Drifter 7 - Women's - 2017</td><td>46</td></tr><tr><td>Surly Wednesday Frameset - 2017</td><td>32</td></tr><tr><td>Electra Koa 3i Ladies' - 2018</td><td>12</td></tr><tr><td>Surly Steamroller - 2017</td><td>49</td></tr><tr><td>Trek Marlin 5 - 2018</td><td>54</td></tr><tr><td>Electra Treasure 3i 20\" - 2018</td><td>29</td></tr><tr><td>Trek Domane SL 5 Disc Women's - 2018</td><td>34</td></tr><tr><td>Electra Townie Original 21D EQ Ladies' - 2018</td><td>36</td></tr><tr><td>Electra Tiger Shark 1 (20-inch) - Boys' - 2018</td><td>44</td></tr><tr><td>Electra Water Lily 1 (16-inch) - Girl's - 2018</td><td>67</td></tr><tr><td>Haro Shift R3 - 2017</td><td>41</td></tr><tr><td>Sun Bicycles Brickell Tandem 7 - 2017</td><td>30</td></tr><tr><td>Surly Pack Rat - 2018</td><td>41</td></tr><tr><td>Electra Townie 7D (20-inch) - Boys' - 2017</td><td>38</td></tr><tr><td>Trek Domane SL Frameset - 2018</td><td>35</td></tr><tr><td>Trek Procaliber 6 - 2018</td><td>24</td></tr><tr><td>Heller Shagamaw Frame - 2016</td><td>26</td></tr><tr><td>Electra Daydreamer 3i Ladies' - 2018</td><td>49</td></tr><tr><td>Electra Amsterdam Fashion 3i Ladies' - 2017/2018</td><td>47</td></tr><tr><td>Sun Bicycles Brickell Tandem CB - 2017</td><td>60</td></tr><tr><td>Trek Domane AL 2 - 2018</td><td>36</td></tr><tr><td>Sun Bicycles Boardwalk (24-inch Wheels) - 2017</td><td>71</td></tr><tr><td>Electra Townie Balloon 8D EQ Ladies' - 2016/2017/2018</td><td>121</td></tr><tr><td>Trek Procaliber Frameset - 2018</td><td>53</td></tr><tr><td>Electra Townie Original 21D - 2016</td><td>92</td></tr><tr><td>Trek Domane SLR 6 Disc - 2018</td><td>30</td></tr><tr><td>Electra Cruiser Lux Fat Tire 1 Ladies - 2017</td><td>63</td></tr><tr><td>Trek Domane SL 7 Women's - 2018</td><td>53</td></tr><tr><td>Trek Emonda ALR 6 - 2018</td><td>54</td></tr><tr><td>Trek Stache Carbon Frameset - 2018</td><td>59</td></tr><tr><td>Electra Girl's Hawaii 1 (20-inch) - 2015/2016</td><td>29</td></tr><tr><td>Trek Lift+ Lowstep - 2018</td><td>39</td></tr><tr><td>Electra Relic 3i - 2018</td><td>72</td></tr><tr><td>Sun Bicycles Streamway 7 - 2017</td><td>11</td></tr><tr><td>Surly Big Fat Dummy Frameset - 2018</td><td>46</td></tr><tr><td>Trek Slash 8 27.5 - 2016</td><td>28</td></tr><tr><td>Electra Moto 3i (20-inch) - Boy's - 2017</td><td>43</td></tr><tr><td>Trek CrossRip+ - 2018</td><td>47</td></tr><tr><td>Electra Townie Original 21D EQ - 2017/2018</td><td>81</td></tr><tr><td>Haro Flightline One ST - 2017</td><td>47</td></tr><tr><td>Trek Precaliber 16 Boys - 2017</td><td>39</td></tr><tr><td>Trek Domane SL 6 - 2018</td><td>42</td></tr><tr><td>Trek Stache 5 - 2017</td><td>52</td></tr><tr><td>Trek Boy's Kickster - 2015/2017</td><td>57</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Trek Fuel EX 8 29 XT - 2018",
         75
        ],
        [
         "Sun Bicycles Lil Kitt'n - 2017",
         48
        ],
        [
         "Trek Ticket S Frame - 2018",
         56
        ],
        [
         "Electra Cyclosaurus 1 (16-inch) - Boy's - 2018",
         32
        ],
        [
         "Electra Morningstar 3i Ladies' - 2018",
         28
        ],
        [
         "Trek Precaliber 16 Girl's - 2018",
         55
        ],
        [
         "Electra Straight 8 1 (20-inch) - Boy's - 2018",
         24
        ],
        [
         "Trek Remedy 9.8 - 2017",
         35
        ],
        [
         "Trek XM700+ Lowstep - 2018",
         86
        ],
        [
         "Electra Amsterdam Original 3i - 2015/2017",
         11
        ],
        [
         "Trek Precaliber 24 (7-Speed) - Boys - 2018",
         30
        ],
        [
         "Trek Dual Sport+ - 2018",
         59
        ],
        [
         "Electra White Water 3i - 2018",
         43
        ],
        [
         "Electra Super Moto 8i - 2018",
         35
        ],
        [
         "Trek X-Caliber Frameset - 2018",
         60
        ],
        [
         "Surly Straggler 650b - 2016",
         59
        ],
        [
         "Electra Amsterdam Fashion 7i Ladies' - 2017",
         62
        ],
        [
         "Trek Superfly 20 - 2018",
         37
        ],
        [
         "Surly Ogre Frameset - 2017",
         42
        ],
        [
         "Sun Bicycles Cruz 7 - 2017",
         115
        ],
        [
         "Trek Emonda S 5 - 2017",
         37
        ],
        [
         "Trek Domane ALR 5 Disc - 2018",
         39
        ],
        [
         "Electra Cruiser 7D Ladies' - 2016/2018",
         44
        ],
        [
         "Electra Cruiser 1 Tall - 2016/2018",
         54
        ],
        [
         "Trek Precaliber 20 6-speed Boy's - 2018",
         27
        ],
        [
         "Electra Tiger Shark 3i - 2018",
         41
        ],
        [
         "Haro Shredder Pro 20 - 2017",
         23
        ],
        [
         "Trek Marlin 6 - 2018",
         27
        ],
        [
         "Strider Strider 20 Sport - 2018",
         54
        ],
        [
         "Trek Fuel EX 7 29 - 2018",
         64
        ],
        [
         "Electra Townie Original 1 - 2018",
         12
        ],
        [
         "Surly ECR 27.5 - 2018",
         59
        ],
        [
         "Trek Domane SLR 6 Disc Women's - 2018",
         44
        ],
        [
         "Trek Domane SLR 8 Disc - 2018",
         24
        ],
        [
         "Pure Cycles Vine 8-Speed - 2016",
         27
        ],
        [
         "Electra Sweet Ride 1 (20-inch) - Girl's - 2018",
         41
        ],
        [
         "Trek X-Caliber 8 - 2018",
         46
        ],
        [
         "Trek Precaliber 20 Boy's - 2018",
         41
        ],
        [
         "Trek Domane AL 3 - 2018",
         52
        ],
        [
         "Electra Townie Commute 8D - 2018",
         119
        ],
        [
         "Surly Troll Frameset - 2018",
         41
        ],
        [
         "Electra Townie 3i EQ (20-inch) - Boys' - 2017",
         55
        ],
        [
         "Trek Kids' Neko - 2018",
         69
        ],
        [
         "Electra Glam Punk 3i Ladies' - 2017",
         64
        ],
        [
         "Trek X-Caliber 7 - 2018",
         52
        ],
        [
         "Surly Ice Cream Truck Frameset - 2016",
         38
        ],
        [
         "Trek Emonda SL 6 Disc - 2018",
         43
        ],
        [
         "Trek Domane SL 5 - 2018",
         56
        ],
        [
         "Trek Fuel EX 9.8 27.5 Plus - 2017",
         30
        ],
        [
         "Trek Domane SLR 6 Disc - 2017",
         54
        ],
        [
         "Trek Precaliber 24 21-speed Boy's - 2018",
         43
        ],
        [
         "Trek Domane ALR 5 Gravel - 2018",
         24
        ],
        [
         "Electra Sugar Skulls 1 (20-inch) - Girl's - 2017",
         71
        ],
        [
         "Trek Domane ALR Disc Frameset - 2018",
         41
        ],
        [
         "Trek Crockett 5 Disc - 2018",
         37
        ],
        [
         "Trek Remedy 29 Carbon Frameset - 2016",
         13
        ],
        [
         "Trek Domane SLR 9 Disc - 2018",
         54
        ],
        [
         "Sun Bicycles Revolutions 24 - Girl's - 2017",
         33
        ],
        [
         "Electra Soft Serve 1 (16-inch) - Girl's - 2018",
         44
        ],
        [
         "Electra Townie Original 21D - 2018",
         109
        ],
        [
         "Trek Session DH 27.5 Carbon Frameset - 2017",
         32
        ],
        [
         "Haro Shredder 20 - 2017",
         50
        ],
        [
         "Trek Verve+ - 2018",
         79
        ],
        [
         "Electra Amsterdam Original 3i Ladies' - 2017",
         12
        ],
        [
         "Electra Treasure 1 20\" - 2018",
         48
        ],
        [
         "Trek Girl's Kickster - 2017",
         70
        ],
        [
         "Electra Townie Original 7D EQ - 2018",
         34
        ],
        [
         "Sun Bicycles Biscayne Tandem 7 - 2017",
         16
        ],
        [
         "Electra Townie Balloon 3i EQ - 2017/2018",
         90
        ],
        [
         "Sun Bicycles Spider 3i - 2017",
         46
        ],
        [
         "Trek Farley Carbon Frameset - 2018",
         41
        ],
        [
         "Trek Emonda SL 7 - 2018",
         50
        ],
        [
         "Electra Cruiser 7D (24-Inch) Ladies' - 2016/2018",
         69
        ],
        [
         "Surly Karate Monkey 27.5+ Frameset - 2017",
         65
        ],
        [
         "Trek Kids' Dual Sport - 2018",
         34
        ],
        [
         "Trek Fuel EX 5 27.5 Plus - 2017",
         25
        ],
        [
         "Electra Townie Balloon 7i EQ Ladies' - 2017/2018",
         87
        ],
        [
         "Haro SR 1.3 - 2017",
         53
        ],
        [
         "Electra Starship 1 16\" - 2018",
         38
        ],
        [
         "Trek Domane SL 8 Disc - 2018",
         39
        ],
        [
         "Electra Superbolt 1 20\" - 2018",
         9
        ],
        [
         "Surly Krampus - 2018",
         38
        ],
        [
         "Trek Precaliber 16 Boy's - 2018",
         37
        ],
        [
         "Trek CrossRip 2 - 2018",
         29
        ],
        [
         "Trek Precaliber 20 6-speed Girl's - 2018",
         67
        ],
        [
         "Trek X-Caliber 8 - 2017",
         53
        ],
        [
         "Electra Girl's Hawaii 1 (16-inch) - 2015/2016",
         79
        ],
        [
         "Trek Crockett 7 Disc - 2018",
         34
        ],
        [
         "Electra Townie Balloon 8D EQ - 2016/2017/2018",
         90
        ],
        [
         "Electra Townie Original 1 Ladies' - 2018",
         38
        ],
        [
         "Heller Shagamaw GX1 - 2018",
         30
        ],
        [
         "Trek Domane SL 6 Disc - 2018",
         25
        ],
        [
         "Electra Queen of Hearts 3i - 2018",
         24
        ],
        [
         "Electra Delivery 3i - 2016/2017/2018",
         47
        ],
        [
         "Electra Cruiser 7D - 2016/2017/2018",
         74
        ],
        [
         "Electra Cruiser Lux 3i Ladies' - 2018",
         39
        ],
        [
         "Trek Superfly 24 - 2017/2018",
         35
        ],
        [
         "Surly ECR Frameset - 2018",
         37
        ],
        [
         "Trek Precaliber 12 Boys - 2017",
         57
        ],
        [
         "Electra Townie Commute 27D - 2018",
         75
        ],
        [
         "Trek Powerfly 5 FS - 2018",
         70
        ],
        [
         "Trek Emonda SLR 8 - 2018",
         29
        ],
        [
         "Electra Townie Original 3i EQ Ladies' - 2018",
         17
        ],
        [
         "Trek Silque SLR 8 Women's - 2017",
         12
        ],
        [
         "Pure Cycles William 3-Speed - 2016",
         43
        ],
        [
         "Sun Bicycles Cruz 3 - Women's - 2017",
         67
        ],
        [
         "Trek Precaliber 12 Girls - 2017",
         43
        ],
        [
         "Trek Domane S 5 Disc - 2017",
         39
        ],
        [
         "Electra Amsterdam Royal 8i - 2017/2018",
         45
        ],
        [
         "Electra Townie Go! 8i - 2017/2018",
         120
        ],
        [
         "Trek XM700+ - 2018",
         59
        ],
        [
         "Trek Verve+ Lowstep - 2018",
         40
        ],
        [
         "Electra Townie Balloon 7i EQ - 2018",
         96
        ],
        [
         "Electra Sweet Ride 3i (20-inch) - Girls' - 2018",
         68
        ],
        [
         "Haro SR 1.1 - 2017",
         51
        ],
        [
         "Trek Farley Alloy Frameset - 2017",
         27
        ],
        [
         "Electra Cruiser 7D Tall - 2016/2018",
         58
        ],
        [
         "Trek Domane ALR Frameset - 2018",
         34
        ],
        [
         "Trek Domane SL 5 Disc - 2018",
         77
        ],
        [
         "Electra Straight 8 3i (20-inch) - Boy's - 2017",
         47
        ],
        [
         "Trek CrossRip 1 - 2018",
         28
        ],
        [
         "Surly Straggler 650b - 2018",
         62
        ],
        [
         "Electra Amsterdam Royal 8i Ladies - 2018",
         26
        ],
        [
         "Electra Moto 3i - 2018",
         75
        ],
        [
         "Electra Straight 8 3i - 2018",
         37
        ],
        [
         "Trek Remedy 27.5 C Frameset - 2018",
         56
        ],
        [
         "Trek Precaliber 24 (21-Speed) - Girls - 2017",
         16
        ],
        [
         "Electra Girl's Hawaii 1 16\" - 2017",
         107
        ],
        [
         "Electra Townie Commute Go! - 2018",
         40
        ],
        [
         "Electra Townie Original 7D EQ - Women's - 2016",
         65
        ],
        [
         "Electra Loft Go! 8i - 2018",
         59
        ],
        [
         "Electra Townie Commute Go! Ladies' - 2018",
         95
        ],
        [
         "Surly Krampus Frameset - 2018",
         26
        ],
        [
         "Electra Townie Commute 27D Ladies - 2018",
         93
        ],
        [
         "Surly Straggler - 2016",
         49
        ],
        [
         "Electra Townie Original 7D - 2017",
         125
        ],
        [
         "Surly Big Dummy Frameset - 2017",
         52
        ],
        [
         "Electra Cruiser Lux 7D - 2018",
         43
        ],
        [
         "Trek Domane SL Frameset Women's - 2018",
         65
        ],
        [
         "Trek Precaliber 12 Girl's - 2018",
         60
        ],
        [
         "Electra Cruiser 1 Ladies' - 2018",
         10
        ],
        [
         "Trek Powerfly 8 FS Plus - 2017",
         78
        ],
        [
         "Surly Pack Rat Frameset - 2018",
         28
        ],
        [
         "Electra Townie Balloon 3i EQ Ladies' - 2018",
         68
        ],
        [
         "Sun Bicycles Drifter 7 - 2017",
         19
        ],
        [
         "Electra Straight 8 1 (16-inch) - Boy's - 2018",
         43
        ],
        [
         "Electra Townie Commute 8D Ladies' - 2018",
         60
        ],
        [
         "Trek Domane ALR 4 Disc - 2018",
         20
        ],
        [
         "Trek Domane S 6 - 2017",
         21
        ],
        [
         "Trek Domane SLR 6 - 2018",
         18
        ],
        [
         "Surly ECR - 2018",
         37
        ],
        [
         "Trek 1120 - 2018",
         41
        ],
        [
         "Electra Cruiser 1 - 2016/2017/2018",
         34
        ],
        [
         "Sun Bicycles Biscayne Tandem CB - 2017",
         36
        ],
        [
         "Sun Bicycles Atlas X-Type - 2017",
         68
        ],
        [
         "Haro Downtown 16 - 2017",
         44
        ],
        [
         "Sun Bicycles ElectroLite - 2017",
         27
        ],
        [
         "Trek Powerfly 5 Women's - 2018",
         17
        ],
        [
         "Trek MT 201 - 2018",
         43
        ],
        [
         "Trek Domane AL 2 Women's - 2018",
         77
        ],
        [
         "Trek Conduit+ - 2018",
         22
        ],
        [
         "Strider Classic 12 Balance Bike - 2018",
         46
        ],
        [
         "Electra Under-The-Sea 1 16\" - 2018",
         51
        ],
        [
         "Trek Precaliber 24 21-speed Girl's - 2018",
         40
        ],
        [
         "Electra Cruiser Lux Fat Tire 7D - 2018",
         39
        ],
        [
         "Trek Silque SLR 7 Women's - 2017",
         61
        ],
        [
         "Trek Precaliber 16 Girls - 2017",
         39
        ],
        [
         "Pure Cycles Western 3-Speed - Women's - 2015/2016",
         34
        ],
        [
         "Surly Straggler - 2018",
         109
        ],
        [
         "Haro SR 1.2 - 2017",
         29
        ],
        [
         "Trek Marlin 7 - 2017/2018",
         71
        ],
        [
         "Electra Townie Original 3i EQ - 2017/2018",
         31
        ],
        [
         "Trek Super Commuter+ 8S - 2018",
         25
        ],
        [
         "Surly Wednesday - 2017",
         22
        ],
        [
         "Trek Fuel EX 5 Plus - 2018",
         39
        ],
        [
         "Trek Remedy 9.8 27.5 - 2018",
         19
        ],
        [
         "Electra Cruiser 1 (24-Inch) - 2016",
         81
        ],
        [
         "Electra Townie Original 7D EQ - 2016",
         88
        ],
        [
         "Trek Domane ALR 3 - 2018",
         40
        ],
        [
         "Trek Powerfly 5 - 2018",
         67
        ],
        [
         "Trek Emonda S 4 - 2017",
         27
        ],
        [
         "Trek Madone 9.2 - 2017",
         43
        ],
        [
         "Electra Cruiser Lux 7D Ladies' - 2018",
         32
        ],
        [
         "Sun Bicycles Streamway - 2017",
         73
        ],
        [
         "Trek 820 - 2018",
         42
        ],
        [
         "Electra Superbolt 3i 20\" - 2018",
         43
        ],
        [
         "Heller Bloodhound Trail - 2018",
         52
        ],
        [
         "Trek Fuel EX 9.8 29 - 2017",
         41
        ],
        [
         "Sun Bicycles Lil Bolt Type-R - 2017",
         27
        ],
        [
         "Strider Sport 16 - 2018",
         36
        ],
        [
         "Trek Precaliber 20 Girl's - 2018",
         54
        ],
        [
         "Trek Boone 7 Disc - 2018",
         64
        ],
        [
         "Electra Townie Original 7D - 2015/2016",
         43
        ],
        [
         "Trek Boone Race Shop Limited - 2017",
         17
        ],
        [
         "Trek Procal AL Frameset - 2018",
         23
        ],
        [
         "Electra Townie Go! 8i Ladies' - 2018",
         100
        ],
        [
         "Haro Shredder 20 Girls - 2017",
         62
        ],
        [
         "Electra Savannah 3i (20-inch) - Girl's - 2017",
         63
        ],
        [
         "Trek Domane SL 5 Women's - 2018",
         63
        ],
        [
         "Electra Cruiser Lux 1 Ladies' - 2018",
         61
        ],
        [
         "Trek Powerfly 7 FS - 2018",
         17
        ],
        [
         "Sun Bicycles Streamway 3 - 2017",
         24
        ],
        [
         "Trek Emonda SLR 6 - 2018",
         31
        ],
        [
         "Electra Tiger Shark 3i (20-inch) - Boys' - 2018",
         23
        ],
        [
         "Electra Townie Original 7D EQ Ladies' - 2017/2018",
         51
        ],
        [
         "Trek Precaliber 12 Boy's - 2018",
         52
        ],
        [
         "Trek Domane SL Disc Frameset - 2017",
         30
        ],
        [
         "Trek Boone 5 Disc - 2018",
         48
        ],
        [
         "Trek Stache 5 - 2018",
         53
        ],
        [
         "Trek Neko+ - 2018",
         28
        ],
        [
         "Surly Troll Frameset - 2017",
         69
        ],
        [
         "Trek Lift+ - 2018",
         56
        ],
        [
         "Sun Bicycles Revolutions 24 - 2017",
         37
        ],
        [
         "Trek Madone 9 Frameset - 2018",
         43
        ],
        [
         "Electra Cruiser Lux 1 - 2016/2018",
         63
        ],
        [
         "Trek Fuel EX 8 29 - 2016",
         36
        ],
        [
         "Trek Remedy 7 27.5 - 2018",
         62
        ],
        [
         "Electra Cruiser Lux 3i - 2018",
         39
        ],
        [
         "Trek Boone 7 - 2017",
         29
        ],
        [
         "Electra Townie Original 21D Ladies' - 2018",
         16
        ],
        [
         "Sun Bicycles Cruz 7 - Women's - 2017",
         79
        ],
        [
         "Trek Domane SLR Disc Frameset - 2018",
         35
        ],
        [
         "Trek Domane SL 6 - 2017",
         16
        ],
        [
         "Trek Domane SLR Frameset - 2018",
         5
        ],
        [
         "Trek Domane AL 3 Women's - 2018",
         14
        ],
        [
         "Trek Precaliber 24 7-speed Girl's - 2018",
         50
        ],
        [
         "Electra Savannah 1 (20-inch) - Girl's - 2018",
         59
        ],
        [
         "Trek Conduit+ - 2016",
         51
        ],
        [
         "Trek Fuel EX 8 29 - 2018",
         54
        ],
        [
         "Trek Domane ALR 4 Disc Women's - 2018",
         27
        ],
        [
         "Electra Heartchya 1 (20-inch) - Girl's - 2018",
         39
        ],
        [
         "Trek 820 - 2016",
         55
        ],
        [
         "Trek Kickster - 2018",
         43
        ],
        [
         "Ritchey Timberwolf Frameset - 2016",
         45
        ],
        [
         "Haro Flightline Two 26 Plus - 2017",
         54
        ],
        [
         "Surly Ice Cream Truck Frameset - 2017",
         70
        ],
        [
         "Surly Wednesday Frameset - 2016",
         34
        ],
        [
         "Trek Super Commuter+ 7 - 2018",
         64
        ],
        [
         "Sun Bicycles Cruz 3 - 2017",
         109
        ],
        [
         "Electra Cruiser Lux 1 - 2017",
         49
        ],
        [
         "Electra Moto 1 - 2016",
         31
        ],
        [
         "Sun Bicycles Drifter 7 - Women's - 2017",
         46
        ],
        [
         "Surly Wednesday Frameset - 2017",
         32
        ],
        [
         "Electra Koa 3i Ladies' - 2018",
         12
        ],
        [
         "Surly Steamroller - 2017",
         49
        ],
        [
         "Trek Marlin 5 - 2018",
         54
        ],
        [
         "Electra Treasure 3i 20\" - 2018",
         29
        ],
        [
         "Trek Domane SL 5 Disc Women's - 2018",
         34
        ],
        [
         "Electra Townie Original 21D EQ Ladies' - 2018",
         36
        ],
        [
         "Electra Tiger Shark 1 (20-inch) - Boys' - 2018",
         44
        ],
        [
         "Electra Water Lily 1 (16-inch) - Girl's - 2018",
         67
        ],
        [
         "Haro Shift R3 - 2017",
         41
        ],
        [
         "Sun Bicycles Brickell Tandem 7 - 2017",
         30
        ],
        [
         "Surly Pack Rat - 2018",
         41
        ],
        [
         "Electra Townie 7D (20-inch) - Boys' - 2017",
         38
        ],
        [
         "Trek Domane SL Frameset - 2018",
         35
        ],
        [
         "Trek Procaliber 6 - 2018",
         24
        ],
        [
         "Heller Shagamaw Frame - 2016",
         26
        ],
        [
         "Electra Daydreamer 3i Ladies' - 2018",
         49
        ],
        [
         "Electra Amsterdam Fashion 3i Ladies' - 2017/2018",
         47
        ],
        [
         "Sun Bicycles Brickell Tandem CB - 2017",
         60
        ],
        [
         "Trek Domane AL 2 - 2018",
         36
        ],
        [
         "Sun Bicycles Boardwalk (24-inch Wheels) - 2017",
         71
        ],
        [
         "Electra Townie Balloon 8D EQ Ladies' - 2016/2017/2018",
         121
        ],
        [
         "Trek Procaliber Frameset - 2018",
         53
        ],
        [
         "Electra Townie Original 21D - 2016",
         92
        ],
        [
         "Trek Domane SLR 6 Disc - 2018",
         30
        ],
        [
         "Electra Cruiser Lux Fat Tire 1 Ladies - 2017",
         63
        ],
        [
         "Trek Domane SL 7 Women's - 2018",
         53
        ],
        [
         "Trek Emonda ALR 6 - 2018",
         54
        ],
        [
         "Trek Stache Carbon Frameset - 2018",
         59
        ],
        [
         "Electra Girl's Hawaii 1 (20-inch) - 2015/2016",
         29
        ],
        [
         "Trek Lift+ Lowstep - 2018",
         39
        ],
        [
         "Electra Relic 3i - 2018",
         72
        ],
        [
         "Sun Bicycles Streamway 7 - 2017",
         11
        ],
        [
         "Surly Big Fat Dummy Frameset - 2018",
         46
        ],
        [
         "Trek Slash 8 27.5 - 2016",
         28
        ],
        [
         "Electra Moto 3i (20-inch) - Boy's - 2017",
         43
        ],
        [
         "Trek CrossRip+ - 2018",
         47
        ],
        [
         "Electra Townie Original 21D EQ - 2017/2018",
         81
        ],
        [
         "Haro Flightline One ST - 2017",
         47
        ],
        [
         "Trek Precaliber 16 Boys - 2017",
         39
        ],
        [
         "Trek Domane SL 6 - 2018",
         42
        ],
        [
         "Trek Stache 5 - 2017",
         52
        ],
        [
         "Trek Boy's Kickster - 2015/2017",
         57
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "product_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "stock_remaining",
         "type": "\"long\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "inventory = spark.sql(\"\"\"\n",
    "SELECT\n",
    "    p.product_name,\n",
    "    SUM(s.quantity) stock_remaining\n",
    "FROM biker_r_project.silver.products p\n",
    "JOIN biker_r_project.silver.stocks s\n",
    "ON p.product_id=s.product_id\n",
    "GROUP BY p.product_name\n",
    "\"\"\")\n",
    "\n",
    "display(inventory)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "1feee608-22d0-4c3f-a89f-75921162878a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>total_orders</th><th>total_customers</th><th>total_products</th><th>total_revenue</th></tr></thead><tbody><tr><td>1615</td><td>1445</td><td>307</td><td>7689116.5576</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         1615,
         1445,
         307,
         7689116.5576
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "total_orders",
         "type": "\"long\""
        },
        {
         "metadata": "{}",
         "name": "total_customers",
         "type": "\"long\""
        },
        {
         "metadata": "{}",
         "name": "total_products",
         "type": "\"long\""
        },
        {
         "metadata": "{}",
         "name": "total_revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "kpi = spark.sql(\"\"\"\n",
    "SELECT\n",
    "COUNT(DISTINCT order_id) total_orders,\n",
    "COUNT(DISTINCT customer_id) total_customers,\n",
    "COUNT(DISTINCT product_id) total_products,\n",
    "SUM(revenue) total_revenue\n",
    "FROM biker_r_project.gold.sales_fact\n",
    "\"\"\")\n",
    "\n",
    "display(kpi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "6d2fba1b-fb5c-4148-b5ff-4e86fe79ec90",
     "showTitle": false,
     "tableResultSettingsMap": {
      "0": {
       "dataGridStateBlob": "{\"version\":1,\"tableState\":{\"columnPinning\":{\"left\":[\"#row_number#\"],\"right\":[]},\"columnSizing\":{},\"columnVisibility\":{}},\"settings\":{\"columns\":{}},\"syncTimestamp\":1781550409583}",
       "filterBlob": null,
       "queryPlanFiltersBlob": null,
       "tableResultIndex": 0
      }
     },
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>brand_name</th><th>revenue</th></tr></thead><tbody><tr><td>Trek</td><td>4602754.35</td></tr><tr><td>Electra</td><td>1205320.82</td></tr><tr><td>Surly</td><td>949507.06</td></tr><tr><td>Sun Bicycles</td><td>341994.93</td></tr><tr><td>Haro</td><td>185384.55</td></tr><tr><td>Heller</td><td>171459.08</td></tr><tr><td>Pure Cycles</td><td>149476.34</td></tr><tr><td>Ritchey</td><td>78898.95</td></tr><tr><td>Strider</td><td>4320.48</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "Trek",
         4602754.35
        ],
        [
         "Electra",
         1205320.82
        ],
        [
         "Surly",
         949507.06
        ],
        [
         "Sun Bicycles",
         341994.93
        ],
        [
         "Haro",
         185384.55
        ],
        [
         "Heller",
         171459.08
        ],
        [
         "Pure Cycles",
         149476.34
        ],
        [
         "Ritchey",
         78898.95
        ],
        [
         "Strider",
         4320.48
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "brand_name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "revenue",
         "type": "\"double\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": [
       "Databricks visualization. Run in Databricks to view."
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1.subcommand+json": {
       "baseErrorDetails": null,
       "bindings": {},
       "collapsed": false,
       "command": "%python\n__backend_agg_display_orig = display\n__backend_agg_dfs = []\ndef __backend_agg_display_new(df):\n    __backend_agg_df_modules = [\"pandas.core.frame\", \"databricks.koalas.frame\", \"pyspark.sql.dataframe\", \"pyspark.pandas.frame\", \"pyspark.sql.connect.dataframe\", \"pyspark.sql.classic.dataframe\"]\n    if (type(df).__module__ in __backend_agg_df_modules and type(df).__name__ == 'DataFrame') or isinstance(df, list):\n        __backend_agg_dfs.append(df)\n\ndisplay = __backend_agg_display_new\n\ndef __backend_agg_user_code_fn():\n    import base64\n    exec(base64.standard_b64decode(\"c3RvcmVfcGVyZiA9IHNwYXJrLnNxbCgiIiIKU0VMRUNUCiAgICBzdG9yZV9uYW1lLAogICAgUk9VTkQoU1VNKHJldmVudWUpLDIpIHJldmVudWUKRlJPTSBiaWtlcl9yX3Byb2plY3QuZ29sZC5zYWxlc19mYWN0CkdST1VQIEJZIHN0b3JlX25hbWUKT1JERVIgQlkgcmV2ZW51ZSBERVNDCiIiIikKCmRpc3BsYXkoc3RvcmVfcGVyZik=\").decode())\n\ntry:\n    # run user code\n    __backend_agg_user_code_fn()\n\n    #reset display function\n    display = __backend_agg_display_orig\n\n    if len(__backend_agg_dfs) > 0:\n        # create a temp view\n        if type(__backend_agg_dfs[0]).__module__ == \"databricks.koalas.frame\":\n            # koalas dataframe\n            __backend_agg_dfs[0].to_spark().createOrReplaceTempView(\"DatabricksView8aa8fb9\")\n        elif type(__backend_agg_dfs[0]).__module__ == \"pandas.core.frame\" or isinstance(__backend_agg_dfs[0], list):\n            # pandas dataframe\n            spark.createDataFrame(__backend_agg_dfs[0]).createOrReplaceTempView(\"DatabricksView8aa8fb9\")\n        else:\n            __backend_agg_dfs[0].createOrReplaceTempView(\"DatabricksView8aa8fb9\")\n        #run backend agg\n        display(spark.sql(\"\"\"WITH q AS (select * from DatabricksView8aa8fb9) SELECT `store_name`,SUM(`revenue`) `column_26923a16405` FROM q GROUP BY `store_name`\"\"\"))\n    else:\n        displayHTML(\"dataframe no longer exists. If you're using dataframe.display(), use display(dataframe) instead.\")\n\n\nfinally:\n    spark.sql(\"drop view if exists DatabricksView8aa8fb9\")\n    display = __backend_agg_display_orig\n    del __backend_agg_display_new\n    del __backend_agg_display_orig\n    del __backend_agg_dfs\n    del __backend_agg_user_code_fn\n\n",
       "commandTitle": "Visualization 1",
       "commandType": "auto",
       "commandVersion": 0,
       "commentThread": [],
       "commentsVisible": false,
       "contentSha256Hex": null,
       "customPlotOptions": {
        "redashChart": [
         {
          "key": "type",
          "value": "CHART"
         },
         {
          "key": "options",
          "value": {
           "alignYAxesAtZero": true,
           "coefficient": 1,
           "columnConfigurationMap": {
            "x": {
             "column": "store_name",
             "id": "column_26923a16404"
            },
            "y": [
             {
              "column": "revenue",
              "id": "column_26923a16405",
              "transform": "SUM"
             }
            ]
           },
           "dateTimeFormat": "DD/MM/YYYY HH:mm",
           "direction": {
            "type": "counterclockwise"
           },
           "error_y": {
            "type": "data",
            "visible": true
           },
           "globalSeriesType": "column",
           "legend": {
            "traceorder": "normal"
           },
           "missingValuesAsZero": true,
           "numberFormat": "0,0.[00000]",
           "percentFormat": "0[.]00%",
           "series": {
            "error_y": {
             "type": "data",
             "visible": true
            },
            "stacking": null
           },
           "seriesOptions": {
            "column_26923a16405": {
             "name": "revenue",
             "yAxis": 0
            }
           },
           "showDataLabels": false,
           "sizemode": "diameter",
           "sortX": true,
           "sortY": true,
           "swappedAxes": true,
           "textFormat": "",
           "useAggregationsUi": true,
           "valuesOptions": {},
           "version": 2,
           "xAxis": {
            "labels": {
             "enabled": true
            },
            "type": "-"
           },
           "yAxis": [
            {
             "type": "-"
            },
            {
             "opposite": true,
             "type": "-"
            }
           ]
          }
         }
        ]
       },
       "datasetPreviewNameToCmdIdMap": {},
       "diffDeletes": [],
       "diffInserts": [],
       "displayType": "redashChart",
       "error": null,
       "errorDetails": null,
       "errorSummary": null,
       "errorTraceType": null,
       "finishTime": 0,
       "globalVars": {},
       "guid": "",
       "height": "auto",
       "hideCommandCode": false,
       "hideCommandResult": false,
       "iPythonMetadata": null,
       "inputWidgets": {},
       "isLockedInExamMode": false,
       "latestAssumeRoleInfo": null,
       "latestUser": "a user",
       "latestUserId": null,
       "listResultMetadata": null,
       "metadata": {},
       "nuid": "c663ad3b-84a5-4724-85b1-208438f48d27",
       "origId": 0,
       "parentHierarchy": [],
       "pivotAggregation": null,
       "pivotColumns": null,
       "position": 33.0,
       "resultDbfsErrorMessage": null,
       "resultDbfsStatus": "INLINED_IN_TREE",
       "results": null,
       "showCommandTitle": false,
       "startTime": 0,
       "state": "input",
       "streamStates": {},
       "subcommandOptions": {
        "queryPlan": {
         "groups": [
          {
           "column": "store_name",
           "type": "column"
          }
         ],
         "selects": [
          {
           "column": "store_name",
           "type": "column"
          },
          {
           "alias": "column_26923a16405",
           "args": [
            {
             "column": "revenue",
             "type": "column"
            }
           ],
           "function": "SUM",
           "type": "function"
          }
         ]
        }
       },
       "submitTime": 0,
       "subtype": "tableResultSubCmd.visualization",
       "tableResultIndex": 0,
       "tableResultSettingsMap": {},
       "useConsistentColors": false,
       "version": "CommandV1",
       "width": "auto",
       "workflows": [],
       "xColumns": null,
       "yColumns": null
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "brand_sales = spark.sql(\"\"\"\n",
    "SELECT\n",
    "    brand_name,\n",
    "    ROUND(SUM(revenue),2) revenue\n",
    "FROM biker_r_project.gold.sales_fact\n",
    "GROUP BY brand_name\n",
    "ORDER BY revenue DESC\n",
    "\"\"\")\n",
    "\n",
    "display(brand_sales)"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "5"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": -1,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "Pyspark work",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}