#questao03
'''
Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da divisão inteira dos valores.
'''
import math
valor_1 = float(input("Insira o valor do dividendo:"))
valor_2 = float(input("insirao valor do divisor")) 
divisao = valor_1 // valor_2
resto = valor_1 % valor_2
print(f'O valor do quocienta da divisão será de {divisao:.4f}')
print(f'O valor do quocienta da divisão será de {resto:.4f}')