#questao04
'''
Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente.
'''
import math
minutos = int(input("Digite uma quantidade de minuntos:"))
h = minutos // 60
m = minutos % 60
print(f'A quantidade de {minutos} formatada para horas será de {h}h e {m}min.')