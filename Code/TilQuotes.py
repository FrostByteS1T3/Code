from GetQuoteTil import get_til_quote
import time
from os import system
system('clear')
def print_quotes():
        print get_til_quote()
        print '---------------------------------------------------------------'
while True:
    print_quotes()
    time.sleep(30)
