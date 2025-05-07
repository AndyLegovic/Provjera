def pretvori_temperaturu(t):
    F = t * 9/5 + 32
    return(F)

temp = float(input("Unesi temperaturu u C: "))
print("Temperatura u F je:",pretvori_temperaturu(temp))
