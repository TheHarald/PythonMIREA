def f23(table):
    # удаление пустых строк
    j = 0
    while j < len(table[0]):
        count = 0
        for i in range(len(table)):
            if table[i][j] is None:
                count += 1
            else:
                break
        if count == len(table):
            for i in range(len(table)):
                del table[i][j]
        else:
            j += 1

    # удаление поворяющихся строк
    i = 0
    while i < len(table) - 1:
        j = i + 1
        while j < len(table):
            if table[i] == table[j]:
                del table[j]
                j -= 1
            j += 1
        i += 1

    # удаление пустых столбцов
    i = 0
    while i < len(table):
        if table[i].count(None) == len(table[i]):
            del table[i]
        else:
            i += 1

    # разделение 1 столбца по !
    for i in range(len(table)):
        new_table = table[i][0].split('!')
        for j in range(1, len(table[i])):
            new_table.append(table[i][j])
        table[i] = new_table

    # слайс 1 и 2 столбца и округление 3
    for i in range(len(table)):
        table[i][0] = table[i][0][6:10]
        table[i][1] = table[i][1][3:15]
        table[i][2] = str(round(float(table[i][2]), 1))

    return table


print(f23([[None, None, None, None], [None, None, '17.06.2000!+7 838 875-6002', '0.31'], [None, None, '17.06.2000!+7 838 875-6002', '0.31'], [None, None, '01.07.2000!+7 040 912-5930', '0.80'], [None, None, '22.07.2004!+7 132 786-7254', '0.68']]))
