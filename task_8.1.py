import math
def distance(x,x1,y,y1):
    distance=0
    a=x-x1
    a1=abs(a)
    b=y-y1
    b1=abs(b)
    z=a1*a1+b1*b1
    distance=math.sqrt(z)
    return distance
print('Задача №1')
x=float(input('Введите действительное число:'))
x1=float(input('Введите действительное число:'))
y=float(input('Введите действительное число:'))
y1=float(input('Введите действительное число:'))
print('Расстояние между точками:',distance(x,x1,y,y1))



