#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

print ('Mostrarei alguns cálculos')
n1 = int(input('Coloque um número inteiro qualquer: '))
n2 = int(input('Coloque outro número inteiro: '))
n3R = float (input ('Desta vez, coloque um número real: '))

ra = (n1*2) * (n2/2)
rb = (n1 * 3) + n3R
rc = n3R ** 3

print (f'O produto do dobro do primeiro número com a metade do segundo número é {ra:.2f}.') # Mesmo ambos os números serem ineteiros, seu resultado pode ser um número com vírgula por conta da operação de fração, assim é necessário formatá-lo
print (f'A soma do triplo do primeiro número com o terceiro é {rb:.2f}.')
print (f'O resultado do terceiro número elevado ao cubo é {rc:.2f}.')

