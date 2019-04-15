# -*- coding: utf-8 -*-

def show1(city):
    print(f'Przed modyfikacja: {city}')
    city[0] = 'Berlin'
    city[1] = 'Londyn'
    print(f'Po modyfikacji: {city}')
    print(f'ID po modyfikacji: {id(city)}')

miasto = ['Gniezno', 'Poznań']
print('\n')
print(f'Przed wywolaniem funkcji show1: {miasto}')
print(f'ID obiektu miasto: {id(miasto)}')
show1(miasto)
print(f'Po wywolaniu funkcji show1: {miasto}')
