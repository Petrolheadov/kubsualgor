s = str(input('Введите строку; '))
first_h = s.find('h')
last_h = s.rfind('h')
# разворачиваем подстроку между первым и последним вхождением буквы h
result = s[:first_h+1] + s[first_h+1:last_h][::-1] + s[last_h:]
print(result) 