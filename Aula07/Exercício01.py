#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


peso = float (input("Digite um peso: ").replace(",","."))
maior = peso
menor = peso

for i in range(4):
    peso = float (input("Digite outro peso: ").replace(",","."))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print()
print(f"O maior peso dentre os 5 é: {maior}")
print(f"O menor peso dentre os 5 é: {menor}")
