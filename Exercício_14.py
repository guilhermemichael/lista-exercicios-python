# 14. João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho e deve pagar multa de R$ 4,00 por quilo excedente acima de 50 kg; faça um programa que calcule o excesso e a multa.

peso = float(input("Digite o peso do peixe em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print(f"O excesso de peso é: {excesso:.2f} kg")
    print(f"A multa a ser paga é: R$ {multa:.2f}")