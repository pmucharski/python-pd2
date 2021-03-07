# #zad.1
# from typing import Dict
#
# lista = ['piłka nożna', 'siatkówka', 'koszykówka', 'hokej', 'łyżwiarstwo']
# print(lista)
#
# lista.reverse()
# print(lista)
#
# lista.append('rugby')
# lista.append('baseball')
# print(lista)
#
# #zad.2
# slownik = {'af':'afery', 'nw':'news', 'pop':'popularne', 'fm':'fame mma'}
# print(slownik)
#
# #zad.3
# slownik1 = {'lol':'league of legends', 'cs':'counter strike', 'wow':'world of tanks'}
# print(slownik1)
# print(len(slownik1))
#
# #zad.4
# napis = input('Wprowadz zdanie:')
# print(napis)
# print(napis.count('a'))
#
#zad.5
# sys.stdout.write('Podaj trzy liczby całkowite: ')
# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# w = a ** b + c
# sys.stdout.write('a ^ b + c = %s' % w)

#zad 6.
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# c = int(input('Podaj c: '))
#
# if a >= b:
#     if a >= c:
#         print('Największe: %d' % a)
#     else:
#         print('Największe: %d' % c)
# elif b >= c:
#     print('Największe: %d' % b)
# else:
#     print('Największe: %d' % c)

#zad 7.
# lista_l = [1, 2, 4, 3.5, 3.66666666666, 7.67]
#
# for elem in lista_l:
#     print(elem * elem)

#zad 8.
# lista_parz = []
# i = 0
# while i < 10:
#     a = int(input('Podaj liczbę: '))
#     if a % 2 == 0:
#         lista_parz.append(a)
#     i += 1
# print(lista_parz)

#zad 9.
# l = [1, 2, 3, 4, 5, 6]
# for i in l:
#     if i == 6:
#         break
#     if i % 2 == 1:
#         print('EEEEE')
#     else:
#         print('E')

#zad. 10
# try:
#     liczba = int(input('Podaj liczbe: '))
#     print(sqrt(liczba))
#
# except Exception as e:
#     print(e)
#     print('Tylko liczby nieujemne!')
