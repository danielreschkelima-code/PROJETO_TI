# Forca do E.M., criado por Daniel Reschke de Lima.
import random
import turtle
import time

# LISTAS DAS MATÉRIAS #
matéria = ['biologia', 'química', 'física', 'geografia', 'filosofia', 'sociologia', 'português', 'matemática', 'inglês', 'história', 'todas']
biologia = ['fotossíntese']

# FUNÇÕES #

# Gráficas
def botaodesenho_txt(texto,tamanho,x,y): # faz o desenho do batão, com as váriaveis de texto e posição
    escritor.teleport(x,y)
    escritor.write (texto, align ='center', font=('OpenSans', tamanho , 'normal'))

def trianguloretangulo(a,b,origem,direção,hipotenusa): #faz um triângulo retângulo
    teorema = (hipotenusa**2)/2
    cateto = teorema**(1/2)

    desenhador.speed(0)
    desenhador.teleport(a,b)
    desenhador.setheading(0)

    if direção == 'left':
        turtle.fillcolor ('black')
        desenhador.left(origem)
        desenhador.forward(hipotenusa)
        desenhador.left(135)
        for i in range (1,3):
            desenhador.forward(cateto)
            desenhador.left(90)
        
    else:
        desenhador.fillcolor ('black')
        desenhador.right(origem)
        desenhador.forward(hipotenusa)
        desenhador.right(135)
        for i in range (1,3):            
            desenhador.forward(cateto)
            desenhador.right(90)

def X(origem,hipotenusa, cor, grossura, x,y):
    teorema = (hipotenusa**2)/2
    quadrado = teorema**(1/2)

    desenhador.setheading(0)
    desenhador.pencolor(cor)
    desenhador.pensize(grossura)
    desenhador.speed(10)
    desenhador.teleport(x,y)
    desenhador.left(origem)
    desenhador.forward(hipotenusa)
    desenhador.left(135)
    desenhador.penup()
    desenhador.forward(quadrado)
    desenhador.pendown()
    desenhador.left(135)
    desenhador.forward(hipotenusa)
        
def linhas(x,y,quantas):
    média = 10*(quantas*0.75)
    desenhador.setheading(0)
    desenhador.teleport(x,y)
    desenhador.pendown()
    desenhador.pencolor('black')
    desenhador.pensize(3)
    desenhador.speed(0)
    
    for i in range (quantas): 
        desenhador.forward(média)
        desenhador.penup()
        desenhador.forward(10)
        desenhador.pendown()
    
# MENUS #
            
# Menus principais
def mainlob():
    tela.clear()
    botaodesenho_txt ('Forca da Tartaruga', 20, 0, 90) # aplicando a função para cada item do menu, assim aparecendo os caractéres.
    botaodesenho_txt ('INICIAR', 15,0, 30)
    botaodesenho_txt ('OPÇÕES',15,0, - 10)
    botaodesenho_txt ('REGRAS',15,0, - 50)
    botaodesenho_txt ('SAIR', 10, 0, - 90)
    
    turtle.listen()
    turtle.onkeypress (piniciar, key = 'i')
    turtle.onkeypress (piniciar, key = 's')
    turtle.onkeypress (popções, key = 'o')
    turtle.onkeypress (pregras, key = 'r')
    turtle.onkeypress (psair, key = 'k')
    turtle.onkeypress (psair, key = 'w')

def iniciar1():   
    tela.clear()
    botaodesenho_txt ('TEMA',50,0,150)
    botaodesenho_txt ('Biologia',30, -400, -30)
    botaodesenho_txt ('TUDO',40,0,-30)
    botaodesenho_txt ('Química',30,400,-30)
    trianguloretangulo (-600,-60,90,'left',100)
    trianguloretangulo (600,-60,270,'r',100)

    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')
    turtle.onkeypress (iniciar2, key = 'd')
    turtle.onkeypress (iniciar2, key = '2')
    turtle.onkeypress (iniciar3, key = 'a')
    turtle.onkeypress (iniciar3, key = '3')
    turtle.onkeypress (ebiologia, key = 'b')
    turtle.onkeypress (etodas, key = 't')
    turtle.onkeypress (equimica, key = 'c')

