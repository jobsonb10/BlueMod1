# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).

def conceito(nota):
    if nota >= 9:
        notaLetra = "A"
    elif nota >= 8:
        notaLetra = "B"
    elif nota >= 7:
        notaLetra = "C"
    elif nota >= 6:
        notaLetra = "D"
    elif nota > 4:
        notaLetra = "E"
    else:
        notaLetra = "F"

    return notaLetra    


nota = float(input("Inform sua nota: ").replace(",","."))
if nota > 10 or nota < 0:
        print("Nota inválida")
else:
    print(f"Sua nota em conceito: {conceito(nota)}")