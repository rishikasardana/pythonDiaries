def madlibs():
    place = input("Place: ")
    adjective = input("Adjective: ")
    animal = input("animal: ")
    object = input("object: ")
    funny_phrase = input("Funny Phrase :")

    madlib = f"Today I went to the {place} and saw a {adjective}{animal}.\
                It was holding a {object} and shouted{funny_phrase}!"
    
    print(madlib)