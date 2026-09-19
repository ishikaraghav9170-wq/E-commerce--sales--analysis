import streamlit as st
from database import run_query
#-----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Dashboard Title
# -----------------------------

st.title("📊 E-Commerce Sales Dashboard")


# -----------------------------
# Get Data
# -----------------------------
query = """
SELECT COUNT(*) AS total_sales
FROM cleaned_sales;
"""

total_sales= run_query(query)
print(total_sales)





# -----------------------------
# Total Sales Records
# -----------------------------

st.subheader("🛒 Total Sales Records")

st.write(
    total_sales.iloc[0]["total_sales"]
)


# -----------------------------
# Total Profit
# -----------------------------



query="""
SELECT SUM(Profit) AS total_profit
FROM cleaned_sales;"""
total_profit=run_query(query)


st.subheader("💰 Total Profit")

st.write(
    total_profit.iloc[0]["total_profit"]
)


# -----------------------------
# Segment Analysis
# -----------------------------


query="""SELECT 
    Segment,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM  cleaned_sales
GROUP BY Segment
ORDER BY total_sales DESC;"""

segment_data=run_query(query)


st.subheader("📊 Sales & Profit by Segment")

st.bar_chart(
    segment_data.set_index("Segment")[
        ["total_sales", "total_profit"]
    ]
)


# -----------------------------
# Segment Data Table
# -----------------------------

st.subheader("📋 Segment Details")

st.dataframe(
    segment_data,
    use_container_width=True
)


# -----------------------------
# Minimum & Maximum Sales
# -----------------------------
query="""SELECT 
    MIN(Sales) AS minimum_sales,
    MAX(Sales) AS maximum_sales
FROM sales;"""
min_max=run_query(query)

st.subheader("💵 Sales Range")

st.write(min_max)