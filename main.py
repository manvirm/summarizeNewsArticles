import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import article

# Download model
nltk.download('punkt')

url = ''

# Pass url into article, creating an article object focused on url
article = Article(url)

# Download and parse data
article.download()
article.parse()

# Natural language processing
article.nlp()

print(f'Title {article.title}')
print(f'Authors {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')