def iniciar2():
    tela.clear()
    botaodesenho_txt ('TEMA',50,0,150)
    botaodesenho_txt ('Física',30,-450, -30)
    botaodesenho_txt ('Matemática',30,-150,-30 )
    botaodesenho_txt ('Geografia',30,150,-30)
    botaodesenho_txt ('Português',30,450,-30)
    trianguloretangulo (-600,-60,90,'left',100)
    trianguloretangulo (600,-60,270,'r',100)

    turtle.listen()
    turtle.onkeypress (iniciar1, key = 'a')
    turtle.onkeypress (iniciar1, key = '1')
    turtle.onkeypress (iniciar3, key = 'd')
    turtle.onkeypress (iniciar3, key = '3')
    turtle.onkeypress (efisica, key = 'f')
    turtle.onkeypress (ematematica, key = 'm')
    turtle.onkeypress (egeografia, key = 'g')
    turtle.onkeypress (eportugues, key = 'p')
    
def iniciar3():
    tela.clear()
    botaodesenho_txt ('TEMA',50,0,150)
    botaodesenho_txt ('Filosofia',30,-450, -30)
    botaodesenho_txt ('Sociologia',30, -150, -30)
    botaodesenho_txt ('História',30, 150, -30)
    botaodesenho_txt ('Inglês',30, 450, -30)
    trianguloretangulo (-600,-60,90,'left',100)
    trianguloretangulo (600,-60,270,'r',100)

    turtle.listen()
    turtle.onkeypress (iniciar2, key = 'a')
    turtle.onkeypress (iniciar2, key = '2')
    turtle.onkeypress (iniciar1, key = 'd')
    turtle.onkeypress (iniciar1, key = '1')
    turtle.onkeypress (efilosofia, key = 'o')
    turtle.onkeypress (esociologia, key = 's')
    turtle.onkeypress (ehistória, key = 'h')
    turtle.onkeypress (eingles, key = 'i')
    

def opções():
    tela.clear()
    botaodesenho_txt ('AINDA NÃO TEM, clique em Q para voltar...',40,0,0)
    
    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')
        
def regras():
    tela.clear()
    botaodesenho_txt ('AINDA NÃO TEM, clique em Q para voltar...',40,0,0)
    
    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')

def sair():
    tela.clear()
    botaodesenho_txt ('Você realmente deseja enforcar a forca?', 50, 0, 200)
    botaodesenho_txt ('SIM/ENFORCAR', 30, -200, -30)
    botaodesenho_txt ('NÃO', 30, 200, -30)

    turtle.listen()
    turtle.onkeypress (turtle.bye, key = 'e')
    turtle.onkeypress (turtle.bye, key = 's')
    turtle.onkeypress (turtle.bye, key = 'k')
    turtle.onkeypress (mainlob, key = 'q')
    turtle.onkeypress (mainlob, key = 'n')

def partida(temaselecionado):
    tela.clear()
    # palavrachave = list(temaselecionado[random.randint(0,len(temaselecionado))])
    palavrachave = list('banana')
    print (palavrachave)
    savechave = palavrachave
    palavrajogador = []
    vidas = 5
    abaixador = 245 # determina o espaço entre o Xs 
    lador = -195 # determina o espaço entre as letras 

    for i in range (0,5):
        X(45,80,'black',10,-600,abaixador)
        abaixador -= 125
    linhas (- 500,0, len(palavrachave))
    botaodesenho_txt ('INUTILIDADES:',20, -325, - 200)
    
    while vidas > 0 or len(palavrachave) > 0:
        print (palavrajogador)
        letra = turtle.textinput('Adivinhe uma letra: ', None)

        if letra not in palavrachave:
            vidas -= 1
            botaodesenho_txt(letra, 20, lador, - 200)
            lador += 20
            # mata um x
            # escreve a letra fora do negócio de palavras
        else:
            for i in range (0,len(palavrachave)-1):
                if palavrachave[i] == letra:
                    del palavrachave[i]
                
            # desenha a letra em algum lugar
            # manda o escritor ir pra outro canto

    if vidas <= 0:
        tela.clear()
        botaodesenho_txt ('ENFORCADO',90,0,0)
        
        # QUER MAIS UMA?
        turtle.onkeypress (iniciar1, key = 'q')
        turtle.onkeypress (iniciar1, key = 'n')
        turtle.onkeypress (psair, key = 'k')
        turtle.onkeypress (partida, key = 's')
        turtle.onkeypress (partida, key = 'e')

    else:
        tela.clear()
        botaodesenho_txt ('ENFORCOU',90,0,0)
        botaodesenho_txt (f'A palavra era: {savechave}', 50, - 200, - 50)
        
        # QUER MAIS UMA?
        turtle.onkeypress (iniciar1, key = 'q')
        turtle.onkeypress (iniciar1, key = 'n')
        turtle.onkeypress (psair, key = 'k')
        turtle.onkeypress (partida, key = 's')
        turtle.onkeypress (partida, key = 'e')
        
