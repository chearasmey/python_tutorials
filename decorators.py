def announce(f):
    def wrapper():
        print("Start wrapper")
        f()
        print("End wraper")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()