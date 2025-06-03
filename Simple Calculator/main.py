# Operation Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

# Calculator function using individual operations
def calculator(n1, n2, opt):
    operations = {
        1: add,
        2: subtract,
        3: divide,
        4: multiply,
    }

    operation_func = operations.get(opt)
    if operation_func:
        return operation_func(n1, n2)
    else:
        return "Invalid Option"

# Main Program
def main():
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    opt = int(input("Choose operation:\n1. Add\t2. Subtract\n3. Divide\t4. Multiply\n5. Exponent\nOperation Choice: "))

    res = calculator(a, b, opt)
    print("Result:", res)

main()
