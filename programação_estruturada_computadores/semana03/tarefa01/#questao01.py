#questao01
'''
Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre quantas fatias cada um recebe e quantas sobram.
'''
qnt_pessoas = int(input("Quantas pessoas iram comer a pizza? "))
fatias_pizza = int(input("São quantas fatias de pizza? "))
fatias_recebidas = qnt_pessoas // fatias_pizza
fatias_sobras = qnt_pessoas % fatias_pizza
print(f'Então serão {fatias_recebidas} pedacos de pizza para cada pessoa.')
print(f'Caso sobre pizza, serão {fatias_sobras} fatias de pizza.')