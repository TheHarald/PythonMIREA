

def f21(args):
    if args[1] == 2006:
        return 12
    elif args[1] == 2008:
        return 11
    elif args[1] == 1986:
        if args[0] == 2013:
            return 5
        elif args[0] == 1982:
            if args[3] == 1970:
                return 0
            elif args[3] == 2010:
                if args[2] == 'nginx':
                    return 1
                elif args[2] == 'latte':
                    return 2
                elif args[2] == 'xbase':
                    return 3
            elif args[3] == 1961:
                return 4
        elif args[0] == 1963:
            if args[2] == 'nginx':
                return 6
            elif args[2] == 'latte':
                if args[3] == 1970:
                    return 7
                elif args[3] == 2010:
                    return 8
                elif args[3] == 1961:
                    return 9
            elif args[2] == 'xbase':
                return 10


def f22(x):
    number = str(bin(x))[2:]
    if len(number) < 32:
        number = '0' * (32 - len(number)) + number


    print(number)

    g = number[0]
    f = number[1:6]
    e = number[6:12]
    d = number[12:14]
    c = number[14:21]
    b = number[21:31]
    a = number[31]
    return int(f+g+b+e+a+d+c, base=2)


def f23():
    table = [
            [None, None, None, None],
            [None, None, '17.06.2000!+7 838 875‐6002', '0.31'],
            [None, None, '17.06.2000!+7 838 875‐6002', '0.31'],
            [None, None, '17.06.2000!+7 838 875‐6002', '0.31'],
            [None, None, '01.07.2000!+7 040 912‐5930', '0.31'],
            [None, None, '22.07.2004!+7 132 786‐7254', '0.68'],
            ]

    table = filter(None, table)

    print(table)

    return 0


print(f22(0x00000000))

