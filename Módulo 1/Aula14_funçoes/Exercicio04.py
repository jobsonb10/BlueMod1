# Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calculoSalario(horasTrabalhadas,reaisHora):
    if horasTrabalhadas > 40:
        horasTrabalhadas = horasTrabalhadas - 40
        salarioComExtra = reaisHora * 1.5
        horasTrabalhadas = horasTrabalhadas * salarioComExtra
        salario = horasTrabalhadas + (40 * reaisHora)
     
    else:
        salario = horasTrabalhadas * reaisHora
        
    return salario
reaisHora = 7
horasTrabalhadas = int(input("Quantas horas você trabalhou? "))
print(f"O seu salário é:{calculoSalario(horasTrabalhadas,reaisHora)}")
