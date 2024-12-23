def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

# User input
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print(f"The result is: {add(a, b)}")
elif choice == '2':
    print(f"The result is: {sub(a, b)}")
elif choice == '3':
    print(f"The result is: {mul(a, b)}")
elif choice == '4':
    print(f"The result is: {div(a, b)}")
else:
    print("Invalid choice")
