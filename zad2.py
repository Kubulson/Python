import math

#2a
def roznica(lista: list[int]) -> int:
    return max(lista) - min(lista)

#2b
def brakujaca_liczba(lista: list[int]) -> int:
    for liczba in range(min(lista), max(lista)):
        if liczba not in lista:
            return liczba
#2c

#2d
def wystepowanie(lista: list[int]) -> set[int]:
    for liczba in lista:
        if lista.count(liczba) > 1:
            return liczba
