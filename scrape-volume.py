# import libraries
import urllib2
from bs4 import BeautifulSoup

import json

from pymongo import MongoClient
from datetime import datetime
# client = MongoClient()
client = MongoClient("mongodb://www.m0d.com:27017")
db = client.crypto
# client = MongoClient("mongodb://mongodb0.example.net:27017")

from pymongo import MongoClient
client = MongoClient("mongodb://www.m0d.com:27017")
db = client.crypto  

coins_page = 'https://api.coinmarketcap.com/v1/ticker/'
# query the website and return the html to thfe variable page
# coin_page_data = urllib2.urlopen(coin_page)
print 'Scraping ' + coins_page
coins_page_data = json.load(urllib2.urlopen(coins_page))

for f in coins_page_data:
  if (db.coins.find({'coin_id':f['id']}).count() > 0):
    # print 'adding '+f['id']
    # adding coin data
    result = db.volumes.insert_one(
        {
            "coin_id": f['id'],
            "24h_volume_usd": f['24h_volume_usd'],
            "market_cap_usd": f['market_cap_usd'],
            "rank": f['rank'],
            "percent_change_24h": f['percent_change_24h'],
            "percent_change_7d": f['percent_change_7d'],
            "source": 'coinmarketcap',
            "source_updated": f['last_updated'],
            "datetime_added":datetime.utcnow()
        }
    )
  else:
    print f['id'] + ' not found.'