#questao04
'''
O tempo é algo legal, especialmente quando você vai calcular quantos minutos há em um número específico de segundos. Peça ao usuário para inserir um número de segundos. Em seguida, use a divisão inteira para mostrar esse tempo em minutos (lembre-se, 1 minuto = 60 segundos) e use o resto da divisão inteira para saber quantos segundos
sobram. Imprima os resultados.
'''
segundos = int(input("Insira uma quantidade de segundos:"))
minutos = segundos // 60
segundos_sobram = segundos % 60
print(f'A quantidade de {segundos} em minutos é {minutos} e sobram {segundos_sobram} segundos.')
{segundos_sobram}