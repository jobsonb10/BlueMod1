# coding: utf-8

from time import sleep

def introducao():

    reset_color = "\033[0m"
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    blue = "\033[1;34;40m"
    magenta = "\033[1;35;40m"
    cyan = "\033[1;36;40m"

    parte1 =  "São Paulo... 2025.\nAs pessoas andam sem rumo...\nNão sabem mais chegar em suas casas, nem os telefones de seus amigos...\nPerderam a noção de quais são os melhores bares, não conseguem mais avaliar mal os restaurantes,\npararam de dançar por não ter onde postar, deixaram de fotografar seus pratos...\ne a pior catástrofe de todas:\nHá tempos não vemos nenhum #tbt de 2015 daquelas viagens, tatuagens novas e mudanças de cabelo.\n\n \033[1;31;40m A INTERNET FOI ROUBADA! \033[0m"


    parte2 ="\n\033[1;33;40m (AVISO:  ESSE JOGO VEIO DO FUTURO ATÉ VOCÊ, AJUDE O NOSSO HERÓI A FAZER AS ESCOLHAS CERTAS E SALVAR A INTERNET PARA QUE VOCÊ POSSA CONTINUAR COMPARTILHANDO SEUS CÓDIGOS DO KWAI!) \033[0m"

    for char in parte1:
        sleep(0.1)
        print(char,end="",flush=True)

    print("\n",parte2)    




def menu1():
    print("\nDiga alguma coisa e invoque o nosso herói:\n")
    print("[1] Oh e agora quem poderá nos defender?")        
    print("[2] Terra, fogo, vento, água, coração!")        
    print("[3] Se você não conhece nenhuma das frases acima, desligue o computador, geração Z")  
    print()
    escolha = input("Escolhe aí:")
    while escolha not in ["1","2","3"]:
        print("Qual a dificuldade de escolher 1,2 ou 3 ?")
        escolha = input("Escolhe aí:")
    if escolha == "1":
        return 1
    elif escolha =="2":
        print("Pegadinha do Malandro! A gente jamais faria um jogo do Capitão Planeta, esse desenho era muito chato!")
        escolha = input("Escolhe outro aí:")
        while escolha not in ["1","3"]:
            escolha = input("Escolhe OUTRO!:")     
    else:
        print("Obrigado por não jogar!")
        return 3


introducao()
menu1()