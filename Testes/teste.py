### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

# print("--=="*5)
# print(f"{nome} \nIdade: {idade}")
# print(f"\nCTPS: {trabalhador[nome][1]}")
# print(f"Contratação: {trabalhador[nome][2]}")
# print(f"Salário: {trabalhador[nome][3]}")
# print(f"Idade de Aposentadoria: 


lista1 = []
listaF = []

while inicio == 'S':
    inicio = input('Você deseja fazer um cadastro? [S/N]').upper()
    nome = input('Digite o seu nome: \n')
    sexo = input('Digite seu sexo biológico: [F/M] \n').upper()
    idade = input('Qual sua idade? \n')
    dic1 = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    lista1.append(dic1[:])
    if sexo =='F':
        listaF.append(dic1[:])
