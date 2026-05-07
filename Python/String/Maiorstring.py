def maiorstring(frase):
    lista = list(frase)
    palavras = []
    palavratemporaria = []
    for i in range(len(lista)):
        if lista[i] == ' ':
            append = [''.join(palavratemporaria), len(palavratemporaria)]
            palavras.append(append)
            palavratemporaria = []   
        else:
            palavratemporaria.append(lista[i])
    append = [''.join(palavratemporaria), len(palavratemporaria)] # não há espaço, então a última palavra precisa ser colocada manualmente
    palavras.append(append)    
    palavrascompletas = palavras.copy()
    for i in range(len(palavras)):
        if len(palavras) >= 2:
            if palavras[-1][1] > palavras[-2][1]:
                del palavras[-2]
            else:
                del palavras[-1]
        else:
            pass
    todas = [palavras, palavrascompletas]
    return todas  

print (f' FUNÇÃO ACHADORA DE PALAVRAS GRANDES '.center(75,'-'),'\n')
entrada = input ('Digite a frase para encontrar a maior palavra: ')
função = maiorstring(entrada)[0]
função1 = maiorstring(entrada)[1]
print(f'''\nA MAIOR PALAVRA É: {função[0][0]}
Nº CARACTERES: {função[0][1]}
''')
print(' RESTANTE DAS PALAVRAS '.center(35,'-'))
print('\nPALAVRA --- N° ')

for i in range(len(função1)):
    print(f'{função1[i][0]:8} -  {função1[i][1]}')
