import ccxt
import json

json_data=open("config/keys.json").read()

keys = json.loads(json_data)
print(keys['binance']['key'])

# hitbtc = ccxt.hitbtc({'verbose': True})
# bitmex = ccxt.bitmex()
# huobi  = ccxt.huobi()
# exmo   = ccxt.exmo({
#     'apiKey': 'YOUR_PUBLIC_API_KEY',
#     'secret': 'YOUR_SECRET_PRIVATE_KEY',
# })
# kraken = ccxt.kraken({
#     'apiKey': 'YOUR_PUBLIC_API_KEY',
#     'secret': 'YOUR_SECRET_PRIVATE_KEY',
# })

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': keys['binance']['key'],
    'secret': keys['binance']['secret'],
    'timeout': 30000,
    'enableRateLimit': True,
})

# # hitbtc_markets = hitbtc.load_markets()
# exchange_markets = exchange.load_markets()
print(exchange.fetch_ticker('BTC/USDT'))
# # print(exchange.id, exchange_markets)
# # print(bitmex.id, bitmex.load_markets())
# # print(huobi.id, huobi.load_markets())

# # print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
# # print(bitmex.fetch_ticker('BTC/USD'))
# # print(huobi.fetch_trades('LTC/CNY'))

# print(exchange.fetch_balance())

# # sell one ฿ for market price and receive $ right now
# # print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))

# # limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
# # print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))

# # pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
# # kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})