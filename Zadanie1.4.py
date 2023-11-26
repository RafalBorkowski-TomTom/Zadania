szerokosc = float(input('Podaj szerokość pomieszczenia w metrach: '))
dlugosc = float(input('Podaj długość pomieszczenie w metrach: '))
wysokosc = float(input('Podaj wysokość pomieszczenie w metrach: '))

obwod = (2 * szerokosc) + (2 * dlugosc)
pow_podlogi = dlugosc * szerokosc
pow_scian = obwod * wysokosc
cena = 0

while True:
    decyzja_gips = input('Czy gipsować ściany (odpowiedz T lub N): ').upper()
    if decyzja_gips == 'T':
        cena = pow_scian * 100
        break
    elif decyzja_gips == 'N':
        break
    else:
        print('Proszę podać odpowiedź T lub N')
        continue

while True:
    decyzja_malowanie= input('Czy malować ściany i sufity (odpowiedz T lub N): ').upper()
    if decyzja_malowanie == 'T':
        cena = cena + ((pow_podlogi + pow_scian) * 30)
        break
    elif decyzja_malowanie == 'N':
        break
    else:
        print('Proszę podać odpowiedź T lub N')
        continue

while True:
    decyzja_podlogi = input('Czy kładziemy panele podłogowe (odpowiedz T lub N): ').upper()
    if decyzja_podlogi == 'T':
        cena = cena + (pow_podlogi * 50)
        break
    elif decyzja_podlogi == 'N':
        break
    else:
        print('Proszę podać odpowiedź T lub N')
        continue

while True:
    decyzja_listwy = input('Czy montujemy listwy przypodłogowe (odpowiedz T lub N): ').upper()
    if decyzja_listwy == 'T':
        cena = cena + (obwod * 40)
        break
    elif decyzja_listwy == 'N':
        break
    else:
        print('Proszę podać odpowiedź T lub N')
        continue

print(f'Cena za wszystkie usługi wynosi: {cena}zł')