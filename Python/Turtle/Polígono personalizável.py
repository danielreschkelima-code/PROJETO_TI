# Polígono personalizado
import turtle 
import random 

lados = int (input ('Digite a quantidade de lados desejada ou 1 caso queira lados infinitos: '))
cor = input ('Digite a cor desejada em inglês, em hexadecimal ou digite "R" para cores alatórias: ')
a = 0

if lados == 1: # caso escolha infinitos:
    distancia = 30
    angulo = int (input ('Digite o ângulo desejado: ')) # ângulo de cada lado
    t = turtle.Pen()
    t.speed (0)
    t.pensize (1)

    if cor == 'R' or cor == 'r': # caso as cores sejam aleatórias:
        while True: # para sempre
            Hcor1 = random.randint (0,16777215) # escolherá um número aleatório de até os limites dados em decimal
            t.pencolor('#' + f'{Hcor1:06X}') # transforma o número aleatório em um hexadecimal (as cores) com pelo menos 6 casas (preenchendo as faltantes com 0).
            t.forward (distancia)
            t.left (angulo)
            distancia += 2

    else: # caso escolha uma cor:
        t.pencolor (cor)
        while True: # para sempre
            t.forward (distancia)
            t.left (angulo)
            distancia += 2
else: # caso escolha lados definidos
    angulo = 360/lados
    t = turtle.Pen()
    t.speed (0)
    t.pensize (1)

    if cor == 'R' or cor == 'r': # caso as cores sejam aleatórias:
        while a < lados: # enquanto o contador for menor que os lados desejados:
            Hcor1 = random.randint (0,16777215)
            t.pencolor('#' + f'{Hcor1:06X}') 
            t.forward (200)
            t.left (angulo)
            a += 1
    else: # caso defina uma cor
        t.pencolor (cor)
        while a < lados: # enquanto o contador for menor que os lados desejados:
            t.forward (200)
            t.left (angulo)
            a += 1
        
