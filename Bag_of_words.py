
import pandas as pd
import numpy as np
import nltk
import re

file = open("WikiQ.txt")
data= file.read()


sentences = nltk.sent_tokenize(data)  
words = nltk.word_tokenize(data)
print(words)


from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))


filter_words=[]
for x in words:
    if x not in stop_words:
        filter_words.append(x)
print(filter_words)


for i in range(len(filter_words)):
    filter_words[i]= filter_words[i].lower()
    filter_words[i] = re.sub(r'\W','', filter_words[i])
    filter_words[i] = re.sub(r'[0-9]','', filter_words[i])
print(filter_words)

wordList= list(filter(None, filter_words))
print(wordList)

#remove space,numbers and punctuation from list


fre=[]
for w in wordList:
        fre.append(wordList.count(w))
frequency=list(zip(wordList,fre))

df=pd.DataFrame(frequency,columns=['Word','Frequency'])
df


df.to_csv('bag_of_words.csv',index=False)
        





