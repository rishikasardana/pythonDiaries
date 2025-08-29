def madlibs():
    country = input("Country: ")
    verb_ing = input("Verb ending in ing: ")
    vehicle = input("Vehicle: ")
    food = input("Food: ")
    adj = input("Adjective: ")



    madlib = f"I traveled to {country} and spent my time {verb_ing}.\
                One day I rode a {vehicle} made of {food}.\
                It was the most {adj} trip ever!"
    
    print(madlib)