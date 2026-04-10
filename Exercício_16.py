# 16. Faça um programa para calcular a quantidade de latas de tinta (18L, R$ 80,00) necessárias para pintar uma área, considerando 1L para 3m², e o preço total.

import math


area = float(input("Digite a área a ser pintada em m²: "))

litros = area / 3
latas = math.ceil(litros / 18)
preco = latas * 80

print(f"Quantidade de latas de tinta necessárias: {latas}")
print(f"Preço total: R$ {preco:.2f}")