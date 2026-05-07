# Turtle - exemplo 2 - espiral quadratica 
import turtle # Aciona a função de desenho
t = turtle.Pen() # abre o desenho
t.speed (7) # define a velocidade do traço
t.pencolor('green') # define a cor do traço
t.pensize (3) # define, em pixels, a grossura do traço
distancia = 0
while distancia  < 1080:
    t.forward (distancia) # faz com que apareça um traço numa distância determinada para frente
    t.left (90) # gira o traçador
    distancia += 4
