expression = input("Expression: ").split(" ")
x, y, z = expression
x = int(x)
z = int(z)

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x -z ))
elif y == "*":
    print(float(x * z))
elif y == "/" and z != 0:
    print(float(x / z))
        