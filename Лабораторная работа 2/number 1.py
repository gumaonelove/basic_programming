'''
Вычислите сумму ряда
'''
from math import fabs, factorial, pi


def first_example(x, N):
    if fabs(x) > 1:
        suma = 0
        for n in range(N+1):
            suma += 1/( (2 * n + 1) * x ** (2 * n + 1) )
        return 2*suma
    else:
        return 'Внимание, по условию задачи |x| > 1'


def second_example(x, N):
    '''Тут должен быть коммент'''
    suma = 0
    for n in range(N+1):
        suma += ((-1)**n * x**n) / (factorial(n))
    return suma


def third_example(x, N):
    suma = 0
    for n in range(N+1):
        suma += ( (-1)**n * x**(2*n) ) / (factorial(2*n))
    return suma


def fourth_example(x, N):
    suma = pi/2
    if x > 1:
        for n in range(N+1):
            suma += ( (-1)**(n+1) ) / ( (2*n+1) * x**(2*n+1) )
        return suma
    else:
        return 'Внимание, по условию задачи x > 1'


def fift_exemple(x, N):
    if fabs(x) <= 1:
        suma = 0
        for n in range(N+1):
            suma += ( (-1)**n ) / ( (2*n+1) * x**(2*n+1) )
        return 2*suma
    else:
        return 'Внимание, по условию задачи |x| <= 1'


def eight_example(x, N):
    suma = 0
    for n in range(N+1):
        suma += ( ((-1)**n) * x**(2*n) )/(factorial(n))


print(
    second_example(
        x=int(input('x: ')),
        N=int(input('n: '))
    )
)