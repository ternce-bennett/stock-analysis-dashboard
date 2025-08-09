# 📊 Stock Analysis Dashboard

An interactive Streamlit web app for comparing the historical and live performance of **NIO** and **Tesla** stocks using Yahoo Finance data.  
The dashboard allows users to explore stock trends, key metrics, and moving averages to make data-driven investment insights.

---

## 📖 Overview
This project fetches real-time and historical data for NIO and Tesla, visualizes price trends, and provides analytical tools for investors and analysts.  
It is built using **Python** and **Streamlit**, with live data sourced from the `yfinance` API.

---

## 📌 Features

| Feature                     | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| 📅 Date Range Picker         | Select custom date ranges to analyze historical stock data. |
| 📈 Price Comparison Chart    | Interactive line chart comparing NIO and Tesla stocks.      |
| 📊 Key Performance Indicators (KPIs) | Average daily return and volatility for both stocks.     |
| 🔁 Volume Traded             | Line charts showing daily traded volume.                     |
| 📉 Daily Returns             | Visualize and compare daily return distributions.            |
| ✅ Real-time Data            | Fetches updated market data from Yahoo Finance via yfinance. |

---

## 📊 Data Sources
- [Yahoo Finance API](https://pypi.org/project/yfinance/) for historical and live stock data.

---

## 🛠 Tech Stack
- **Language:** Python 3.10  
- **Libraries:** Pandas, NumPy, Matplotlib, Streamlit, YFinance  
- **Tools:** Git, VS Code

---

## ⚙️ Setup & Installation
```bash
# 1. Clone the repository
git clone https://github.com/ternce-bennett/stock-analysis-dashboard.git
cd stock-analysis-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
