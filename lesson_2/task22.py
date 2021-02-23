def f22(x):
    number = str(bin(x))[2:]
    if len(number) < 32:
        number = '0' * (32 - len(number)) + number

    g = number[0]
    f = number[1:6]
    e = number[6:12]
    d = number[12:14]
    c = number[14:21]
    b = number[21:31]
    a = number[31]
    return int(f+g+b+e+a+d+c, base=2)