def createFile():
    open("calc_history.txt", 'x').close()

def calc(n1, n2, op):
    if op == '*':
        return print(f"{n1} * {n2}: {n1 * n2}")
    elif op == '+':
        return print(f"Addition: {n1 + n2}")
    elif op == '-':
        return print(f"Subtraction: {n1 - n2}")
    elif op == '/': 
        return print(f"Division: {n1 / n2}")
    else:
        return print("Invalid Operation")

def main():
    user_input = input("What do you want to do? (Calc, history, clear history): ")
    if user_input.lower() != "calc":
        print("This feature is not implemented yet.")
        return
    else:
        n1 = input("Enter first number: ")
        n2 = input("Enter second number: ")
        op = input("Enter Operator (*, +, -, /): ")
        
        calc(float(n1),float(n2),op)

if __name__ == "__main__":
    main()