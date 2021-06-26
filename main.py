import yfinance as yf
import pandas as pd
import scripts_list as sc
import as_tri_fn as ast

interval = "15m"
period = '59d' #keep the period enough long depending on the interval and gap
gap = 20
i = 1
result=open("result.txt","a")
result.write("Assending triangle\n")
for stock in sc.nifty_50:
    print("entered in lop")
    data = yf.download(tickers=stock, period=period, interval=interval)
    print("data downloaded for ", i)
    df = pd.DataFrame(data)
    close = df['Close'].values
    cl = close.tolist()
    cl.reverse()
    ast.ass_triangle(cl, gap, i, stock)
    i += 1
