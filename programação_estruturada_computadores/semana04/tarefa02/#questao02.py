#questao02
'''
Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa
expressa apenas em dias. Considerar sempre os anos com 365 dias e os messes com 30 dias.
'''
print("Vamos descobrir quantos dias de vida você tem desde o dia que nasceu.")
anos = int(input("Quantos anos você tem?"))
meses = int(input("Quantos meses de vida você tem depois que completou ano?"))
dias = int(input("Quantos dias desde o seu útimos mêsversário?"))
anos1 = anos * 365
meses1 = meses * 30
dias_totais = anos1 + meses1 + dias
print(f'Então você tem exatamente {dias_totais} dias de vida.')