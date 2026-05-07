#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

ap = float (input ('Qual o tamanho da área, em metros quadrados, que será pintada? '))
l = ap//3
lata = 18*l
preço = lata*80
if ap >=3 :
    print (f'Com essa área, serão necessárias {lata} latas de tinta e isso irá lhe custar R$ {preço:.2f}.')
else:
    if ap <= 0:
       print ('Essa medida não é valida (não existe medida negativa ou nula).')
    else:
        print ('As latas de tinta têm 18 litros, e uma dessas será suficiente e possívelmente sobrará do produto referente, o que lhe custará R$ 80.00.')
        print ('Para cada 3m² é utilizado 1 lata, como você possui menos do que isso talvez seja interessante comprar uma lata menor...')
        


       
