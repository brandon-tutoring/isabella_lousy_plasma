import random

def remove_punctuation(var):
    no_punct = ""
    punctuation =  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in var: 
        if item not in punctuation:
            no_punct += item + " " 
    return no_punct

def lousy_plasma():

    thesaurus = { "happy": ["GLAD", "BLISSFUL", "ECSTATIC"], "sad"  : ["BLEAK", "BLUE", "DEPRESSED"], "baby": ["FOOL","INFANT"], "bad": ["BADNESS","EVIL","FETOR","UNCLEANESS","WRONG"], "blood":["FOP","KILLING","FLUIDITY"]}

    input1 = input("what is your sentence?").strip()

    words = input1.split(" ")
    remove_punctuation(words)    

    list1 = []

    for item in words:
        if item not in thesaurus.keys():
            list1.append(item)
        else:
            values = thesaurus.get(item)
            list1.append(random.choice(values))
    list1.join()

    

    print(list1)
   

 
lousy_plasma()
