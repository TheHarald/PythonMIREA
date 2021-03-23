def multiply12(x):
    x = x + x + x
    x = x + x
    return x + x


def multiply16(x):
    x = x + x
    x = x + x
    x = x + x
    return x + x


def multiply15(x):  # 3 сложения и 2 вычитание
    temp = x
    x = x + x
    x = x + x
    x = x + x
    x = x - (-x)
    return x - temp


def multiply29(x):  # 6 сложений и одно вычитание.
    temp = x
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    x = x + (-temp)
    x = x + x
    return x-temp


def naive_mul(x, y):
    r = x
    for i in range(1, y):
        x = x + r
    return x


print(naive_mul(11, 11))
