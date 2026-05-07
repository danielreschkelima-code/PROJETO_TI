# Exemplo - Acumuladores - 02/07/2024

n = 1 # contador
soma = 0 # acumulador
while n <= 10:
    valor = int (input (f'Digite o {n}º valor: '))
    soma += valor
    n += 1 # mesma coisa que: n = n + 1
print (f'A soma dos valores digitados é: {soma}.')    
media = soma / 10
print (f'A média dos números é: {media:.2f}.')
