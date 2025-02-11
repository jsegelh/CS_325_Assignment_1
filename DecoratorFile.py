def greetings(func):
    def wrapper(*args):
        print("Hello ", args[0], ".", sep="")
        result = func(*args)
        print("Good Bye ", args[0], ".", sep="")
        return result
    return wrapper

@greetings
def aThing(name):
    print(name, " does a thing!", sep="")
    return


aThing("Bob")