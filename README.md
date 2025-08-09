# 📊 Stock Analysis Dashboard

An interactive Streamlit web app for comparing the historical and live performance of **NIO** and **Tesla** stocks using Yahoo Finance data.  
The dashboard allows users to explore stock trends, key metrics, and moving averages to make data-driven investment insights.

---

## 📖 Overview
This project fetches real-time and historical data for NIO and Tesla, visualizes price trends, and provides analytical tools for investors and analysts.  
It is built using **Python** and **Streamlit**, with live data sourced from the `yfinance` API.

---

## ✨ Features
- 📈 **Live price updates** from Yahoo Finance.
- 📉 **Historical trend analysis** for any date range.
- 📊 **Moving Average Crossover** visualizations to identify potential buy/sell signals.
- 🖥 **Interactive dashboard** with dropdown filters and user controls.

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
