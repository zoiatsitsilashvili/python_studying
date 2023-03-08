def hello(name):
    if name == ("zoia"):
        print("Hello, zoia, nice to meet you!")
    elif name == ("ana"):
        print("Hi, ana, it's great day!")
    else:
        print("Hello, " + name +", you are welcome!")

name = input("What's your name? " )

hello(name)