##Faça um programa para imprimir:
##    1
##    2   2
##    3   3   3
##    .....
##    n   n   n   n   n   n  ... n

print ('Exercício 1')
def números(número):
    lista = []
    for i in range(número):
        lista.append(número)
    return lista
        
n = int (input ('Digite um número inteiro: '))
for i in range(len(números(n))):
    print (números(n)[i], end='  ')

print ('\n\nExercício 2')
def números(número):
    lista = []
    for i in range(número):
        lista.append(i+1)
    return lista
        
n = int (input ('Digite um número inteiro: '))
for i in range(len(números(n))):
    print (números(n)[i], end='  ')
