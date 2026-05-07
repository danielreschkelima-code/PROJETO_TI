# Exercício 08 - Listas - Python Brasil
# Faça um programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []
pessoa = 1
while pessoa < 5:
    paltura = float (input (f'Digite a altura da pessoa {pessoa}: '))
    pidade = int (input (f'Digite a idade da pessoa {pessoa}: '))
    altura.append(paltura)
    idade.append(pidade)
    pessoa += 1

pessoa = 4
x = len(idade)-1
print ('''ALTURAS
''')
while x > -1:
    print (f'Pessoa{pessoa}: {altura[x]}')
    x -= 1
    pessoa -= 1

pessoa = 4
x = len(idade)-1
print ('''
IDADES
''')
while x > -1:
    print (f'Pessoa{pessoa}: {altura[x]}')
    x -= 1
    pessoa -= 1
