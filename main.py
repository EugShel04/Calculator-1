# Простой калькулятор

a = float(input("Введите 1 число: "))
x = input("Введите операцию: ")
b = float(input("Введите 2 число: "))
counter = 1
result = None
if x == "+":
    result = a + b
elif x == "-":
    result = a - b
elif x == "/":
    try:
        result = a / b
    except ZeroDivisionError:
        print("Нельзя делить на ")
        result = 0
        counter = 0
elif x == "*":
    result = a * b
elif x == "**":
    result = a ** b
else:
    print("Нет такой операции")
print("Полученный результат :", result)
print("Операция :", counter)
while result is not None:
    x = input("Введите операцию или введите  'стоп', чтобы завершить: ")
    if x == "стоп":
        print("Итоговый результат равен :", result, ". Всего доброго!")
        break
    c = float(input("Введите число:"))
    if x == "+":
        result += c
    elif x == "-":
        result -= c
    elif x == "/":
        try:
            result /= c
        except ZeroDivisionError:
            print("Нельзя делить на 0")
            counter -= 1
    elif x == "*":
        result *= c
    elif x == "**":
        result **= c
    counter += 1
    print("Полученный результат : ", result)
    print("Операция : ", counter)
