# Digite uma série de strings e as contatene por espaços. Assim que usuário digitar /exit o comando deve parar e printar toda a contatenação.
print('''
CONTATENAÇÃO
''')
palavras = ""
while True:
    novapalavra = input("Digite a nova palavra a ser adicionada ou /exit para a impressão: ")
    if novapalavra != "/exit":
        palavras += novapalavra + " "
    else:
        palavras = palavras[0:-1]
        break
print(f'''
O RESULTADO DA CONTATENAÇÃO FOI:
"{palavras}".
       ''')