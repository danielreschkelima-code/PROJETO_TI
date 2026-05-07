# Exercício 21 - Repetições - Python Brasil - 08/08/2024
# Faça um programa que peça um número inteiro e determine se ele é ou não um
# número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

número = int(input('Digite um nº para testar se é primo: '))
divisor = 2
while divisor < número:
    if número % divisor == 0:
        print(f'É divisível por {divisor}!')
        break
    divisor += 1

if divisor == número:
    print(f'{número} é primo!')
else: 
    print('Não é primo!')
