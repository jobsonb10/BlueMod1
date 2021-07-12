# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

dados = list()
dadosTotais = dict()
anoAtual = 2021
aposentadoria = 0



nome = input("Digite o seu nome: ")
dados.append(int(input("Qual seu ano de nascimento? ")))
dados.append(anoAtual - dados[0])

ctps = (input("Se não tiver emprego digite 0 se sim digite qualquer outro número: "))
if ctps == "0":
    dados.append("Desempregado")
else:
    dados.append(input("Qual o ano de contratação? "))
    dados.append(input("Qual salário? "))
    aposentadoria = int(dados[2]) -  dados[0]
    aposentadoria += 35
    dados.append(aposentadoria)

# dados[0] = ano de nascimento
# dados[1] = idade
# dados[2] = ano de contratação
# dados[3] = salario
# dados[4] = ano de aposentadoria

print(dados)
dadosTotais[nome] = [dados]


print("--=="*5)
print(f"{nome} \nAno de nascimento: {dadosTotais[nome][0]}")
print(f"\nIdade: {dadosTotais[nome][1]}")
print(f"Contratação: {dadosTotais[nome][2]}")
print(f"Salário: {dadosTotais[nome][3]}")
print(f"Idade de Aposentadoria: {dadosTotais[nome][3]}")



