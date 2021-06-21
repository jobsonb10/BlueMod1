# Utilizando os conceitos aprendidos até estruturas de repetição, crie um 
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de 
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha 
# de quantidade de rodadas, se não finalize o programa


import random

continuar = 0

while continuar == 0:
    PC = 0
    usuario = 0
    quantidadeRodadas = int(input("Quantas rodadas iremos fazer? "))   
    while quantidadeRodadas > 0:
        quantidadeRodadas -= 1
        escolha = int(input("Escolha um:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n"))
        escolhaPC = random.randint(1,3)
        
        print()
        if escolha == 1:
            if escolhaPC == 2:
                print("[Pedra x Papel]")
                print("Você perdeu!")
                PC += 1 
            elif escolhaPC == 3:
                print("[Pedra x Tesoura]")
                print("Você ganhou!")
                usuario += 1
            else:
                print("[Pedra x Pedra]")
                print("Empate!")
        
        elif escolha == 2:
            if escolhaPC == 1:
                print("[Papel x Pedra]")
                print("Você ganhou!!")
                usuario += 1
            elif escolhaPC == 2:
                print("[Papel x Papel]")
                print("Empate!")
            else:
                print("[Papel x Tesoura]")
                print("Você perdeu!")
                PC += 1

        elif escolha == 3:
            if escolhaPC == 1:
                print("[Tesoura x Pedra]")
                print("Você perdeu!!")
                PC += 1
            elif escolhaPC == 2:
                print("[Tesoura x Papel]")
                print("Você ganhou!")
                usuario += 1 
            else:
                print("[Tesoura x Tesoura]")
                print("Empate!")

        else:
            print("Opção inválida, tente novamente!")
            quantidadeRodadas += 1  
        print()


    print(f"Computador: {PC}\nVocê: {usuario}\n")
    if usuario > PC:
        print("Você ganhou o jogo, parabéns!")
    elif PC > usuario:
        print("Você perdeu o jogo!")        
    else:
        print("Vocês empataram!!")
    
    print()

    continuar = int(input("Deseja jogar novamente? [Sim/Não]").lower()[0].replace("s", "0").replace("n", "1"))