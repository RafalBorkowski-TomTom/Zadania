import random

losowa_liczba = random.randint(0, 999)
strzal = int(input('Zgadnij losową liczbe od 0 do 999: '))

licznik = 1

while strzal != losowa_liczba:
    if strzal > losowa_liczba:
        print('Twoj strzal jest wiekszy od losowej liczby')
        licznik += 1
        strzal = int(input('Zgadnij losową liczbe od 0 do 999: '))
    else:
        print('Twoj strzal jest mniejszy od losowej liczby')
        licznik += 1
        strzal = int(input('Zgadnij losową liczbe od 0 do 999: '))

print(f'Gratuluje zgadłeś losową liczbę {losowa_liczba} za {licznik} razem ')