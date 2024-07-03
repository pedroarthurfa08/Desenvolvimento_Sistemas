#questao05
'''
Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é
ponderada e que o peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é:
média ponderada = (n1 ∗ 2) + (n2 ∗ 3) + (n3 ∗ 5)
                  -----------------------------
                                 10
'''
print("Nesse progrma será avaliado as notas dos alhnos para definir a média final, considerando que a média é poderada e o peso das notas são 2, 3, 5.")
n1 = float(input("Insira o valor da primeira nota: "))
n2 = float(input("Insira o valor da segunda nota: "))
n3 = float(input("Insira o valor da terceira nota: "))
mediaponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
print(f'O valor da média desse aluno será de {mediaponderada}.')