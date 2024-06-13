#questao 05
'''
Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima:
• Área do piso da sala: largura * comprimento
• Volume da sala: largura * comprimento * altura
• Área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento
'''
altura = float(input("Insira a o valor correspondente a alura da sala:").strip())
comprimento = float(input("Insira a o valor correspondente a comprimento da sala:").strip())
largura = float(input("Insira a o valor correspondente a largura da sala:").strip())
area_piso_sala = largura * comprimento
volume_sala = largura * comprimento * altura
area_paredes_sala = 2 * altura * largura + 2 * altura * comprimento
print(f'A área do piso da sala será de {area_piso_sala:.2f} m².')
print(f'O volume da sala será de {volume_sala:.2f} m³.')
print(f'A área das paredes da sala será de {area_paredes_sala:.2f} m².')