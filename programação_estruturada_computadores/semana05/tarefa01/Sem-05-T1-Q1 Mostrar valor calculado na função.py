'''Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:
def calcular(a, b, c):
return 2 * a + 5 * b - c'''
print("Nesse programa será realizado a operação matemática '2 * a + 5 * b - c', insira três valores correspondentes a, b, c.")

def operação(a, b, c):
    return 2 * a + 5 * b - c

def main():

    a = int(input("Insira um valor para a:"))

    b = int(input("Insira um valor para b:"))

    c = int(input("Insira um valor para c:"))

    print(f'O resultado da opereção 2 * a + 5 * b - c será {operação(a,b,c)}.')

if __name__ =='__main__':
    main()