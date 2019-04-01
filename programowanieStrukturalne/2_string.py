tekst = "Anna, Mateusz, Kowalewscy"

lista = tekst.split(", ")

print(tekst)
print(lista)
print(type(lista)) #list

imie1 = lista[0]
print(imie1)    #Anna

imieDuze = imie1.upper()
print(imieDuze) #ANNA

imieMale = imie1.lower()
print(imieMale) #anna

#sprawdzenie zawartości
print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha() #zwraca True lub False
print(zawartosc)

nazwisko = ""
print(nazwisko.isalpha()) #False

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1, text2)

#wyswietlenie lancucha znakow

#wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona >2.6
text =  "{0}, Java i {1}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych w inny sposób
rok = 2019
miesiac = "kwiecień"
dzien = 1

print("\nData: ", end="")
print(dzien, miesiac, rok)

print("\nData: ", end="")
print(dzien, miesiac, rok, sep="-")
