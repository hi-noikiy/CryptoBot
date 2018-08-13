import sys
from bots.bot import Bot

print(sys.argv)
print(sys.argv[1])
print(sys.argv[2])

config = {
    'exchange': sys.argv[1],
    'interval' : int(sys.argv[2])
}

bot = Bot(config)

bot.trade()