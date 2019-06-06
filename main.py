import datetime
import csv
import pandas as pd
from threading import Timer
from borsdata_sdk import BorsdataAPI
from algorithm import Algorithm

#----------#

def initialize_api():
	borsdata = BorsdataAPI('d4deb78c785b45dc80c8893c72d7c999')
	stocks = borsdata.get_instruments()

	return borsdata, stocks

#----------#

def initialize_files(borsdata, stocks, start_date, end_date):
	for stock in stocks:
		stock_data_list = borsdata.get_instrument_stock_price(stock.insId, start_date, end_date)
		columns = ['Date', 'Highest price', 'Lowest price', 'Closing price', 'Opening price', 'Volatility']
		variables = ['d', 'h', 'l', 'c', 'o', 'v']
		df = pd.DataFrame([[getattr(i,j) for j in variables] for i in stock_data_list], columns = columns)

		df.to_csv('data/' + stock.name + '.csv', index=False)

#----------#

def initialize_variables():
	START_DAYS_AGO = 365
	END_DAYS_AGO = 0
	INITIALIZE_FILES = False
	ALGORITHM_LIST = [Algorithm('sma_50_200', 10)]

	start_date = datetime.date.today() - datetime.timedelta(START_DAYS_AGO)
	end_date = datetime.date.today() - datetime.timedelta(END_DAYS_AGO)

	return start_date, end_date, INITIALIZE_FILES, ALGORITHM_LIST

#----------#

def main():
	borsdata, stocks = initialize_api()
	start_date, end_date, initialize, algorithm_list = initialize_variables()
	file_name = "Report Starting from " + str(start_date)
	if initialize != False:
		initialize_files(borsdata, stocks, start_date, end_date)

	for stock in stocks:
		for algorithm in algorithm_list:
			try:
				stock_df = pd.read_csv('data/' + stock.name + '.csv', sep=',') # Read data
				recommendation_df = algorithm.recommend(stock_df) # Run data through algorithm
				if not recommendation_df.empty:
					''' Store the recommendations '''
					recommendation_df.insert(loc=0, column='Stock name', value=stock.name)
					recommendation_df.to_csv('reports/' + file_name + '.csv', mode='a', index=False, header=False) # Store recommendations

			except FileNotFoundError:
				print('Could not retrieve file: data/' + stock.name + '.csv')

#----------#

if __name__ == "__main__":
	main()
