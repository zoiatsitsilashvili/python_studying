def main():
    count = input("iput text: ")
    if count !=(""):
        print("It's " + str(len(count)) + " symbols")
    else:
        print("there is nothintg")
        main()

main()