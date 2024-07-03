#questao01
'''
Escreva um programa que leia dois valores e mostre na tela, nessa ordem:
a. A soma dos números;
b. A concatenação das strings;
c. A multiplicação dos números;
d. A multiplicação como strings;
e. A divisão dos números;
f. A divisão inteira dos números;
g. A exponenciação;
h. O módulo (resto).
'''
n1 = float(input("Insira um número:"))
n2 = int(input("Insira outro número:"))
n3 = str(n1)
n4 = str(n2)
soma = n1 + n2
concatenação = n3 + n4
multiplicação = n1 * n2
multiplicação_strings = n2 * n3
divisao = n1 / n2
divisao_inteira = n1 // n2
exponeciação = n1 ** n2
modulo = n1 % n2
print(f'A soma destes dois números será: {soma}')
print(f'A concatenação destes dois números será: {concatenação}')
print(f'A multiplicação destes dois números será: {multiplicação}')
print(f'A multiplicação de strings destes dois números será: {multiplicação_strings}')
print(f'A divisão real destes dois números será: {divisao}')
print(f'A divisão interia destes dois números será: {divisao_inteira}')
print(f'A exponeciação destes dois números será: {exponeciação}')
print(f'O módulo ou o resto da divisão destes dois números será: {modulo}')