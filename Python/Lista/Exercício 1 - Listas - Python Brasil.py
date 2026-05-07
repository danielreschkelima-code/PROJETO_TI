# Exercício 1 - Listas - Python Brasil

#           0       1       2       3           4       5           6
cores = ['red', 'violet', 'blue', 'orange', 'yellow', 'green', 'magneta']
#          -7       -6      -5      -4          -3      -2          -1

i = 0 # ou seja, cor = red
while i < len(cores): # repete até que o índice chegue ao final da lista
    print (f'{i}) {cores[i]}') # irá printar a cor correspondente do valor de i
    i += 1 # vai para próxima opnião

print ('\nCores em ordem decrescente com números POSITIVOS...')
i = 6
while i >= 0:
    print (f'{i}) {cores [1]}')
    i -=1 # vai para cor anterior

print('\nCores em ordem decrescente com números NEGATIVOS...')
i = -1
while i >= -len(cores):  # vai parar quando for -8
    print(f'{i}) {cores[i]}')
    i -= 1  # vai para a cor anterior
