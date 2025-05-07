def izdvoji_parne(lista):
    nova_lista = []
    for i in lista:
        if i % 2 == 0:
            nova_lista.append(i)
    return(nova_lista)

lista = []
n = int(input("Koliko brojeva želiš unijeti?"))
for i in range(n):
    broj = int(input("Unesi novi broj"))
    lista.append(broj)

print("Od unesenih brojeva parni su:", izdvoji_parne(lista))
