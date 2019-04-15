# Zasięg zmiennych, zmienne lokalne i globalne

# Precyzja liczby

x = "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(f'Ilosc CHF:{iloscChf}')

plnToChf(400)

def plnToEur(value):
    kursEur = 4.2733
    iloscEur = value / kursEur
    iloscEur = "{0:.4f}".format(iloscEur)
    return iloscEur

iloscPln = input('Podaj złotówki: ')
print(plnToEur(float(iloscPln)))
