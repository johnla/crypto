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

# import libraries
import urllib2
from bs4 import BeautifulSoup

# Regex
import re
import json

from pymongo import MongoClient
from datetime import datetime
# client = MongoClient()
client = MongoClient("mongodb://www.m0d.com:27017")
db = client.crypto
# client = MongoClient("mongodb://mongodb0.example.net:27017")

# specify the url
quote_page = 'https://coinmarketcap.com/all/views/all/'

# query the website and return the html to the variable page
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable soup
soup = BeautifulSoup(page, 'html.parser')

# all_tables=soup.find_all('a')
#
# # right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
# # right_table
#
# print all_tables

# Take out the <div> of name and get its value
coin_data = soup.find_all('td', attrs={'class': 'currency-name'})
i = 1;
for row in coin_data:
  
  coin_text = row.text.strip() # strip() is used to remove starting and trailing
  
  # matchObj = re.match( r'<a href="(.*)">', str(row), re.M|re.I)
 
  # m = re.search('<a href=".*">(.+)</a>.+<a class="currency-name-container" href=".+">(.+)</a>'.decode('utf-8'), str(row).decode('utf-8'), re.M|re.I)
  # print m.groups
  # print m.group(0)
  # print m.group(1)
  
  # if matchObj:
  #    print "matchObj.group() : ", matchObj.group()
  #    print "matchObj.group(1) : ", matchObj.group(1)
  #    print "matchObj.group(2) : ", matchObj.group(2)
  # print coin_text
  m2 = re.search('href="/currencies/(.+)/"', str(row).strip('\n'))  
  m = re.search('(.+)\n+(.+)\n*(.+)?', coin_text, re.I | re.M )
  coin_symbol = m.group(1)
  coin_name = m.group(2)
  coin_id = m2.group(1)
  
  print str(i) + ') coin_name: ' + coin_name + ', coin_symbol: ' + coin_symbol + ', coin_id: ' + coin_id
  i += 1
  
  
  coin_page = 'https://api.coinmarketcap.com/v1/ticker/'+coin_id+'/'
  # query the website and return the html to thfe variable page
  # coin_page_data = urllib2.urlopen(coin_page)
  print 'Scraping '+coin_page
  coin_page_data = json.load(urllib2.urlopen(coin_page))

  # parse the html using beautiful soup and store in variable soup
  # coin_soup = BeautifulSoup(coin_page_data, 'html.parser')
  # coin_deepdata = coin_soup.find_all('td', attrs={'class': 'currency-name'})
  for f in coin_page_data:
    
    print 'found '+str(db.coins.find({'coin_id':coin_id}).count())+' bitcoin'
    
    if (db.coins.find({'coin_id':coin_id}).count() == 0):
        # adding coin data
        result = db.coins.insert_one(
            {
                "coin_id": coin_id,
                "available_supply": f['available_supply'],
                "total_supply": f['total_supply'],
                "max_supply": f['max_supply'],
                "source": f['coinmarketcap'],
                "source_updated": f['last_updated'],
                "datetime_added":datetime.utcnow()
            }
        )
    
        # adding real data
        result = db.volume.insert_one(
            {
                "coin_id": coin_id,
                "rank": f['rank'],
                "available_supply": f['available_supply'],
                "total_supply": f['total_supply'],
                "max_supply": f['max_supply'],
                "24h_volume_usd": f['24h_volume_usd'],
                "market_cap_usd": f['market_cap_usd'],
                "percent_change_1h": f['percent_change_1h'],
                "percent_change_24h": f['percent_change_24h'],
                "percent_change_7d": f['percent_change_7d'],
                "source": 'coinmarketcap',
                "source_updated": f['last_updated'],
                "datetime_added":datetime.utcnow()
            }
        )
    