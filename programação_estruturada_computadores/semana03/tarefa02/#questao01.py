#questao01
'''
Escreva um programa que leia o valor de um raio, calcule e mostre na tela o comprimento da circunferência, a área do círculo, a área da esfera e o volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais.
'''
import math
PI = 3.141592
raio = float(input("Insira o número do raio no qual se deseja descobrir a circunferência, a área do círculo, a área da esfera e o volume da esfera:"))
circunferencia=2*PI*raio
print(f'Circunferencia: {circunferencia:.6f}')
a_circulo=PI*raio**2
print(f'Área do cículo: {a_circulo:.6f}')
a_esfera=4*PI*raio**2
print(f'Área da esfera: {a_esfera:.6f}')
vol_esfera=4/3*PI*raio**3
print(f'Volume da esfera: {vol_esfera:.6f}')