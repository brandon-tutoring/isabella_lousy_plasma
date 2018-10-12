def lousy_plasma0():

    thesaurus = { "happy": "glad", "sad"  : "bleak" }

    input1 = input("what is your sentence?").lower().strip()

    words = input1.split(" ")

    for item in words:
        if item == "happy":
            words.replace("happy", "GLAD", 100)
        elif item == "sad":
            words.replace("sad", "BLEAK", 100)
    

    print(words)
   


lousy_plasma0()
