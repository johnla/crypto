#terminal: export GOOGLE_APPLICATION_CREDENTIALS="/Users/johnla/Downloads/crypto-f2dd7bf5497c.json"

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Tron gets caught again, Plagiarised White Paper, Now its Copy&Pasting Codes.'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# # Detects the sentiment of the text
# sentiment = client.analyze_sentiment(document=document).document_sentiment
#
# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


def classify_text(text):
    """Classifies content categories of the provided text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))

classify_text(text)

