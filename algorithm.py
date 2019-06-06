import pandas as pd
import numpy as np
import algorithm_functions

#----------#

class Algorithm:
    def __init__(self, name, time_window, backtest_lookback_days=30):
        '''
            ATTRIBUTES
                name: String. Name of the algorithm.
                time_window: Integer. Number of time units back in time to offer recommendations for.
                backtest_lookback_days: Integer. Number of days back in time from where the Backtest starts.
        '''

        self.name = name
        self.time_window = time_window
        self.backtest_lookback_days = backtest_lookback_days

        if name == "sma_50_200":
            self.algorithm = algorithm_functions.sma_50_200
        elif name == "something else":
            self.algorithm = algorithm_functions.algorithm_2
        else:
            raise KeyError(str(self.name) + ": That algorithm does not exist.")

    #----------#

    def recommend(self, data):
        '''
            INPUT
                data: DataFrame(Date, Highest price, Lowest price, Closing price, Opening price, Volatility)
                time_window: Int. Number of time units back in time to calculate and offer a recommendation for.
            OUTPUT
                recommendation_df: DataFrame(Signal, Certainty, Datetime, Algorithm name)
        '''
        recommendation_df = pd.DataFrame()
        ''' For each time unit, remove one row (the latest row)'''
        for time_unit in range(1, self.time_window+1):
            back_in_time_data = data.iloc[:-time_unit]
            return_df = self.algorithm(back_in_time_data)
            recommendation_df = recommendation_df.append(return_df)
        return recommendation_df

    #----------#

    def backtest(self, data):
        buy_data = []
        sell_data = []

        capital = float(100000.0)
        lookback_data = data[ : self.backtest_lookback_days]
        future_data = data[self.backtest_lookback_days+1 : ]
        shares = float(0.0)

        for datapoint in future_data:
            ''' Adjust future_data and lookback_data one time_unit as time moves forward with one time_unit '''
            future_data.pop(0)
            lookback_data.append(datapoint)

            signal_list, certainty_list = recommend(lockback_data)
            signal = signal_list[0]
            certainty = certainty_list[0]

            ''' Calculate difference in capital and shares '''
            if signal == "buy":
                money_spent = float(capital * certainty)
                if money_spent > capital:
                    money_spent = capital
                    capital = float(0.0)

                capital -= money_spent
                shares += money_spent / datapoint['price']
                buy_data.append([datapoint['price'], datapoint['datetime']])

            elif signal == "sell":
                sold_shares = float(shares * certainty)
                if sold_shares > shares:
                    sold_shares = shares
                    shares = float(0.0)

                money = sold_shares * datapoint['price']
                capital += money
                sell_data.append([datapoint['price'], datapoint['datetime']])

        print("Final capital: " + str(capital))

#----------#
