def price():
    from Bitcoin import get_price
    import time
    run = raw_input('See bitcoin price [y/n] ').lower()
    if run == 'y':
        while True:
            get_price()
            print '-----------'
            price = get_price()
            time.sleep(15)
            return price
price()
