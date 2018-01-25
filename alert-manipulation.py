import json
import urllib 
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

url = 'https://api.coinmarketcap.com/v1/ticker/'
response = urllib.urlopen(url)
data = json.loads(response.read())
# print data

for f in data:
  try:
    ##
    ## Add price data
    ##
    # result = db.volume.insert_one(
    #     {
    #         "coin_id": f['name'],
    #         "price_usd":f['price_usd'],
    #         "price_btc":f['price_btc'],
    #         "market_cap_usd":f['market_cap_usd'],
    #         "24h_volume_usd":f['24h_volume_usd'],
    #         "available_supply":f['available_supply'],
    #         "total_supply":f['total_supply'],
    #         "percent_change_1h":f['percent_change_1h'],
    #         "percent_change_24h":f['percent_change_24h'],
    #         "percent_change_7d":f['percent_change_7d'],
    #         "velocity_last":f['velocity_last'],
    #         "velocity_24h":f['velocity_last'],
    #         "last_updated":datetime.utcnow()
    #     }
    # )
    i = 0
    if i < 6:
      print(f['name'])
      print(f['price_usd'])
      print(f['price_btc'])
      print(f['24h_volume_usd'])
      print(f['market_cap_usd'])
      print(f['available_supply'])
      print(f['total_supply'])
      print(f['max_supply'])
      print(f['percent_change_1h'])
      print(f['percent_change_24h'])
      print(f['percent_change_7d'])
      print(f['last_updated']) 
      print ''
      i += 1
    
    # pprint.pprint(posts.find_one({"_id": post_id}))
    # {u'_id': ObjectId('...'),
    #  u'author': u'Mike',
    #  u'date': datetime.datetime(...),
    #  u'tags': [u'mongodb', u'python', u'pymongo'],
    #  u'text': u'My first blog post!'}
    
    
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