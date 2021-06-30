x = 'Liczba jest podzielna przez 3'
y = 'Liczba nie jest podzielna przez 3'

#wpisz liczbe
liczba = input('Wprowadz liczbe: ')

#sprawdza czy liczba jest podzielna przez 3
wynik = int(liczba) % 3

#wyświetla czy podana liczba jest podzielna przez 3
if wynik > 0:
    print(y)
elif wynik == 0:
    print(x)

    #sprawdza pierwiastek z liczby
    import math
    (pierwiastek) = math.sqrt(int(liczba))

#sprawdza  czy pierwiastek jest liczba naturalna
    perfect_square = isinstance(pierwiastek, int)

    print (perfect_square)