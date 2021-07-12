import random
class Lancador():
    def __init__(self,objetoLancado):
        if objetoLancado == 'dado':
            self.objeto = objetoLancado
        else:
            self.objeto = objetoLancado
            self.moeda = ['Cara', 'Coroa']

    def jogarObjeto(self):
        if self.objeto == 'moeda':
            randomNumber = random.choice(self.moeda)
            print('Sua Moeda deu', randomNumber) 
        else: 
            randomNumber = random.randint(1,6)
            print('Número do dado', randomNumber) 

objetoLancado = int(input('O que você deseja Lançar?\n[1] Cara ou Coroa.\n[2] Dado.'))
if objetoLancado == 1:
    moeda = Lancador('moeda')
    moeda.jogarObjeto()
elif objetoLancado == 2:
    dado = Lancador('dado')
    dado.jogarObjeto()
