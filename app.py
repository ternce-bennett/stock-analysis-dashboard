import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Title
st.set_page_config(page_title="Stock Comparison Dashboard", layout="wide")
st.title("📈 NIO vs TSLA Stock Analysis Dashboard")

# Sidebar inputs
with st.sidebar:
    st.header("Input Parameters")
    start_date = st.date_input("Start date", pd.to_datetime("2022-01-01"))
    end_date = st.date_input("End date", pd.to_datetime("2025-01-01"))
    show_ma = st.checkbox("Show Moving Averages", value=True)

# Tickers to compare
tickers = ["NIO", "TSLA"]
data = {}

# Fetch data for both tickers
for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df["MA50"] = df["Close"].rolling(window=50).mean()
    df["MA200"] = df["Close"].rolling(window=200).mean()
    df["Returns"] = df["Close"].pct_change()
    data[ticker] = df

# Check if data is available
if any(df.empty for df in data.values()):
    st.error("No data found for one or more tickers in the selected date range.")
    st.stop()

# KPIs comparison
st.subheader("📊 Key Performance Indicators")
col1, col2 = st.columns(2)
col1.metric("NIO Avg Daily Return", f"{data['NIO']['Returns'].mean():.2%}")
col2.metric("TSLA Avg Daily Return", f"{data['TSLA']['Returns'].mean():.2%}")
col1.metric("NIO Volatility", f"{data['NIO']['Returns'].std():.2%}")
col2.metric("TSLA Volatility", f"{data['TSLA']['Returns'].std():.2%}")

# Price comparison chart
st.subheader("📈 Price Chart Comparison")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data["NIO"].index, y=data["NIO"]["Close"], name="NIO Close"))
fig.add_trace(go.Scatter(x=data["TSLA"].index, y=data["TSLA"]["Close"], name="TSLA Close"))
if show_ma:
    fig.add_trace(go.Scatter(x=data["NIO"].index, y=data["NIO"]["MA50"], name="NIO MA 50"))
    fig.add_trace(go.Scatter(x=data["TSLA"].index, y=data["TSLA"]["MA50"], name="TSLA MA 50"))
    fig.add_trace(go.Scatter(x=data["NIO"].index, y=data["NIO"]["MA200"], name="NIO MA 200"))
    fig.add_trace(go.Scatter(x=data["TSLA"].index, y=data["TSLA"]["MA200"], name="TSLA MA 200"))
fig.update_layout(xaxis_title="Date", yaxis_title="Price", height=500)
st.plotly_chart(fig, use_container_width=True)

# Volume charts
st.subheader("🔄 Volume Traded")
col1, col2 = st.columns(2)
col1.write("NIO")
col1.line_chart(data["NIO"]["Volume"])
col2.write("TSLA")
col2.line_chart(data["TSLA"]["Volume"])

# Daily Returns charts
st.subheader("📉 Daily Returns")
col1, col2 = st.columns(2)
col1.write("NIO")
col1.line_chart(data["NIO"]["Returns"].dropna())
col2.write("TSLA")
col2.line_chart(data["TSLA"]["Returns"].dropna())
