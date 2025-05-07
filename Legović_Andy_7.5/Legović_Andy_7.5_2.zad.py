def je_palindrom(rijec):
    if rijec.lower() == rijec[::-1].lower():
        return(True)
    else:
        return(False)

rijec = input("Unesi neku rijec")
print(je_palindrom(rijec))
    
    
