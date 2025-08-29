def madlibs():
    number = input("Number: ")
    food = input("Food: ")
    liquid = input("Liquid: ")
    number2 = input("Number: ")
    temp = input("temperature: ")
    plural_noun = input("Plural Noun: ")

    madlib = f"Take {number} cups of {food} and mix it with {liquid}.\
                Bake it for {number2} minutes at {temp} degrees.\
                Serve with {plural_noun} on the side."
    
    print(madlib)