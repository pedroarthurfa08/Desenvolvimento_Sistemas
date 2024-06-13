#questao04
'''
Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a última meia-noite até a hora lida.
'''
print("Vamos descobrir quantos segundos se passaram desde a meia-noite")
hora = int(input("Insira uma quantidade de horas:"))
minuto = int(input("Insira uma quantidade de minutos:"))
segundos = int(input("Insira uma quantidade de segundos:"))
h1 = hora * 3600
m2 = minuto * 60
total_segundos = h1 + m2 + segundos
print(f'A quantidade de segundos total será de {total_segundos} segundos')