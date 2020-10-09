<<<<<<< HEAD
import nltk, urllib.request, re
=======
import nltk
import urllib.request
import re
>>>>>>> 35f01ce88a0c2ade734b76890c3e18a12d7c0a0d
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://pt.wikipedia.org/wiki/SpaceX')
html = response.read()

soup = BeautifulSoup(html,'lxml')
text = soup.get_text(strip = True)
text = text.lower()

text = re.sub(r'[^\w\s]', ' ', text)
text = re.sub("\d+", ' ', text)

tokens = [t for t in text.split()]

clean_tokens = []
stopwords = nltk.corpus.stopwords.words('portuguese')
for token in tokens:
    if token not in stopwords and len(token) < 20:
        clean_tokens.append(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)