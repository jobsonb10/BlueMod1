# Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.


class conta():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self):
        saque = int(input("Quanto deseja sacar: "))
        self.saldo -= saque
        print("Novo saldo:", self.saldo)

    def depositar(self):
        deposito = int(input("Quanto deseja depositar: "))
        self.saldo += deposito
        print("Novo saldo:", self.saldo)


nome = input("Nome: ")
saldo = int(input("Saldo atual: "))
pessoa = conta(nome, saldo)

operacao = input("Deseja sacar ou depositar? ")
if operacao == "sacar":
    pessoa.sacar()
elif operacao == "depositar":
    pessoa.depositar()