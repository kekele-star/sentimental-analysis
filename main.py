from textblob import textblob
from newspaper import Article

url = "https://en.wikipedia.org/wiki/Computer_science"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)