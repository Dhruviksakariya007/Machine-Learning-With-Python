FILE = "calc_history.txt"

def createFile():
    open(FILE, 'x').close()

def history():
    his = open(FILE, 'r')
    print(his.read())
    his.close()

def saveHistory(result):
    his = open(FILE, 'a')
    his.write(f"{result}\n")
    his.close()

def clearHistory():
    open(FILE, 'w').close()

def calc(n1, n2, op):
    if op == '*':
        return f"{n1} * {n2}: {n1 * n2}"
    elif op == '+':
        return f"{n1} + {n2}: : {n1 + n2}"
    elif op == '-':
        return f"{n1} - {n2}: {n1 - n2}"
    elif op == '/': 
        return f"{n1} / {n2}: {n1 / n2}"
    else:
        return print("Invalid Operation")

def main():

    while True:
        user_input = input("What do you want to do? (Calc, history, clear history, exit): ")

        if user_input.lower() == "history":
            history()
        
        elif user_input.lower() == "clear history" or user_input.lower() == "clearhistory" or user_input.lower() == "clear":
            clearHistory()
            print("History cleared.")
            
        elif user_input.lower() == "calc":
            n1 = input("Enter first number: ")
            n2 = input("Enter second number: ")
            op = input("Enter Operator (*, +, -, /): ")
            
            result = calc(float(n1),float(n2),op)
            print(result)
            saveHistory(result)
        
        elif user_input.lower() == "exit":
            print("Exiting...")
            break

        else:
            print("INVALID INPUT \nExiting...")
            break

if __name__ == "__main__":
    main()
    