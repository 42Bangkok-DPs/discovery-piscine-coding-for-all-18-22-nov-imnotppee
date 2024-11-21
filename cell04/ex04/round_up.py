number = float(input("Give me a number: "))

if number.is_integer():
    print(int(number))
else:
    rounded_number = int(number + 1)
    print(rounded_number)