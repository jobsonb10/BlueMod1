# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação 
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para 
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é 
# reprovado.


situacao = dict()
notaMedia = list()

while True:
    nome = (input("Digite o seu nome: "))

    notaMedia.append(int(input("Digite sua média: ")))

    if notaMedia[0] < 0 or notaMedia[0] > 10:
        print("Média inválida, tente novamente!")
        print()
    elif notaMedia[0] >= 7:
        notaMedia.append("Aprovado")
        break

    elif notaMedia[0] < 5:
        notaMedia.append("Reprovado")
        break

    else:
        notaMedia.append("Recuperação") 
        break


situacao[nome] = notaMedia


print(situacao)



