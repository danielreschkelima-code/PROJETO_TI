# Laço de repetição com for - exemplo 01 - 10/10/2024

L = [15, 7, 27, 39]

# imprime cada um dos elementos da lista L
for elemento in L:
    print(elemento)

# for com contador, enumerate()
for i, elemento in enumerate(L):
    print(i, elemento)

# mesma coisa que o for anterior, mas com uma variável só
for tupla in enumerate(L):
    print(tupla[0], tupla[1])

# mesma coisa, usando while
i = 0
while i < len(L):
    print(i, L[i])
    i += 1
