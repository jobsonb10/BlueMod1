# 5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

# IMC = peso/(altura**2)

def IMC(peso,altura):
    imc = peso/(altura**2)
    return imc

peso = 75
altura = 1.68
print(f"Seu IMC é: {IMC(peso,altura):.2f}")
