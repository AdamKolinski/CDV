print("Hello World!")
print(5)

'''
komentarz blokowy
'''

#potęgowanie
potega = 2 ** 10
print(potega)

#pobieranie danych z klawiatury
imie = input()

#konkatenacja +
print("Twoje imię to: " + imie)

nazwisko = input("Podaj nazwisko: ")
print("Twoje nazwisko: " + nazwisko)
print()

#Twoje imie ..., Twoje nazwisko ...
print("Nazywasz się " + imie + " " + nazwisko)

'''
Uzytkownik podaje swój wiek,
wyświetl dane w formacie
Twój wiek: ... lat
'''

print("Podaj swój wiek: ", end="")
wiek = input()
print("Twój wiek:", wiek, "lat")


nazwisko = "Kowalski"
print(nazwisko)

pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko) - 1]
print(ostatniZnak)