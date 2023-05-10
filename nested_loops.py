for x in range(4):
    for y in range (3):
        print(f"{x}, {y}")


numbers = [5,2,5,2,2]
for x_count in numbers:
    output =""
    for coun in range(x_count):
        output = output + "x"
    print(output)