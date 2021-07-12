# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma 
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando 
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

listaFinal = []
listaMulheres = []
listaIdades = []
IdadesAcimaMedia = []
continuar = "S"
cadastros = 0
mediaIdades = 0

while continuar == "S":
    
    cadastros += 1
    dicionario = {}
    nome = input("\nNome: ")
    sexo = input("Sexo[M/F]: ").upper()
    while sexo != "F" and sexo != "M":
        print("Dado inválido!")
        sexo = input("Sexo[M/F]: ").upper()

    idade = int(input("Idade: "))
    listaIdades.append(idade)
    mediaIdades += idade
    dicionario[nome] = [sexo, idade]
    
    listaFinal.append(dicionario)
    
    if sexo == "F":
        listaMulheres.append(dicionario)
    
    while True:
        continuar = input("\nDeseja continuar? [S/N]").upper()
        if continuar != "S" and continuar != "N":
            print("Opção inválida, tente novamente!")
        else:
            break



mediaIdades = mediaIdades/cadastros

for i in range(len(listaIdades)):
    if listaIdades[i] > mediaIdades:
        IdadesAcimaMedia.append(listaIdades[i])


print("-"*25)
print(f"Número de pessoas cadastradas: {cadastros}")
print(f"Média das idades: {mediaIdades} anos.")
print(f"Mulheres: {listaMulheres}")
print(f"Idades acima da média: {IdadesAcimaMedia}")
print("-"*25)