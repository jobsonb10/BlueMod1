### EXERCICIO 01

frase = input("Digite uma frase: ").lower()
letraA = 0
letraE = 0
letraI = 0
letraO = 0
letraU = 0

for i in frase:
    if i == "a":
        letraA += 1
    elif i == "e":
        letraE += 1
    elif i == "i":
        letraI += 1
    elif i == "o":
        letraO += 1
    elif i == "u":
        letraU += 1

print(f"Foram encontradas {letraA} letras 'A' na frase. ")
print(f"Foram encontradas {letraE} letras 'E' na frase. ")
print(f"Foram encontradas {letraI} letras 'I' na frase. ")
print(f"Foram encontradas {letraO} letras 'O' na frase. ")
print(f"Foram encontradas {letraU} letras 'U' na frase. ")



