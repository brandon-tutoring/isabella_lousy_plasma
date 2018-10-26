import string
import random

def remove_punctuation(var):
    no_punct = ""
    for item in var:
        if item not in string.punctuation:
            no_punct += item
    return no_punct


t = open('thesaurus', 'r')
dict1 = {}
for line in t:
    split_words = line.split(",")
    key = split_words.pop(0)
    dict1.update({key:split_words})


def lousy_plasma():

    empty_string = ""          
    input1 = input("what is your sentence?").strip()
    input1 = remove_punctuation(input1).split()

    for item in input1:
        if item in dict1.keys():
            empty_string += random.choice(dict1[item]) + " "
        else:
            empty_string += item + " "
    print(empty_string)
    


 
lousy_plasma()
