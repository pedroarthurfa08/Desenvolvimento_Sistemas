#questao05
'''
A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa Escreva um programa
que leia o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. Mostre na tela quanto será a bonificação do funcionário.
'''
temp_serviço = float(input("Insira o seu tempo de serviçona empresa:"))
valor_bonificacao = float(input("Insira o valor da bonificação que você receberá da empresa:"))
vt_bonificacao = temp_serviço * valor_bonificacao
print(f'Então o valor que você receberá de bonificação da empresa que você trabalhou será de R$ {vt_bonificacao:.2f}')