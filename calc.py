def calc(n1, n2, op):
    if op == '*':
        return print(f"Multiplication: {n1 * n2}")
    elif op == '+':
        return print(f"Addition: {n1 + n2}")
    elif op == '-':
        return print(f"Subtraction: {n1 - n2}")
    elif op == '/': 
        return print(f"Division: {n1 / n2}")
    else:
        return print("Invalid Operation")

def main():
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    op = input("Enter Operator (*, +, -, /): ")

    result = calc(float(n1),float(n2),op)
    if int(result) == result:
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()