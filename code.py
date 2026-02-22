import yfinance as yf
largeCap = yf.download("POWERGRID.NS", start = "2025-03-04", end = "2026-03-04", interval = "1d")
print("Large Cap Stock Analysis: POWERGRID (NSE)")
print(largeCap.describe()["Close"])
smallCap = yf.download("CYIENTDLM.NS", start = "2025-03-04", end = "2026-03-04", interval = "1d")
print("Small Cap Stock Analysis: CYIENTDLM (NSE)")
print(smallCap.describe()["Close"])