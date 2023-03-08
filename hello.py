def hello(me):
    print("Hello, "+ me +", nice to meet you!")

name = input("What's your name? " )
hello(name.strip().title())