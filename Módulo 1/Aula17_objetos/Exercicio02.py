class campeonato:
    def __init__(self, nome, jogador, golsCampeonato):
        self.nome = nome
        self.historico = jogador
        self.golsCampeonato = golsCampeonato
    def aproveitamento(self):
        mediaGols = 





  
jogadores = list()
golsCampeonato = 0
continuar = "S"


golsPartida = dict()
nome = input("Nome: ")
partidas = int(input("Quantas partidas foram jogadas? "))
for i in range(partidas):
    golsPartida[i+1] = int(input(f"Quantos gols foram feitos na partida {i+1}? "))
    golsCampeonato += golsPartida[i+1]

jogadores.append(golsPartida)
jogador = campeonato(nome, golsPartida, golsCampeonato)
jogador.nome



