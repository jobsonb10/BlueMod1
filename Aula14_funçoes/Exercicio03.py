# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto: que é a quantia de imposto sobre vendas expressa em porcentagem 
# e custo: que é o custo de um item antes do imposto. A função “altera” 
# o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    custoAumentado =  custo * (taxaImposto/100)
    custo += custoAumentado
    return custo

preco = float(input("Qual o preço do item: ").replace(",","."))
imposto = float(input("Qual vai ser a taxa de imposto em porcentagem: ").replace(",","."))
print(f"Preço após a taxação do imposto: {somaImposto(imposto,preco)}")

