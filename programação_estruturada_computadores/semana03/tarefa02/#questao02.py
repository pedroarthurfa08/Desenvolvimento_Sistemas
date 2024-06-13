#questão02
'''
Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado para duas casas decimais.
'''
import math
preço = float(input("Insira o preço a ser descontado:"))
preço_desconto = preço * 0.90
preço_desconto = round(preço_desconto,2 )
print(f'O valor do desconto será de {preço_desconto}reias.')