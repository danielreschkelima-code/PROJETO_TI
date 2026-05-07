# Exercício 6 - Estrutura de Repetição - 02/07/2024
# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
import time
# Imprime um em baixo do outro:
x = 1
while x <= 20:
    print (x)
    x += 1

# Imprime um do lado do outro:
x = 1
while x < 20:
    print (x,end =', ')
    x += 1
    time.sleep(0.5)
print (x,end ='.')
print ('\nFim!') # \n representa representa o carcatere de nova linha.
