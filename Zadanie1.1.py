dzien = int(input('W jaki dzień tygodnia oddałeś/aś buty do szewca (liczba od 1 do 7): '))

while True:
    if 1 <= dzien <= 7:

        ile_dni = int(input('Ile dni potrwa naprawa: '))
        oddam = dzien + ile_dni

        while oddam > 7:
            oddam = oddam - 7

        if oddam == 1:
            print('Buty będą do odbioru w poniedziałek')
            break
        elif oddam == 2:
            print('Buty będą do odbioru we wtorek')
            break
        elif oddam == 3:
            print('Buty będą do odbioru w środę')
            break
        elif oddam == 4:
            print('Buty będą do odbioru w czwartek')
            break
        elif oddam == 5:
            print('Buty będą do odbioru w piątek')
            break
        elif oddam == 6:
            print('Buty będą do odbioru w sobotę')
            break
        elif oddam == 7:
            print('Buty będą do odbioru w niedziele')
            break
    else:
        dzien = int(input('To ma być liczba od 1 do 7 więc skup się i podaj prawidłowy dzień: '))
        continue
