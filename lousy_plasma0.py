import string
import random

def remove_punctuation(var):
    no_punct = ""
    for item in var:
        if item not in string.punctuation:
            no_punct += item
    return no_punct


t = open('thesaurus', 'r')
dict1 = { "happy": ["GLAD", "BLISSFUL", "ECSTATIC"], "sad"  : ["BLEAK", "BLUE", "DEPRESSED"], "baby": ["FOOL","INFANT"], "bad": ["BADNESS","EVIL","FETOR","UNCLEANESS","WRONG"], "blood":["FOP","KILLING","FLUIDITY"]}
for line in t:
    split_words = line.split(",")
    key = split_words.pop([0])
    syn = {split_words[0]:split_words - split_word[0]}
    print(syn)
    break


def lousy_plasma():

    empty_string = ""          
    input1 = input("what is your sentence?").strip()
    input1 = input1.split()
    input1 = remove_punctuation(input1).split()
    for item in input1:
        if item in dict1.keys():
            empty_string += random.choice(dict1[item]) + " "
        else:
            empty_string += item + " "
    print(empty_string)
    


 
lousy_plasma()

