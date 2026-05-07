# Filas (Fifo: First Out) - Fila de Banco - 19/09/2024

fila = []
filaprioritária = []
ficha = 0


while True:
    print ('''Sistema de fila de banco...
F - Entrar na fila
A - Atender cliente na fila
S - Sair do programa
''')
    op = input ('Digite a operação desejada: ').upper()
    if op == 'F':
        a = input ('Digite P para fila prioritária e N para normal: ').upper()
        while a != 'N' and a != 'P':
            print ('Coloque uma opção válida...')
            a = input ('Digite P para fila prioritária e N para normal: ').upper()
            
        ficha += 1 #gera um novo número

        if a == 'N':
            fila.append (ficha)
            print (f'Ficha n° {ficha} adicionada na fila!')
        else:
            filaprioritária.append (ficha)
            print (f'Ficha n° {ficha} adicionada na fila prioritária!')
        
    elif op == 'A':
        if len(fila) < 0 and len(filaprioritária) < 0:
            print ('Não há clientes a serem atendidos!')
        elif a == 'P':      
            print (f'O cliente número {filaprioritária.pop(0)} foi atendido com prioridade!')
        else:
            print (f' O cliente número {fila.pop(0)} foi atendido!')
        
    elif op == 'S':
        print ('Finalizando o programa')
        break
    else:
        print ('''Digite apenas os itens na lista...
''')
