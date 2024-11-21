table = 0 
while table <= 10:  # Outer loop
    print(f"Table de {table}: ", end="")  # Print
    num = 0 
    while num <= 10: 
        print(table * num, end=" ")  # Print
        num += 1
    print() # New Line
    table += 1