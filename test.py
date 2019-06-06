from borsdata_sdk import BorsdataAPI
import pandas as pd
borsdata = BorsdataAPI('d4deb78c785b45dc80c8893c72d7c999')

# Meta
markets = borsdata.get_markets()
branches = borsdata.get_branches()
countries = borsdata.get_countries()
sectors = borsdata.get_sectors()

instruments = borsdata.get_instruments()

# Entries for stock with insId == 3
entries = borsdata.get_instrument_stock_price(3)
entries_from_to = borsdata.get_instrument_stock_price(3, '2009-04-22', '2009-04-25')

columns = [
    'Date',
    'Highest price',
    'Lowest price',
    'Closing price',
    'Opening price',
    'Volatility'
]
variables = ['d', 'h', 'l', 'c', 'o', 'v']
df = pd.DataFrame([[getattr(i,j) for j in variables] for i in entries_from_to], columns = columns)

print(df)

# Updated instruments
updated_instruments = borsdata.get_instruments_updated()

# Last entries of updated instruments
list_of_updated_instruments = borsdata.get_instrument_stock_price_last()

# Reports
yearly_reports = borsdata.get_instrument_reports(3, 'year')
r12s = borsdata.get_instrument_reports(3, 'r12')
quarters = borsdata.get_instrument_reports(3, 'quarter')
