#questao03
'''
A fábrica de doces precisa de ajuda para embalar os doces corretamente. Cada pacote deve conter um número inteiro de doces. Peça ao usuário para inserir o número de doces produzidos e o número de pacotes disponíveis.
Divida os doces igualmente entre os pacotes fazendo a divisão inteira para garantir que cada pacote contém a mesma quantidade de doces. Imprima o número de doces em cada pacote.
'''
qnt_doce = int(input("Insira a quantidade de doces que serão embrulhados:"))
qnt_pacote = int(input("Insira o número de pacotes dispóniveis para embalar os doces:"))
doces_embados = qnt_doce // qnt_pacote
print(f'Então cada pacote terá {doces_embados} doces.')