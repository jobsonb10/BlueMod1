# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.

def comparacao(valor1,valor2):
    if valor1 > valor2:
        return valor1
    elif valor1 < valor2:
        return valor2
    else:
        igual = "Os numeros são iguais"
        return igual


n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

print(comparacao(n1,n2))

