import math
def power(a,n):
    for i in range (1,n):
        a=a*a
        return a
print('Задача №2')
a=float(input('Введите действительное положительное число:'))
n=int(input('Введите целое число:'))
print('Число возведённое в степень n:',power(a,n))