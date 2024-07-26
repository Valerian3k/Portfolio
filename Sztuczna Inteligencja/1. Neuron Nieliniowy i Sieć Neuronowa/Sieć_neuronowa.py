def animal(x1, x2, x3, x4, x5):
    ssak = [4, 0.01, 0.01, -1, -1.5]
    ptak = [2, -1, 2, 2.5, 2]
    ryba = [-1, 3.5, 0.01, -2, 1.5]

    sSsak = ssak[0]*x1 + ssak[1]*x2 + ssak[2]*x3 + ssak[3]*x4 +ssak[4]*x5
    sPtak = ptak[0]*x1 + ptak[1]*x2 + ptak[2]*x3 + ptak[3]*x4 +ptak[4]*x5
    sRyba = ryba[0]*x1 + ryba[1]*x2 + ryba[2]*x3 + ryba[3]*x4 +ryba[4]*x5

    if(sSsak > sRyba and sSsak > sPtak):
        return "Ssak"
    elif(sRyba > sPtak):
        return "Ryba"
    else:
        return "Ptak"


d1 = float(input("Ile ma nóg? Liczba: "))
d2 = float(input("Czy żyje w wodzie? Liczba: "))
d3 = float(input("Czy umie latać? Liczba: "))
d4 = float(input("Czy jest pokryte piórami? Liczba: "))
d5 = float(input("Czy rodzi się z jaj? Liczba: "))

print(animal(d1, d2, d3, d4, d5))
