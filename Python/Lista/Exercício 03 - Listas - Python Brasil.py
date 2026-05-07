
# Exercício 03 - Listas - Python Brasil - 28/08/2024

# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [7.5, 9.0, 9.5, 10.0]

soma = 0
i = 0  # inicia em 0, pois 0 é o índice do 1º elemento da lista notas
while i < len(notas):
    print(f'Nota: {notas[i]}')
    soma += notas[i]
    i+=1
média = soma / len(notas)  # só pode calcular média quando soma está pronta
print(f'Média: {média:.1f}')
