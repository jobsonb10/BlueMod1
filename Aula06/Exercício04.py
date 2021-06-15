qtd = int (input("Informe quantos números serão somados"))
soma = 0
cont = 0

if qtd < 1:
    print("Obrigado!")

soma = int (input("Digite um número: "))

for i in range(1,qtd):
    cont = int (input("Digite outro número: "))
    soma = soma + cont

print(f"Total: {soma}")