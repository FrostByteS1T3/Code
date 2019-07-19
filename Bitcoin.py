def get_price():
    import json
    import requests
    bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    response = requests.get(bitcoin_api_url)
    if response.status_code == 200:
        print 'Success'
    elif response.status_code == 404:
        print 'not found'
    data = response.text
    price = data[132:140]
    print '$' + price
    return price