# Portais de menu
def piniciar():
    # indicação
    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')
    turtle.onkeypress (iniciar1, key = 'i')
    turtle.onkeypress (iniciar1, key = 'e')
    turtle.onkeypress (popções, key = 's')
    # remover indicação
    
def popções():
    # indicação
    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')
    turtle.onkeypress (opções, key = 'o')
    turtle.onkeypress (opções, key = 'e')
    turtle.onkeypress (piniciar, key = 'w')
    turtle.onkeypress (pregras, key = 's')
    # remover indicação

def pregras():
    # indicação
    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')
    turtle.onkeypress (regras, key = 'r')
    turtle.onkeypress (regras, key = 'e')
    turtle.onkeypress (popções, key = 'w')
    turtle.onkeypress (psair, key = 's')
    # remover indicação


def psair():
    # indicação
    turtle.listen()
    turtle.onkeypress (mainlob, key = 'q')    
    turtle.onkeypress (sair, key = 'k')
    turtle.onkeypress (sair, key = 'e')
    turtle.onkeypress (pregras, key = 'w')
    # remover indicação

# Escolha do tema

def ebiologia():
    temaselecionado = matéria[0]
    partida(temaselecionado)

def equimica():
    temaselecionado = matéria[1]
    partida(temaselecionado)

def efisica():
    temaselecionado = matéria[2]
    partida(temaselecionado)

def egeografia():
    temaselecionado = matéria[3]
    partida(temaselecionado)
    
def efilosofia():
    temaselecionado = matéria[4]
    partida(temaselecionado)
    
def esociologia():
    temaselecionado = matéria[5]
    partida(temaselecionado)

def eportugues():
    temaselecionado = matéria[6]
    partida(temaselecionado)

def ematematica():
    temaselecionado = matéria[7]
    partida(temaselecionado)

def eingles():
    temaselecionado = matéria[8]
    partida(temaselecionado)
    
def ehistória():
    temaselecionado = matéria[9]
    partida(temaselecionado)
    
def etodas():
    temaselecionado = matéria[random.randint(0,len(matéria)-1)]
    partida(temaselecionado)
    
# FAZEDORES #

# escritor n°1
escritor = turtle.Turtle()
escritor.hideturtle
escritor.penup

# desenhador n°1
desenhador = turtle.Turtle()
desenhador.hideturtle
desenhador.penup

# controlador da tela
tela = turtle.Screen() 

# O JOGO EM SI #

turtle.hideturtle
turtle.title ('Forca da Tartaruga')
escritor.write ('Forca da Tartaruga', align = 'center', font= ('Opensans', 50, 'normal'))
time.sleep(1.5)
tela.clear()

print ('''GUIA DE CONTROLE

Controle geral:
W - para cima
S - para baixo
A - esquerda
D - direita
Q - voltar/ cancelar
E ou a mesma tecla da opção para confirmar

Tela principal:      
I - iniciar
O - opções
R - regras
K - sair

Escolha de modo:
T - tudo
B - biologia
O - filosofia
F - física
G - geografia
H - história
I - inglês
M - matemática
P - português
C - quimíca
S - sociologia
''')

mainlob()
tela.mainloop()