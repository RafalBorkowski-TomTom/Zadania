import random
import sys

wiersz_gracz = random.randint(1, 10)
kol_gracz = random.randint(1, 10)
wiersz_skarb = random.randint(1, 10)
kol_skarb = random.randint(1, 10)
licznik = 0
pozycja_skarbu = (wiersz_skarb, kol_skarb)
pozycja_gracza = (wiersz_gracz, kol_gracz)
#print(f'Pozycja skarbu to: {pozycja_skarbu}')
#print(f'Pozycja gracza to: {pozycja_gracza}')

odleglosc_kol = abs(kol_skarb - kol_gracz)
odleglosc_wiersz = abs(wiersz_skarb - wiersz_gracz)

while pozycja_skarbu != pozycja_gracza:
    while True:
        ruch = input("Podaj kierunek ruchu (W/S/A/D): ").upper()
        licznik += 1

        if ruch not in ['W', 'S', 'A', 'D']:
            print("Niepoprawny ruch. Użyj klawiszy W, S, A lub D.")
            continue
        else:
            break
#    print(odleglosc_wiersz)
#    print(odleglosc_kol)
    if ruch == 'W' and wiersz_gracz < 10:
        wiersz_gracz += 1
        if odleglosc_wiersz > abs(wiersz_skarb - wiersz_gracz):
            print('Przybliżyłeś się do skarbu')
            odleglosc_wiersz = abs(wiersz_skarb - wiersz_gracz)
        else:
            print('Oddaliłeś się od skarbu')
            odleglosc_wiersz = abs(wiersz_skarb - wiersz_gracz)
    elif ruch == 'S' and wiersz_gracz > 1:
        wiersz_gracz -= 1
        if odleglosc_wiersz > abs(wiersz_skarb - wiersz_gracz):
            print('Przybliżyłeś się do skarbu')
            odleglosc_wiersz = abs(wiersz_skarb - wiersz_gracz)
        else:
            print('Oddaliłeś się od skarbu')
            odleglosc_wiersz = abs(wiersz_skarb - wiersz_gracz)
    elif ruch == 'A' and kol_gracz > 1:
        kol_gracz -= 1
        if odleglosc_kol > abs(kol_skarb - kol_gracz):
            print('Przybliżyłeś się do skarbu')
            odleglosc_kol = abs(kol_skarb - kol_gracz)
        else:
            print('Oddaliłeś się od skarbu')
            odleglosc_kol = abs(kol_skarb - kol_gracz)
    elif ruch == 'D' and kol_gracz < 10:
        kol_gracz += 1
        if odleglosc_kol > abs(kol_skarb - kol_gracz):
            print('Przybliżyłeś się do skarbu')
            odleglosc_kol = abs(kol_skarb - kol_gracz)
        else:
            print('Oddaliłeś się od skarbu')
            odleglosc_kol = abs(kol_skarb - kol_gracz)
    else:
        print('Wyskoczyłeś za plansze i przegrałeś')
        sys.exit()
    pozycja_gracza = (wiersz_gracz, kol_gracz)
#    print(pozycja_gracza)

print(f'Znalazłeś skarb za {licznik} próbą')
