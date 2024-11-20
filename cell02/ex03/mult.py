num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

product = num1 * num2

if product > 0:
    print(f"{num1} x {num2} = {product}")
    print("The result is positive.")
elif product < 0:
    print(f"{num1} x {num2} = {product}")
    print("The result is negative.")
else:
    print(f"{num1} x {num2} = {product}")
    print("The result is positive and negative.")