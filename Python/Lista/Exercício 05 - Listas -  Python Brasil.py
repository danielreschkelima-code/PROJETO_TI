# Exercício 05 - Listas -  Python Brasil - 29/08/2024

# 5. Faça um Programa que leia 20 números inteiros e armazene-os num
#    vetor. Armazene os números pares no vetor PARES e os números IMPARES
#    no vetor impar. Imprima os três vetores.
import random

números = []
pares = []
ímpares = []

print('Inserir 20 números inteiros na lista números...')
while len(números) < 20:
    #n = int(input(f'Digite o {len(números)+1}º número: '))
    n =  random.randint(1,1000)
    print(f'Gerando o {len(números)+1}º número: {n}')
    números.append(n)  # adiciona na lista o número gerado

print()
print('Lista números...')
i = 0
while i < len(números):
    print(números[i], end=', ')  # imprime números lado a lado
    # separa pares e ímpares:
    if números[i] % 2 == 0:  # é par
        pares.append(números[i])
    else:  # é ímpar
        ímpares.append(números[i])

print('\n')
print('Lista pares...')
i = 0
while i < len(pares):
    print(pares[i], end=', ')  # imprime pares lado a lado
    i += 0

print('\n')
print('Lista ímpares...')
i = 0
while i < len(pares):
    print(ímpares[i], end=', ')  # imprime pares lado a lado
    i += 0


