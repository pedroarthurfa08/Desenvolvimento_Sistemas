#questao 05
'''
Você é um aprendiz de feiticeiro encarregado de preparar uma poção mágica especial. Para isso, você precisa de porções dos ingredientes mágicos Pó de Lua Estelar, Essência de Dragão e Lágrimas de Fênix. No entanto, cada ingrediente tem um preço diferente no mercado mágico. O ingrediente Pó de Lua Estelar custa 5 moedas de ouro por porção, Essência de Dragão custa 3 moedas de ouro por porção, e o Lágrimas de Fênix custa 8 moedas de ouro por porção. O programa deve começar perguntando quantas porções de cada ingrediente são necessárias para a poção que você está preparando. Depois, o programa deve calcular o custo total baseado na quantidade de cada ingrediente e seus respectivos preços. Finalmente, o programa deve mostrar o custo total para preparar a poção.
Por exemplo, se a porção tem 2 Pó de Lua Estelar, 3 Essência de Dragão e 1 Lágrima de Fênix o custo total será:
(2 * 5) + (3 * 3) + (1 * 8) = 27 (o custo total será de 27 moedas de ouro)
'''
pó_estelar = (5)
essência_dragão = (3)
lágrima_fênix = (8)
print("Bom dia meu nobre!")
qnt_pó_estelar = int(input("Qual a quantidade da porção de Pó de Lua Estelar? "))
vt_pó_de_lua_estela = pó_estelar * qnt_pó_estelar
qnt_essência_dragão = int(input("Qual a quantidade de porção de Essênia de Dragão? "))
vt_essência_dragão = essência_dragão * qnt_essência_dragão
qnt_lágrima_fênix = int(input("Qual a quantidade da porção de lágrimas de Fênix? "))
vt_lágrima_fênix = lágrima_fênix * qnt_lágrima_fênix
valor_total = vt_essência_dragão + vt_pó_de_lua_estela + vt_lágrima_fênix
print(f'O custo total da sua compra será de {valor_total} moedas de ouro.')