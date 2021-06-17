# #01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

print()
opcao = 0
maior = 0

valor1 = float (input("Digite o primeiro valor: "))
valor2 = float (input("Digite o segundo valor: "))

while opcao != 5: 
    print("\nSelecione uma das opções: ")
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    opcao = int (input())
    
    
    
    if opcao < 1 or opcao > 5:
        print()
        print("Número inválido!!")
    
    
    elif opcao == 1:
        print()
        print(f"Resultado da soma entre {valor1} e {valor2} é = {valor1 + valor2}\n")
    
    
    
    elif opcao == 2:
        print()
        print(f"Resultado da multiplicação entre {valor1} e {valor2} é = {valor1 * valor2}\n")
    
    
    
    
    elif opcao == 3:
        print()
        if valor1 > valor2:
            print(f"O maior entre os dois números é: {valor1}")
        elif valor1 < valor2:
            print(f"O maior entre os dois números é: {valor2}")
        else:
            print("Os números são iguais!")
    
    
    
    elif opcao == 4:
        print()
        valor1 = float (input("Digite o primeiro valor: "))
        valor2 = float (input("Digite o segundo valor: "))
    

    else:
        print()
        print("Muito obrigado!")
   


if opcao < 1 or opcao > 5:
    print("Número inválido!!")





