def autoriza_voto(anoNascimento):  #Verifica se o eleitor está apto a votar, obrigado a votar ou tem o voto opcional
    anoAtual = 2021
    idade = anoAtual - anoNascimento
    if idade >= 18 and idade <= 70:
        autorizacao = "Obrigatório"
        return autorizacao
    elif idade < 16 and idade >= 0:
        autorizacao = "Negado"
        return autorizacao
    else:
        autorizacao = "Opcional"
        return autorizacao

def votacao(autorizacao,voto): #Valida e computa o voto no seu respectivo canditato guardando em um dicionário.

    if voto == 1:
        apuracao[candidato1] += 1
        
    elif voto == 2:
        apuracao[candidato2] += 1
        
    elif voto == 3:
        apuracao[candidato3] += 1
        
    elif voto == 4:
        apuracao["Votos nulos"] += 1
        
    elif voto == 5:
        apuracao["Votos em branco"] += 1

    if autorizacao == "Negado":
        return "Você não pode Votar!"
    elif autorizacao == "Opcional":
        return "Voto opcional!"
    else:
        return "Voto obrigatório!"
            
            
candidato1 = "Bolsonaro"
candidato2 = "Lula"
candidato3 = "Janice"
maior = 0           #variavel pra verificar qual é o candidato com maior numero de votos
eleito = 0          # variavel que salva o nome do candidato com maior numero de votos
        
apuracao = {candidato1: 0, candidato2: 0, candidato3: 0, "Votos nulos": 0, "Votos em branco": 0}
continuar = "0"


while continuar == "0":
    anoNascimento = int(input("Informe seu ano de nascimento: "))
    print("Seja bem - vindo!")
    print("Dê o seu voto:")
    print(f"[1] {candidato1}")
    print(f"[2] {candidato2}")
    print(f"[3] {candidato3}")
    print(f"[4] Voto nulo")
    print(f"[5] Voto em branco")
    voto = int(input())
    if voto < 1 or voto > 5:        #verificação pra garantir que o usuario escolha apenas os candidatos disponiveis
        print("Comando inválido!")
    else:
        print(votacao(autoriza_voto(anoNascimento), voto))
    
    
    continuar = input("Deseja computar outro voto? [SIM/NÃO]").upper()[0].replace("S", "0").replace("N", "1")
    print()

print("Resultado da votação")
for c in apuracao:                #printar o resultado da votaçao
    print(c + ":",apuracao[c])


for i in apuracao:                # verificar dentre os valores do dicionario qual é o maior numero e qual seu respectivo candidato
    if apuracao[i] > maior:
        maior = apuracao[i]
        eleito = i

contador = 0

for empate in apuracao:          # verificar se esse numero(que é o maior) se repete mais de uma vez, havendo assim um empate
    if maior == apuracao[empate]:
        contador += 1

if contador > 1:
    print("A votação terminou empatada!")
else:
    print()
    print(eleito, "venceu a votação!")