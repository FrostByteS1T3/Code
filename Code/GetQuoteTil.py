def get_til_quote():
    import requests
    import time
    import json
    url = 'https://www.reddit.com/r/todayilearned/new/.json'
    response = requests.get(url, headers = {'User-agent': 'TilBot'})
    text_data = response.text
    quote = text_data[text_data.find('\"title\":'):text_data.find('\"link_flair_richtext\"') - 1]
    trimmed = quote.replace('\"title\": ', '')
    print trimmed
    return trimmed
