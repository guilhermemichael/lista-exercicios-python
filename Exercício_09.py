# 9. Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = (fahrenheit - 32) * 5.0/9.0

print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")