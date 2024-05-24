import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)

def logarithm(x, base=math.e):
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers.")
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return math.factorial(x)

def main():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11): ")

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'):
            if choice == '6':
                num1 = float(input("Enter number: "))
                print(f"Square Root({num1}) = {square_root(num1)}")

            elif choice == '7':
                num1 = float(input("Enter number: "))
                base = input("Enter base (default is e): ")
                base = float(base) if base else math.e
                print(f"Logarithm({num1}) with base {base} = {logarithm(num1, base)}")

            elif choice == '8':
                num1 = float(input("Enter angle in degrees: "))
                print(f"Sine({num1}) = {sine(num1)}")

            elif choice == '9':
                num1 = float(input("Enter angle in degrees: "))
                print(f"Cosine({num1}) = {cosine(num1)}")

            elif choice == '10':
                num1 = float(input("Enter angle in degrees: "))
                print(f"Tangent({num1}) = {tangent(num1)}")

            elif choice == '11':
                num1 = int(input("Enter number: "))
                print(f"Factorial({num1}) = {factorial(num1)}")

            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

                elif choice == '5':
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")

        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
