import math
def func():
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    x = 8
    if x == 8:
        y = (6 * (math.pow(a, 2) + x + math.pow(b, 2))) / (a * b * x) / (4 * (math.pow(a, 2) - x + math.pow(b, 2)))
        print("Ответ: ", y)
    else:
        print("Неверный x")


func()