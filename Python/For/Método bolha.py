from random import shuffle
numeros = int (input('Digite o número de elementos da lista: '))
lista = list(range(numeros))
shuffle(lista)

trocas = 1
fim = len(lista)-1

while fim > 1:
    trocou = False
    i = 0
    while i < fim:
        if lista[i] > lista[i+1]:
            print (f'Troca n° {trocas}: {lista[i]} <-> {lista[i+1]}' )
            lista [i], lista[i+1] = lista [i+1], lista[i]
            trocas +=1
            trocou = True
        i += 1
    if not trocou:
        break
    fim -= 1

print ('''
Lista organizada:''')

for n in range (len(lista)-1):
    print (n, end=', ')
    
print (f'{lista[-1]}.')
print ()
print (f'A quantidade de trocas foi de {trocas-1}')
  
    
    
    
