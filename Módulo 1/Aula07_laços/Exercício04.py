#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#     Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

quantidadeNumeros = 6
soma = 0
quantidadePares = 0


for i in range(quantidadeNumeros):
    number = int (input("Digite um número inteiro: "))
    if number % 2 == 0:
        soma = soma + number
        quantidadePares += 1

print()
print(f"{quantidadePares} números pares foram encontrados! ")
print(f"A soma desses números é: {soma}!")