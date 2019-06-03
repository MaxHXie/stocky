class Stock:
	def __init__(self, stock_name, borsdata_id):
		self.stock_name = stock_name
		self.borsdata_id = borsdata_id
		self.todays_price = 0
		self.ma_days = [50,200] # Define which ma_x you want to calculate. e.g. if you want MA50 and MA200 then define it as [50, 200]
		self.ma_x = {}
		
	def calculate_ma_x(self, historic_prices, ma_days):
		ma_x = sum(historic_prices)/ma_days
		self.ma_x[ma_days] = ma_x
		return ma_x