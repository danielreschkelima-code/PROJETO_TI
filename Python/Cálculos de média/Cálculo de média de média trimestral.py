#Exemplo 01 - cálculo de média - 12/03/2024
#Daniel Reschke de Lima
# A hashtag é utilizada para anotações, já que o computador ignora o conteúdo após ela.
print ('Olá, calcule sua média trimestral. Não se apavore, sempre há outro jeito...')
a = input ('Digite a nota do 1° trimestre: ') #input faz com que ele pergunte e aguarde um valor.
b = input ('Digite a nota do 2° trimestre: ')
c = input ('Digite a nota do 3° trimestre: ')
a = float (a) #float transoforma a variável de texto para número.
b = float (b)
c = float (c)
#a = 10
#b = 10
#c = 10
média = (a+b+c)/3 #cálculo da média.
print ("Esta é a sua média: ")
print (média) # mostra o resultado da média.
if média <7:
    print ("Quem sabe ainda tenha um recuperação...")# perfumaria.
else:
    print ("Parabénsss, sua nota é grande quanto o número de 's'.")
           

