#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

number = int (input("Digite um número inteiro: "))

for i in range(11):
    print(f"{number}  x  {i}  =  {i*number}")