# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, 
# ela deve crescer 0,5 cm


class modelar:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self,anos):

        self.idade += anos
        if self.idade < 21:
            self.altura += (0.005 * anos)
    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos
    
    def crescer(self, metros):
        self.altura += metros

nome = input("Nome: ").title()
idade = int(input("Idade: "))
peso = float(input("Peso: ").replace(",","."))
altura = float(input("Altura: ").replace(",","."))

pessoa = modelar(nome, idade, peso, altura)
print("Selecione uma opção: ")
print("[1] Envelhecer")
print("[2] Engordar")
print("[3] Emagrecer")
print("[4] Crescer")
acao = input()

if acao == "1":
    anos = int(input("Quantos anos vai envelhecer? "))
    pessoa.envelhecer(anos)
elif acao == "2":
    quilos = float(input("Quantos quilos vai engordar? ").replace(",","."))
    pessoa.engordar(quilos)
elif acao == "3":
    quilos = float(input("Quantos quilos vai emagrecer? ").replace(",","."))
    pessoa.emagrecer(quilos)
else:
    metros = float(input("Quantos metros vai crescer? ").replace(",","."))
    pessoa.crescer(metros)

print("\nNovos atributos: ")
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Peso: {pessoa.peso}")
print(f"Altura: {pessoa.altura}")