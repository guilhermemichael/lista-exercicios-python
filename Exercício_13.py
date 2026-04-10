# 13. Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes.

gigabytes = float(input("Digite o tamanho do arquivo em Gigabytes: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024

print(f"O tamanho do arquivo em Megabytes é: {megabytes:.2f} MB")
print(f"O tamanho do arquivo em Kilobytes é: {kilobytes:.2f} KB")