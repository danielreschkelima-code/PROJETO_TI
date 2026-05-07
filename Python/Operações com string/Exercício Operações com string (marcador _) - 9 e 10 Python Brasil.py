# Exercício Operações com string - 9 Python Brasil
# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Fórmula1: c = 5 * ((f-32) / 9).
# Fórmula2: f = c *1,8+32.
print ('Conversão de graus Fahrenheit para graus Celsius (que é uma medida melhor) ou o oposto...')
print ('Digite 1 para conversão de Fahrenheit para Celsius.')
print ('Digite 2 para conversão de Celsius para Fahrenheit.')
tomadadedecisao = int(input ('Selecione aqui: '))
if tomadadedecisao  == 1:
    f = float (input ('Qual é a temperatura em Fahrenheit? '))
    c = 5 * ((f-32) / 9)
    print ('Esta é a temperatura correspondente em graus Celsius:')
    print ('%.2fº' % c)
    if c < 0:
        print ('Vou congelar.')
    if c > 30:
        print ('Que calor!')

if tomadadedecisao == 2:
    c = float (input ('Qual é a temperatura em Celsius? '))
    f = c * 1.8 + 32
    print ('Esta é a temperatura correspondente em graus Celsius:')
    print ('%.2fº' % f)
if tomadadedecisao > 2 or tomadadedecisao < 1:
    print ('Essa conversão não está disponível, sinto muito...')
    
     
    


