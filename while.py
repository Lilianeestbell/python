responses = {}
active = True
while active:
    name = input("what's your name")
    response = input('which mountain would you like to climb someday')
    responses[name] = response
    repeat = input("would you like to let another person to respond(yes/no)")
    if repeat == 'no':
        active = False
        print("there are results:----")
        for name, response in responses.items():
            print(name+ " would like to climb" + response + ".")