
def menu1():
    print("\nSiga-me os bons!\n")
    print("[1] COPAN")        
    print("[2] IBIRAPUERA")        
    print("[3] ESTAÇÃO DA LUZ")  
    print("[4] MASP")
    escolha = input("Escolhe aí:")
    while escolha not in ["1","2","3","4"]:
        print("Escolha inválida")
        escolha = input("Escolhe aí:")
    if escolha == "1":
        escolha1("1")
    elif escolha =="2":
        escolha1("2")
    elif escolha == "3":
        escolha1("3")            
    else:
        escolha1("4")

def escolha1(escolha):
    if escolha == "1":
        print("Em meio ao grande bloco de concreto em formato de onda, depois de bater na porta de mais de mil apartamentos, o gafanhoto vermelho encontra em um corredor a sua primeira pista: Um tapa-olho!")
        menu_vilao()
    elif escolha == "2":
        print("Nosso herói percorreu todos os museus, pistas de skate, e até dentro do lago ele procurou por mais pistas, mas não encontrou nada!")
        menu1()
    elif escolha == "3":
        print("Nessa estação, o Chapolin encontrou um padre, o padre precisava de uma ajuda: 'Ajuda' ")
        ajuda = input("Você acha que o herói deve ajudar o padre ou não? [S/N]: ").upper()
        while ajuda not in ["S","N"]:
            ajuda = input("Opção inválida! Digite novamente. [S/N]").upper()
        if ajuda == "S":
                chapolin.respect += 1
        menu1()
    elif escolha == "4":
        print("Abaixo do imenso vão livre do MASP, ele encontrou uma artesã, que disse ter visto um homem fugindo de algo.")
        print('Disse também ter ouvido ele falar que matou o mar morto')
        menu_vilao()
    
def menu_vilao():
    opcao = 1
    while opcao == 1:
        print("\nEaí, já sabe qual o vilão que roubou a internet? ")
        print("\n[1] Opção 1")
        print("[2] Alma Negra")
        print("[3] Opção 3")
        print("[4] Opção 4")
        vilao = input()

        if vilao == "2":
            print("Isso aí, o pirata Alma negra foi o responsável por essa atrocidade. Agora seu dever é encontrá-lo para recuperar a internet!")
            break
        else:
            opcao = int(input("[1] Tentar acertar o vilão novamente\n[2] Voltar e tentar encontrar mais pistas"))
            if opcao == 2:
                menu1()
                break
    



menu1()