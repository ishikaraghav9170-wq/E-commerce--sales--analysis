import mysql.connector
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt



# -----------------------------
# MySQL Connection
# -----------------------------

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@12345",
        database="ecommerce_db"
    )
    return connection


# Test connection
try:
    connection = get_connection()

    if connection.is_connected():
        print("MySQL connection successful")

    connection.close()

except Exception as e:
    print(f"MySQL connection failed: {e}")


# -----------------------------
# Run SQL Query
# -----------------------------

def run_query(query):
    connection = get_connection()

    df = pd.read_sql(query, connection)

    connection.close()

    return df


query = """
SELECT COUNT(*) AS total_sales
FROM cleaned_sales;
"""

ts= run_query(query)

print(ts)



query="""
SELECT SUM(Profit) AS total_profit
FROM cleaned_sales;"""
tp=run_query(query)
print(tp)



query="""SELECT 
    Segment,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM  cleaned_sales
GROUP BY Segment
ORDER BY total_sales DESC;"""


result=run_query(query)
print(result)


query="""
SELECT 
    MIN(Sales) AS minimum_sales,
    MAX(Sales) AS maximum_sales
FROM cleaned_sales;"""

min_max=run_query(query)
print(min_max)