## Exercício 15 - Listas - Python Brasil
## Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
## encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
## Mostre a quantidade de valores que foram lidos;
## Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
## Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
## Calcule e mostre a soma dos valores;
## Calcule e mostre a média dos valores;
## Calcule e mostre a quantidade de valores acima da média calculada;
## Calcule e mostre a quantidade de valores abaixo de sete;
## Encerre o programa com uma mensagem;

valores = []
valoresamedia = []
valores7 = []
soma = 0

while True:
    valor = float (input('Digite um valor ou digite - 1 para terminar: '))
    if valor == -1:
        break
    else:
        valores.append(valor)
        soma += valor

quantidade = len(valores)
print (f'''
QUANTIDADE DE VALORES LIDOS: {quantidade}

''')

média = soma/len(valores)

for tupla in enumerate(valores):
    if tupla [1] > média:
        valoresamedia.append(tupla[1])
    if tupla [1] < 7:
        valores7.append(tupla[1])
    if tupla[0] == 0:
        print (f'VALORES LIDOS: {tupla[1]}', end =', ')
    elif tupla[1] == valores[-1]: 
        print (valores[-1], end ='.')
    else:
        print (f'{tupla[1]}', end = ', ')

print ('''

VALORES LIDOS (ORDEM INVERSA)''')

valorinverso = -1

while valorinverso >= - len(valores):
    print (valores[valorinverso])
    valorinverso -= 1

valoracima = len (valoresamedia)
valorabaixo = len(valores7)

print(f'''
SOMA DOS VALORES: {soma:.2f}
MÉDIA DOS VALORES: {média:.2f}
QUANTIDADE DE VALORES ACIMA DA MÉDIA: {valoracima}
QUANTIDADE DE VALORES ABAIXO DE 7: {valorabaixo}

PROGRAMA ENCERRADO!''')

    
       
    
