# Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, 
# sendo que nesses casos Fevereiro terá 29 dias.


import datetime

def check_date(day, month, year):
    correctDate = None
    try:
        newDate = datetime.datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate


def formatacao(dia, mes, ano):
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    calendario = dict()
    
    calendario["1"] = "Janeiro"
    calendario["2"] = "Fevereiro"
    calendario["3"] = "Março"
    calendario["4"] = "Abril"
    calendario["5"] = "Maio"
    calendario["6"] = "Junho"
    calendario["7"] = "Julho"
    calendario["8"] = "Agosto"
    calendario["9"] = "Setembro"
    calendario["10"] = "Outubro"
    calendario["11"] = "Novembro"
    calendario["12"] = "Dezembro"

    mes = calendario.get(str(mes))

    dataExtenso = str(dia) + " de " + mes + " de " + str(ano)
    return dataExtenso
    



data = input("Informe a data")

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

correctdate = check_date(dia, mes, ano)

if correctdate:
    dataEscrita = formatacao(dia,mes, ano)
    print(dataEscrita)
else:
    print("Data incorreta!")