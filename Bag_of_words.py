

import pandas as pd
import numpy as np
import nltk
import re


file = open("WikiQ.txt")
data= file.read()

sentences = nltk.sent_tokenize(data)  
words = nltk.word_tokenize(data)
#tokeniztion


from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))

filter_words=[]
for x in words:
    if x not in stop_words:
        filter_words.append(x)
print(filter_words)

# stopwords were filtered


for i in range(len(filter_words)):
    filter_words[i]= filter_words[i].lower()
    filter_words[i] = re.sub(r'\W','', filter_words[i])
    filter_words[i] = re.sub(r'[0-9]','', filter_words[i])
print(filter_words)

wordList= list(filter(None, filter_words))
print(wordList)

#Removed number,symbols and spaces

def CountFrequency(wordList):
    count = {}
    for i in wordList:
        count[i] = count.get(i, 0) + 1
    return count
print(CountFrequency(wordList))

frequency=list(CountFrequency(wordList).items())
print(frequency)
# converted from dictionary to list

df=pd.DataFrame(frequency,columns=['Word','Frequency'])
df
df.to_csv('bag_of_words.csv',index=False)
        
