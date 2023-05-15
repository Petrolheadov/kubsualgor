s = str(input('введите СТРОКУ, пожалуйста! - '))
mid = len(s) // 2
result = s[mid:] + s[:mid]
print(result)
