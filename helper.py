from binance.enums import *
from binance.client import Client
import config

client = Client(config.binance_api_key, config.binance_secret_key)

def Get_kline(pair, interval):
    "Gets 500 candles of kline data, creates a CSV that appends itself"
    import numpy, csv
    from numpy import genfromtxt
    kline = client.get_klines(symbol=pair, interval=interval)
    with open(f'{pair}_{interval}.csv', 'w', newline='') as csvfile:
        csv.DictReader(csvfile)
        csvwriter = csv.writer(csvfile, delimiter=',')
        for i in kline:
            csvwriter.writerow(i)
    ohlc_data = genfromtxt(f'{pair}_{interval}.csv', delimiter=',')
    Get_kline.opentimes    = numpy.array(ohlc_data[:,0])
    Get_kline.opens        = numpy.array(ohlc_data[:,1])
    Get_kline.highs        = numpy.array(ohlc_data[:,2])
    Get_kline.lows         = numpy.array(ohlc_data[:,3])
    Get_kline.closes       = numpy.array(ohlc_data[:,4])
    Get_kline.volumes      = numpy.array(ohlc_data[:,5])
    Get_kline.closetimes   = numpy.array(ohlc_data[:,6])
    Get_kline.quotevolumes = numpy.array(ohlc_data[:,7])
  
def Trade_history(pair):
    return client.get_my_trades(symbol=pair)

def Open_orders(pair):
    return client.get_open_orders(symbol=pair)

def Asset_balance(pair):
    return client.get_asset_balance(asset=pair)

def Get_price(pair):
    json_price    = client.get_symbol_ticker(symbol=pair)
    return json_price["price"]
    
def Limit_buy(pair, quantity, price):
    return client.order_limit_buy(symbol= pair,quantity=quantity, price=price)

def Limit_sell(pair, quantity, price):
    return client.order_limit_sell(symbol = pair,quantity=quantity, price=price)

def Market_buy(pair, quantity):
    return client.order_market_buy(symbol=pair,quantity=quantity)    

def Market_sell(pair, quantity):    
    return client.order_market_sell(symbol=pair,quantity=quantity)

def Print_price(pair, decimals=2):
    price = Get_price(pair)
    return print(f'{pair}:{round(price, decimals)}')
