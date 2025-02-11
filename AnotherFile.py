def reverseGreeting(func):
    def wrapper(*args):
        print("Good Bye ", args[0], ".", sep="")
        result = func(*args)
        print("Hello ", args[0], ".", sep="")
        return result
    return wrapper

@reverseGreeting
def anotherThing(name):
    print(name, " does another thing!", sep="")

anotherThing("Bob")