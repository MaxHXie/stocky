import pandas as pd
import numpy as np
import functions

'''
ALL ALGORITHM FUNCTIONS HAVE TO RETURN A ONE ROW DATAFRAME WITH COLUMNS: ['Signal', 'Certainty', 'Datetime', 'Algorithm name']
That dataframe only returns the buy/sell decision for the data in the single point in time it was given.
'''

def sma_50_200(data):
    '''
        INPUT
            data: DataFrame(Date, Highest price, Lowest price, Closing price, Opening price, Volatility)
        OUTPUT
            recommendation_df: ONE ROW DataFrame(Signal, Certainty, Datetime, Algorithm name)
    '''

    def calculate_signal(short_mavg, long_mavg):
        if short_mavg.iloc[-1] > long_mavg.iloc[-1] and short_mavg.iloc[-2] < long_mavg.iloc[-2]:
            signal = 'buy'
        elif short_mavg.iloc[-1] < long_mavg.iloc[-1] and short_mavg.iloc[-2] > long_mavg.iloc[-2]:
            signal = 'sell'
        else:
            signal = 'none'

        return signal

    #----------#

    def calculate_certainty(short_mavg, long_mavg):
            slope_difference = (short_mavg.iloc[-1] / short_mavg.iloc[-2] ) - ( long_mavg.iloc[-1] / long_mavg.iloc[-2] )
            certainty = abs((functions.sigmoid(slope_difference) - 0.5) * 2)
            return certainty

    #----------#

    short_window = 50
    long_window = 200

    calc_df = pd.DataFrame(columns=['short_mavg', 'long_mavg'])
    empty_df = pd.DataFrame()

    if len(data.index) < 3:
        return empty_df

    calc_df['short_mavg'] = data['Closing price'].rolling(window=short_window, center=False).mean()
    calc_df['long_mavg'] = data['Closing price'].rolling(window=long_window, center=False).mean()

    signal = calculate_signal(calc_df['short_mavg'], calc_df['long_mavg'])
    certainty = calculate_certainty(calc_df['short_mavg'], calc_df['long_mavg'])
    date = data.iloc[-1]['Date']
    name = 'sma_50_200'

    if signal == 'none':
        return empty_df

    recommendation_df = pd.DataFrame({
        'Signal':[signal],
        'Certainty':[certainty],
        'Datetime':[date],
        'Algorithm name':[name]
    })

    return recommendation_df

#----------#

def algorithm_2(data):
    return recommendation_df
