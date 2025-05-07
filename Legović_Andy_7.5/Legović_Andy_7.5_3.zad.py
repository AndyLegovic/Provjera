def izracunaj_prosjek(lista):
    prosjek = sum(lista) / len(lista)
    return(prosjek)

lista = []
n = int(input("Koliko brojeva želiš unijeti?"))
for i in range(n):
    broj = int(input("Unesi novi broj"))
    lista.append(broj)
print("Prosjek unesenih brojeva je:", izracunaj_prosjek(lista))
