import math

try:
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    x = float(input("Введите x: "))
    try:
        if (x < 8):
            y = (6 * (math.pow(a, 2) + x + math.pow(b, 2))) / (a * b * x)
        else:
            y = (4 * (math.pow(a, 2) - x + math.pow(b, 2)))
        print("Ответ: " + format(y, "#.2f"))
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные!")
