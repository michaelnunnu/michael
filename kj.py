from __future__ import annotations
from requests import Session
from requests.exceptions import ReadTimeout
from pathlib import Path
from pickle import loads as pickle_loads, dumps as pickle_dumps
from mthrottle import Throttle
from datetime import datetime
import math,os
from datetime import datetime
import numpy as np
import pandas_ta as taa
from requests import Session
from datetime import date, timedelta
import pyotp
import datetime
import enum
import requests
import dateutil.parser
import pyotp,time
import json
import logging
import random
import re
import string
import pandas as pd
import websocket
import requests
import json,re
from io import StringIO
import time,threading,sys
import pytz
import pandas_market_calendars as mcal

nyse = mcal.get_calendar('NSE')
#eastern_tz = pytz.timezone('Asia/Kolkata')
d = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
#tz_NY = pytz.timezone('Asia/Kolkata')   
#utc_offset = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
today = date.today()
today1 = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date()
print("michael",datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time(),d.minute,datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date(),file=sys.stderr)
start_date = (datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d'))
if (datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time() > datetime.time(0, 0,0)) and (datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time() < datetime.time(9, 17, 0)):
    start_date = (datetime.datetime.now(pytz.timezone('Asia/Kolkata'))- timedelta(days=1)).strftime('%Y-%m-%d')
# else
end_date = start_date
#print(start_date)
#d = (datetime.datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
#print(d)
# Show available calendars
#print(mcal.get_calendar_names())
i = 1
x = 1
while i:
    early = nyse.schedule(start_date=start_date, end_date=end_date)
    start_date = (datetime.datetime.now(pytz.timezone('Asia/Kolkata')) - timedelta(days=x)).strftime('%Y-%m-%d')
    x = x + 1
    if len(early)>0:
        i = 0
        print(early.index.strftime('%Y-%m-%d').values[0])
fromm = early.index.strftime('%Y-%m-%d').values[0]
print("michael kj fromm ",fromm,file=sys.stderr)
# class kite:

#     # Exchanges
#     EXCHANGE_NSE = "NSE"
#     EXCHANGE_BSE = "BSE"
#     EXCHANGE_NFO = "NFO"
#     EXCHANGE_CDS = "CDS"
#     EXCHANGE_BFO = "BFO"
#     EXCHANGE_MCX = "MCX"
#     EXCHANGE_BCD = "BCD"

#     # Products
#     PRODUCT_MIS = "MIS"
#     PRODUCT_CNC = "CNC"
#     PRODUCT_NRML = "NRML"
#     PRODUCT_CO = "CO"

#     # Order types
#     ORDER_TYPE_MARKET = "MARKET"
#     ORDER_TYPE_LIMIT = "LIMIT"
#     ORDER_TYPE_SLM = "SL-M"
#     ORDER_TYPE_SL = "SL"

#     # Varities
#     VARIETY_REGULAR = "regular"
#     VARIETY_CO = "co"
#     VARIETY_AMO = "amo"
#     VARIETY_ICEBERG = "iceberg"
#     VARIETY_AUCTION = "auction"

#     # Transaction type
#     TRANSACTION_TYPE_BUY = "BUY"
#     TRANSACTION_TYPE_SELL = "SELL"

#     # Validity
#     VALIDITY_DAY = "DAY"
#     VALIDITY_IOC = "IOC"
#     VALIDITY_TTL = "TTL"

#     # Position Type
#     POSITION_TYPE_DAY = "day"
#     POSITION_TYPE_OVERNIGHT = "overnight"

#     # Margins segments
#     MARGIN_EQUITY = "equity"
#     MARGIN_COMMODITY = "commodity"

#     # GTT order type
#     GTT_TYPE_OCO = "two-leg"
#     GTT_TYPE_SINGLE = "single"

# #     base_dir = Path(__file__).parent
#     base_url = 'https://api.kite.trade'
#     def __init__(self, enctoken=None):
#         return None

#     def instruments(s, exchange=None):
#         '''return a CSV dump of all tradable instruments'''

#         url = f'{base_url}/instruments'

#         if exchange:
#             url += f'/{exchange}'

#         res = s.get(url)

#         if res:
#             return res.content

#     def quote(s, instruments: str | list | tuple | set):
#         '''Return the full market quotes - ohlc, OI, bid/ask etc'''
#         base_url = 'https://api.kite.trade'

#         if type(instruments) in (list, tuple, set) and len(instruments) > 500:
#             raise ValueError('Instruments length cannot exceed 500')

#         res = s.get(f"{base_url}/quote",params={'i': instruments})

#         return res.json()['data'] if res else None

#     def ohlc(s, instruments: str | list | tuple | set):
#         '''Returns ohlc and last traded price'''
#         base_url = 'https://api.kite.trade'

#         if type(instruments) in (list, tuple, set) and len(instruments) > 1000:
#             raise ValueError('Instruments length cannot exceed 1000')

#         res = s.get(f"{base_url}/quote/ohlc", params={'i': instruments})

#         return res.json()['data'] if res else None

#     def ltp(instruments,s):
#         '''Returns the last traded price'''

#         if type(instruments) in (list, tuple, set) and len(instruments) > 1000:
#             raise ValueError('Instruments length cannot exceed 1000')
#         base_url = 'https://api.kite.trade'
#         res = s.get(f"{base_url}/quote/ltp", params={'i': instruments[0]})
#         print(res.json()['data'][instruments[0]]['last_price'])
#         print(type(res.json()['data'][instruments[0]]['last_price']))
#         return res.json()['data'][instruments[0]]['last_price'] if res else None

#     def holdings(s):
#         '''Return the list of long term equity holdings'''
#         base_url = 'https://api.kite.trade'
#         res = s.get(f'{base_url}/portfolio/holdings')

#         return res.json()['data'] if res else None

#     def positions(s):
#         '''Retrieve the list of short term positions'''
#         base_url = 'https://api.kite.trade'
#         res = s.get(f'{base_url}/portfolio/positions')

#         return res.json()['data'] if res else None

#     def auctions(s,self):
#         '''Retrieve the list of auctions that are currently being held'''
#         base_url = 'https://api.kite.trade'
#         res = s.get(f'{base_url}/portfolio/auctions')

#         return res.json()['data'] if res else None

#     def margins(s, segment=None):
#         '''Returns funds, cash, and margin information for the user
#         for equity and commodity segments'''
#         base_url = 'https://api.kite.trade'

#         url = f'{base_url}/user/margins'

#         if segment:
#             url += f'/{segment}'
#         res = s.get(url)

#         return res.json()['data'] if res else None

#     def profile(s):
#         '''Retrieve the user profile'''
#         base_url = 'https://api.kite.trade'
#         res = s.get(f'{base_url}/user/profile')

#         return res.json()['data'] if res else None

#     def historical_data(s,
#                         instrument_token: str,
#                         from_dt: datetime,
#                         to_dt: datetime,
#                         interval: str,
#                         continuous=False,
#                         oi=False):
#         '''return historical candle records for a given instrument.'''

#         url = f"{base_url}/instruments/historical/{instrument_token}/{interval}"

#         payload = {
#             "from": from_dt,
#             "to": to_dt,
#             "continuous": int(continuous),
#             "oi": int(oi)
#         }

#         res = s.get(url, method='GET', params=payload)

#         return res.json()['data']['candles'] if res else None

#     def place_order(s,
#                     variety,
#                     exchange,
#                     tradingsymbol,
#                     transaction_type,
#                     quantity,
#                     product,
#                     order_type,
#                     price=None,
#                     validity=None,
#                     validity_ttl=None,
#                     disclosed_quantity=None,
#                     trigger_price=None,
#                     iceberg_legs=None,
#                     iceberg_quantity=None,
#                     auction_number=None,
#                     tag=None):
#         '''Place an order of a particular variety'''
#         base_url = 'https://api.kite.trade'
#         url = f'{base_url}/orders/{variety}'

#         params = locals()

#         # del params['self']

#         for k in list(params.keys()):
#             if params[k] is None:
#                 del params[k]

#         res = s.post(url, data=params)
        
#         return res.json()['data']['order_id'] if res else None

#     def modify_order(s,variety,
#                      order_id,
#                      quantity,
#                      price):
#         '''Modify an open order.'''
#         base_url = 'https://api.kite.trade'
#         url = f'{base_url}/orders/{variety}/{order_id}'

#         params = locals()

#         for k in list(params.keys()):
#             if params[k] is None:
#                 del (params[k])

#         res = s.put(url,data=params)

#         return res.json()['data']['order_id'] if res else None

#     def cancel_order(s, variety, order_id):
#         '''Cancel an order.'''
#         base_url = 'https://api.kite.trade'
#         url = f'{base_url}/orders/{variety}/{order_id}'
#         res = s.delete(url)

#         return res.json()['data']['order_id'] if res else None

#     def orders(s):
#         '''Get list of all orders for the day'''
#         base_url = 'https://api.kite.trade'
#         res = s.get(f'{base_url}/orders')

#         return res.json()['data'] if res else None

#     def order_history(s, order_id):
#         '''Get history of individual orders'''
#         base_url = 'https://api.kite.trade'
#         url = f'{base_url}/orders/{order_id}'

#         res = s.get(url)

#         return res.json()['data'] if res else None

#     def trades(s):
#         '''Get the list of all executed trades for the day'''
#         base_url = 'https://api.kite.trade'
#         url = f'{base_url}/trades'

#         res = s.get(url)

#         return res.json()['data'] if res else None

#     def order_trades(s, order_id):
#         '''Get the the trades generated by an order'''
#         base_url = 'https://api.kite.trade'
#         url = f'{base_url}/orders/{order_id}/trades'
#         res = s.get(url)

#         return res.json()['data'] if res else None
        
class KiteApp:
    # Products
    PRODUCT_MIS = "MIS"
    PRODUCT_CNC = "CNC"
    PRODUCT_NRML = "NRML"
    PRODUCT_CO = "CO"

    # Order types
    ORDER_TYPE_MARKET = "MARKET"
    ORDER_TYPE_LIMIT = "LIMIT"
    ORDER_TYPE_SLM = "SL-M"
    ORDER_TYPE_SL = "SL"

    # Varities
    VARIETY_REGULAR = "regular"
    VARIETY_CO = "co"
    VARIETY_AMO = "amo"

    # Transaction type
    TRANSACTION_TYPE_BUY = "BUY"
    TRANSACTION_TYPE_SELL = "SELL"

    # Validity
    VALIDITY_DAY = "DAY"
    VALIDITY_IOC = "IOC"

    # Exchanges
    EXCHANGE_NSE = "NSE"
    EXCHANGE_BSE = "BSE"
    EXCHANGE_NFO = "NFO"
    EXCHANGE_CDS = "CDS"
    EXCHANGE_BFO = "BFO"
    EXCHANGE_MCX = "MCX"

    def __init__(self, enctoken):
        self.enctoken = enctoken
        self.headers = {"Authorization": f"enctoken {self.enctoken}"}
        self.session = requests.session()
        self.root_url = "https://kite.zerodha.com/oms"
        self.session.get(self.root_url, headers=self.headers)

    def instruments(self, exchange=None):
        data = self.session.get(f"https://api.kite.trade/instruments").text.split("\n")
        Exchange = []
        for i in data[1:-1]:
            row = i.split(",")
            if exchange is None or exchange == row[11]:
                Exchange.append({'instrument_token': int(row[0]), 'exchange_token': row[1], 'tradingsymbol': row[2],
                                 'name': row[3][1:-1], 'last_price': float(row[4]),
                                 'expiry': dateutil.parser.parse(row[5]).date() if row[5] != "" else None,
                                 'strike': float(row[6]), 'tick_size': float(row[7]), 'lot_size': int(row[8]),
                                 'instrument_type': row[9], 'segment': row[10],
                                 'exchange': row[11]})
        return Exchange

    def historical_data(self, instrument_token, from_date, to_date, interval, continuous=False, oi=False):
        params = {"from": from_date,
                  "to": to_date,
                  "interval": interval,
                  "continuous": 1 if continuous else 0,
                  "oi": 1 if oi else 0}
        lst = self.session.get(
            f"{self.root_url}/instruments/historical/{instrument_token}/{interval}", params=params,
            headers=self.headers).json()["data"]["candles"]
        records = []
        for i in lst:
            record = {"date": dateutil.parser.parse(i[0]), "open": i[1], "high": i[2], "low": i[3],
                      "close": i[4], "volume": i[5],}
            if len(i) == 7:
                record["oi"] = i[6]
            records.append(record)
        return records

    def margins(self):
        margins = self.session.get(f"{self.root_url}/user/margins", headers=self.headers).json()["data"]
        return margins

    def profile(self):
        profile = self.session.get(f"{self.root_url}/user/profile", headers=self.headers).json()["data"]
        return profile

    def orders(self):
        orders = self.session.get(f"{self.root_url}/orders", headers=self.headers).json()["data"]
        return orders

    def order_history(self, order_id):
        '''Get history of individual orders'''
        url = f'{self.root_url}/orders/{order_id}'

        res = self.session.get(url, headers=self.headers)

        return res.json()['data'] if res else None

    def order_trades(self, order_id):
        '''Get the the trades generated by an order'''
        url = f'{self.root_url}/orders/{order_id}/trades'
        res = self.session.get(url, headers=self.headers)
        return res.json()['data'] if res else None

    def ltp(self, instruments):
        '''Returns the last traded price'''

        if type(instruments) in (list, tuple, set) and len(instruments) > 1000:
            raise ValueError('Instruments length cannot exceed 1000')
        base_url = 'https://api.kite.trade'
        res = self.session.get(f"{self.root_url}/quote/ltp", headers={'i': instruments[0]})
        print(res)
        print(type(res.json()['data'][instruments[0]]['last_price']))
        return res.json()['data'][instruments[0]]['last_price'] if res else None
    
    def positions(self):
        positions = self.session.get(f"{self.root_url}/portfolio/positions", headers=self.headers).json()["data"]
        return positions

    def place_order(self, variety, exchange, tradingsymbol, transaction_type, quantity, product, order_type, price=None,
                    validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                    trailing_stoploss=None, tag=None):
        params = locals()
        del params["self"]
        for k in list(params.keys()):
            if params[k] is None:
                del params[k]
        print("current price ",params," ", fromm,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        order_id = self.session.post(f"{self.root_url}/orders/{variety}",
                                     data=params, headers=self.headers).json()["data"]["order_id"]
        return order_id

    def modify_order(self, variety, order_id, parent_order_id=None, quantity=None, price=None, order_type=None,
                     trigger_price=None, validity=None, disclosed_quantity=None):
        params = locals()
        del params["self"]
        for k in list(params.keys()):
            if params[k] is None:
                del params[k]

        order_id = self.session.put(f"{self.root_url}/orders/{variety}/{order_id}",
                                    data=params, headers=self.headers).json()["data"][
            "order_id"]
        return order_id

    def cancel_order(self, variety, order_id, parent_order_id=None):
        order_id = self.session.delete(f"{self.root_url}/orders/{variety}/{order_id}",
                                       data={"parent_order_id": parent_order_id} if parent_order_id else {},
                                       headers=self.headers).json()["data"]["order_id"]
        return order_id



def order_place(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,reject_count,cancel_count,sqr_order_id):
    kt_order_id_1 = ''
    s = s
    file_list = file_list
    drive = drive
    retry_order = retry_order
    time.sleep(2)
    ord_plc = True
    val_pending = 0
    order_place_fail = 0
    order_history_fail = 0
    order_datafetch_fail = 0
    loop_rejected = 0
    loop1 = 0
    loop2 = 0
    loop3 = 0
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    # strategy = strategy
    instru = instru
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    fresh_position= fresh_position
    buy_sell = buy_sell
    modification_error = 0
    cancellation_error = 0
    rejection_error = 0
    multiple_sqr_off_error = 0
    order_pending_error = 0
    multi_sqr_off_error = 0
    executed = 0
    all_api_failed = 0
    contract = contract
    sqr_off_order = sqr_off_order
    ord_hist = ''
    order_trade_data = ''
    modify_counter = 0
    loop_time1 = 0
    loop_time2 = 0
    loop_time3 = 0
    leg1_sqr_off_error = 0
    leg1_fail_leg2_not_placed = 0
    expiry = expiry
    folder = '1vjTc2vhRc9gmlPRQ5D6IHaL9gt07yHtf'
    modify_counter = 0
    cancel_loop = 0
    modify_loop = 0
    status = status
    reject_count = reject_count
    cancel_count = cancel_count
    COLUMN_NAMES=['current_signal','entry_time','exit_time','leg','instru','order_id','qty','price_when_order_placed','fresh_position','buy_sell','instrument_id','trading_symbol','modification_error','cancellation_error','rejection_error','multiple_sqr_off_error','order_pending_error','multi_sqr_off_error','executed','all_api_failed','leg1_sqr_off_error','leg1_fail_leg2_not_placed','entry_price','strike','contract','status','exit_price','expiry','trade_id','sqr_off_order','reject_count','cancel_count','sqr_order_id']
    df64=pd.DataFrame(columns=COLUMN_NAMES) 
    buy_sell = buy_sell
    if status == "pending" or status == "modified":
        kt_order_id_1 = kt_order_id_1
        val_pending = 1
    else:
        val_pending = 0
    while ord_plc:
        print("entering while loop",datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if not kt_order_id_1 or not val_pending or status == "cancelled" or status == "rejected":
            # try:
            #     # a = 'NFO:'+ str(symbol_opt_1)
            #     # instruments = [a]
            #     # price = float(kite.ltp(instruments,s)) + 1
            #     price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
            #     price = price_df['close'].iloc[-1] + 1
            #     print("current price ",price," ", fromm,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            # except Exception as e:
            #     order_place_fail = 1
            #     print("Failed to get LTP",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            #     price = price_opt_1 + 2
            # if False:
            # #if abs(((price - price_opt_1) / price_opt_1) * 100) > 25:
            #     ord_plc = False 
            #     print("price has crossed 25% band ",price," ",price_opt_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            #     status = ""
            #     OMT_log = []
            #     kk = 0
            #     nn = 0
            #     OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
            #     file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
            #     for index, file in enumerate(file_list):
            #         if(file['title'] =="order_manage.txt"):
            #             nn = file['id']
            #             df29 = file.GetContentFile(file['title'])
            #             df64 = pd.read_csv("order_manage.txt")
            #     if bool(nn):
            #         df07 = pd.DataFrame.from_dict(OMT_log)
            #         df08 = pd.concat([df64,df07])                            
            #         df08.to_csv("order_manage.txt", index=False)
            #         update_file = drive.CreateFile({'id': nn})
            #         update_file.SetContentFile("order_manage.txt")
            #         update_file.Upload()
            #     else:
            #         df08 = pd.DataFrame.from_dict(OMT_log)
            #         df08.to_csv("order_manage.txt", index=False)
            #         gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
            #         gfile.SetContentFile("order_manage.txt")
            #         gfile.Upload()
            #     break
            try:
                margins_data = s.margins()
                avl_margin_before_trade = 0
                # for i in margins_data:
                    # print(i)
                avl_margin_before_trade = margins_data['equity']['available']['live_balance']
                print("current margin ",avl_margin_before_trade,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                avl_margin_before_trade = 0
                print("Failed to get margin",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            try:
                position_data =''
                position_data = s.positions()
                position_datafetch_initial = 0
                for i in position_data['day']:
                    if i['instrument_token'] == opt_id_1:
                        position_datafetch_initial = i['quantity']
                        position_datafetch_initial_check = 1
                print("current position check done ",datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                position_datafetch_initial_check = 0
                print("Failed to get position_data",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            try:
                print("order being placed at price ",price," ", fromm,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                kt_order_id_1 = s.place_order(variety=KiteApp.VARIETY_REGULAR,exchange=KiteApp.EXCHANGE_NFO,tradingsymbol=symbol_opt_1,transaction_type=buy_sell,quantity=quantity,product=KiteApp.PRODUCT_NRML,order_type=KiteApp.ORDER_TYPE_LIMIT,price=price)
    #             kt_order_id_1 = kite.place_order(kite.VARIETY_REGULAR,kite.EXCHANGE_NFO,symbol_opt_1,kite.TRANSACTION_TYPE_+signal,15,kite.PRODUCT_NRML,kite.ORDER_TYPE_LIMIT,price=price)
                order_place_fail = 0
                print("placed order",kt_order_id_1," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                 print("entering sell position"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                order_place_fail = 1
                print("Failed to place order",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if kt_order_id_1:
            time.sleep(3)
            try:
                ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
                print("printing order history",kt_order_id_1," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                order_history_fail = 0
                if ord_hist['status'] == 'COMPLETE':
                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    executed = 1
                    ord_plc = False
                    ord_plc_extra = True
                    # opt_id_1 = 100
                    if (fresh_position > 0) and (executed > 0):
                        status = "open"
                        OM_log = []
                        kk = 0
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        kt_order_id_1 = ''
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_complete.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_complete.txt")
                                print(df63)
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
#                             print(df07)
                            df08 = pd.concat([df63,df07])
                            print(df08)
                            df08.to_csv("order_complete.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_complete.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_complete.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                            gfile.SetContentFile("order_complete.txt")
                            gfile.Upload()
                        OM_log = []
                        print("order saved to file"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                     if (fresh_position > 0) and (executed > 0) and retry_order:
#                         status = "open"
#                         colname = ["entry_time", "entry_price","executed","status"]
# #                         OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order})
#                         file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
#                         for index, file in enumerate(file_list):
#                             if(file['title'] =="order_complete.txt"):
#                                 kk = file['id']
#                                 df29 = file.GetContentFile(file['title'])
#                                 df63 = pd.read_csv("order_complete.txt")
#                         if bool(kk):
#                             stats = kk
#                             df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,1,"open"]
#                             df63.to_csv("order_complete.txt", index=False)
#                             update_file = drive.CreateFile({'id': stats})
#                             update_file.SetContentFile("order_complete.txt")
#                             update_file.Upload()
                    if (fresh_position < 1) and (executed > 0):
                        status = "close"
                        colname = ["exit_time", "exit_price","status"]
#                         OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_complete.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_complete.txt")
                            if(file['title'] =="order_sqr_complete.txt"):
                                nn = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df64 = pd.read_csv("order_sqr_complete.txt")
                        if bool(kk):
                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                            df63.to_csv("order_complete.txt", index=False)
                            df64.to_csv("order_sqr_complete.txt", index=False)
                            update_file = drive.CreateFile({'id': kk})
                            update_file.SetContentFile("order_complete.txt")
                            update_file.Upload()
                            update_file = drive.CreateFile({'id': nn})
                            update_file.SetContentFile("order_sqr_complete.txt")
                            update_file.Upload()
                        print("order saved to file"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            #send a signal to check the status while algo is running
                elif ord_hist['status'] == 'REJECTED':
                    # loop_rejected = loop_rejected + 1
                    print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    reject_count = reject_count + 1
                    if not retry_order and fresh_position > 0:
                        status = "rejected"
                        rejection_error = 1
                        OM_log = []
                        OMT_log = []
                        kk = 0
                        nn = 0
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_reject.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_reject.txt")
                            if(file['title'] =="order_manage.txt"):
                                nn = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df64 = pd.read_csv("order_manage.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_reject.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_reject.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_reject.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                            gfile.SetContentFile("order_reject.txt")
                            gfile.Upload()
                        if bool(nn):
                            df07 = pd.DataFrame.from_dict(OMT_log)
                            df08 = pd.concat([df64,df07])                            
                            df08.to_csv("order_manage.txt", index=False)
                            update_file = drive.CreateFile({'id': nn})
                            update_file.SetContentFile("order_manage.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OMT_log)
                            df08.to_csv("order_manage.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                            gfile.SetContentFile("order_manage.txt")
                            gfile.Upload()
                    if (not retry_order and fresh_position < 1) or retry_order:
                        rejection_error = 1
                        status = "rejected"
                        colname = ["rejection_error","reject_count"]
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
#                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_reject.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_reject.txt")
                            if(file['title'] =="order_manage.txt"):
                                nn = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df64 = pd.read_csv("order_manage.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_reject.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_reject.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_reject.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                            gfile.SetContentFile("order_reject.txt")
                            gfile.Upload()
                        if bool(nn):
                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                            df64.to_csv("order_manage.txt", index=False)
                            update_file = drive.CreateFile({'id': nn})
                            update_file.SetContentFile("order_manage.txt")
                            update_file.Upload()
                        else:
                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                            df64.to_csv("order_manage.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                            gfile.SetContentFile("order_manage.txt")
                            gfile.Upload()

#                     if retry_order:
#                         rejection_error = 1
#                         status = "rejected"
#                         colname = ["entry_time", "entry_price","rejection_error","status"]
#                         file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
#                         for index, file in enumerate(file_list):
#                             if(file['title'] =="order_manage.txt"):
#                                 kk = file['id']
#                                 df29 = file.GetContentFile(file['title'])
#                                 df63 = pd.read_csv("order_manage.txt")
#                         if bool(kk):
#                             stats = kk
#                             df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,1,"rejected"]
#                             df63.to_csv("order_manage.txt", index=False)
#                             update_file = drive.CreateFile({'id': stats})
#                             update_file.SetContentFile("order_manage.txt")
#                             update_file.Upload()

                    OM_log = []
                    OMT_log = []
                    rejection_error = 0
                    kt_order_id_1 = ''
                    # if (loop_rejected < 3):
                    #     time.sleep(10)
                    # else:
                    #     time.sleep(300*(loop_rejected - 2))
                elif ord_hist['status'] == 'CANCELLED':
                    print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
#                     time.sleep(10)
#                     kt_order_id_1 = ''
#                     loop_rejected = loop_rejected + 1
#                     ord_plc = True
                    cancel_count = cancel_count + 1
#                     kt_order_id_1 = ''
                    if not retry_order and fresh_position > 0:
                        status = "cancelled"
                        cancellation_error = 1
                        OM_log = []
                        OMT_log = []
                        kk = 0
                        nn = 0
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_cancel.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_cancel.txt")
                            if(file['title'] =="order_manage.txt"):
                                nn = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df64 = pd.read_csv("order_manage.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_cancel.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_cancel.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_cancel.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                            gfile.SetContentFile("order_cancel.txt")
                            gfile.Upload()
                        if bool(nn):
                            df07 = pd.DataFrame.from_dict(OMT_log)
                            df08 = pd.concat([df64,df07])                            
                            df08.to_csv("order_manage.txt", index=False)
                            update_file = drive.CreateFile({'id': nn})
                            update_file.SetContentFile("order_manage.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OMT_log)
                            df08.to_csv("order_manage.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                            gfile.SetContentFile("order_manage.txt")
                            gfile.Upload()
                    if (not retry_order and fresh_position < 1) or retry_order:
                        cancellation_error = 1
                        status = "cancelled"
                        colname = ["cancellation_error","cancel_count"]
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
#                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_cancel.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_cancel.txt")
                            if(file['title'] =="order_manage.txt"):
                                nn = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df64 = pd.read_csv("order_manage.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_cancel.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_cancel.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_cancel.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                            gfile.SetContentFile("order_cancel.txt")
                            gfile.Upload()
                        if bool(nn):
                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                            df64.to_csv("order_manage.txt", index=False)
                            update_file = drive.CreateFile({'id': nn})
                            update_file.SetContentFile("order_manage.txt")
                            update_file.Upload()
                        else:
                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                            df64.to_csv("order_manage.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                            gfile.SetContentFile("order_manage.txt")
                            gfile.Upload()

                    OM_log = []
                    OMT_log = []
                    cancellation_error = 0
                    kt_order_id_1 = ''
                else:
                    loop1 = loop1 + 1
                    print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    print("looping",loop1)
                    if (loop1 < 6):
                        loop_time1 = loop_time1 + 5
                        time.sleep(loop_time1)
                    elif (loop1<15) and (loop1>=6):
                        loop_time1 = loop_time1 + 5
                        time.sleep(loop_time1)
                    elif (loop1>=15) and (loop1<26):
                        loop_time1 = loop_time1 + 5
                        time.sleep(loop_time1)
                    val_pending = 1
                    status = "pending"
                    if (fresh_position > 0) and (executed < 1) and not retry_order:
    #                     status = ""
                        ord_plc = False
                        OM_log = []
                        kk = ''
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        kt_order_id_1 = ''
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_pending.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_pending.txt")
                                print(df63)
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            print(df07)
                            df08 = pd.concat([df63,df07])
                            print(df08)
                            df08.to_csv("order_pending.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_pending.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_pending.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                            gfile.SetContentFile("order_pending.txt")
                            gfile.Upload()
                        OM_log = []

#                     modify_counter = modify_counter + 1
#                     if ord_hist['exchange_timestamp'] and (modify_counter > 5) and (modify_counter < 20):
#                         order_modify = True
#                         modify_val_pending = 0
#                         modify_order_id = 0
#                         try:
#                             # price = kite.ltp(symbol_opt_1) + 1
#                             a = 'NFO:'+ str(symbol_opt_1)
#                             instruments = [a]
#                             price = float(kite.ltp(instruments,s)) + 1
#                         except Exception as e:
#     #                         order_place_fail = 1
#                             price = 0
#                             print("Failed to get LTP for modifying the order", e)
#                         while order_modify and price and not (abs(((price - price_opt_1) / price_opt_1) * 100) > 25):
#                             try:
#                                 if not modify_order_id or not modify_val_pending:
#                                     price = price + 1
#                                     modify_order_id = kite.modify_order(s,kite.VARIETY_REGULAR, kt_order_id_1, quantity,590) 
#                                     if modify_order_id:
#                                         kt_order_id_1 = modify_order_id
#                                     time.sleep(3)
#                                 try:
#                                     modify_ord_hist = ''
#                                     modify_ord_hist = kite.order_history(s,order_id=kt_order_id_1)[0]
# #                                     order_history_fail = 0
#                                     if modify_ord_hist['status'] == 'MODIFIED':
#                                         order_modify = False
#                                         status = "modified"
#                                         modification_error = 0
#                                     else:
#                                         modify_val_pending = 1
#                                         modify_loop = modify_loop + 1
#                                         if (modify_loop < 6):
#                                             time.sleep(10)
#                                         else:
#                                             order_modify = False
#                                             modification_error = 1
#                                             #send a signal to check the status while algo is running
#                                 except Exception as e:
#         #                             order_place_fail = 1
#                                     print("Failed to get order history details for modified order",e)
#                                     modify_loop = modify_loop + 1
#                                     if (modify_loop < 6):
#                                         time.sleep(10)
#                                     else:
#                                         order_modify = False
#                                         modification_error = 1
#                             except Exception as e:
#                                 order_modify = False
#                                 modification_error = 1
#                                 print("Failed to modify order",e)
#                     elif ord_hist['exchange_timestamp'] and (modify_counter >= 20 or not (abs(((price - price_opt_1) / price_opt_1) * 100) > 25)):
#                         order_cancel = True
#                         cancel_val_pending = 0
#                         cancel_order_id= 0
#                         while order_cancel:
#                             try:
#                                 if not cancel_order_id or not cancel_val_pending:
#                                     cancel_order_id = kite.cancel_order(kite.VARIETY_REGULAR, kt_order_id_1) 
#                                 if cancel_order_id:
#                                     kt_order_id_1 = cancel_order_id
#                                     time.sleep(3)
#                                     try:
#                                         cancel_ord_hist = ''
#                                         cancel_ord_hist = kite.order_history(cancel_order_id)
#     #                                     order_history_fail = 0
#                                         if cancel_ord_hist['status'] == 'CANCELLED':
#                                             order_cancel = False
#                                             status = "cancelled"
#                                             cancellation_error = 0
#                                         else:
#                                             cancel_val_pending = 1
#                                             cancel_loop = cancel_loop + 1
#                                             if (cancel_loop < 6):
#                                                 time.sleep(10)
#                                             else:
#                                                 order_cancel = False
#                                                 cancellation_error = 1
#                                                 #send a signal to check the status while algo is running
#                                     except Exception as e:
#             #                             order_place_fail = 1
#                                         print("Failed to get order history details for cancelled order"+e)
#                                         cancel_loop = cancel_loop + 1
#                                         if (cancel_loop < 6):
#                                             time.sleep(10)
#                                         else:
#                                             order_cancel = False
#                                             cancellation_error = 1
#                                 else:
#                                     time.sleep(3)
#                                     try:
#                                         cancel_ord_hist = ''
#                                         cancel_ord_hist = kite.order_history(kt_order_id_1)
#     #                                     order_history_fail = 0
#                                         if cancel_ord_hist['status'] == 'CANCELLED':
#                                             order_cancel = False
#                                             cancellation_error = 0
#                                         else:
#                                             cancel_val_pending = 1
#                                             cancel_loop = cancel_loop + 1
#                                             if (cancel_loop < 6):
#                                                 time.sleep(10)
#                                             else:
#                                                 order_cancel = False
#                                                 cancellation_error = 1
#                                                 #send a signal to check the status while algo is running
#                                     except Exception as e:
#             #                             order_place_fail = 1
#                                         print("Failed to get order history details for cancelled order"+e)
#                                         cancel_loop = cancel_loop + 1
#                                         if (cancel_loop < 6):
#                                             time.sleep(10)
#                                         else:
#                                             order_cancel = False
#                                             cancellation_error = 1
#                             except Exception as e:
#                                 order_cancel = False
#                                 cancellation_error = 1
#                                 print("Failed to cancel the order")
                print("inside order history check after order id generation"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                 print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                # if (fresh_position > 0) and (executed < 1) and (loop1 >= 26) and not retry_order:

            except Exception as e:
                order_history_fail = 1
                print("Failed to fetch order history data",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            if not ord_hist or order_history_fail:
                try:
                    print("check trades"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    order_trade_data = ''
                    order_trade_data = s.order_trades(kt_order_id_1)
                    order_trade_datafetch_fail = 0
                    for i in order_trade_data:
                        if i['order_id'] == kt_order_id_1:
                            print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            executed = 1
                            ord_plc = False
                            ord_plc_extra = True
                            # opt_id_1 = 100
                            if (fresh_position > 0) and (executed > 0):
                                status = "open"
                                OM_log = []
                                kk = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                        print(df63)
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
        #                             print(df07)
                                    df08 = pd.concat([df63,df07])
                                    print(df08)
                                    df08.to_csv("order_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                    gfile.SetContentFile("order_complete.txt")
                                    gfile.Upload()
                                OM_log = []
                            if (fresh_position < 1) and (executed > 0):
                                status = "close"
                                colname = ["exit_time", "exit_price","status"]
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                    if(file['title'] =="order_sqr_complete.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_sqr_complete.txt")

                                if bool(kk):
                                    df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                    df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                    df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                    df63.to_csv("order_complete.txt", index=False)
                                    df64.to_csv("order_sqr_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_sqr_complete.txt")
                                    update_file.Upload()

                except Exception as e:
                    order_trade_datafetch_fail = 1
                    print("Failed to fetch trade data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not order_trade_data or order_trade_datafetch_fail:            
                    try:
                        print("checking orders"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_data = ''
                        ord_data = s.orders()
                        order_datafetch_fail = 0
                        for i in ord_data:
                            if i['order_id'] == kt_order_id_1 and i['transaction_type'] == buy_sell:
                                if i['status'] == 'COMPLETE':
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    executed = 1
                                    ord_plc = False
                                    ord_plc_extra = True
                                    # opt_id_1 = 100
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                #                             print(df07)
                                            df08 = pd.concat([df63,df07])
                                            print(df08)
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        colname = ["exit_time", "exit_price","status"]
                #                         OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")

                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                                elif i['status'] == 'REJECTED':
                                    print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    reject_count = reject_count + 1
                                    if not retry_order and fresh_position > 0:
                                        status = "rejected"
                                        rejection_error = 1
                                        OM_log = []
                                        OMT_log = []
                                        kk = 0
                                        nn = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_reject.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_reject.txt")
                                            if(file['title'] =="order_manage.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_manage.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_reject.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_reject.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_reject.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                            gfile.SetContentFile("order_reject.txt")
                                            gfile.Upload()
                                        if bool(nn):
                                            df07 = pd.DataFrame.from_dict(OMT_log)
                                            df08 = pd.concat([df64,df07])                            
                                            df08.to_csv("order_manage.txt", index=False)
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_manage.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OMT_log)
                                            df08.to_csv("order_manage.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                            gfile.SetContentFile("order_manage.txt")
                                            gfile.Upload()
                                    if (not retry_order and fresh_position < 1) or retry_order:
                                        rejection_error = 1
                                        status = "rejected"
                                        colname = ["rejection_error","reject_count"]
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_reject.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_reject.txt")
                                            if(file['title'] =="order_manage.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_manage.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_reject.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_reject.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_reject.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                            gfile.SetContentFile("order_reject.txt")
                                            gfile.Upload()
                                        if bool(nn):
                                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                            df64.to_csv("order_manage.txt", index=False)
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_manage.txt")
                                            update_file.Upload()
                                        else:
                                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                            df64.to_csv("order_manage.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                            gfile.SetContentFile("order_manage.txt")
                                            gfile.Upload()

                                    OM_log = []
                                    OMT_log = []
                                    rejection_error = 0
                                    kt_order_id_1 = ''
                                elif i['status'] == 'CANCELLED':
                                    print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    cancel_count = cancel_count + 1
                                    if not retry_order and fresh_position > 0:
                                        status = "cancelled"
                                        cancellation_error = 1
                                        OM_log = []
                                        OMT_log = []
                                        kk = 0
                                        nn = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_cancel.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_cancel.txt")
                                            if(file['title'] =="order_manage.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_manage.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_cancel.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_cancel.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_cancel.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                            gfile.SetContentFile("order_cancel.txt")
                                            gfile.Upload()
                                        if bool(nn):
                                            df07 = pd.DataFrame.from_dict(OMT_log)
                                            df08 = pd.concat([df64,df07])                            
                                            df08.to_csv("order_manage.txt", index=False)
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_manage.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OMT_log)
                                            df08.to_csv("order_manage.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                            gfile.SetContentFile("order_manage.txt")
                                            gfile.Upload()
                                    if (not retry_order and fresh_position < 1) or retry_order:
                                        cancellation_error = 1
                                        status = "cancelled"
                                        colname = ["cancellation_error","cancel_count"]
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_cancel.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_cancel.txt")
                                            if(file['title'] =="order_manage.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_manage.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_cancel.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_cancel.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_cancel.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                            gfile.SetContentFile("order_cancel.txt")
                                            gfile.Upload()
                                        if bool(nn):
                                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                            df64.to_csv("order_manage.txt", index=False)
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_manage.txt")
                                            update_file.Upload()
                                        else:
                                            df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                            df64.to_csv("order_manage.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                            gfile.SetContentFile("order_manage.txt")
                                            gfile.Upload()

                                    OM_log = []
                                    OMT_log = []
                                    cancellation_error = 0
                                    kt_order_id_1 = ''

                                else:
                                    print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    loop1 = loop1 + 1
                                    print("looping",loop1)
                                    if (loop1 < 6):
                                        loop_time1 = loop_time1 + 5
                                        time.sleep(loop_time1)
                                    elif (loop1<15) and (loop1>=6):
                                        loop_time1 = loop_time1 + 5
                                        time.sleep(loop_time1)
                                    elif (loop1>=15) and (loop1<26):
                                        loop_time1 = loop_time1 + 5
                                        time.sleep(loop_time1)
                                    val_pending = 1
                                    status = "pending"
                                    if (fresh_position > 0) and (executed < 1) and not retry_order:
                    #                     status = ""
                                        ord_plc = False
                                        OM_log = []
                                        kk = ''
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_pending.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_pending.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            print(df07)
                                            df08 = pd.concat([df63,df07])
                                            print(df08)
                                            df08.to_csv("order_pending.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_pending.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_pending.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                                            gfile.SetContentFile("order_pending.txt")
                                            gfile.Upload()
                                        OM_log = []
                    except Exception as e:
                        order_datafetch_fail = 1
                        print("Failed to fetch order data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                         print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    if not ord_data or order_datafetch_fail:
                        try:
                            print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            if position_datafetch_initial_check  < 1:
                                all_api_failed = 1
                                status = ""
                                OMT_log = []
                                kk = 0
                                nn = 0
                                OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_manage.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_manage.txt")
                                if bool(nn):
                                    df07 = pd.DataFrame.from_dict(OMT_log)
                                    df08 = pd.concat([df64,df07])                            
                                    df08.to_csv("order_manage.txt", index=False)
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_manage.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OMT_log)
                                    df08.to_csv("order_manage.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                    gfile.SetContentFile("order_manage.txt")
                                    gfile.Upload()
                                break
                            position_data =''
                            position_data = s.positions()
                            position_datafetch_fail = 0
                            for i in position_data['day']:
                                if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                                    executed = 1
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    ord_plc_extra = True
                                    # opt_id_1 = 100
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                #                             print(df07)
                                            df08 = pd.concat([df63,df07])
                                            print(df08)
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        colname = ["exit_time", "exit_price","status"]
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")

                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                        except Exception as e:
                            position_datafetch_fail = 1
                            print("Failed to fetch position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                             print("Failed to fetch order data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if not position_data or position_datafetch_fail:
                            try:
                                print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if avl_margin_before_trade  < 1:
                                    all_api_failed = 1
                                    status = ""
                                    OMT_log = []
                                    kk = 0
                                    nn = 0
                                    OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_manage.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_manage.txt")
                                    if bool(nn):
                                        df07 = pd.DataFrame.from_dict(OMT_log)
                                        df08 = pd.concat([df64,df07])                            
                                        df08.to_csv("order_manage.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_manage.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OMT_log)
                                        df08.to_csv("order_manage.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                        gfile.SetContentFile("order_manage.txt")
                                        gfile.Upload()
                                    break
                                margins_data = s.margins()
                                margins_datafetch_fail = 0
                                # for i in margins_data:
                                if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                                    executed = 1
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    ord_plc_extra = True
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        colname = ["exit_time", "exit_price","status"]
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")
                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                            except Exception as e:
                                margins_datafetch_fail = 1
                                all_api_failed = 1
                                print("Failed to fetch margin data all api falied"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if (fresh_position > 0) and (executed < 1) and not retry_order:
                                    ord_plc = False
                                    OM_log = []
                                    kk = ''
                                    OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    kt_order_id_1 = ''
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_pending.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_pending.txt")
                                            print(df63)
                                    if bool(kk):
                                        stats = kk
                                        df07 = pd.DataFrame.from_dict(OM_log)
                                        print(df07)
                                        df08 = pd.concat([df63,df07])
                                        print(df08)
                                        df08.to_csv("order_pending.txt", index=False)
                                        update_file = drive.CreateFile({'id': stats})
                                        update_file.SetContentFile("order_pending.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OM_log)
                                        df08.to_csv("order_pending.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                                        gfile.SetContentFile("order_pending.txt")
                                        gfile.Upload()
                                    OM_log = []
#                                 print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        elif not kt_order_id_1 or order_place_fail:
            try:
                print("Failed to order id or order place fail so check orders"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                ord_data = ''
                ord_data = s.orders()
                order_datafetch_fail = 0
                order_datafetch_found = 0
                for i in ord_data:
                    if i['instrument_token'] == opt_id_1 and i['transaction_type'] == buy_sell:
                        order_datafetch_found = 1
                        if i['status'] == 'COMPLETE':
                            print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            executed = 1
                            if (fresh_position > 0) and (executed > 0):
                                status = "open"
                                OM_log = []
                                kk = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                    gfile.SetContentFile("order_complete.txt")
                                    gfile.Upload()
                                OM_log = []
                            if (fresh_position < 1) and (executed > 0):
                                status = "open"
                                OM_log = []
                                kk = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                    gfile.SetContentFile("order_complete.txt")
                                    gfile.Upload()
                                OM_log = []
                        elif i['status'] == 'REJECTED':
                            print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            reject_count = reject_count + 1
                            if not retry_order and fresh_position > 0:
                                status = "rejected"
                                rejection_error = 1
                                OM_log = []
                                OMT_log = []
                                kk = 0
                                nn = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_reject.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_reject.txt")
                                    if(file['title'] =="order_manage.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_manage.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_reject.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_reject.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_reject.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                    gfile.SetContentFile("order_reject.txt")
                                    gfile.Upload()
                                if bool(nn):
                                    df07 = pd.DataFrame.from_dict(OMT_log)
                                    df08 = pd.concat([df64,df07])                            
                                    df08.to_csv("order_manage.txt", index=False)
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_manage.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OMT_log)
                                    df08.to_csv("order_manage.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                    gfile.SetContentFile("order_manage.txt")
                                    gfile.Upload()
                                if (not retry_order and fresh_position < 1) or retry_order:
                                    rejection_error = 1
                                    status = "rejected"
                                    colname = ["rejection_error","reject_count"]
                                    OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_reject.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_reject.txt")
                                        if(file['title'] =="order_manage.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_manage.txt")
                                    if bool(kk):
                                        df07 = pd.DataFrame.from_dict(OM_log)
                                        df08 = pd.concat([df63,df07])
                                        df08.to_csv("order_reject.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_reject.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OM_log)
                                        df08.to_csv("order_reject.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                        gfile.SetContentFile("order_reject.txt")
                                        gfile.Upload()
                                    if bool(nn):
                                        df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                        df64.to_csv("order_manage.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_manage.txt")
                                        update_file.Upload()
                                    else:
                                        df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                        df64.to_csv("order_manage.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                        gfile.SetContentFile("order_manage.txt")
                                        gfile.Upload()
                                    OM_log = []
                                    OMT_log = []
                                    rejection_error = 0
                                    kt_order_id_1 = ''
                        elif i['status'] == 'CANCELLED':
                            print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            cancel_count = cancel_count + 1
                            if not retry_order and fresh_position > 0:
                                status = "cancelled"
                                cancellation_error = 1
                                OM_log = []
                                OMT_log = []
                                kk = 0
                                nn = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_cancel.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_cancel.txt")
                                    if(file['title'] =="order_manage.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_manage.txt")
                                if bool(kk):
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_cancel.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_cancel.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_cancel.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                    gfile.SetContentFile("order_cancel.txt")
                                    gfile.Upload()
                                if bool(nn):
                                    df07 = pd.DataFrame.from_dict(OMT_log)
                                    df08 = pd.concat([df64,df07])                            
                                    df08.to_csv("order_manage.txt", index=False)
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_manage.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OMT_log)
                                    df08.to_csv("order_manage.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                    gfile.SetContentFile("order_manage.txt")
                                    gfile.Upload()
                            if (not retry_order and fresh_position < 1) or retry_order:
                                cancellation_error = 1
                                status = "cancelled"
                                colname = ["cancellation_error","cancel_count"]
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_cancel.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_cancel.txt")
                                    if(file['title'] =="order_manage.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_manage.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_cancel.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_cancel.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_cancel.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                    gfile.SetContentFile("order_cancel.txt")
                                    gfile.Upload()
                                if bool(nn):
                                    df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                    df64.to_csv("order_manage.txt", index=False)
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_manage.txt")
                                    update_file.Upload()
                                else:
                                    df64.loc[(df64.leg==leg), colname] = [rejection_error,reject_count]
                                    df64.to_csv("order_manage.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                    gfile.SetContentFile("order_manage.txt")
                                    gfile.Upload()

                            OM_log = []
                            OMT_log = []
                            cancellation_error = 0
                            kt_order_id_1 = ''
                        else:
                            print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            loop1 = loop1 + 1
                            print("looping",loop1)
                            if (loop1 < 6):
                                loop_time1 = loop_time1 + 5
                                time.sleep(loop_time1)
                            elif (loop1<15) and (loop1>=6):
                                loop_time1 = loop_time1 + 5
                                time.sleep(loop_time1)
                            elif (loop1>=15) and (loop1<26):
                                loop_time1 = loop_time1 + 5
                                time.sleep(loop_time1)
                            val_pending = 1
                            status = "pending"
                            if (fresh_position > 0) and (executed < 1) and not retry_order:
                    #                     status = ""
                                ord_plc = False
                                OM_log = []
                                kk = ''
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_pending.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_pending.txt")
                                        print(df63)
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    print(df07)
                                    df08 = pd.concat([df63,df07])
                                    print(df08)
                                    df08.to_csv("order_pending.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_pending.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_pending.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                                    gfile.SetContentFile("order_pending.txt")
                                    gfile.Upload()
                                OM_log = []
                if not order_datafetch_found:
                    raise Exception("order not found in ord_data")
                    # raise TypeError
            except Exception as e:
                order_datafetch_fail = 1
                print("Failed to fetch order data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                 print("Failed to fetch margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not ord_data or order_datafetch_fail or not order_datafetch_found:
                    try:
                        print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if position_datafetch_initial_check  < 1:
                            all_api_failed = 1
                            status = ""
                            OMT_log = []
                            kk = 0
                            nn = 0
                            OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_manage.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_manage.txt")
                            if bool(nn):
                                df07 = pd.DataFrame.from_dict(OMT_log)
                                df08 = pd.concat([df64,df07])                            
                                df08.to_csv("order_manage.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_manage.txt")
                                update_file.Upload()
                            else:
                                df08 = pd.DataFrame.from_dict(OMT_log)
                                df08.to_csv("order_manage.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                gfile.SetContentFile("order_manage.txt")
                                gfile.Upload()
                            break
                        position_data =''
                        position_data = s.positions()
                        position_datafetch_fail = 0
                        position_datafetch_found = 0
                        for i in position_data['day']:
                            if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                                position_datafetch_found = 1
                                executed = 1
                                print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                ord_plc = False
                                # opt_id_1 = 100
                                if (fresh_position > 0) and (executed > 0):
                                    status = "open"
                                    OM_log = []
                                    kk = 0
                                    OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    kt_order_id_1 = ''
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_complete.txt")
                                            print(df63)
                                    if bool(kk):
                                        stats = kk
                                        df07 = pd.DataFrame.from_dict(OM_log)
                                        df08 = pd.concat([df63,df07])
                                        df08.to_csv("order_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': stats})
                                        update_file.SetContentFile("order_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OM_log)
                                        df08.to_csv("order_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                        gfile.SetContentFile("order_complete.txt")
                                        gfile.Upload()
                                OM_log = []
                            if (fresh_position < 1) and (executed > 0):
                                status = "close"
                                colname = ["exit_time", "exit_price","status"]
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                    if(file['title'] =="order_sqr_complete.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_sqr_complete.txt")
                                if bool(kk):
                                    df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                    df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                    df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                    df63.to_csv("order_complete.txt", index=False)
                                    df64.to_csv("order_sqr_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_sqr_complete.txt")
                                    update_file.Upload()
                        if not position_datafetch_found:
                            raise Exception("order not found in ord_data")
                    except Exception as e:
                        position_datafetch_fail = 1
                        print("Failed to fetch position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if not position_data or position_datafetch_fail or not position_datafetch_found:
                            try:
                                print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if avl_margin_before_trade  < 1:
                                    all_api_failed = 1
                                    status = ""
                                    OMT_log = []
                                    kk = 0
                                    nn = 0
                                    OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_manage.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_manage.txt")
                                    if bool(nn):
                                        df07 = pd.DataFrame.from_dict(OMT_log)
                                        df08 = pd.concat([df64,df07])                            
                                        df08.to_csv("order_manage.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_manage.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OMT_log)
                                        df08.to_csv("order_manage.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                        gfile.SetContentFile("order_manage.txt")
                                        gfile.Upload()
                                    break
                                margins_data = s.margins()
                                margins_datafetch_fail = 0
                                margins_datafetch_found = 0
                                # for i in margins_data:
                                if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                                    executed = 1
                                    margins_datafetch_found = 1
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    ord_plc_extra = True
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                            #                             print(df07)
                                            df08 = pd.concat([df63,df07])
                                            print(df08)
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        kk = 0
                                        nn = 0
                                        colname = ["exit_time", "exit_price","status"]
                            #                         OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")

                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                                if not margins_datafetch_found:
                                    raise Exception("order not found in ord_data")
                            except Exception as e:
                                margins_datafetch_fail = 1
                                all_api_failed = 1
                                print("Failed to fetch margin data ",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if not retry_order and fresh_position > 0:
                                    status = ""
                                    cancellation_error = 1
                                    OM_log = []
                                    OMT_log = []
                                    kk = 0
                                    nn = 0
                                    OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_manage.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_manage.txt")
                                    if bool(nn):
                                        df07 = pd.DataFrame.from_dict(OMT_log)
                                        df08 = pd.concat([df64,df07])                            
                                        df08.to_csv("order_manage.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_manage.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OMT_log)
                                        df08.to_csv("order_manage.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_manage.txt"})
                                        gfile.SetContentFile("order_manage.txt")
                                        gfile.Upload()
                                break
    return executed

def order_modify(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,kt_order_id_1):
    ord_plc = True
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    instru = instru
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    buy_sell = buy_sell
    contract = contract
    status = status
    kt_order_id_1 = kt_order_id_1
    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    while ord_plc:
        print("modify order"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        try:
            a = 'NFO:'+ str(symbol_opt_1)
            instruments = [a]
            # price = float(kite.ltp(instruments,s)) + 1
            price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
            price = price_df['close'].iloc[-1] + 1
        except Exception as e:
            order_place_fail = 1
            print("Failed to get LTP"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            print(str(e), file=sys.stderr)
            price = price_opt_1 + 2
        if abs(((price - price_opt_1) / price_opt_1) * 100) > 25:
            print("price moved beyond 25% so break"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            ord_plc = False 
            break
        try:
            price = price + 1
            modify_order_id = s.modify_order(KiteApp.VARIETY_REGULAR, kt_order_id_1, quantity,price=price) 
            if modify_order_id:
                print("order modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                kt_order_id_1 = modify_order_id
            time.sleep(3)
            try:
                modify_ord_hist = ''
                modify_ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
                if modify_ord_hist['status'] == 'MODIFIED':
                    print("order modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    status = "modified"
                    modification_error = 0
                    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                else:
                    print("order not modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    modify_val_pending = 1
                    modification_error = 1
                    ord_plc = False 
                    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

                        #send a signal to check the status while algo is running
            except Exception as e:
    #                             order_place_fail = 1
                print("Failed to get order history details for modified order"+e, file=sys.stderr)
                modification_error = 1
                ord_plc = False 
                modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

        except Exception as e:
            ord_plc = False
            modification_error = 1
            print("Failed to modify order",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return status,price,modify_time

def order_modify_multiple(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,kt_order_id_1):
    ord_plc = True
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    fresh_position= fresh_position
    buy_sell = buy_sell
    contract = contract
    sqr_off_order = sqr_off_order
    status = status
    kt_order_id_1 = kt_order_id_1
    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    while ord_plc:
        print("modify order multiple"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        try:
            a = 'NFO:'+ str(symbol_opt_1)
            instruments = [a]
            # price = float(kite.ltp(instruments,s)) + 1
            price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
            price = price_df['close'].iloc[-1] + 1
        except Exception as e:
            order_place_fail = 1
            print("Failed to get LTP"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            print(str(e), file=sys.stderr)
            price = price_opt_1 + 2
        if abs(((price - price_opt_1) / price_opt_1) * 100) > 25:
            print("price moved beyond 25% so break"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            ord_plc = False 
            break
        try:
            price = price + 1
            modify_order_id = s.modify_order(KiteApp.VARIETY_REGULAR, kt_order_id_1, quantity,price=price) 
            if modify_order_id:
                print("order modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                kt_order_id_1 = modify_order_id
            time.sleep(3)
            try:
                modify_ord_hist = ''
                modify_ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
                if modify_ord_hist['status'] == 'MODIFIED':
                    ord_plc = False
                    print("order modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    status = "modified"
                    modification_error = 0
                    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                else:
                    print("order not modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    modify_val_pending = 1
                    modification_error = 1
                    ord_plc = False 
                    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            except Exception as e:
                print("Failed to get order history details for modified order",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                modification_error = 1
                ord_plc = False 
        except Exception as e:
            ord_plc = False
            modification_error = 1
            print("Failed to modify order multiple",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
    return status,price,modify_time

def check_order_history(s,kt_order_id_1,opt_id_1,fresh_position,status):
    try:
        print("check order history"," ",kt_order_id_1," ",opt_id_1," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        status = status
        ord_hist = ''
        ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
        # ord_hist1 = kite.order_history(s,order_id=kt_order_id_1)
        print(ord_hist," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        # print(ord_hist1," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        print("printing order history",kt_order_id_1,ord_hist['status']," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        order_history_fail = 0
        if ord_hist['status'] == 'COMPLETE':
            if fresh_position > 0:
                status = "open"
            if fresh_position < 1:
                status = "close"
        elif ord_hist['status'] == 'REJECTED':
            status = "rejected"
        elif ord_hist['status'] == 'CANCELLED':
            status = "cancelled"
        else:
            status ="pending"
    except Exception as e:
        order_history_fail = 1
        print("Failed to fetch order history data",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if not ord_hist or order_history_fail:
            try:
                order_trade_data = ''
                order_trade_data = s.order_trades(kt_order_id_1)
                order_trade_datafetch_fail = 0
                for i in order_trade_data:
                    if i['order_id'] == kt_order_id_1:
                        if fresh_position > 0:
                            status = "open"
                        if fresh_position < 1:
                            status = "close"
            except Exception as e:
                order_trade_datafetch_fail = 1
                print("Failed to fetch trade data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not order_trade_data or order_trade_datafetch_fail:            
                    try:
                        ord_data = ''
                        ord_data = s.orders()
                        order_datafetch_fail = 0
                        for i in ord_data:
                            if i['order_id'] == kt_order_id_1 :
                                if i['status'] == 'COMPLETE':
                                    if fresh_position > 0:
                                        status = "open"
                                    if fresh_position < 1:
                                        status = "close"
                            elif i['status'] == 'REJECTED':
                                status = "rejected"
                            elif i['status'] == 'CANCELLED':
                                status = "cancelled"
                            else:
                                status ="pending"
                    except Exception as e:
                        order_datafetch_fail = 1
                        print("Failed to fetch order data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
#                     if not ord_data or order_datafetch_fail:
#                         try:
#                             position_data = ''
#                             position_data = kite.positions(s)
#                             position_datafetch_fail = 0
#                             for i in position_data:
#                                 if i['day']['instrument_token'] == opt_id_1:
#                                     if fresh_position > 0:
#                                         status = "open"
#                                     if fresh_position < 1:
#                                         status = "close"
#                         except Exception as e:
#                             position_datafetch_fail = 1
#                             print("Failed to fetch position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        all_api_failed = 1
                        print("Failed to fetch margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)

    #                     if not position_data or position_datafetch_fail:
    #                         try:
    #                             margins_data = kite.margins()
    #                             margins_datafetch_fail = 0
    #                             for i in kite.margins():
    #                                 if i['equity']['available']['opening_balance'] == i['equity']['available']['live_balance']:
    #                                     if fresh position > 0:
    #                                         status = "open"
    #                                     if fresh position < 1:
    #                                         status = "close"
    #                 except Exception as e:
    #                     margins_datafetch_fail = 1
    return status

def order_cancel_place(s,kt_order_id_1,status):
    status = status
    print("trying to cancel the order"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
    cancel_the_order = s.cancel_order(KiteApp.VARIETY_REGULAR, kt_order_id_1) 
    if cancel_the_order:
        try:
            cancel_ord_hist = s.order_history(cancel_the_order)[-1]
            print(cancel_ord_hist, datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            if cancel_ord_hist['status'] == 'CANCELLED':
                print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                status = "cancelled"
        except Exception as e:
            print("Failed to cancel the order"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
    return status

def order_place_sqr_complete(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,reject_count,cancel_count,sqr_order_id):
    kt_order_id_1 = ''
    file_list = file_list
    drive = drive
    retry_order = retry_order
    time.sleep(2)
    ord_plc = True
    val_pending = 0
    order_place_fail = 0
    order_history_fail = 0
    order_datafetch_fail = 0
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    instru = instru
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    fresh_position= fresh_position
    buy_sell = buy_sell
    modification_error = 0
    cancellation_error = 0
    rejection_error = 0
    multiple_sqr_off_error = 0
    order_pending_error = 0
    multi_sqr_off_error = 0
    executed = 0
    all_api_failed = 0
    contract = contract
    sqr_off_order = sqr_off_order
    ord_hist = ''
    order_trade_data = ''
    modify_counter = 0
    loop_time1 = 0
    loop_time2 = 0
    loop_time3 = 0
    leg1_sqr_off_error = 0
    leg1_fail_leg2_not_placed = 0
    expiry = expiry
    folder = '1vjTc2vhRc9gmlPRQ5D6IHaL9gt07yHtf'
    modify_counter = 0
    cancel_loop = 0
    modify_loop = 0
    status = status
    reject_count = reject_count
    cancel_count = cancel_count
    df63=pd.DataFrame()
    COLUMN_NAMES=['current_signal','entry_time','exit_time','leg','instru','order_id','qty','price_when_order_placed','fresh_position','buy_sell','instrument_id','trading_symbol','modification_error','cancellation_error','rejection_error','multiple_sqr_off_error','order_pending_error','multi_sqr_off_error','executed','all_api_failed','leg1_sqr_off_error','leg1_fail_leg2_not_placed','entry_price','strike','contract','status','exit_price','expiry','trade_id','sqr_off_order','reject_count','cancel_count','sqr_order_id']
    df64=pd.DataFrame(columns=COLUMN_NAMES) 
    while ord_plc:
        try:
            no_ltp = 1
            a = 'NFO:'+ str(symbol_opt_1)
            instruments = [a]
            # price = float(kite.ltp(instruments,s)) + 1
            price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
            price = price_df['close'].iloc[-1] + 1
            print("current price ",price,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            order_place_fail = 1
            print("Failed to get LTP",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            #place market order
            price = price_opt_1 + 2
            no_ltp = 1
        try:
            margins_data = s.margins()
            avl_margin_before_trade = 0
            # for i in margins_data:
            avl_margin_before_trade = margins_data['equity']['available']['live_balance']
            print("current margin ",avl_margin_before_trade,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            avl_margin_before_trade = 0
            print("Failed to get margin",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        try:
            position_data =''
            position_data = s.positions()
            position_datafetch_initial = 0
            for i in position_data['day']:
                if i['instrument_token'] == opt_id_1:
                    position_datafetch_initial = i['quantity']
                    position_datafetch_initial_check = 1
            print("current position check done ",datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            position_datafetch_initial_check = 0
            print("Failed to get position_data",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        try:
            if no_ltp:
                kt_order_id_1 = s.place_order(variety=KiteApp.VARIETY_REGULAR,exchange=KiteApp.EXCHANGE_NFO,tradingsymbol=symbol_opt_1,transaction_type=buy_sell,quantity=quantity,product=KiteApp.PRODUCT_NRML,order_type=KiteApp.ORDER_TYPE_MARKET,price=price)
            else:
                kt_order_id_1 = s.place_order(s,variety=KiteApp.VARIETY_REGULAR,exchange=KiteApp.EXCHANGE_NFO,tradingsymbol=symbol_opt_1,transaction_type=buy_sell,quantity=quantity,product=KiteApp.PRODUCT_NRML,order_type=KiteApp.ORDER_TYPE_LIMIT,price=price)
#             kt_order_id_1 = kite.place_order(kite.VARIETY_REGULAR,kite.EXCHANGE_NFO,symbol_opt_1,kite.TRANSACTION_TYPE_+signal,15,kite.PRODUCT_NRML,kite.ORDER_TYPE_LIMIT,price=price)
            order_place_fail = 0
            print("placed order ",kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            order_place_fail = 1
            print("Failed to place order",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if kt_order_id_1:
            time.sleep(3)
            try:
                ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
                print("printing order history",kt_order_id_1," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                order_history_fail = 0
                if ord_hist['status'] == 'COMPLETE':
                    executed = 1
                    ord_plc = False
                    status = "close"
                    colname = ["sqr_order_id","exit_time", "exit_price","status"]
                    kk = 0
                    nn = 0
                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                    for index, file in enumerate(file_list):
                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                            kk = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                        if(file['title'] =="order_sqr_complete.txt"):
                            nn = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df64 = pd.read_csv("order_sqr_complete.txt")
                    if bool(kk):
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                        # df64 = df63.iloc[:0]
                        print(df64)
                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                        print(df64)
                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': kk})
                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                        update_file.Upload()
                    else:
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                        gfile.Upload()
                    if bool(nn):
                        df64.to_csv("order_sqr_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': nn})
                        update_file.SetContentFile("order_sqr_complete.txt")
                        update_file.Upload()
                    else:
                        df64.to_csv("order_sqr_complete.txt", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                        gfile.SetContentFile("order_sqr_complete.txt")
                        gfile.Upload()
                    kt_order_id_1 = ''
                            #send a signal to check the status while algo is running
                elif ord_hist['status'] == 'REJECTED':
                    print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    reject_count = reject_count + 1
                    status = "rejected"
                    rejection_error = 1
                    kk = 0
                    nn = 0
                    colname = ["sqr_order_id","rejection_error","reject_count","status"]
    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count})
                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                    for index, file in enumerate(file_list):
                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                            kk = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                        if(file['title'] =="order_reject_complete.txt"):
                            nn = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df64 = pd.read_csv("order_reject_complete.txt")

                    if bool(nn):
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,status]
                        df07 = df63[(df63.leg==leg)]
                        df08 = pd.concat([df64,df07])
                        df08.to_csv("order_reject_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': nn})
                        update_file.SetContentFile("order_reject_complete.txt")
                        update_file.Upload()
                    else:
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,status]
                        df07 = df63[(df63.leg==leg)]
                        df08 = pd.concat([df64,df07])
                        df08.to_csv("order_reject_complete.txt", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject_complete.txt"})
                        gfile.SetContentFile("order_reject_complete.txt")
                        gfile.Upload()
                    if bool(kk):
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,"open"]
                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': kk})
                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                        update_file.Upload()
                    else:
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,"open"]
                        df63.to_csv("order_tobe_sqr_complete", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                        gfile.Upload()
                    rejection_error = 0
                elif ord_hist['status'] == 'CANCELLED':
                    print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    cancel_count = cancel_count + 1
                    cancellation_error = 1
                    status = "cancelled"
                    kk = 0
                    nn = 0
                    colname = ["sqr_order_id","cancellation_error","cancel_count","status"]
    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count})
                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                    for index, file in enumerate(file_list):
                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                            kk = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                        if(file['title'] =="order_cancel_complete.txt"):
                            nn = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df64 = pd.read_csv("order_cancel_complete.txt")

                    if bool(nn):
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,status]
                        df07 = df63[(df63.leg==leg)]
                        df08 = pd.concat([df64,df07])
                        df08.to_csv("order_cancel_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': nn})
                        update_file.SetContentFile("order_cancel_complete.txt")
                        update_file.Upload()
                    else:
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,status]
                        df07 = df63[(df63.leg==leg)]
                        df08 = pd.concat([df64,df07])
                        df08.to_csv("order_cancel_complete.txt", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel_complete.txt"})
                        gfile.SetContentFile("order_cancel_complete.txt")
                        gfile.Upload()
                    if bool(kk):
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,"open"]
                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': kk})
                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                        update_file.Upload()
                    else:
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,"open"]
                        df63.to_csv("order_tobe_sqr_complete", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                        gfile.Upload()
                    cancellation_error = 0
                else:
                    print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    val_pending = 1
                    status = "pending"
                    ord_plc = False
                    kk = 0
                    nn = 0
                    colname = ["sqr_order_id","status"]
    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count})
                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                    for index, file in enumerate(file_list):
                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                            kk = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                        if(file['title'] =="order_pending_complete.txt"):
                            nn = file['id']
                            df29 = file.GetContentFile(file['title'])
                            df64 = pd.read_csv("order_pending_complete.txt")

                    if bool(nn):
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                        df07 = df63[(df63.leg==leg)]
                        df08 = pd.concat([df64,df07])
                        df08.to_csv("order_pending_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': nn})
                        update_file.SetContentFile("order_pending_complete.txt")
                        update_file.Upload()
                    else:
                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                        df07 = df63[(df63.leg==leg)]
                        df08 = pd.concat([df64,df07])
                        df08.to_csv("order_pending_complete.txt", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending_complete.txt"})
                        gfile.SetContentFile("order_pending_complete.txt")
                        gfile.Upload()
                    if bool(kk):
    #                     df63.loc[(df63.leg==leg), colname] = [rejection_error,reject_count,"open"]
                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                        update_file = drive.CreateFile({'id': kk})
                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                        update_file.Upload()
                    else:
                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                        df63.to_csv("order_tobe_sqr_complete", index=False)
                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                        gfile.Upload()
            except Exception as e:
                order_history_fail = 1
                print("Failed to fetch order history data",e," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            if not ord_hist or order_history_fail:
                try:
                    print("checking trades"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    order_trade_data = ''
                    order_trade_data = s.order_trades(kt_order_id_1)
                    order_trade_datafetch_fail = 0
                    for i in order_trade_data:
                        if i['order_id'] == kt_order_id_1:
                            executed = 1
                            ord_plc = False
                            status = "close"
                            colname = ["sqr_order_id","exit_time", "exit_price","status"]
                            kk = 0
                            nn = 0
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_sqr_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_sqr_complete.txt")
                            if bool(kk):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                # df64 = df63.iloc[:0]
                                print(df64)
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                print(df64)
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
                            if bool(nn):
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                gfile.SetContentFile("order_sqr_complete.txt")
                                gfile.Upload()
                            kt_order_id_1 = ''
                except Exception as e:
                    order_trade_datafetch_fail = 1
                    print("Failed to fetch trade data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not order_trade_data or order_trade_datafetch_fail:            
                    try:
                        print("checking order "," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_data = ''
                        ord_data = s.orders()
                        order_datafetch_fail = 0
                        for i in ord_data:
                            if i['order_id'] == kt_order_id_1 and i['transaction_type'] == buy_sell:
                                if i['status'] == 'COMPLETE':
                                    print("order complete"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    executed = 1
                                    ord_plc = False
                                    status = "close"
                                    colname = ["sqr_order_id","exit_time", "exit_price","status"]
                                    kk = 0
                                    nn = 0
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                        if(file['title'] =="order_sqr_complete.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_sqr_complete.txt")
                                    if bool(kk):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                        # df64 = df63.iloc[:0]
                                        print(df64)
                                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                        print(df64)
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                        gfile.Upload()
                                    if bool(nn):
                                        df64.to_csv("order_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df64.to_csv("order_sqr_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                        gfile.SetContentFile("order_sqr_complete.txt")
                                        gfile.Upload()
                                    kt_order_id_1 = ''
                                elif i['status'] == 'REJECTED':
                                    print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    reject_count = reject_count + 1
                                    status = "rejected"
                                    rejection_error = 1
                                    kk = 0
                                    nn = 0
                                    colname = ["sqr_order_id","rejection_error","reject_count","status"]
                    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                        if(file['title'] =="order_reject_complete.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_reject_complete.txt")

                                    if bool(nn):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,status]
                                        df07 = df63[(df63.leg==leg)]
                                        df08 = pd.concat([df64,df07])
                                        df08.to_csv("order_reject_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_reject_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,status]
                                        df07 = df63[(df63.leg==leg)]
                                        df08 = pd.concat([df64,df07])
                                        df08.to_csv("order_reject_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject_complete.txt"})
                                        gfile.SetContentFile("order_reject_complete.txt")
                                        gfile.Upload()
                                    if bool(kk):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,"open"]
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,"open"]
                                        df63.to_csv("order_tobe_sqr_complete", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                        gfile.Upload()

                                    rejection_error = 0
                                elif i['status'] == 'CANCELLED':
                                    print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    cancel_count = cancel_count + 1
                                    cancellation_error = 1
                                    status = "cancelled"
                                    kk = 0
                                    nn = 0
                                    colname = ["sqr_order_id","cancellation_error","cancel_count","status"]
                    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                        if(file['title'] =="order_cancel_complete.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_cancel_complete.txt")
                                    if bool(nn):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,status]
                                        df07 = df63[(df63.leg==leg)]
                                        df08 = pd.concat([df64,df07])
                                        df08.to_csv("order_cancel_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_cancel_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,status]
                                        df07 = df63[(df63.leg==leg)]
                                        df08 = pd.concat([df64,df07])
                                        df08.to_csv("order_cancel_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel_complete.txt"})
                                        gfile.SetContentFile("order_cancel_complete.txt")
                                        gfile.Upload()
                                    if bool(kk):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,"open"]
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,"open"]
                                        df63.to_csv("order_tobe_sqr_complete", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                        gfile.Upload()
                                    cancellation_error = 0
                                else:
                                    print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    val_pending = 1
                                    status = "pending"
                                    ord_plc = False
                                    kk = 0
                                    nn = 0
                                    colname = ["sqr_order_id","status"]
                    #                         OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                        if(file['title'] =="order_pending_complete.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_pending_complete.txt")

                                    if bool(nn):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                                        df07 = df63[(df63.leg==leg)]
                                        df08 = pd.concat([df64,df07])
                                        df08.to_csv("order_pending_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_pending_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                                        df07 = df63[(df63.leg==leg)]
                                        df08 = pd.concat([df64,df07])
                                        df08.to_csv("order_pending_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending_complete.txt"})
                                        gfile.SetContentFile("order_pending_complete.txt")
                                        gfile.Upload()
                                    if bool(kk):
                    #                     df63.loc[(df63.leg==leg), colname] = [rejection_error,reject_count,"open"]
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                        gfile.Upload()
                    except Exception as e:
                        order_datafetch_fail = 1
                        print("Failed to fetch order data")
                    if not ord_data or order_datafetch_fail:
                        try:
                            print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            if position_datafetch_initial_check  < 1:
                                all_api_failed = 1
                                break
                            position_data =''
                            position_data = s.positions()
                            position_datafetch_fail = 0
                            for i in position_data['day']:
                                if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                                    executed = 1
                                    ord_plc = False
                                    status = "close"
                                    colname = ["sqr_order_id","exit_time", "exit_price","status"]
                                    kk = 0
                                    nn = 0
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                        if(file['title'] =="order_sqr_complete.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_sqr_complete.txt")
                                    if bool(kk):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                        # df64 = df63.iloc[:0]
                                        print(df64)
                                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                        print(df64)
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                        gfile.Upload()
                                    if bool(nn):
                                        df64.to_csv("order_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df64.to_csv("order_sqr_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                        gfile.SetContentFile("order_sqr_complete.txt")
                                        gfile.Upload()
                                    kt_order_id_1 = ''
                        except Exception as e:
                            position_datafetch_fail = 1
                            print("Failed to fetch position data")

                        if not position_data or position_datafetch_fail:
                            try:
                                print("checking margin"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if avl_margin_before_trade  < 1:
                                    all_api_failed = 1
                                    ord_plc = False
                                margins_data = s.margins()
                                margins_datafetch_fail = 0
                                # for i in margins_data:
                                if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                                    executed = 1
                                    ord_plc = False
                                    status = "close"
                                    colname = ["sqr_order_id","exit_time", "exit_price","status"]
                                    kk = 0
                                    nn = 0
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_tobe_sqr_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                        if(file['title'] =="order_sqr_complete.txt"):
                                            nn = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df64 = pd.read_csv("order_sqr_complete.txt")
                                    if bool(kk):
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                        # df64 = df63.iloc[:0]
                                        print(df64)
                                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                        print(df64)
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                        df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                        df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                        df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                        gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                        gfile.Upload()
                                    if bool(nn):
                                        df64.to_csv("order_sqr_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': nn})
                                        update_file.SetContentFile("order_sqr_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df64.to_csv("order_sqr_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                        gfile.SetContentFile("order_sqr_complete.txt")
                                        gfile.Upload()
                                    kt_order_id_1 = ''
                            except Exception as e:
                                margins_datafetch_fail = 1
                                all_api_failed = 1
                                print("Failed to fetch margin data")
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_tobe_sqr_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                    if(file['title'] =="order_pending_complete.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_pending_complete.txt")
                                if bool(nn):
                                    df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                                    df07 = df63[(df63.leg==leg)]
                                    df08 = pd.concat([df64,df07])
                                    df08.to_csv("order_pending_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_pending_complete.txt")
                                    update_file.Upload()
                                else:
                                    df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                                    df07 = df63[(df63.leg==leg)]
                                    df08 = pd.concat([df64,df07])
                                    df08.to_csv("order_pending_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending_complete.txt"})
                                    gfile.SetContentFile("order_pending_complete.txt")
                                    gfile.Upload()
                                if bool(kk):
                #                     df63.loc[(df63.leg==leg), colname] = [rejection_error,reject_count,"open"]
                                    df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                    df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                    update_file.Upload()
                                else:
                                    df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                    df63.to_csv("order_tobe_sqr_complete", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                    gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                    gfile.Upload()

        elif not kt_order_id_1 or order_place_fail:
            try:
                print("no order id checking orders "," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                ord_data = ''
                ord_data = s.orders()
                order_datafetch_fail = 0
                for i in ord_data:
                    if i['instrument_token'] == opt_id_1 and i['transaction_type'] == buy_sell:
                        if i['status'] == 'COMPLETE':
                            print("order complete"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            executed = 1
                            ord_plc = False
                            status = "close"
                            colname = ["sqr_order_id","exit_time", "exit_price","status"]
                            kk = 0
                            nn = 0
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_sqr_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_sqr_complete.txt")
                            if bool(kk):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
                            if bool(nn):
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                gfile.SetContentFile("order_sqr_complete.txt")
                                gfile.Upload()
                            kt_order_id_1 = ''
                        elif i['status'] == 'REJECTED':
                            print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            reject_count = reject_count + 1
                            status = "rejected"
                            rejection_error = 1
                            kk = 0
                            nn = 0
                            colname = ["sqr_order_id","rejection_error","reject_count","status"]
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_reject_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_reject_complete.txt")
                            if bool(nn):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,status]
                                df07 = df63[(df63.leg==leg)]
                                df08 = pd.concat([df64,df07])
                                df08.to_csv("order_reject_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_reject_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,status]
                                df07 = df63[(df63.leg==leg)]
                                df08 = pd.concat([df64,df07])
                                df08.to_csv("order_reject_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject_complete.txt"})
                                gfile.SetContentFile("order_reject_complete.txt")
                                gfile.Upload()
                            if bool(kk):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,"open"]
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,rejection_error,reject_count,"open"]
                                df63.to_csv("order_tobe_sqr_complete", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
                            rejection_error = 0
                        elif i['status'] == 'CANCELLED':
                            print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            cancel_count = cancel_count + 1
                            cancellation_error = 1
                            status = "cancelled"
                            kk = 0
                            nn = 0
                            colname = ["sqr_order_id","cancellation_error","cancel_count","status"]
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_cancel_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_cancel_complete.txt")
                            if bool(nn):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,status]
                                df07 = df63[(df63.leg==leg)]
                                df08 = pd.concat([df64,df07])
                                df08.to_csv("order_cancel_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_cancel_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,status]
                                df07 = df63[(df63.leg==leg)]
                                df08 = pd.concat([df64,df07])
                                df08.to_csv("order_cancel_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel_complete.txt"})
                                gfile.SetContentFile("order_cancel_complete.txt")
                                gfile.Upload()
                            if bool(kk):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,"open"]
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,cancellation_error,cancel_count,"open"]
                                df63.to_csv("order_tobe_sqr_complete", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
                            cancellation_error = 0
                        else:
                            print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            val_pending = 1
                            status = "pending"
                            ord_plc = False
                            kk = 0
                            nn = 0
                            colname = ["sqr_order_id","status"]
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_pending_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_pending_complete.txt")

                            if bool(nn):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                                df07 = df63[(df63.leg==leg)]
                                df08 = pd.concat([df64,df07])
                                df08.to_csv("order_pending_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_pending_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,status]
                                df07 = df63[(df63.leg==leg)]
                                df08 = pd.concat([df64,df07])
                                df08.to_csv("order_pending_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending_complete.txt"})
                                gfile.SetContentFile("order_pending_complete.txt")
                                gfile.Upload()
                            if bool(kk):
            #                     df63.loc[(df63.leg==leg), colname] = [rejection_error,reject_count,"open"]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
            except Exception as e:
                order_datafetch_fail = 1
                print("Failed to fetch order data")
            if not ord_data or order_datafetch_fail:
                try:
                    print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    if position_datafetch_initial_check  < 1:
                        all_api_failed = 1
                        break
                    position_data =''
                    position_data = s.positions()
                    position_datafetch_fail = 0
                    for i in position_data['day']:
                        if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                            executed = 1
                            ord_plc = False
                            status = "close"
                            colname = ["sqr_order_id","exit_time", "exit_price","status"]
                            kk = 0
                            nn = 0
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_sqr_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_sqr_complete.txt")
                            if bool(kk):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                # df64 = df63.iloc[:0]
                                print(df64)
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                print(df64)
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
                            if bool(nn):
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                gfile.SetContentFile("order_sqr_complete.txt")
                                gfile.Upload()
                            kt_order_id_1 = ''
                except Exception as e:
                    position_datafetch_fail = 1
                    print("Failed to fetch position data")

                if not position_data or position_datafetch_fail:
                    try:
                        print("checking margin"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if avl_margin_before_trade  < 1:
                            all_api_failed = 1
                            ord_plc = False
                        margins_data = s.margins()
                        margins_datafetch_fail = 0
                        # for i in margins_data:
                        if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                            executed = 1
                            ord_plc = False
                            status = "close"
                            colname = ["sqr_order_id","exit_time", "exit_price","status"]
                            kk = 0
                            nn = 0
                            file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                            for index, file in enumerate(file_list):
                                if(file['title'] =="order_tobe_sqr_complete.txt"):
                                    kk = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df63 = pd.read_csv("order_tobe_sqr_complete.txt")
                                if(file['title'] =="order_sqr_complete.txt"):
                                    nn = file['id']
                                    df29 = file.GetContentFile(file['title'])
                                    df64 = pd.read_csv("order_sqr_complete.txt")
                            if bool(kk):
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': kk})
                                update_file.SetContentFile("order_tobe_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df63.loc[(df63.leg==leg), colname] = [kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                df63.to_csv("order_tobe_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_tobe_sqr_complete.txt"})
                                gfile.SetContentFile("order_tobe_sqr_complete.txt")
                                gfile.Upload()
                            if bool(nn):
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                update_file = drive.CreateFile({'id': nn})
                                update_file.SetContentFile("order_sqr_complete.txt")
                                update_file.Upload()
                            else:
                                df64.to_csv("order_sqr_complete.txt", index=False)
                                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_sqr_complete.txt"})
                                gfile.SetContentFile("order_sqr_complete.txt")
                                gfile.Upload()
                            kt_order_id_1 = ''
                        ord_plc = False
                    except Exception as e:
                        margins_datafetch_fail = 1
                        all_api_failed = 1
                        ord_plc = False
                        print("Failed to fetch margin data")
            ord_plc = False
    return status

def order_multiple_place(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,reject_count,cancel_count,sqr_order_id):
    sqr_order_id = sqr_order_id
    retry_order = retry_order
    time.sleep(2)
    ord_plc = True
    val_pending = 0
    order_place_fail = 0
    order_history_fail = 0
    order_datafetch_fail = 0
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    instru = instru
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    fresh_position= fresh_position
    buy_sell = buy_sell
    modification_error = 0
    cancellation_error = 0
    rejection_error = 0
    multiple_sqr_off_error = 0
    order_pending_error = 0
    multi_sqr_off_error = 0
    executed = 0
    all_api_failed = 0
    contract = contract
    sqr_off_order = sqr_off_order
    ord_hist = ''
    order_trade_data = ''
    modify_counter = 0
    loop_time1 = 0
    loop_time2 = 0
    loop_time3 = 0
    leg1_sqr_off_error = 0
    leg1_fail_leg2_not_placed = 0
    expiry = expiry
    modify_counter = 0
    cancel_loop = 0
    modify_loop = 0
    status = status
    reject_count = reject_count
    cancel_count = cancel_count
    while ord_plc:
        try:
            a = 'NFO:'+ str(symbol_opt_1)
            instruments = [a]
            # price = float(kite.ltp(instruments,s)) + 1
            price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
            price = price_df['close'].iloc[-1] + 1
            print("current price ",price,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            order_place_fail = 1
            print("Failed to get LTP",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            break
        try:
            margins_data = s.margins()
            avl_margin_before_trade = 0
            # for i in margins_data:
            avl_margin_before_trade = margins_data['equity']['available']['live_balance']
            print("current margin ",avl_margin_before_trade,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            avl_margin_before_trade = 0
            print("Failed to get margin",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        try:
            position_data =''
            position_data = s.positions()
            position_datafetch_initial = 0
            for i in position_data['day']:
                if i['instrument_token'] == opt_id_1:
                    position_datafetch_initial = i['quantity']
                    position_datafetch_initial_check = 1
            print("current position check done ",datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            position_datafetch_initial_check = 0
            print("Failed to get position_data",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        try:
            kt_order_id_1 = s.place_order(variety=KiteApp.VARIETY_REGULAR,exchange=KiteApp.EXCHANGE_NFO,tradingsymbol=symbol_opt_1,transaction_type=buy_sell,quantity=quantity,product=KiteApp.PRODUCT_NRML,order_type=KiteApp.ORDER_TYPE_LIMIT,price=price)
            order_place_fail = 0
            print("placed order",kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            order_place_fail = 1
            print("Failed to place order",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
    if kt_order_id_1:
        time.sleep(3)
        try:
            ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
            print("printing order history",kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            order_history_fail = 0
            if ord_hist['status'] == 'COMPLETE':
                print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                executed = 1
                ord_plc = False
                status = "close"
                kt_order_id_1 = ''
            elif ord_hist['status'] == 'REJECTED':
                print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                ord_plc = False
                reject_count = reject_count + 1
                kt_order_id_1 = ''
                status = "rejected"
                rejection_error = 1
            elif ord_hist['status'] == 'CANCELLED':
                print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                ord_plc = False
                cancel_count = cancel_count + 1
                cancellation_error = 1
                status = "cancelled"
            else:
                print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                val_pending = 1
                status = "pending"
                ord_plc = False
        except Exception as e:
            order_history_fail = 1
            print("Failed to fetch order history data",e, datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if not ord_hist or order_history_fail:
            try:
                print("check trades"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                order_trade_data = ''
                order_trade_data = s.order_trades(kt_order_id_1)
                order_trade_datafetch_fail = 0
                for i in order_trade_data:
                    if i['order_id'] == kt_order_id_1:
                        ord_plc = False
                        status = "close"
                        executed = 1
            except Exception as e:
                order_trade_datafetch_fail = 1
                print("Failed to fetch trade data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            if not order_trade_data or order_trade_datafetch_fail:            
                try:
                    print("check orders"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_data = ''
                    ord_data = s.orders()
                    order_datafetch_fail = 0
                    for i in ord_data:
                        if i['order_id'] == kt_order_id_1 and i['transaction_type'] == buy_sell:
                            if i['status'] == 'COMPLETE':
                                print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                ord_plc = False
                                executed = 1
                                status = "close"
                            elif i['status'] == 'REJECTED':
                                print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                ord_plc = False
                                reject_count = reject_count + 1
                                kt_order_id_1 = ''
                                status = "rejected"
                            elif i['status'] == 'CANCELLED':
                                print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                ord_plc = False
                                cancel_count = cancel_count + 1
                                cancellation_error = 1
                                status = "cancelled"
                            else:
                                print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                val_pending = 1
                                status = "pending"
                                ord_plc = False
                except Exception as e:
                    order_datafetch_fail = 1
                    print("Failed to fetch order data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not ord_data or order_datafetch_fail:
                    try:
                        print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if position_datafetch_initial_check  < 1:
                            all_api_failed = 1
                            ord_plc = False
                        position_data =''
                        position_data = s.positions()
                        position_datafetch_fail = 0
                        for i in position_data['day']:
                            if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                                print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                ord_plc = False
                                executed = 1
                                status = "close"
                    except Exception as e:
                        position_datafetch_fail = 1
                        print("Failed to fetch position data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)

                    if not position_data or position_datafetch_fail:
                        try:
                            print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            if avl_margin_before_trade  < 1:
                                all_api_failed = 1
                                ord_plc = False
                            margins_data = s.margins()
                            margins_datafetch_fail = 0
                            # for i in margins_data:
                            if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                                ord_plc = False
                                executed = 1
                                status = "close"
                        except Exception as e:
                            margins_datafetch_fail = 1
                            all_api_failed = 1
                            print("Failed to fetch margin data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
    elif not kt_order_id_1 or order_place_fail:
        try:
            print("checking orders"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            ord_data = ''
            ord_data = s.orders()
            order_datafetch_fail = 0
            for i in ord_data:
                if i['order_id'] == kt_order_id_1 and i['transaction_type'] == buy_sell:
                    if i['status'] == 'COMPLETE':
                        print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_plc = False
                        executed = 1
                        status = "close"
                    elif i['status'] == 'REJECTED':
                        print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_plc = False
                        reject_count = reject_count + 1
                        kt_order_id_1 = ''
                        status = "rejected"
                    elif i['status'] == 'CANCELLED':
                        print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_plc = False
                        cancel_count = cancel_count + 1
                        cancellation_error = 1
                        status = "cancelled"
                    else:
                        print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        val_pending = 1
                        status = "pending"
                        ord_plc = False
        except Exception as e:
            order_datafetch_fail = 1
            print("Failed to fetch order data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if not ord_data or order_datafetch_fail:
            try:
                print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if position_datafetch_initial_check  < 1:
                    all_api_failed = 1
                    ord_plc = False
                position_data =''
                position_data = s.positions()
                position_datafetch_fail = 0
                for i in position_data['day']:
                    if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                        print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_plc = False
                        executed = 1
                        status = "close"
            except Exception as e:
                position_datafetch_fail = 1
                print("Failed to fetch position data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            if not position_data or position_datafetch_fail:
                try:
                    print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    if avl_margin_before_trade  < 1:
                        all_api_failed = 1
                        ord_plc = False
                    margins_data = s.margins()
                    margins_datafetch_fail = 0
                    # for i in margins_data:
                    if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                        ord_plc = False
                        executed = 1
                        status = "close"
                except Exception as e:
                    margins_datafetch_fail = 1
                    all_api_failed = 1
                    print("Failed to fetch margin data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
    return status

def order_modify_complete(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,kt_order_id_1):
    ord_plc = True
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    status = status
    kt_order_id_1 = kt_order_id_1
    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    while ord_plc:
        try:
            a = 'NFO:'+ str(symbol_opt_1)
            instruments = [a]
            # price = float(kite.ltp(instruments,s)) + 1
            price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
            price = price_df['close'].iloc[-1] + 1
            print("current price ",price,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        except Exception as e:
            order_place_fail = 1
            print("Failed to get LTP",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            price = price_opt_1 + 2
        if abs(((price - price_opt_1) / price_opt_1) * 100) > 25:
            print("price has crossed 25% band ",price," ",price_opt_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            ord_plc = False 
            break
        try:
            price = price + 1
            modify_order_id = s.modify_order(KiteApp.VARIETY_REGULAR, kt_order_id_1, quantity,price=price) 
            if modify_order_id:
                kt_order_id_1 = modify_order_id
            time.sleep(3)
            try:
                modify_ord_hist = ''
                modify_ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
                if modify_ord_hist['status'] == 'MODIFIED':
                    print("order modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    status = "modified"
                    modification_error = 0
                    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                else:
                    print("order not modified"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    modify_val_pending = 1
                    modification_error = 1
                    modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                    ord_plc = False 
            except Exception as e:
                print("Failed to get order history details for modified order",e, datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                modification_error = 1
                ord_plc = False 
                modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        except Exception as e:
            print("Failed to modify order",e, datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            ord_plc = False
            modification_error = 1
            modify_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return status,price,modify_time


def order_place_manage(s,file_list,drive,current_signal,opt_id_1,symbol_opt_1,price_opt_1,quantity,instru,fresh_position,leg,strike,contract,expiry,trade_id,sqr_off_order,buy_sell,retry_order,status,reject_count,cancel_count,sqr_order_id):
    s = s
    file_list = file_list
    drive = drive
    retry_order = retry_order
    ord_plc = True
    val_pending = 0
    order_place_fail = 0
    order_history_fail = 0
    order_datafetch_fail = 0
    loop_rejected = 0
    loop1 = 0
    loop2 = 0
    loop3 = 0
    leg = leg
    trade_id = trade_id
    current_signal = current_signal
    # strategy = strategy
    instru = instru
    opt_id_1 = opt_id_1
    symbol_opt_1 = symbol_opt_1
    price = price_opt_1
    quantity = quantity
    fresh_position= fresh_position
    buy_sell = buy_sell
    modification_error = 0
    cancellation_error = 0
    rejection_error = 0
    multiple_sqr_off_error = 0
    order_pending_error = 0
    multi_sqr_off_error = 0
    executed = 0
    all_api_failed = 0
    contract = contract
    sqr_off_order = sqr_off_order
    ord_hist = ''
    order_trade_data = ''
    modify_counter = 0
    loop_time1 = 0
    loop_time2 = 0
    loop_time3 = 0
    leg1_sqr_off_error = 0
    leg1_fail_leg2_not_placed = 0
    expiry = expiry
    folder = '1vjTc2vhRc9gmlPRQ5D6IHaL9gt07yHtf'
    modify_counter = 0
    cancel_loop = 0
    modify_loop = 0
    status = status
    reject_count = reject_count
    cancel_count = cancel_count
    COLUMN_NAMES=['current_signal','entry_time','exit_time','leg','instru','order_id','qty','price_when_order_placed','fresh_position','buy_sell','instrument_id','trading_symbol','modification_error','cancellation_error','rejection_error','multiple_sqr_off_error','order_pending_error','multi_sqr_off_error','executed','all_api_failed','leg1_sqr_off_error','leg1_fail_leg2_not_placed','entry_price','strike','contract','status','exit_price','expiry','trade_id','sqr_off_order','reject_count','cancel_count','sqr_order_id']
    df64=pd.DataFrame(columns=COLUMN_NAMES) 
    buy_sell = buy_sell
    while ord_plc:
        if not kt_order_id_1 or not val_pending or status == "cancelled" or status == "rejected":
            try:
                a = 'NFO:'+ str(symbol_opt_1)
                instruments = [a]
                # price = float(kite.ltp(instruments,s)) + 1
                price_df = pd.DataFrame(s.historical_data(opt_id_1, fromm, fromm, "minute", continuous=False, oi=True))
                price = price_df['close'].iloc[-1] + 1
                print("current price ",price,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                order_place_fail = 1
                print("Failed to get LTP",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                price = price_opt_1 + 2
            if abs(((price - price_opt_1) / price_opt_1) * 100) > 25:
                print("price has crossed 25% band ",price," ",price_opt_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                ord_plc = False 
                break
            try:
                margins_data = s.margins()
                avl_margin_before_trade = 0
                # for i in margins_data:
                    # print(i)
                avl_margin_before_trade = margins_data['equity']['available']['live_balance']
                print("current margin ",avl_margin_before_trade,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                avl_margin_before_trade = 0
                print("Failed to get margin",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            try:
                position_data =''
                position_data = s.positions()
                position_datafetch_initial = 0
                for i in position_data['day']:
                    if i['instrument_token'] == opt_id_1:
                        position_datafetch_initial = i['quantity']
                        position_datafetch_initial_check = 1
                print("current position check done ",datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                position_datafetch_initial_check = 0
                print("Failed to get position_data",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            try:
                kt_order_id_1 = s.place_order(variety=KiteApp.VARIETY_REGULAR,exchange=KiteApp.EXCHANGE_NFO,tradingsymbol=symbol_opt_1,transaction_type=buy_sell,quantity=quantity,product=KiteApp.PRODUCT_NRML,order_type=KiteApp.ORDER_TYPE_LIMIT,price=price)
    #             kt_order_id_1 = kite.place_order(kite.VARIETY_REGULAR,kite.EXCHANGE_NFO,symbol_opt_1,kite.TRANSACTION_TYPE_+signal,15,kite.PRODUCT_NRML,kite.ORDER_TYPE_LIMIT,price=price)
                order_place_fail = 0
                print("placed order",kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                order_place_fail = 1
                print("Failed to place order",e,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        if kt_order_id_1:
            time.sleep(3)
            try:
                ord_hist = s.order_history(order_id=kt_order_id_1)[-1]
                print("printing order history",kt_order_id_1,datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                order_history_fail = 0
                if ord_hist['status'] == 'COMPLETE':
                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    executed = 1
                    ord_plc = False
                    ord_plc_extra = True
                    # opt_id_1 = 100
                    if (fresh_position > 0) and (executed > 0):
                        status = "open"
                        OM_log = []
                        kk = 0
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        kt_order_id_1 = ''
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_complete.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_complete.txt")
                                print(df63)
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
#                             print(df07)
                            df08 = pd.concat([df63,df07])
                            print(df08)
                            df08.to_csv("order_complete.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_complete.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_complete.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                            gfile.SetContentFile("order_complete.txt")
                            gfile.Upload()
                        OM_log = []
                    if (fresh_position < 1) and (executed > 0):
                        status = "close"
                        colname = ["exit_time", "exit_price","status"]
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_complete.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_complete.txt")
                            if(file['title'] =="order_sqr_complete.txt"):
                                nn = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df64 = pd.read_csv("order_sqr_complete.txt")
                        if bool(kk):
                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                            df63.to_csv("order_complete.txt", index=False)
                            df64.to_csv("order_sqr_complete.txt", index=False)
                            update_file = drive.CreateFile({'id': kk})
                            update_file.SetContentFile("order_complete.txt")
                            update_file.Upload()
                            update_file = drive.CreateFile({'id': nn})
                            update_file.SetContentFile("order_sqr_complete.txt")
                            update_file.Upload()
                elif ord_hist['status'] == 'REJECTED':
                    print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    reject_count = reject_count + 1
                    if not retry_order and fresh_position > 0:
                        status = "rejected"
                        rejection_error = 1
                        OM_log = []
                        OMT_log = []
                        kk = 0
                        nn = 0
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_reject.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_reject.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_reject.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_reject.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_reject.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                            gfile.SetContentFile("order_reject.txt")
                            gfile.Upload()
                    if (not retry_order and fresh_position < 1) or retry_order:
                        rejection_error = 1
                        status = "rejected"
                        colname = ["rejection_error","reject_count"]
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_reject.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_reject.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_reject.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_reject.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_reject.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                            gfile.SetContentFile("order_reject.txt")
                            gfile.Upload()
                    OM_log = []
                    OMT_log = []
                    rejection_error = 0
                    kt_order_id_1 = ''
                elif ord_hist['status'] == 'CANCELLED':
                    print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    ord_plc = False
                    cancel_count = cancel_count + 1
                    if not retry_order and fresh_position > 0:
                        status = "cancelled"
                        cancellation_error = 1
                        OM_log = []
                        OMT_log = []
                        kk = 0
                        nn = 0
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_cancel.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_cancel.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_cancel.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_cancel.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_cancel.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                            gfile.SetContentFile("order_cancel.txt")
                            gfile.Upload()
                    if (not retry_order and fresh_position < 1) or retry_order:
                        cancellation_error = 1
                        status = "cancelled"
                        colname = ["cancellation_error","cancel_count"]
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_cancel.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_cancel.txt")
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_cancel.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_cancel.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_cancel.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                            gfile.SetContentFile("order_cancel.txt")
                            gfile.Upload()
                    OM_log = []
                    OMT_log = []
                    cancellation_error = 0
                    kt_order_id_1 = ''
                else:
                    print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    loop1 = loop1 + 1
                    print("looping",loop1)
                    if (loop1 < 6):
                        loop_time1 = loop_time1 + 5
                        time.sleep(loop_time1)
                    elif (loop1<15) and (loop1>=6):
                        loop_time1 = loop_time1 + 5
                        time.sleep(loop_time1)
                    elif (loop1>=15) and (loop1<26):
                        loop_time1 = loop_time1 + 5
                        time.sleep(loop_time1)
                    val_pending = 1
                    status = "pending"
                    if (fresh_position > 0) and (executed < 1) and not retry_order:
                        ord_plc = False
                        OM_log = []
                        kk = ''
                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                        kt_order_id_1 = ''
                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                        for index, file in enumerate(file_list):
                            if(file['title'] =="order_pending.txt"):
                                kk = file['id']
                                df29 = file.GetContentFile(file['title'])
                                df63 = pd.read_csv("order_pending.txt")
                                print(df63)
                        if bool(kk):
                            stats = kk
                            df07 = pd.DataFrame.from_dict(OM_log)
                            df08 = pd.concat([df63,df07])
                            df08.to_csv("order_pending.txt", index=False)
                            update_file = drive.CreateFile({'id': stats})
                            update_file.SetContentFile("order_pending.txt")
                            update_file.Upload()
                        else:
                            df08 = pd.DataFrame.from_dict(OM_log)
                            df08.to_csv("order_pending.txt", index=False)
                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                            gfile.SetContentFile("order_pending.txt")
                            gfile.Upload()
                        OM_log = []
                print("inside order history check after order id generation", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            except Exception as e:
                order_history_fail = 1
                print("Failed to fetch order history data",e, datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
            if not ord_hist or order_history_fail:
                try:
                    print("check trades"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    order_trade_data = ''
                    order_trade_data = s.order_trades(kt_order_id_1)
                    order_trade_datafetch_fail = 0
                    for i in order_trade_data:
                        if i['order_id'] == kt_order_id_1:
                            print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            executed = 1
                            ord_plc = False
                            ord_plc_extra = True
                            if (fresh_position > 0) and (executed > 0):
                                status = "open"
                                OM_log = []
                                kk = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                        print(df63)
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    print(df08)
                                    df08.to_csv("order_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                    gfile.SetContentFile("order_complete.txt")
                                    gfile.Upload()
                                OM_log = []
                            if (fresh_position < 1) and (executed > 0):
                                status = "close"
                                colname = ["exit_time", "exit_price","status"]
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                    if(file['title'] =="order_sqr_complete.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_sqr_complete.txt")
                                if bool(kk):
                                    df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                    df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                    df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                    df63.to_csv("order_complete.txt", index=False)
                                    df64.to_csv("order_sqr_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_sqr_complete.txt")
                                    update_file.Upload()
                except Exception as e:
                    order_trade_datafetch_fail = 1
                    print("Failed to fetch trade data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not order_trade_data or order_trade_datafetch_fail:            
                    try:
                        print("checking orders"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        ord_data = ''
                        ord_data = s.orders()
                        order_datafetch_fail = 0
                        for i in ord_data:
                            if i['order_id'] == kt_order_id_1 and i['transaction_type'] == buy_sell:
                                if i['status'] == 'COMPLETE':
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    executed = 1
                                    ord_plc = False
                                    ord_plc_extra = True
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        colname = ["exit_time", "exit_price","status"]
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")
                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                                elif i['status'] == 'REJECTED':
                                    print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    reject_count = reject_count + 1
                                    if not retry_order and fresh_position > 0:
                                        status = "rejected"
                                        rejection_error = 1
                                        OM_log = []
                                        OMT_log = []
                                        kk = 0
                                        nn = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_reject.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_reject.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_reject.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_reject.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_reject.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                            gfile.SetContentFile("order_reject.txt")
                                            gfile.Upload()
                                    if (not retry_order and fresh_position < 1) or retry_order:
                                        rejection_error = 1
                                        status = "rejected"
                                        colname = ["rejection_error","reject_count"]
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_reject.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_reject.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_reject.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_reject.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_reject.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                            gfile.SetContentFile("order_reject.txt")
                                            gfile.Upload()
                                    OM_log = []
                                    OMT_log = []
                                    rejection_error = 0
                                    kt_order_id_1 = ''
                                elif i['status'] == 'CANCELLED':
                                    print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    ord_plc = False
                                    cancel_count = cancel_count + 1
                                    if not retry_order and fresh_position > 0:
                                        status = "cancelled"
                                        cancellation_error = 1
                                        OM_log = []
                                        OMT_log = []
                                        kk = 0
                                        nn = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_cancel.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_cancel.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_cancel.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_cancel.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_cancel.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                            gfile.SetContentFile("order_cancel.txt")
                                            gfile.Upload()
                                    if (not retry_order and fresh_position < 1) or retry_order:
                                        cancellation_error = 1
                                        status = "cancelled"
                                        colname = ["cancellation_error","cancel_count"]
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_cancel.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_cancel.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_cancel.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_cancel.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_cancel.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                            gfile.SetContentFile("order_cancel.txt")
                                            gfile.Upload()
                                    OM_log = []
                                    OMT_log = []
                                    cancellation_error = 0
                                    kt_order_id_1 = ''
                                else:
                                    print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    loop1 = loop1 + 1
                                    print("looping",loop1)
                                    if (loop1 < 6):
                                        loop_time1 = loop_time1 + 5
                                        time.sleep(loop_time1)
                                    elif (loop1<15) and (loop1>=6):
                                        loop_time1 = loop_time1 + 5
                                        time.sleep(loop_time1)
                                    elif (loop1>=15) and (loop1<26):
                                        loop_time1 = loop_time1 + 5
                                        time.sleep(loop_time1)
                                    val_pending = 1
                                    status = "pending"
                                    if (fresh_position > 0) and (executed < 1) and not retry_order:
                    #                     status = ""
                                        ord_plc = False
                                        OM_log = []
                                        kk = ''
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_pending.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_pending.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_pending.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_pending.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_pending.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                                            gfile.SetContentFile("order_pending.txt")
                                            gfile.Upload()
                                        OM_log = []
                    except Exception as e:
                        order_datafetch_fail = 1
                        print("Failed to fetch order data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                    if not ord_data or order_datafetch_fail:
                        try:
                            print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            if position_datafetch_initial_check  < 1:
                                all_api_failed = 1
                                break
                            position_data =''
                            position_data = s.positions()
                            position_datafetch_fail = 0
                            for i in position_data['day']:
                                if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    executed = 1
                                    ord_plc = False
                                    ord_plc_extra = True
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        colname = ["exit_time", "exit_price","status"]
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")
                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                        except Exception as e:
                            position_datafetch_fail = 1
                            print("Failed to fetch position data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if not position_data or position_datafetch_fail:
                            try:
                                print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if avl_margin_before_trade  < 1:
                                    all_api_failed = 1
                                    break
                                margins_data = s.margins()
                                margins_datafetch_fail = 0
                                if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    executed = 1
                                    ord_plc = False
                                    ord_plc_extra = True
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        colname = ["exit_time", "exit_price","status"]
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")
                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                            except Exception as e:
                                margins_datafetch_fail = 1
                                all_api_failed = 1
                                print("Failed to fetch margin data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
        elif not kt_order_id_1 or order_place_fail:
            try:
                print("Failed to get order id or order place fail so check orders"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                ord_data = ''
                ord_data = s.orders()
                order_datafetch_fail = 0
                for i in ord_data:
                    if i['instrument_token'] == opt_id_1 and i['transaction_type'] == buy_sell:
                        if i['status'] == 'COMPLETE':
                            print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            executed = 1
                            if (fresh_position > 0) and (executed > 0):
                                status = "open"
                                OM_log = []
                                kk = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                    gfile.SetContentFile("order_complete.txt")
                                    gfile.Upload()
                                OM_log = []
                            if (fresh_position < 1) and (executed > 0):
                                status = "open"
                                OM_log = []
                                kk = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_complete.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                    gfile.SetContentFile("order_complete.txt")
                                    gfile.Upload()
                                OM_log = []
                        elif i['status'] == 'REJECTED':
                            print("order rejected"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            reject_count = reject_count + 1
                            if not retry_order and fresh_position > 0:
                                status = "rejected"
                                rejection_error = 1
                                OM_log = []
                                OMT_log = []
                                kk = 0
                                nn = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_reject.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_reject.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_reject.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_reject.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_reject.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                    gfile.SetContentFile("order_reject.txt")
                                    gfile.Upload()
                                if (not retry_order and fresh_position < 1) or retry_order:
                                    rejection_error = 1
                                    status = "rejected"
                                    colname = ["rejection_error","reject_count"]
                                    OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_reject.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_reject.txt")
                                    if bool(kk):
                                        df07 = pd.DataFrame.from_dict(OM_log)
                                        df08 = pd.concat([df63,df07])
                                        df08.to_csv("order_reject.txt", index=False)
                                        update_file = drive.CreateFile({'id': kk})
                                        update_file.SetContentFile("order_reject.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OM_log)
                                        df08.to_csv("order_reject.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_reject.txt"})
                                        gfile.SetContentFile("order_reject.txt")
                                        gfile.Upload()
                                    OM_log = []
                                    OMT_log = []
                                    rejection_error = 0
                                    kt_order_id_1 = ''
                        elif i['status'] == 'CANCELLED':
                            print("order cancelled"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            ord_plc = False
                            cancel_count = cancel_count + 1
                            if not retry_order and fresh_position > 0:
                                status = "cancelled"
                                cancellation_error = 1
                                OM_log = []
                                OMT_log = []
                                kk = 0
                                nn = 0
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                OMT_log.append({'current_signal':current_signal,'entry_time':'','exit_time':'','leg':leg,'instru':instru,'order_id': '','qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':0,'cancellation_error':0,'rejection_error':0,'multiple_sqr_off_error':0,'order_pending_error':0,'multi_sqr_off_error':0,'executed':0,'all_api_failed':0,'leg1_sqr_off_error':0,'leg1_fail_leg2_not_placed':0,'entry_price': price,'strike': int(strike),'contract': contract,'status':'','exit_price':'','expiry':expiry,'trade_id':0,'sqr_off_order':0,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_cancel.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_cancel.txt")
                                if bool(kk):
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_cancel.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_cancel.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_cancel.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                    gfile.SetContentFile("order_cancel.txt")
                                    gfile.Upload()
                            if (not retry_order and fresh_position < 1) or retry_order:
                                cancellation_error = 1
                                status = "cancelled"
                                colname = ["cancellation_error","cancel_count"]
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_cancel.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_cancel.txt")
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    df08 = pd.concat([df63,df07])
                                    df08.to_csv("order_cancel.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_cancel.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_cancel.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_cancel.txt"})
                                    gfile.SetContentFile("order_cancel.txt")
                                    gfile.Upload()
                            OM_log = []
                            OMT_log = []
                            cancellation_error = 0
                            kt_order_id_1 = ''
                        else:
                            print("order pending"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                            loop1 = loop1 + 1
                            print("looping",loop1)
                            if (loop1 < 6):
                                loop_time1 = loop_time1 + 5
                                time.sleep(loop_time1)
                            elif (loop1<15) and (loop1>=6):
                                loop_time1 = loop_time1 + 5
                                time.sleep(loop_time1)
                            elif (loop1>=15) and (loop1<26):
                                loop_time1 = loop_time1 + 5
                                time.sleep(loop_time1)
                            val_pending = 1
                            status = "pending"
                            if (fresh_position > 0) and (executed < 1) and not retry_order:
                    #                     status = ""
                                ord_plc = False
                                OM_log = []
                                kk = ''
                                OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': str(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                kt_order_id_1 = ''
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_pending.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_pending.txt")
                                        print(df63)
                                if bool(kk):
                                    stats = kk
                                    df07 = pd.DataFrame.from_dict(OM_log)
                                    print(df07)
                                    df08 = pd.concat([df63,df07])
                                    print(df08)
                                    df08.to_csv("order_pending.txt", index=False)
                                    update_file = drive.CreateFile({'id': stats})
                                    update_file.SetContentFile("order_pending.txt")
                                    update_file.Upload()
                                else:
                                    df08 = pd.DataFrame.from_dict(OM_log)
                                    df08.to_csv("order_pending.txt", index=False)
                                    gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_pending.txt"})
                                    gfile.SetContentFile("order_pending.txt")
                                    gfile.Upload()
                                OM_log = []

            except Exception as e:
                order_datafetch_fail = 1
                print("Failed to fetch order data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                if not ord_data or order_datafetch_fail:
                    try:
                        print("check position data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if position_datafetch_initial_check  < 1:
                            all_api_failed = 1
                            break
                        position_data =''
                        position_data = s.positions()
                        position_datafetch_fail = 0
                        for i in position_data['day']:
                            if position_datafetch_initial_check and i['instrument_token'] == opt_id_1 and (i['quantity'] != position_datafetch_initial ):
                                executed = 1
                                ord_plc = False
                                # opt_id_1 = 100
                                if (fresh_position > 0) and (executed > 0):
                                    status = "open"
                                    OM_log = []
                                    kk = 0
                                    OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                    kt_order_id_1 = ''
                                    file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                    for index, file in enumerate(file_list):
                                        if(file['title'] =="order_complete.txt"):
                                            kk = file['id']
                                            df29 = file.GetContentFile(file['title'])
                                            df63 = pd.read_csv("order_complete.txt")
                                            print(df63)
                                    if bool(kk):
                                        stats = kk
                                        df07 = pd.DataFrame.from_dict(OM_log)
                                        df08 = pd.concat([df63,df07])
                                        df08.to_csv("order_complete.txt", index=False)
                                        update_file = drive.CreateFile({'id': stats})
                                        update_file.SetContentFile("order_complete.txt")
                                        update_file.Upload()
                                    else:
                                        df08 = pd.DataFrame.from_dict(OM_log)
                                        df08.to_csv("order_complete.txt", index=False)
                                        gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                        gfile.SetContentFile("order_complete.txt")
                                        gfile.Upload()
                                OM_log = []
                            if (fresh_position < 1) and (executed > 0):
                                status = "close"
                                colname = ["exit_time", "exit_price","status"]
                                file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                for index, file in enumerate(file_list):
                                    if(file['title'] =="order_complete.txt"):
                                        kk = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df63 = pd.read_csv("order_complete.txt")
                                    if(file['title'] =="order_sqr_complete.txt"):
                                        nn = file['id']
                                        df29 = file.GetContentFile(file['title'])
                                        df64 = pd.read_csv("order_sqr_complete.txt")
                                if bool(kk):
                                    df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                    df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                    df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                    df63.to_csv("order_complete.txt", index=False)
                                    df64.to_csv("order_sqr_complete.txt", index=False)
                                    update_file = drive.CreateFile({'id': kk})
                                    update_file.SetContentFile("order_complete.txt")
                                    update_file.Upload()
                                    update_file = drive.CreateFile({'id': nn})
                                    update_file.SetContentFile("order_sqr_complete.txt")
                                    update_file.Upload()
                    except Exception as e:
                        position_datafetch_fail = 1
                        print("Failed to fetch position data", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                        if not position_data or position_datafetch_fail:
                            try:
                                print("check margin data"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                if avl_margin_before_trade  < 1:
                                    all_api_failed = 1
                                    break
                                margins_data = s.margins()
                                margins_datafetch_fail = 0
                                if avl_margin_before_trade and abs(avl_margin_before_trade - margins_data['equity']['available']['live_balance']) > 50:
                                    print("order executed"," ", datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                    executed = 1
                                    ord_plc = False
                                    ord_plc_extra = True
                                    if (fresh_position > 0) and (executed > 0):
                                        status = "open"
                                        OM_log = []
                                        kk = 0
                                        OM_log.append({'current_signal':current_signal,'entry_time':datetime.datetime.now(pytz.timezone('Asia/Kolkata')),'exit_time':'','leg':leg,'instru':instru,'order_id': kt_order_id_1,'qty':quantity,'price_when_order_placed': price_opt_1,'fresh_position': fresh_position,'buy_sell': buy_sell,'instrument_id':opt_id_1,'trading_symbol':symbol_opt_1,'modification_error':modification_error,'cancellation_error':cancellation_error,'rejection_error':rejection_error,'multiple_sqr_off_error':multiple_sqr_off_error,'order_pending_error':order_pending_error,'multi_sqr_off_error':multi_sqr_off_error,'executed':executed,'all_api_failed':0,'leg1_sqr_off_error':leg1_sqr_off_error,'leg1_fail_leg2_not_placed':leg1_fail_leg2_not_placed,'entry_price': price,'strike': int(strike),'contract': contract,'status':status,'exit_price':'','expiry':expiry,'trade_id':trade_id,'sqr_off_order':sqr_off_order,'reject_count':reject_count,'cancel_count':cancel_count,'sqr_order_id':0})
                                        kt_order_id_1 = ''
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                                print(df63)
                                        if bool(kk):
                                            stats = kk
                                            df07 = pd.DataFrame.from_dict(OM_log)
                                            df08 = pd.concat([df63,df07])
                                            df08.to_csv("order_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': stats})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                        else:
                                            df08 = pd.DataFrame.from_dict(OM_log)
                                            df08.to_csv("order_complete.txt", index=False)
                                            gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : "order_complete.txt"})
                                            gfile.SetContentFile("order_complete.txt")
                                            gfile.Upload()
                                        OM_log = []
                                    if (fresh_position < 1) and (executed > 0):
                                        status = "close"
                                        kk = 0
                                        nn = 0
                                        colname = ["exit_time", "exit_price","status"]
                                        file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
                                        for index, file in enumerate(file_list):
                                            if(file['title'] =="order_complete.txt"):
                                                kk = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df63 = pd.read_csv("order_complete.txt")
                                            if(file['title'] =="order_sqr_complete.txt"):
                                                nn = file['id']
                                                df29 = file.GetContentFile(file['title'])
                                                df64 = pd.read_csv("order_sqr_complete.txt")
                                        if bool(kk):
                                            df63.loc[(df63.leg==leg), colname] = [datetime.datetime.now(pytz.timezone('Asia/Kolkata')),price,"close"]
                                            df64.loc[len(df64)] = df63.iloc[df63.index[(df63.leg==leg)].values[0]]
                                            df63 = df63.drop(df63.index[(df63.leg==leg)].values[0])
                                            df63.to_csv("order_complete.txt", index=False)
                                            df64.to_csv("order_sqr_complete.txt", index=False)
                                            update_file = drive.CreateFile({'id': kk})
                                            update_file.SetContentFile("order_complete.txt")
                                            update_file.Upload()
                                            update_file = drive.CreateFile({'id': nn})
                                            update_file.SetContentFile("order_sqr_complete.txt")
                                            update_file.Upload()
                            except Exception as e:
                                margins_datafetch_fail = 1
                                all_api_failed = 1
                                print("Failed to fetch margin data",e, datetime.datetime.now(pytz.timezone('Asia/Kolkata')), file=sys.stderr)
                                break
    return executed,val_pending
