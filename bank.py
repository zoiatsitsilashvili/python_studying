
answer = str(input("Answer: ")).lstrip().lower()

if answer.startswith("hello") or ("hello, " + ""):
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")

