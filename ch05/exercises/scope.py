def multiply(num1, num2):
    acc = num2
    for _ in range(num1 - 1):
        num2 += acc
    return num2

def exponent(num, exp):
    acc = num
    for _ in range(exp - 1):
        num = multiply(num, acc)
    return num
    

def square(num):
    return exponent(num, 2)

def main():
    print("Operation choices:")
    print("1: Multiplication")
    print("2: Exponent")
    print("3: Square")
    operation = input()
    if operation == "1":
        num1 = int(input("Value 1: "))
        num2 = int(input("Value 2: "))
        output = multiply(num1, num2)
    elif operation == "2":
        num1 = int(input("Base: "))
        num2 = int(input("Exponent: "))
        output = exponent(num1, num2)
    elif operation == "3":
        num1 = int(input("Value: "))
        output = square(num1)
    else: output = "That wasn't an option!"
    print(output)

main()