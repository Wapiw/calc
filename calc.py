def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Calculator Program")
print("------------------")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting the program...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result: ", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")