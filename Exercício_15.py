# 15. Faça um programa que calcule o salário mensal com descontos de 11% (IR), 8% (INSS) e 5% (sindicato), mostrando salário bruto, descontos e salário líquido.

salario_bruto = float(input("Digite o salário bruto: "))

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%): R$ {ir:.2f}")
print(f"Desconto INSS (8%): R$ {inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")