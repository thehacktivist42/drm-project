import yfinance as yf
largeCap = yf.download("POWERGRID.NS", start = "2025-03-04", end = "2026-03-04", interval = "1d")
print(largeCap.head()["Close"])
smallCap = yf.download("CYIENTDLM.NS", start = "2025-03-04", end = "2026-03-04", interval = "1d")
print(smallCap.head()["Close"])