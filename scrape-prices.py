# import libraries
import urllib2
from bs4 import BeautifulSoup

import json
import config
import scrape_coin
from pymongo import MongoClient
from datetime import datetime
# client = MongoClient()
client = MongoClient("mongodb://"+config.mongodb_cred['uri'] +":"+config.mongodb_cred['port'])
db = client.crypto
# client = MongoClient("mongodb://mongodb0.example.net:27017")

coins_page = 'https://api.coinmarketcap.com/v1/ticker/'
# query the website and return the html to thfe variable page
# coin_page_data = urllib2.urlopen(coin_page)
print 'Scraping ' + coins_page
coins_page_data = json.load(urllib2.urlopen(coins_page))

for f in coins_page_data:
  if (db.coins.find({'coin_id':f['id']}).count() > 0):
    # print 'adding '+f['id']
    # adding coin data
    result = db.prices.insert_one(
        {
            "coin_id": f['id'],
            "price_usd": f['price_usd'],
            "price_btc": f['price_btc'],
            "percent_change_1h": f['percent_change_1h'],
            "source": 'coinmarketcap',
            "source_updated": f['last_updated'],
            "datetime_added":datetime.utcnow()
        }
    )
  else:
    print f['id'] + ' not found.'
    scrape_coin.scrapeCoin(f['id'])
