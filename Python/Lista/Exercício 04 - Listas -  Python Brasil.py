# Exercício 04 - Listas -  Python Brasil - 29/08/2024
# 4. Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.
import random
import string

#caracteres = ['q','w','e','r','t','y','u','i','o','p']
caracteres = random.choices(string.ascii_lowercase, k=10)  # sorteia 10 letras 

vogais = ['a', 'e', 'i', 'o', 'u']

quant_consoantes = 0
i = 0
while i < len(caracteres):
    if caracteres[i] not in vogais:  # não é vogal, então será consoante
        print(caracteres[i])  # imprime a letra, porque é consoante
        quant_consoantes += 1   # conta a consoante encontrada
    i += 1

print(f'Foram encontradas {quant_consoantes} consoantes na lista caracteres,')
quant_vogais = len(caracteres) - quant_consoantes
print(f'e {quant_vogais} vogais.')


