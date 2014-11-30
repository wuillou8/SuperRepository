'''
	Python script doing tokenisation, case removal, stemming and filtering the stopwords.
        Notice that snowball is an "agressive" stemmer (losses).
'''

import nltk, csv, string
from nltk.stem import snowball
snowball = nltk.stem.SnowballStemmer('english')

from nltk.corpus import stopwords
stop=set(stopwords.words('english'))

''' treatment (should be enough, I have left the numbers)'''
#sentence could be read from file. In case of several lines, use reduce as on line 30
#if desired to pass the stemmer a long string. 
sentence = "The parser is now stricter with respect to multi-line quoted fields. \
Previously, if a line ended within a quoted field without a terminating newline character." 
#tokenize and rm punctuation
tknwrd = nltk.word_tokenize(sentence.translate(None, string.punctuation))
#remove stopwords
tknwrd = filter(lambda x: x not in stop,map(lambda x: x.lower(), tknwrd))
#stemming architects -> architect
tknwrd = map(lambda x: snowball.stem(x),tknwrd)
#output1
print tknwrd
#output2
print reduce(lambda x, y: x +','+y, tknwrd)
#output3
for i in tknwrd:
    print i
