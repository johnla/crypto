# from lxml import html
# import requests
#
# page = requests.get('https://www.reddit.com/r/CryptoCurrency/')
# tree = html.fromstring(page.content)
# #This will create a list of buyers:
# titles = tree.xpath('//a[@class="title"]/text()')
# print 'Reddit Titles: ', titles


# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.reddit.com/r/CryptoCurrency/'

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
name_box = soup.find_all('a', attrs={'data-event-action': 'title'})
for row in soup.find_all('a', attrs={'data-event-action': 'title'}):
  title = row.text.strip() # strip() is used to remove starting and trailing
  print title
  
  document = types.Document(
      content=title,
      type=enums.Document.Type.PLAIN_TEXT)
  # # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(document=document).document_sentiment

  print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

# # get the index price
# price_box = soup.find('div', attrs={'class':'price'})
# price = price_box.text
# print price