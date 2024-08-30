from textblob import textblob
from newspaper import Article

# url = "https://www.bbc.com/news/ul-england-london-52963555
# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

with open('text.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
