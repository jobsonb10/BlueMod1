L = ["MELANCIA", "BANANA"]
secreta = list(range(len(L[0])))
vidas = 6

print()

for i in range(len(L[0])):
    secreta[i] = "_"

print(secreta) 

for i in range(vidas):
    letra = input("Digite uma letra: ").upper()
    if letra == L[0]:
        print("\nParabéns, você acertou!")
        print(L[0])
        break
    for j in range(len(L[0])):
        if letra == L[0][j]:
            secreta[j] = L[0][j]
    print()
    print(secreta)
    print()        

