import random

class acao():

    def __init__(self,quantidadeLados):
        self.quantidadeLados = quantidadeLados

    def jogar(self):
        return random.randint(1,self.quantidadeLados)


continuar = "S"
while continuar == "S":
    object = input("Qual objeto? [moeda ou dado] ").lower()
    if object == "moeda":
        object = acao(2)
        if object.jogar() == 1:
            print("Sua moeda deu cara!")
        else:
            print("Sua moeda deu coroa!")

    if object == "dado":
        object = acao(6)
        print(f"Seu dado parou no número: {object.jogar()}")
    print()
    continuar = input("Deseja girar outro objeto? [S/N]").upper()
