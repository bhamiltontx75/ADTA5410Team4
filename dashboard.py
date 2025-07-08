import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load data
df = pd.read_csv("group4cleaneddata.csv", parse_dates=['booking_datetime'])

st.title("ADTA5410 Team 4 Dashboard")
st.write("Welcome to Team 4's Dashboard.")

# --- Interactive Histogram ---
st.subheader("Distribution of Stay Nights")
bins = st.slider("Select number of bins for histogram", min_value=5, max_value=50, value=20)
fig_hist = px.histogram(df, x='stay_nights', nbins=bins, marginal='rug', title='Stay Nights Distribution')
st.plotly_chart(fig_hist)

# --- Interactive Box Plot ---
st.subheader("Market Segment vs. Average Daily Rate")
selected_markets = st.multiselect("Filter market segments", options=df['market_segment'].unique(), default=df['market_segment'].unique())
filtered_df = df[df['market_segment'].isin(selected_markets)]
fig_box = px.box(filtered_df, x='market_segment', y='avg_daily_rate', title='Boxplot of Market Segment vs. Avg Daily Rate')
st.plotly_chart(fig_box)

# --- Interactive Pairplot Equivalent ---
st.subheader("Scatter Matrix of Key Metrics")
fig_matrix = px.scatter_matrix(
    df,
    dimensions=['target_value', 'stay_nights', 'lead_time_days', 'avg_daily_rate'],
    title="Scatter Matrix of Booking Features",
    height=700
)
st.plotly_chart(fig_matrix)

# --- Correlation Heatmap ---
st.subheader("Correlation Matrix")
corr = df.corr(numeric_only=True)
fig_heatmap = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale='RdBu_r',
    title="Correlation Matrix",
    aspect="auto"
)
st.plotly_chart(fig_heatmap)
