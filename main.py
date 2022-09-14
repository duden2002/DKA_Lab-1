import math
try:
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    x = 8
    try:
        y = (6 * (math.pow(a, 2) + x + math.pow(b, 2))) / (a * b * x) / (4 * (math.pow(a, 2) - x + math.pow(b, 2)))
        print("Ответ: " , y)
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные!")