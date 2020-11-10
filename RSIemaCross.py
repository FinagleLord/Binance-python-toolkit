from helper import *
import time, tulipy, os, ctypes
from ansicolors import bg, fg
import ansicolors as ac
os.system('cls||clear')

pair     = 'ETHUSDT'
interval = '15m'
quantity = 0.25 # ETH
inpos    = False
testing  = True

def strat(pair, quantity, interval):
    global inpos
    while True:
        # get data
        Get_kline(pair, interval)
        closes = Get_kline.closes
        # indicators
        rsi         = tulipy.rsi(closes,14)
        rsiema      =    tulipy.ema(rsi,22)
        last_rsi    =    rsi[-1] 
        last_rsiema = rsiema[-1]
        
        
        # Buy
        if last_rsi > last_rsiema and last_rsi > 50 and inpos == False: 
            if testing == False:
                print(f'Buying {quantity} {pair}')
                price = Get_price(pair)
                order_succeded = Limit_buy(pair, quantity, price)
                if order_succeded:
                    inpos = True
                    print(f'{fg.yellow}sucess{ac.clear}')
        
        # Sell      
        elif inpos and last_rsi < last_rsiema or last_rsi < 50:
            if testing == False:
                print(f'Selling {quantity} {pair}')
                price = Get_price(pair)
                order_succeded = Limit_sell(pair, quantity, price)
                if order_succeded:
                    print(f'{fg.yellow}sucess{ac.clear}')
                    time.sleep(3600)
                    inpos = False
                      
        
        price = Get_price(pair)
        print(f'{pair}: {round(price, 2)}')
        time.sleep(1)
        
ctypes.windll.kernel32.SetConsoleTitleW(f"RSIemaCross: {pair}")
strat(pair,quantity,interval)
    
