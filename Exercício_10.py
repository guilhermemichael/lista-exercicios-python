# 10. Faça um programa que peça a temperatura em graus Celsius, transforme e mostre a temperatura em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9.0/5.0) + 32

print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}°F")