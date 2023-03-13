def main():
    meal_time = convert(input("What time is it? "))
    if 7 <= meal_time <= 8:
        print("It's breakfeast time")
    elif 12 <= meal_time >= 13:
        print("It's lunch time")
    elif 18 <= meal_time >= 20:
        print("It's dinner time")
    else:
        print("It's not meal time")

def convert(time):
    hours, minutes = time.split(":")
    convert_time = float(minutes)/60
    return float(hours) + convert_time


if __name__ == "__main__":
    main()