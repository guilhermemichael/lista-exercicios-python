# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tempo = (tamanho * 8) / velocidade / 60

print(f"O tempo aproximado de download do arquivo é: {tempo:.2f} minutos")