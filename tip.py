#პროცენტის კალკულატორი, დავაბრუნოთ "%"" და "$"" შეყვანის განსხვავებული 
#მეთოდები როგორც float.
def main():
    dollars = dollars_to_float(input("How much was the meal? ").replace("$", ""))
    percent = percent_to_float(input("what percentage would you like to tip? ").replace("%", ""))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d)


def percent_to_float(p):
    return float(p)/100

 
''' შესაძლებელია ასე გაკეთებაც
def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return d
   
def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    return p
''' 

main()