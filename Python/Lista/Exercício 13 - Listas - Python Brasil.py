# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas
# e mostre todas
# as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mediamensal = []

mesabaixo = []
tempmesabaixo = []

mesacima = []
tempmesacima = []

mesneutro = []

somatemp = 0
i = 0
while i < len (meses):
    mestemp = float (input (f'Digite a temperatura média (ºC) de {meses[i]}: '))
    mediamensal.append(mestemp)
    somatemp += mestemp
    i += 1

mediaanual = somatemp / len(meses)

i = 0
while i < len(meses):
    if mediamensal[i] < mediaanual:
        tempmesabaixo.append(mediamensal[i])
        mesabaixo.append(meses[i])

    elif mediamensal[i] > mediaanual:
        tempmesacima.append(mediamensal [i])
        mesacima.append(meses[i])
    else:
        mesneutro.append(meses[i])
    i += 1
print (f'\nA média anual da temperatura (ºC)foi de: {mediaanual:.2f}', end = '\n')
print ('')
print ('MESES ACIMA DA MÉDIA', end='\n')
i = 0
while i < len(mesacima):
    print (f'{mesacima[i]} : {tempmesacima[i]:.2f} ºC')
    i += 1
print ('''
MESES ABAIXO DA MÉDIA''', end='\n')
i = 0
while i < len (mesabaixo):
    print (f'{mesabaixo[i]} : {tempmesabaixo[i]:.2f} ºC')
    i += 1
i = 0
if len(mesneutro) > 0:
    print ('''
MESES NA MÉDIA''', end='\n')
    while i < len(mesneutro):
        print (f'{mesneutro[i]} : {mediaanual:.2f} ºC')
        i += 1
