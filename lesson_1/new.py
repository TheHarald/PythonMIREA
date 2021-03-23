import math


def f11(x, y, z):
    return ((math.cos(y) + 31 * (y ** 4) + 1) / ((z ** 4) + 8 * (z ** 2))) -\
        (math.sqrt((48 * (x ** 3) - 59 * (z ** 6) + 69) / (math.log(z) - math.sin(x)))) -\
        (((z ** 3) - 65 * (x ** 5) - 83) / (14 * (x ** 8) + 7 * (y ** 7)))


def f12(x):
    if x < 153:
        return 22 * x ** 2 + x ** 4
    elif 153 <= x < 253:
        return 60 * (math.sin(x) - x - 99) ** 2 - x ** 8
    elif x >= 253:
        return x ** 3 + x + 51


def f13(n, m):
    temp = 0.0
    temp2 = 0.0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp += (math.tan(i) - math.fabs(j))
            temp2 += 70 * i ** 3 - j ** 2

    return 26 * temp2 - temp


def f14(n):
    if n == 0:
        return 7
    if n < 0:
        return None
    return math.cos(f14(n-1)) - math.fabs(f14(n-1)) - 23


print(f11(34, -58, 2))
print(f11(32, 75, 4))