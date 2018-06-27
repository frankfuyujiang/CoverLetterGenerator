import nltk
import os
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

#get input text 
dirpath = os.getcwd() + "/Job Summary.txt"
data = state_union.raw(dirpath)

#initialize utilities
lemma = nltk.wordnet.WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
mystop_words=["\'ll","position","work","job","role","year","valley","skill","day","summary","must"]
jobDesStopWords=stop_words.union(mystop_words)

#tokenize into sentences and then words
sents = sent_tokenize(data)
words = []
for s in sents:
	words += word_tokenize(s)

#filter words 
filtered_words = []
unlemmatized = []
words = [w.lower() for w in words]
for w in words:
	if w not in string.punctuation and w not in jobDesStopWords:
		unlemmatized.append(w)
		filtered_words.append(lemma.lemmatize(w))
#print (unlemmatized)
#print(filtered_words)

fdist = FreqDist(filtered_words)
top_ten = fdist.most_common(60)

print(top_ten)