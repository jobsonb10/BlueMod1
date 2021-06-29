def autoriza_voto(anoNascimento):
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

def votacao(autorizacao,voto):
    candidato1 = "Bolsonaro"
    candidato2 = "Lula"
    candidato3 = "Janice"


    if autorizacao == "Negado":
        return "Você não pode Votar!"
    else:
        print("Seja bem - vindo!")
        print("Dê o seu voto:")
        print(f"[1] {candidato1}")
        print(f"[2] {candidato2}")
        print(f"[3] {candidato3}")
        print(f"[4] Voto nulo")
        print(f"[5] Voto em branco")
        voto = int(input())
        return voto


continuar = 0
candidato1 = "Bolsonaro"
candidato2 = "Lula"
candidato3 = "Janice"

while continuar == 0:
    anoNascimento = int(input("Informe seu ano de nascimento: "))
    print("Seja bem - vindo!")
    print("Dê o seu voto:")
    print(f"[1] {candidato1}")
    print(f"[2] {candidato2}")
    print(f"[3] {candidato3}")
    print(f"[4] Voto nulo")
    print(f"[5] Voto em branco")
    voto = int(input())


    autoriza_voto(anoNascimento)
    
    
    
    
    
    votacao(autoriza_voto(anoNascimento))
    
