# 6. Desafio: 
# Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, 
# assim como o nome desses alunos, o programa tem que calcular a média desse aluno e mostrar a situação dele,
# seguindo os mesmos critérios apresentados no exercício 3. 
# No final apresente todos nomes, as 5 notas, as médias e as situações dos 15 alunos de uma vez só.


quantidadeAlunos = 2
quantidadeNotas = 3
nota = 0
listaNotas = list()
mediaNotas = 0
nome = list()
dicionario = dict()


for i in range(quantidadeAlunos):
    nome.append(input("Nome: ").title())
    cont = 0
    for j in range(quantidadeNotas):
        cont += 1
        while True: 
            nota = int(input(f"Nota {cont}: "))
            if nota < 0 and nota > 10:
                print("\nNota inválida, digite novamente!\n")
            else:
                listaNotas.append(nota)
                break
        mediaNotas += listaNotas[j]
    
    dicionario[nome[i]] = [listaNotas]    

    mediaNotas = mediaNotas/quantidadeNotas

    for aprovacao in range(len(listaNotas)):
        if listaNotas[aprovacao] >= 7:
            dicionario[nome[i]] = "Aprovado"
        elif listaNotas[aprovacao] >= 5:
            dicionario[nome[i]] = "Recuperação"
        else:
            dicionario[nome[i]] = "Reprovado"
    listaNotas = list()    


print(dicionario)