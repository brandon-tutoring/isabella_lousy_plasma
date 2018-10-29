import string
import random

def remove_punctuation(var):
    no_punct = ""
    for item in var:
        if item not in string.punctuation:
            no_punct += item
    return no_punct




# no longer in use.
'''def lousy_plasma():
    empty_string = ""          
    input1 = input("what is your sentence?").strip()
    input1 = remove_punctuation(input1).split( )
    for item in input1:
        if item in dict1.keys():
            empty_string += random.choice(dict1[item]).upper() + " "            
        else:
            empty_string += item + " "
    print(empty_string)
    from os import system
    system("say -i -v Fiona " + "\"" + empty_string + "\"")'''


    
def word_changer(words):
    words = words.strip()
    words_without_punct = remove_punctuation(words).split()
    result = ""
    c = 0

    for item in words_without_punct:
        if item in dict1.keys():
            if c % 2 == 0:
                result += random.choice(dict1[item]).upper() 

            else:
                result += item 
            c += 1
        else:
            result += item 
        result += " "
    return(result)


t = open('thesaurus', 'r')
dict1 = {}
for line in t:
    split_words = line.split(",")
    key = split_words.pop(0)
    dict1.update({key:split_words})


bad_blood_lyrics = open('bad_blood.txt', 'r')
lyrics = bad_blood_lyrics.read()

print(word_changer(lyrics))
