import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import os

from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# Database Connection
# -----------------------------------

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

# -----------------------------------
# Data Loading
# -----------------------------------

cases_df = pd.read_sql(
    "SELECT * FROM cases",
    connection
)

escalation_df = pd.read_sql(
    "SELECT * FROM escalations",
    connection
)

knowledge_df = pd.read_sql(
    "SELECT * FROM knowledge",
    connection
)

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Agentic Support Hub Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Agentic Support Hub Dashboard")

st.markdown("---")

# -----------------------------------
# KPI Section
# -----------------------------------

total_cases = len(cases_df)
total_escalations = len(escalation_df)
knowledge_articles = len(knowledge_df)
ai_resolved = total_cases - total_escalations

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Cases",
        total_cases
    )

with col2:
    st.metric(
        "Escalations",
        total_escalations
    )

with col3:
    st.metric(
        "Knowledge Articles",
        knowledge_articles
    )

with col4:
    st.metric(
        "AI Resolved",
        ai_resolved
    )

st.markdown("---")

# -----------------------------------
# Charts Section
# -----------------------------------

chart_col1, chart_col2 = st.columns(2)

# Product Distribution

with chart_col1:

    st.subheader("📦 Product Distribution")

    product_counts = (
        cases_df["product"]
        .value_counts()
        .reset_index()
    )

    product_counts.columns = [
        "Product",
        "Count"
    ]

    fig_product = px.pie(
        product_counts,
        names="Product",
        values="Count",
        hole=0.4
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )

# Case Resolution Status

with chart_col2:

    st.subheader("📈 Resolution Overview")

    resolution_data = pd.DataFrame({
        "Type": [
            "AI Resolved",
            "Escalated"
        ],
        "Count": [
            ai_resolved,
            total_escalations
        ]
    })

    fig_resolution = px.bar(
        resolution_data,
        x="Type",
        y="Count",
        color="Type",
        text="Count"
    )

    st.plotly_chart(
        fig_resolution,
        use_container_width=True
    )

st.markdown("---")

# -----------------------------------
# Escalations
# -----------------------------------

st.subheader("⚠ Recent Escalations")

if len(escalation_df) > 0:

    st.dataframe(
        escalation_df.sort_values(
            by="id",
            ascending=False
        ),
        use_container_width=True
    )

else:

    st.success(
        "No escalated cases found."
    )

st.markdown("---")

# -----------------------------------
# Recent Cases
# -----------------------------------

st.subheader("📋 Recent Cases")

st.dataframe(
    cases_df.sort_values(
        by="id",
        ascending=False
    ),
    use_container_width=True
)

connection.close()