# 1.	Faça um programa,com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

def somar(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma

num = list()

num.append(int(input("Digite um número")))
num.append(int(input("Digite um número")))
num.append(int(input("Digite um número")))

print(somar(num[0],num[1],num[2]))

