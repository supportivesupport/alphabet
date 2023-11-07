import random
import logging

logging.basicConfig(level=logging.INFO, filemode='a', filename="log.log")
Logger = logging.getLogger(__name__)
a = random.randint(1, 300)
Logger.info(f"{a}")
b = random.randint(1, 200)
Logger.info(f"{b}")
c = random.randint(1, 100)
Logger.info(f"{c}")
d = (a + b + c) / 13
Logger.info(f"{d}")
e = d % 2
Logger.info(f"{e}")
f = e ** 3
Logger.info(f"{f}")
g = f % 10 * 100000
Logger.info(g)
h = int(g) + random.randint(1, 10)
Logger.info(h)
