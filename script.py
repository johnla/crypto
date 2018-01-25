import json
import urllib 
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
# client = MongoClient("mongodb://mongodb0.example.net:27017")
db = client.test
# db.dataset
# db['dataset']
# coll = db.dataset
# coll = db['dataset']

url = 'https://api.coinmarketcap.com/v1/ticker/'
response = urllib.urlopen(url)
data = json.loads(response.read())
# print data
for f in data:
  try:
    ##
    ## Add price data
    ##
    result = db.prices.insert_one(
        {
            "coin_id": f['name'],
            "price_usd":f['price_usd'],
            "price_btc":f['price_btc'],
            "market_cap_usd":f['market_cap_usd'],
            "24h_volume_usd":f['24h_volume_usd'],
            "available_supply":f['available_supply'],
            "total_supply":f['total_supply'],
            "percent_change_1h":f['percent_change_1h'],
            "percent_change_24h":f['percent_change_24h'],
            "percent_change_7d":f['percent_change_7d'],
            "last_updated":datetime.utcnow()
        }
    )
    
    ##
    ## Remove crypto extra fields
    ##
    # db.crypto.update({}, {'$unset': {'24h_volume_usd':1, 'available_supply':1, 'total_supply':1, 'percent_change_1h':1, 'percent_change_24h':1, 'percent_change_7d':1}} , multi=True);
    
    ##
    ## Update crypto records
    ##
    # db.crypto.update_one(
    #     {"name": f['name']},
    #     {
    #     "$set": {
    #         "id":f['id'],
    #         "symbol":f['symbol'],
    #         "max_supply":f['max_supply'],
    #         "last_updated":datetime.utcnow()
    #     }
    #     }
    # )

  except Exception, e:
    print str(e)