from Bitcoin import get_price
import time
run = raw_input('See bitcoin price [y/n] ').lower()
if run == 'y':
    while True:
        get_price()
        print '-----------'
        time.sleep(15)
