# Turtle - exercício 01 - desenhar polígono regular de n lados - 22/08/2024
import turtle
cores = ['red', 'violet', 'blue', 'orange', 'yellow', 'green', 'magenta']
turtle.bgcolor('black')
t = turtle.Pen()  # abre a janela (P tem que ser maiúsculo)
t.speed(0)  # velocidade entre 1 e 10, o máximo é 0
#t.pencolor('red')  # define a cor da linha
t.pensize(3)  # define a largura da linha em pixels

lados = int(input('Digite a quantidade de lados do polígono: '))
ângulo = 360/lados  # matematicamente, o ângulo diminui conforme o acrescimo de lados
distância = 1200/lados  # tamanho do lado diminui conforme a quantidade de lados para se ajustar a tela
    
x = 0
while x < lados:
    t.pencolor(cores[x%7])  # seleciona uma cor entre 0 e 6
    t.forward(distância)
    t.left(ângulo)
    x += 1
