import os
import time

def limpar_tela():
    if os.name == 'nt': #windows
        os.system('cls')
    else:
        os.system('clear')
limpar_tela()

coração = ["  ⬜⬜  ⬜⬜  ","⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜","  ⬜⬜⬜⬜⬜  ","    ⬜⬜⬜    ","      ⬜"]

print("Brandon, apesar de gostar muito do terminal, te prefiro um milhão de vezes. Por isso uso dele para ti, e não o contrário:")
time.sleep(3.5)
print()

def imprimir(a):
    for i in range (0,len(coração)):
        print(coração[i])
        time.sleep(a)

imprimir(0.5)
print()
imprimir(0.5)
print()
imprimir(0.5)
limpar_tela()

c = "<3"
contador = 0
while contador < 30:
    print(c)
    print()
    imprimir(0.1)
    print()
    contador += 1
    time.sleep(0.1)

time.sleep(2)
limpar_tela()

print("EU TE AMO MUITO MUITO MUITO MUITO MUITO!")
