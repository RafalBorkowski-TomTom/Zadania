import calendar
import locale

locale.setlocale(locale.LC_TIME, 'pl_PL.utf8')

dzien = int(input('W jaki dzień tygodnia oddałeś/aś buty do szewca (liczba od 1 do 7): '))

while True:
    if 1 <= dzien <= 7:

        ile_dni = int(input('Ile dni potrwa naprawa: '))
        oddam = dzien + ile_dni

        while oddam > 7:
            oddam = oddam - 7

        nazwa_dnia = calendar.day_name[oddam - 1]
        print(f'Buty będą do odbioru w dzień: {nazwa_dnia}')
        break

    else:
        dzien = int(input('To ma być liczba od 1 do 7 więc skup się i podaj prawidłowy dzień: '))
        continue
