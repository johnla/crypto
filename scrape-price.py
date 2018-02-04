from pymongo import MongoClient
client = MongoClient("mongodb://www.m0d.com:27017")
db = client.crypto
# print str(db.coins.find().count()) + ' coins'

print 'found '+str(db.coins.find({'coin_id':'bitcoin'}).count())+' bitcoin'
for coin in db.coins.find({'coin_id':'bitcoin'}):
  coin_id = coin['coin_id']
  print coin
  