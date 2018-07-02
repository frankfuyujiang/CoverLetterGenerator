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
ps=PorterStemmer()
stop_words = set(stopwords.words("english"))
mystop_words=["\'ll","position","work","job","role","year","valley","skill","day","summary","must","salary",'ready','great','enriched','include','top','position','500','fortune','large','set','include','reasonable','providing','decent','like','using','along',]
jobDesStopWords=stop_words.union(mystop_words)

weighedKeyWords = {'python':10}
template={'experience':["I worked at SAP for almost 3 years. While working there, I worked with fortune 500 companies like Coca-cola as a development support engineer by helping them with customization and consulting issues."],
			'data':["In my academic years, I completed many projects involving data cleansing, plotting, simulation and extrapolation using Matlab and Python.",
			"I obtained my certificate offered by Microsoft in \"Programming with Python for Data Science\" where I practiced with real datasets and real problem and achieved 91% upon obtaining the certificate."],
			'analytic':["I also applied data analysis to the sales data of a local business I owned and came up with new promotion based on the model. This new strategy has led to a 30% increment in the monthly revenue."],
			'degree':["I graduated from Queen's University in Canada with a degree of Specialization in Biomedical Computing."]}

#tokenize into sentences and then words
sents = sent_tokenize(data)
words = []
for s in sents:
	words += word_tokenize(s)

#filter words 
filtered_words = []
words = [w.lower() for w in words]
for w in words:
	w = lemma.lemmatize(w);
	if w not in string.punctuation and w not in jobDesStopWords:
		filtered_words.append(w)
#print (unlemmatized)
#print(filtered_words)

fdist = FreqDist(filtered_words)
top_200 = fdist.most_common(200)



print(top_200)
test=['abc','bcd'];
test.extend(['efg']*10);
print(test)

name=input('What is your name? ')
jobPosition=input('What is your job position? ')
companyName=input('What is the company\'s name? ')
numbered_Top200 = []
for i in range(0,len(top_200)):
	numberedkword=str(i+1)+" "+str(top_200[i][0])
	print(numberedkword)
	#numbered_Top200.append(str(i+1)+". "+str(top_200[i][0]))
#print(numbered_Top200);
keywords=input('Please select select the corresponding number for the word separated by comma with no space. ');
keywords=keywords.split(',');
textbody="";
for s in keywords:
	keyword=top_200[int(s)-1][0]
	if keyword in template:
		textbody=textbody+(template[keyword][0])+" "
	else:
		print("keyword {0} is not in template, please fix your template".format(keyword));

coverletter=("Dear Recruiting Manager, \nMy name is " +name+", I am writing this letter to express my interest in the "+jobPosition+" position available at "+companyName+
	    ". As I thoroughly reading through the job description, I feel that with my knowledge and experience, I will be an excellent candidate for this position.\n"+ textbody +
		"\nI am a person who likes to be challenged and to be given responsibility. It would be my pleasure to grow together alongside with the company. With all my unique "+
		"experience and technical backgrounds, I believe I am a great candidate for this "+jobPosition+" position. \nI therefore hope we could have the chance to discuss about "+
		"this opportunity further in an interview session.\nSincerely, \n\n"+name)
print(coverletter)



