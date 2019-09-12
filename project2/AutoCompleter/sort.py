import operator
from fuzzywuzzy import process
wordlist=[]
word_count={}
with open('word_search.tsv') as data:       #opning the tsv file as databases
     for x in data:
         word,count=x.split("\t")          #spliting the word and occurence
         wordlist.append(word)
         word_count[word]=int(count.strip()) #removing extra spaces and converting into int type and adding

#checking wheather the word in words
def search(val):
    result=[]
    for word in wordlist:
        if val in word:
            result.append(word)
    return result


def sorting(results,incomplete_word,limit=25):
    results=process.extract(incomplete_word,results,limit=limit)
    return results
