s = str(input('введите строку: '))
first_f = s.find('f')
if first_f == -1:
    print(-2)
else:
    second_f = s.find('f', first_f + 1)
    if second_f == -1:
        print(-1)
    else:
        print(second_f)
