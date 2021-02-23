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



    for i in range(len(table)):
        new_table = table[i][0].split('!')
        for j in range(1, len(table[i])):
            new_table.append(table[i][j])
        table[i] = new_table

    for i in range(len(table)):
        table[i][0] = table[i][0][6:10]
        table[i][1] = table[i][1][3:15]
        table[i][2] = round(float(table[i][2]), 1)

    return table


print(f23([[None, None, '03.08.2004!+7 952 572‐8613', '0.88'],
           [None, None, '04.02.1999!+7 719 066‐9521', '0.76'],
           [None, None, '06.04.2003!+7 073 338‐8297', '0.48'],
           [None, None, None, None],
           [None, None, '04.03.2002!+7 784 893‐2471', '0.25'],
           [None, None, '04.03.2002!+7 784 893‐2471', '0.25'],
           ]))
