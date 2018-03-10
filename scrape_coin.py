# from lxml import html
# import requests
#
# page = requests.get('https://www.reddit.com/r/CryptoCurrency/')
# tree = html.fromstring(page.content)
# #This will create a list of buyers:
# titles = tree.xpath('//a[@class="title"]/text()')
# print 'Reddit Titles: ', titles


# Imports the Google Cloud client library
# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types

# Instantiates a client
# client = language.LanguageServiceClient()

import config

# import libraries
import urllib2
from bs4 import BeautifulSoup

# Regex
import re
import json

from pymongo import MongoClient
from datetime import datetime
# client = MongoClient()
client = MongoClient("mongodb://"+config.mongodb_cred['uri'] +":"+config.mongodb_cred['port'])
db = client.crypto

  
def scrapeCoin( coin_id ):
   print "scrapeCoin: " + coin_id
   coin_page = 'https://api.coinmarketcap.com/v1/ticker/'+coin_id
   coin_page_data = json.load(urllib2.urlopen(coin_page))
   print coin_page_data
   print coin_page_data[0]['price_usd']
   # adding coin data
   result = db.coins.insert_one(
       {
           "coin_id": coin_id,
           "available_supply": coin_page_data[0]['available_supply'],
           "total_supply": coin_page_data[0]['total_supply'],
           "max_supply": coin_page_data[0]['max_supply'],
           "source": 'coinmarketcap',
           "source_updated": coin_page_data[0]['last_updated'],
           "datetime_added":datetime.utcnow()
       }
   )
   # adding real data
   result = db.volume.insert_one(
       {
           "coin_id": coin_id,
           "rank": coin_page_data[0]['rank'],
           "available_supply": coin_page_data[0]['available_supply'],
           "total_supply": coin_page_data[0]['total_supply'],
           "max_supply": coin_page_data[0]['max_supply'],
           "24h_volume_usd": coin_page_data[0]['24h_volume_usd'],
           "market_cap_usd": coin_page_data[0]['market_cap_usd'],
           "percent_change_1h": coin_page_data[0]['percent_change_1h'],
           "percent_change_24h": coin_page_data[0]['percent_change_24h'],
           "percent_change_7d": coin_page_data[0]['percent_change_7d'],
           "source": 'coinmarketcap',
           "source_updated": coin_page_data[0]['last_updated'],
           "datetime_added":datetime.utcnow()
       }
   )
