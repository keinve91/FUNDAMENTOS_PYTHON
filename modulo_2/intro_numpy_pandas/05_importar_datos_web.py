import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf

# --- OPCIÓN 1: PANDAS DATAREADER (Ejemplo: Naver) ---
# Extrae datos de la web a un DataFrame.
# Argumentos: Código de la acción, Fuente ('naver'), Inicio, Fin.
# '005930' es Samsung en el índice KOSPI.
datos_samsung = pdr.DataReader('005930', 'naver', '2022-01-01', '2022-01-31')

# --- OPCIÓN 2: YFINANCE (Ejemplo: Yahoo Finance) ---
# Más robusto para datos de acciones de EE.UU. como el SPY (S&P 500).
stock = 'SPY'
startdate = '2022-01-01'
enddate = '2022-01-31'

# Descarga los datos directamente a un DataFrame
stocks_df = yf.download(stock, start=startdate, end=enddate)
print(stocks_df)