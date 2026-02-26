
keep_going = True
number = float(input("What's the first number?: "))
while keep_going:
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Pick an operation?: ")
    next_number = float(input("What's the next number?: "))

    def calculator(num1 , num2, operation):
        if operation == "+" :
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2

    result = calculator(number, next_number, operation)
    print(f"{number} {operation} {next_number} = {result}")

    cont = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation, or type anything else to stop: ")
    if cont == 'y':
        number = result
    elif cont == 'n':
        number = int(input("What's the first number?: "))
    else:
        keep_going = False