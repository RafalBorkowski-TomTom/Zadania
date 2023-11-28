a = int(input('Podaj ilość linii naszej choinki: '))

for i in range(a):
    print('{:^{szerokosc}}'.format((i*2+1)*'*', szerokosc=a*2+1))
