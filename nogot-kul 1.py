fodelseManad = input("skriv ditt födelsemånad: ")

fodels = int(fodelseManad)

if fodels >= 6 and fodels <= 9:
    print(1250*29+625)
else:
    print(1250*30)