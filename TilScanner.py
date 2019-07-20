import requests
import json
from os import system
system('clear')
url = 'https://www.reddit.com/r/todayilearned/new/.json'
response = requests.get(url, headers = {'User-agent': 'TilBot'})
text_data = response.text
#if '\"title\"' in text_data:
    #print text_data
    #print text_data.find('\"title\"')
    #print text_data.find('\"link_flair_richtext\"')
    #print text_data[text_data.find('\"title\":'):text_data.find('\"link_flair_richtext\"')]
#else:
    #print text_data
quote = text_data[text_data.find('\"title\":'):text_data.find('\"link_flair_richtext\"') - 1]
trimmed = quote.replace('\"title\": ', '')
print trimmed
