def madlibs():
    adj = input("Adjective: ")
    noun = input("noun: ")
    verb_ing = input("verb ending in ing: ")
    adj2 = input("Adjective: ")
    celeb = input("celebrity: ")
    plural_obj = input("Plural Object: ")

    madlib = f"My superhero name is {adj} {noun}.\
        I fight crime using {verb_ing}.\
        My enemy is {adj2} {celeb} who wants all the {plural_obj}."
    

    print(madlib)