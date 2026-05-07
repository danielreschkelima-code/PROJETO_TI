# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int (input ('Digite a base do número: '))
expoente = int (input ('Digite o expoente do número: '))
resultado = base
x = 1
while x < expoente:
    resultado = resultado * base # mesmo que: resultado *= resultado.
    x += 1
print (f'{base}**{expoente} = {resultado}')
