"""
17. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math

area = float(input("Digite a área a ser pintada em m²: "))
litros = (area / 6) * 1.10

# Situação 1: Comprar apenas latas de 18 litros
latas = math.ceil(litros / 18)
preco_latas = latas * 80
print(f"Situação 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas necessárias: {latas}")
print(f"Preço total: R$ {preco_latas:.2f}")

# Situação 2: Comprar apenas galões de 3,6 litros
galoes = math.ceil(litros / 3.6)
preco_galoes = galoes * 25
print(f"\nSituação 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões necessários: {galoes}")
print(f"Preço total: R$ {preco_galoes:.2f}")

# Situação 3: Misturar latas e galões
latas_mistura = math.floor(litros / 18)
resto_litros = litros - (latas_mistura * 18)
galoes_mistura = math.ceil(resto_litros / 3.6)
preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)
print(f"\nSituação 3: Misturar latas e galões")
print(f"Quantidade de latas necessárias: {latas_mistura}")
print(f"Quantidade de galões necessários: {galoes_mistura}")
print(f"Preço total: R$ {preco_mistura:.2f}")