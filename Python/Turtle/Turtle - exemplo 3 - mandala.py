# Turtle - exemplo 3 - mandala - 22/08/2024
import turtle
import random
#           0       1       2       3           4       5           6
cores = ['red', 'violet', 'blue', 'orange', 'yellow', 'green', 'magenta']
#          -7       -6      -5      -4          -3      -2          -1
turtle.bgcolor('black')  # cor de fundo (aqui em preto)
t = turtle.Pen()  # abre a janela (P tem que ser maiúsculo)
t.shape('turtle')  # define o símbolo da tartaruga
t.shapesize(3)  # define o tamanho da tartaruga
t.speed(0)  # velocidade entre 1 e 10, o máximo é 0
t.pensize(3)  # define a largura da linha em pixels
   
distância = 10
while distância < 1080:
    t.pencolor(random.choice(cores)) # define a cor aleatória
    t.forward(distância)
    t.left(150)
    distância += 3
