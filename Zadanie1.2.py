import math
a = float(input('Podaj pierwszą długość boku trójkąta: '))
b = float(input('Podaj drugą długość boku trójkąta: '))
c = float(input('Podaj trzecią długość boku trójkąta: '))

while True:
    if a + b > c and a + c > b and b + c > a:
        print('podane boki mogą być trójkątem')
        break
    else:
        print('Podane boki nie mogą być trójkątem')
        a = float(input('Podaj pierwszą długość boku trójkąta: '))
        b = float(input('Podaj drugą długość boku trójkąta: '))
        c = float(input('Podaj trzecią długość boku trójkąta: '))
        continue

p = (a+b+c)/2

pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'Pole powierzchni trójkąta o podanych bokach wynosi: {pole}')
