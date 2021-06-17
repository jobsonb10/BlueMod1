#03 - Crie um programa que leia o ano de nascimento de sete pessoas. 
#     No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

anoAtual = 2021
maiores = 0
menores = 0

for i in range(7):
    anoNascimento = int (input("Digite um ano de nascimento: "))
    if (anoAtual - anoNascimento) <0:
        print("Essa pessoa não nasceu ainda!!")
    elif (anoAtual - anoNascimento) < 18:
        menores += 1
    elif (anoAtual - anoNascimento) >= 18:
        maiores += 1


print()
print(f"{maiores} pessoas já são maiores de idade! ")
print(f"{menores} pessoas ainda não atingiram a maioridade!")