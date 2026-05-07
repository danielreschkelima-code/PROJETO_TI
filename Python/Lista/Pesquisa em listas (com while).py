# Pesquisa em listas (com while) - 10/10/2024
# pesquisa linear,
# imprimir todas as posições em que o número for encontrado

L = [15, 7, 27, 39]

L = L*5

p = int(input('Digite um número para procurar: '))
achou = False

i = 0
while i < len(L):
    if L[i] == p:
        if achou == False:  # primeira vez que encontrou
            print(f'{p} foi encontrado na posições: {i}', end=', ')
            achou = True
        else:  # proximas vezes que encontrou
            print(i, end=', ')
    i+=1

if achou == False:
    print(f'{p} não foi encontrado na lista L.')
else:
    print('da lista L.')  # termina a frase quando encontrou elementos


