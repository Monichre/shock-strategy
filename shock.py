#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import time

import requests
from kumex.client import Trade


def get_kline(s, r, f, t, timeout=5, is_sandbox=False):
    headers = {}
    url = 'https://kitchen.kumex.com/kumex-kline/history'
    if is_sandbox:
        url = 'https://kitchen-sdb.kumex.com/kumex-kline/history'
    uri_path = url
    data_json = ''
    p = []
    if s:
        p.append("{}={}".format('symbol', s))
    if r:
        p.append("{}={}".format('resolution', r))
    if f:
        p.append("{}={}".format('from', f))
    if t:
        p.append("{}={}".format('to', t))
    data_json += '&'.join(p)
    uri_path += '?' + data_json

    response_data = requests.request('GET', uri_path, headers=headers, timeout=timeout)
    return check_response_data(response_data)


def check_response_data(response_data):
    if response_data.status_code == 200:
        try:
            d = response_data.json()
        except ValueError:
            raise Exception(response_data.content)
        else:
            if d and d.get('s'):
                if d.get('s') == 'ok':
                    return d
                else:
                    raise Exception("{}-{}".format(response_data.status_code, response_data.text))
    else:
        raise Exception("{}-{}".format(response_data.status_code, response_data.text))


if __name__ == "__main__":
    # read configuration from json file
    with open('config.json', 'r') as file:
        config = json.load(file)

    symbol = config['symbol']
    resolution = config['resolution']
    valve = config['valve']
    api_key = config['api_key']
    api_secret = config['api_secret']
    api_passphrase = config['api_passphrase']
    leverage = config['leverage']
    size = config['size']
    sandbox = config['is_sandbox']
    trade = Trade(api_key, api_secret, api_passphrase, is_sandbox=sandbox)

    while 1:
        time_to = int(time.time())
        time_from = time_to - resolution * 60 * 35
        data = get_kline(symbol, resolution, time_from, time_to, is_sandbox=sandbox)
        print('now time =', time_to)
        print('symbol closed time =', data['t'][-1])
        if time_to != data['t'][-1]:
            continue
        now_price = data['c'][-1]
        print('closed price =', now_price)
        # high_track
        high_track = data['h'][-31:-1]
        high_track.sort(reverse=True)
        print('high_track =', high_track[0])
        # low_track
        low_track = data['l'][-31:-1]
        low_track.sort()
        print('low_track =', low_track[0])
        # interval_range
        interval_range = (high_track[0] - low_track[0]) / (high_track[0] + low_track[0])
        print('interval_range =', interval_range)

        order_flag = 0
        # current position qty of the symbol
        position_details = trade.get_position_details(symbol)
        print('current position qty of the symbol =', position_details['currentQty'])
        if position_details['currentQty'] > 0:
            order_flag = 1
        elif position_details['currentQty'] < 0:
            order_flag = -1

        if order_flag == 1 and now_price < low_track[0]:
            order = trade.create_limit_order(symbol, 'sell', position_details['realLeverage'],
                                             position_details['currentQty'], now_price)
            print('order_flag == 1,order id =', order['orderId'])
            order_flag = 0
        elif order_flag == -1 and now_price > high_track[0]:
            order = trade.create_limit_order(symbol, 'buy', position_details['realLeverage'],
                                             position_details['currentQty'], now_price)
            print('order_flag == -1,order id =', order['orderId'])
            order_flag = 0

        if interval_range < valve and order_flag == 0:
            if now_price > high_track[0]:
                order = trade.create_limit_order(symbol, 'buy', leverage, size, now_price)
                print('now price > high track,buy order id =', order['orderId'])
                order_flag = 1
            if now_price < high_track[0]:
                order = trade.create_limit_order(symbol, 'sell', leverage, size, now_price)
                print('now price < high track,sell order id =', order['orderId'])
                order_flag = -1
