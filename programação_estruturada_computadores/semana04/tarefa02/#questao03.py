#questao03
'''
Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit
(baseado na fórmula abaixo):
Fahrenheit = (Celsius x (9 / 5)) + 32
'''
print("Vamos descobrir a temperatura em graus Fahrenheit, se basenado na temperatura em graus Celsius.")
celsius = float(input("Qual a temperatura atual em graus Celsius? ").strip())
fahrenheit = (celsius * (9 / 5)) + 32
print(f'Então a temperatura em Fahrenheit será de {fahrenheit}°')