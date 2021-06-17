# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
#    a) tamanho da lista.
#    b) maior valor da lista.
#    c) menor valor da lista.
#    d) soma de todos os elementos da lista.
#    e) lista em ordem crescente.
#    f) lista em ordem decrescente.


L = [5, 7, 2, 9, 4, 1, 3]
maior = 0
menor = L[0]
soma = 0
cont = 0



for i in L:
    if i > maior:
        maior = i

    if i < menor:
        menor = i
    
    soma = soma + L [cont]
    cont += 1
    

print(len(L))
print(maior)
print(menor)
print(soma)
L.sort()
print(L)
L.reverse()
print(L)