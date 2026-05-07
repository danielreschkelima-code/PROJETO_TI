# Exercício 5.11 do livro azul
# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os primeiros 24 meses.
# Escreva o total ganho com juros.

di = float (input ('Digite o seu depósito inicial: '))
j1 = float (input ('Digite a taxa de juros de sua poupança: '))

while di < 0 or j1 < 0:
    print ('Tanto o depósito inicial como a taxa de juros devem ser positivos.')
    di = float (input ('Digite o seu depósito inicial: '))
    j1 = float (input ('Digite a taxa de juros de sua poupança: '))

repetição = 1
inicial = di # guarda o valor inicial

while repetição <= 24:
    di += di * j1/100
    print (f'Após o {repetição}º mês o valor com juros foi de: R$ {di:.2f}.')
    repetição += 1

ganho = di - inicial
print (f'O ganho total dos juros foi de: R$ {ganho:.2f}.')
