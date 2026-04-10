# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Quanto você ganha por hora? "))

horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario = ganho_hora * horas_trabalhadas

print(f"O total do seu salário no mês é: R$ {salario:.2f}")