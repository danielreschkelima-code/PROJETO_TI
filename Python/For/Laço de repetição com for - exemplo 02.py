# Laço de repetição com for - exemplo 02 - 10/10/2024
# uso do range()

lista = list(range(10))  # cria uma lista que vai de 0 até 9 (não inclui 10)

for número in lista:
    print(número)

print()

# o for pode percorrer diretamente o range:
for n in range(10):
    print(n)

print()

# imprime até número escolhido
limite = int(input('Digite o número até o qual deseja imprimir: '))
for n in range(limite):
    print(n, end=', ')
print(limite)  # imprime o último sem vírgula no final

print()

# determinar o início e o fim do range()
for n in range(1,11):  # inicia em 1 e termina em 10
    print(n)

# determina o início, o fim e o passo
print('tabuada do 2...')
for n in range(2,21,2):  # inicia em 2 e termina em 20, anda de 2 em 2
    print(n)





