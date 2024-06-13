#questao03
nt = int(input("Diga o nível de volume atual do seu aparelho:").strip())
nd = int(input("Diga o nível total de volume que deseja ter no seu aparelho:").strip())
dv = nd - nt
print(f'A diferença entre o nível de volume atual do seu aparelho e a total é de: {dv}%')