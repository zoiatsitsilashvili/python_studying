
price = 50
# ვაილის დახმარებით აქ შეგვყავს თანხა მანამ, სანამ არ მივიღებთ ნულს.
while True:
    print("Amount Due: " + str(price))
    n = int(input("Insert Coin: ")) 
    if n == 5 or n == 10 or n == 25:
        price -= n
    if n < price:
        continue
    #თუ თანხა ნაკლებია ან ტოლია ნულის ვწყვეტთ ციკლს
    if price <= 0:
        break
    
#კოდი სრულყოფილი არაა რადგან განსხვავებული თანხის შეყვანის შემთხვევაში 
# არ გვაქს გაწერილი გამომავალი პრინტი