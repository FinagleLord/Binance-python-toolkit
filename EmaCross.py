from helper import *
import time, tulipy, os, ctypes
import ansicolors as ac
from ac import bg, fg, clp
os.system('cls||clear')
inpos    = False


pair     = input('What pair: ')
clp('valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M', fg.magenta)
interval = input('What interval: ') 
quantity = input('What quantity: ')
testing  = config.testing

def strat(pair, quantity, interval):
    global inpos
    while True:
        price = Get_price(pair)
        # get data
        Get_kline(pair, interval)
        closes = Get_kline.closes
        # indicators
        shortema      = tulipy.ema(closes,22)
        medema        = tulipy.ema(closes,50)
        longema       = tulipy.ema(closes,200)
        last_close    = closes[-1]
        last_shortema = shortema[-1] 
        last_medema   = medema[-1]
        last_longema  = longema[-1]
        # Buy
        if last_close > last_shortema and last_close > last_medema and last_close > last_longema and inpos ==False:
            print(f'Buying {quantity} {pair}')
            if testing == False:
                price = Get_price(pair)
                order_succeded = Limit_buy(pair, quantity, price)
                if order_succeded:
                    inpos = True
                    print('sucess')
        # Sell      
        elif inpos and last_close > last_shortema or last_close > last_medema or last_close > last_longema:
            print('Selling')
            if testing == False:
                price = Get_price(pair)
                order_succeded = Limit_sell(pair, quantity, price)
                if order_succeded:
                    time.sleep(3600)
                    inpos = False
                    print('sucess')
        print(f'{pair}:{price}')
        time.sleep(1)
        
ctypes.windll.kernel32.SetConsoleTitleW(f"EmaCross: {pair}")
strat(pair,quantity,interval)
