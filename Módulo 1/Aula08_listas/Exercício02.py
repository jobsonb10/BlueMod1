# 2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" 
#    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a 
#    pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
#    como "Cúmplice" e 5 como "Assassino". 
#    Caso contrário, ele será classificado como "Inocente

question = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
L = list(range(len(question)))
soma = 0


for i in range(len(question)):
    L[i] = int(input(f"{question[i]} [SIM/NÃO]: ").upper().replace("A","Ã").replace("NÃO","0").replace("SIM","1"))
    soma = soma + L[i]

print()

if soma == 2:
    print("Você é suspeito(a)! ")
elif soma == 3 or soma == 4:
    print("Você é Cúmplice! ")
elif soma == 5:
    print("Você é assassino(a)!")
elif soma == 0 or soma == 1:
    print("Você é inocente! ")
else:
    print("Reveja suas respostas e tente novamente!")


