import json
import time
import os
import ccxt
import json
from datetime import datetime

#----------------------------------------------
#          Base Class Of Trading Bot
#----------------------------------------------

class Bot:
    _name      = None
    _exchange  = None
    _interval  = None
    _run       = True
    _config    = None

    def __init__(self, config):
        self._name      = "Base Bot"
        self._config    = config
        self._interval  = config['interval']
        self.setExchange(config['exchange'])
    
    def getName(self):
        return self._name

    def setExchange(self, exchange):
        exchange_id = exchange.lower()
        json_data=open("./config/keys.json").read()
        keys = json.loads(json_data)
        try:
            exchange_class = getattr(ccxt, exchange_id)
            self._exchange = exchange_class({
                'apiKey': keys[exchange_id]['key'],
                'secret': keys[exchange_id]['secret'],
                'timeout': 30000,
                'enableRateLimit': True,
            })
        except: 
            raise Exception("Error setting exchange")

    def getExchange(self):
        return self._exchange

    def trade(self):
        # Print Start Trading Message
        print(str(datetime.now()) + ": Bot Started Trading.\n")
        # Run
        while self._run:
            #Get Market Summary
            # data   = self._exchange.getSummary()
            #Analyze What To Do Based On Market Data
            # action = self._algorithm.analyze(data)
            #Set Record In The Log
            record = self.log('buy', 1000)
            print(record + "\n")
            time.sleep(self._interval)

    def stop(self):
        print(str(datetime.now()) + ": Bot Stopped Trading.\n")
        self._run = False

    def log(self, action, price):
        now = datetime.now()
        filename = os.getcwd() + '/logs/_log_' + self._config['exchange'] + '_' + str(now.day) + '_' + str(now.month) + '_' + str(now.year) + '.txt'
        
        if os.path.exists(filename):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        file = open(filename,append_write) 
        text = str(now) + ' - ' + action.upper() + ', Price: ' + str(price)
        file.write(text + '\n') 
        file.close()
        return text
