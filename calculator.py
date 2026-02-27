def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

print("Выберите операцию: +, -, *, /")
operation = input("Операция: ")

num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))

if operation == "+":
    print(add(num1, num2))
elif operation == "-":
    print(subtract(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
elif operation == "/":
    print(divide(num1, num2))
else:
    print("Неверная операция")
