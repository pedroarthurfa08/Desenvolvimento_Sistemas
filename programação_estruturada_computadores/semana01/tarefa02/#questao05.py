#questao05
kmateM = float(input("Quantos quilometros (km), daqui até marte? ").strip())
kmdanave = float(input("Quantos quilometros/hora (km/h), a sua nave espacial atinge? ").strip())
tempmart = kmateM / kmdanave
print(f'Então você deverá chegar em Marte em {tempmart} horas.')