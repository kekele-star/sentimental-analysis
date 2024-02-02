from textblob import textblob
from newspaper import Article

url = ""
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)