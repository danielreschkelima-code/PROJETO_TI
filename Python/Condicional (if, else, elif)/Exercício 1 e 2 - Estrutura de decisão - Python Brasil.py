# Faça um Programa que peça dois números e imprima o maior deles.
# Faça um Programa que peça um valor e mostre na tela
# se o valor é positivo ou negativo.
a = float (input ('Digite qualquer número: '))
b = float (input ('Digite outro número: '))

if a > b:
    print (a)
else:
    if b > a:
        print (b)
    else:
        print ('Os números são iguais...')

if a > 0:
    print ('O primeiro número é positivo.')
else:
    if a < 0:
        print ('o primeiro número é negativo.')
    else:
        print ('O primeiro número é um número nulo.')

if b > 0:
    print ('O segundo número é positivo.')
else:
    if b < 0:
        print ('O segundo número é positivo.')
    else:
        print ('O segundo número é um número nulo.')
            
        

