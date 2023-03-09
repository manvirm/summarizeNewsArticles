import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Download model
nltk.download('punkt')

url = 'https://www.bbc.com/news/world-middle-east-64631354'

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

# Sentiment Analysis
analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

# GUI 
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x1600')

# Display title, author, published data

tlabel = tk.Label(root, text = "Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.pack()

alabel = tk.Label(root, text = "Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Published Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state= 'disabled', bg='#dddddd')
publication.pack()

root.mainloop()