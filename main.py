import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt 

ticker = yf.Ticker("AAPL")
df = ticker.history(period="6mo")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,6), sharex=True)

ax1.plot(df.index, df["Close"])
ax1.set_title("AAPL - 6 Month Close Price")
ax1.set_ylabel("Price (USD)")

df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

ax1.plot(df.index, df["Close"], label="Close")
ax1.plot(df.index, df["MA20"], label="MA20")
ax1.plot(df.index, df["MA50"], label="MA50")
ax1.legend()

ax2.bar(df.index, df["Volume"], color="grey")
ax2.set_ylabel("Volume")

plt.tight_layout()
plt.show()

